# Sylph - conversational interaction with OpenAI Chat Completion API

Sylph is a Python script that interacts with the OpenAI Chat Completion API to generate responses based on a given input JSON file. It appends the generated response to the `messages` list with the role "assistant" and saves the result to an output JSON file. This architecture allows the output file, perhaps with another "user" message added, or with other edits, to be fed back as input, enabling a conversational loop.

Sylph was first created by Peter Kaminski and ChatGPT (GPT-4) on 2023-03-21. Peter guided ChatGPT, and ChatGPT wrote all the code. See the [[Names]] and [[Prompts]] Markdown files and the Git commit log for background. See [[Roadmap]] for thoughts on future development.

Comments and bug reports are welcome at <https://github.com/peterkaminski/sylph/issues>, and I'm happy to review pull requests.

The first version used the Completion endpoint and the `text-davinci-002` model, but we switched it to use the Chat Completion endpoint and `gpt-3.5-turbo` to get to Sylph v1.

Note, there may be some breaking architectural or input/output method changes in future versions to make it easier to add a prompt to the output and feed it back as the input.

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone this repository or download the `sylph.py` file.
2. Install the `requests` library (recommended: activate a Python virtual environment first):

```bash
pip install requests
```

## Usage

1. Set the OPENAI_API_KEY environment variable to your OpenAI API key:

```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

You can copy `env.sh-template` to `env.sh`, add your API key to it, and then use `source env.sh` to add your API key to the environment.

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

For more information about the values in this file, read about the "chat format" in the [Chat completion introduction](https://platform.openai.com/docs/guides/chat/introduction) and the [Chat Completion API Reference](https://platform.openai.com/docs/api-reference/chat).

3. Run the program with the input JSON file and specify the output JSON file path:

```bash
python sylph.py --input input.json --output output.json
```

Or you can change directory to where `sylph.py` is located and run it as an executable:

```bash
./sylph.py --input input.json --output output.json
```

The generated response will be appended to the messages list with the role "assistant" and saved in the output JSON file.

To have a conversation, you can add another message in the messages list with the role "user", and use that as the input file in the next run.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
