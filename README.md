# ChatGPT API Interaction

This Python script interacts with the OpenAI ChatGPT API to generate responses based on a given input JSON file. It appends the generated response to the `messages` list with the role "assistant" and saves the result to an output JSON file.

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone this repository or download the `chatgpt_api_interaction.py` file.
2. Install the `requests` library:

```bash
pip install requests
```

## Usage

1. Set the OPENAI_API_KEY environment variable to your OpenAI API key:

```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

2. Prepare an input JSON file with the following format:

```json
{
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "What is the capital of France?"
    }
  ],
  "max_tokens": 150,
  "n": 1,
  "temperature": 0.5
}
```

3. Run the program with the input JSON file and specify the output JSON file path:

```bash
python chatgpt_api_interaction.py --input input.json --output output.json
```

The generated response will be appended to the messages list with the role "assistant" and saved in the output JSON file.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
