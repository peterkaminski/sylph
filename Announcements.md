# Announcements

## OGM Mailing List, 2023-03-21

I just used ChatGPT (GPT-4) to write a simple Python utility for round-trip conversations with OpenAI's Chat Completion API (basically, the API version of ChatGPT).

- <https://toolsforthought.rocks/@peterkaminski/110062125558070089>
- <https://github.com/peterkaminski/sylph>

Sylph v1 is not usable unless you speak JSON natively, but hopefully that will improve.  Even then, you'll still have to know how to run a Python utility, but I think that's an easier lift than grokking JSON.

The cool thing about Sylph: the input and output JSON structures are identical, enabling conversational loops. Just append a new message in the output and feed it back as input!

This is the first time I've used AI to help me write code. In this case, I let it write **all** the code. It felt like driving a moon rover via text messages, rather than driving an Earth car by sitting in the driver's seat, but it worked!

I think it took me about the same amount of time, maybe somewhat less, than just writing it myself.  After getting used to driving a moon rover via text messages, maybe it would be faster.

As I said, ChatGPT wrote all the code, so theoretically, I didn't need to know Python to do this.  But I'm a Python coder, so I liked being able to read and understand the code (and was ready to grab the wheel).  There's also some rigmarole to running a Python CLI program that a Python dev would know, that a non-dev probably wouldn't.

ChatGPT and I both made some mistakes in the process. It was very good at fixing them. This capability, to recover from a mistake gracefully, is **super** useful in an AI.

ChatGPT, quite reasonably from the way I asked, started with a slightly older interface library, which doesn't support GPT-3.5  and later (OpenAI changed the API slightly to fit the "chat" model better).  ChatGPT was super smooth removing the old library calls and swapping in the new library calls.  Doing the same thing would have given a novice programmer a bit of a pause, I think.

Overall, it was a good experience, and now I have a foundation to build the next version!

## Mastodon, 2023-03-21

<https://toolsforthought.rocks/@peterkaminski/110062125558070089>

I'm pleased to announce Sylph v1, a simple Python command-line utility to do #ChatGPT via API instead of web.

v1 is not usable unless you speak #JSON natively, but hopefully that will improve.

I iteratively specified it with ~9 prompts over ~2 hours. #GPT4 wrote the code.

The cool thing: the input and output JSON structures are identical, enabling conversational loops. Just append a new message in the output and feed it back as input!

I'm happy to get issues and PRs.

https://github.com/peterkaminski/sylph
