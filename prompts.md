# Prompts

(These are the prompts to ChatGPT which created the initial program.)

write a python program that interacts with the chatgpt api. it should take input from stdin, and output to either a file or stdout, based on an argument.

change it so the api key is read from an environment variable

modify the program so it saves the input and output in a json file, and so it reads the input from a json file. include the role (system, user, or assistant) in the json file.

modify it so the output is the raw output from the API, and the input reads a JSON file in the same format as the raw output from the API

modify it so it reads input from a JSON file with the same format as the raw API input and saves the output as in the same format as raw API input to a JSON file.

no, the output format is still using the API output format. change it so the output format is the same as the input format.

now change it so it uses the chat completion endpoint, rather than the completion endpoint

(I ran the program with the wrong input file, and got a `KeyError: 'messages'` error. I asked ChatGPT to fix the error, and it replied that the key was missing, and gave a modified read_input function with an added input sanity check.)

thanks. now i am getting this error: openai.error.InvalidRequestError: Invalid URL (POST /v1/chat/completions)

(ChatGPT replied: "Apologies for the confusion. The Chat Completion API is not directly available in the OpenAI Python library. However, you can use the requests library to make a POST request to the Chat Completion API. Here's the modified version of the program using the requests library:")

(I got a 404 "Invalid URL (POST /v1/chat/completions)" error and asked ChatGPT about it. It backtracked and wanted me to go back to the completion endpoint. But I fixed the problem by setting the model to "gpt-3.5-turbo" insted of "text-davinci-002". As OpenAPI notes, "Because gpt-3.5-turbo performs at a similar capability to text-davinci-003 but at 10% the price per token, we recommend gpt-3.5-turbo for most use cases.")
