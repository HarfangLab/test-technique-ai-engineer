# AI Engineer / Technical Case

👋 Welcome! Here's everything you need to work on the AI Engineer technical case which is part of HarfangLab's recruitement process.

ℹ️ Instead of doing this technical case, you can share some relevant code you're proud of that you have done on a previous project

## Overview

### About the interview

The technical case is primarily a discussion support for the onsite technical interview. 
The topics are intentionally dense, especially considering that the preparation period may be very short. 
The goal isn't to cover everything exhaustively but to provide an overall understanding and let you develop the areas of work you wish. 

We will ask you at the beginning of the interview how much time you were able to dedicate to this preparation.

We want to see code. It's important that this code can be executed. This allows us to observe your habits and understand your thought process. As 
mentioned above, you can provide us with code you've done elsewhere.  

### Interview goal

Your goal is to build an LLM-powered assistant that is capable of answering the questions inside `questions.jsonl`.
You will see that questions range across N topics : 
* The files inside `documents`.
* etc.

### LLM API

In order for you to test your code, you need access to an API serving a real LLM.

We suggest using one of [Mistral AI](https://mistral.ai/), since they are free
to use (under reasonable limits) and can be setup quickly.

To get an API key, simply go to https://admin.mistral.ai/organization/api-keys and login.
Once you have an account, generate a key in the `API Key` drawer.

### Starting up

We suggest using [`uv`](https://docs.astral.sh/uv/) for package management.

In `quickstart.py`, you will find a simple working example that you can run like this : 

```bash
MISTRAL_API_KEY=*** uv run python quickstart.py
```
