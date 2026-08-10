# AI Engineer / Technical Case

👋 Welcome! Here's everything you need to work on the AI Engineer technical case which is part of HarfangLab's recruitement process.

## Overview - About the interview

The technical case is primarily a discussion support for the onsite technical interview. The topics are intentionally dense, especially considering that the preparation period may be very short. The goal isn't to cover everything exhaustively but to provide an overall understanding and let you develop the areas of work you wish. We will ask you at the beginning of the interview how much time you were able to dedicate to this preparation.

The technical case is split into two parts: a technical subject and a case study subject.

## The technical subject

We want to see code. It's important that this code can be executed. This allows us to observe your habits and understand your thought process.

ℹ️ Instead of doing the technical subject, you can share some relevant code you're proud of that you have done on a previous project.

You can submit your answers in the way that suits you best:
* By making a new private github repository and adding [HugoMichard](https://github.com/HugoMichard) and [goncalogiga](https://github.com/goncalogiga) as contributors (preferred)
* By sending a ZIP file with your code
* ...Or any other method you prefer!

⚠️ If you choose to share your answers using a github repository, don't forget to make it private !

### Goal

Your goal is to build an LLM-powered assistant that is capable of answering the questions inside `questions.jsonl`.
You will see that questions range across different topics : 
* The files inside `documents`.
* Interfacing with APIs
* Searching the web

### Starting up

#### LLM API

In order for you to test your code, you need access to an API serving a real LLM.

We suggest using one of [Mistral AI](https://mistral.ai/), since they are free
to use (under reasonable limits) and can be setup quickly.

To get an API key, simply go to https://admin.mistral.ai/organization/api-keys and login.
Once you have an account, generate a key in the `API Key` drawer.

#### Boilerplate

We suggest using [`uv`](https://docs.astral.sh/uv/) for package management.

In `quickstart.py`, you will find a simple working example that you can run like this : 

```bash
MISTRAL_API_KEY=*** uv run python quickstart.py
```

ℹ️ There is absolutely no need to use any of the code present in `quickstart.py` nor `uv` in your solution. You may use any library or framework you want. This boilerplate is only here to help you get a head start.

### Evaluation

Your solution will be evaluated on the following criteria, listed from the most to the least important:
* **It runs**
* **Architecture & design choices**
* **Code quality**
* **Answer quality**

ℹ️ Answering all the questions is not a requirement. The last ones are deliberately hard. 

ℹ️ Coding everything is also not a requirement. You may document the limitations you are aware of, and how you would tackle parts you do not have the time to do, and we will discuss them during the interview.


## The case study subject

We propose several topics for the case study. We ask you to prepare at least one. You are free to make any assumptions you deem relevant.

ℹ️ You do not need to code anything on this subject, we only want to know how you would tackle the topic you choose.

### Domain classification

Suppose you have access to a dataset of `N` links with a category label (blog, business, art ...). Given a new link, the goal is to determine its category. How would you tackle this task ?

### Malware detection

Suppose you have access to a dataset of `N` malicious pe files and `M` benign pe files. For each of these files, you have access to their label (malicious / benign). Given a new file, the goal is to determine whether it is malicious or not. How would you tackle this task ?
