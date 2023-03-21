import openai
import os
import argparse
import json

def call_chatgpt(input_data):
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    if not openai.api_key:
        raise ValueError("Please set the 'OPENAI_API_KEY' environment variable")

    messages = input_data["messages"]

    response = openai.ChatCompletion.create(
        model=input_data["engine"],
        messages=messages,
        max_tokens=input_data["max_tokens"],
        n=input_data["n"],
        temperature=input_data["temperature"],
    )

    return response.choices[0].message['content']

def read_input(input_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    return data

def save_output(output_file, input_data, response_text):
    output_data = input_data.copy()
    output_data['response'] = response_text

    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Interact with ChatGPT")
    parser.add_argument("-i", "--input", required=True, help="Specify the input JSON file path")
    parser.add_argument("-o", "--output", required=True, help="Specify the output JSON file path")
    args = parser.parse_args()

    input_data = read_input(args.input)
    response_text = call_chatgpt(input_data)
    save_output(args.output, input_data, response_text)
    print(f"Input and response saved to {args.output}")

if __name__ == "__main__":
    main()
