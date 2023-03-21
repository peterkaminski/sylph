import openai
import os
import argparse
import json

def call_chatgpt(prompt):
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    if not openai.api_key:
        raise ValueError("Please set the 'OPENAI_API_KEY' environment variable")

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response

def read_input(input_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
        return data['prompt']

def save_output(output_file, response):
    response_dict = {
        'id': response.id,
        'object': response.object,
        'created': response.created,
        'model': response.model,
        'usage': {
            'prompt_tokens': response.usage['prompt_tokens'],
            'completion_tokens': response.usage['completion_tokens'],
            'total_tokens': response.usage['total_tokens']
        },
        'choices': [
            {
                'text': choice.text,
                'index': choice.index,
                'logprobs': None,
                'finish_reason': choice.finish_reason
            } for choice in response.choices
        ]
    }

    with open(output_file, 'w') as f:
        json.dump(response_dict, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Interact with ChatGPT")
    parser.add_argument("-i", "--input", required=True, help="Specify the input JSON file path")
    parser.add_argument("-o", "--output", required=True, help="Specify the output JSON file path")
    args = parser.parse_args()

    user_input = read_input(args.input)
    response = call_chatgpt(user_input)
    save_output(args.output, response)
    print(f"Raw API input and output saved to {args.output}")

if __name__ == "__main__":
    main()
