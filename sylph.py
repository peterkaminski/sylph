import openai
import sys
import argparse
import os

# Function to call ChatGPT API
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

    return response.choices[0].text.strip()

# Function to output to stdout
def output_stdout(text):
    print(text)

# Function to output to a file
def output_file(text, file_path):
    with open(file_path, "w") as f:
        f.write(text)

def main():
    parser = argparse.ArgumentParser(description="Interact with ChatGPT")
    parser.add_argument("-f", "--file", help="Specify the output file path")
    args = parser.parse_args()

    user_input = input("Enter your prompt for ChatGPT: ")
    response = call_chatgpt(user_input)

    if args.file:
        output_file(response, args.file)
        print(f"ChatGPT response saved to {args.file}")
    else:
        output_stdout(response)

if __name__ == "__main__":
    main()
