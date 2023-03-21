#!/usr/bin/env python

# Sylph v1.0.0 - https://github.com/peterkaminski/sylph

import os
import argparse
import json
import requests

def call_chatgpt(input_data):
    api_key = os.environ.get("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("Please set the 'OPENAI_API_KEY' environment variable")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    url = "https://api.openai.com/v1/chat/completions"

    response = requests.post(url, headers=headers, json=input_data)

    if response.status_code != 200:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

    response_json = response.json()
    return response_json['choices'][0]['message']

def read_input(input_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    if "messages" not in data:
        raise KeyError("The 'messages' key is missing in the input JSON file")

    return data

def save_output(output_file, input_data, response_message):
    output_data = input_data.copy()
    output_data['messages'].append(response_message)

    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Interact with ChatGPT")
    parser.add_argument("-i", "--input", required=True, help="Specify the input JSON file path")
    parser.add_argument("-o", "--output", required=True, help="Specify the output JSON file path")
    args = parser.parse_args()

    input_data = read_input(args.input)
    response_message = call_chatgpt(input_data)
    save_output(args.output, input_data, response_message)
    print(f"Input and response saved to {args.output}")

if __name__ == "__main__":
    main()
