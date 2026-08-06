import json
import os
import random
from pathlib import Path

import click
from dotenv import load_dotenv
from mistralai.client import Mistral
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from tenacity import retry, stop_after_attempt, wait_exponential

load_dotenv()

console = Console()

api_key = os.getenv("MISTRAL_API_KEY")

AVAILABLE_MODELS = [
    "ministral-3b-2512",
    "mistral-8b-2512",
]

MAX_TOKENS_IN_ANSWER = 32


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def get_answer(mistral: Mistral, model: str, question: str) -> str:
    """Queries the LLM for an answer.

    Args:
        mistral (Mistral):
            The mistral client
        model (str):
            The model to be used
        question (str):
            The question to be asked
    """
    response = mistral.chat.complete(
        model=model,
        messages=[{"role": "user", "content": question}],
        max_tokens=MAX_TOKENS_IN_ANSWER,
    )

    return response.choices[0].message.content


def answer_and_display(mistral: Mistral, model: str, question: str) -> None:
    """Asks one question and renders the answer, or the error if it fails.

    Args:
        mistral (Mistral):
            The mistral client
        model (str):
            The model to be used
        question (str):
            The question to be asked
    """
    try:
        with console.status("[dim]thinking…[/]"):
            answer = get_answer(mistral, model, question)
    except Exception as e:
        console.print(Panel(str(e), title="error", border_style="red"))
        return

    console.print(Panel(Markdown(answer), border_style="green", padding=(1, 2)))


@click.command()
@click.option(
    "--model", "-m", type=click.Choice(AVAILABLE_MODELS), default="ministral-3b-2512"
)
@click.option(
    "--questions-file",
    "-f",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    default=Path("questions.jsonl"),
)
@click.option("--num-questions", "-n", type=int, default=10)
def main(model: str, num_questions: int, questions_file: Path):
    if not api_key:
        console.print("[bold red]MISTRAL_API_KEY not set[/]")
        return

    questions = [
        json.loads(line).get("question")
        for line in questions_file.read_text().splitlines()
        if line.strip() and not line.strip().startswith("//")
    ]

    selected = random.sample(questions, min(num_questions, len(questions)))
    total = len(selected)

    console.print(f"[bold]Model:[/] [magenta]{model}[/]")
    console.print(
        f"Answering [bold]{total}[/] questions from [cyan]{questions_file}[/]"
    )

    with Mistral(api_key=api_key) as mistral:
        for i, question in enumerate(selected, 1):
            console.rule(f"[dim]{i}/{total}[/]")
            console.print(question, style="bold cyan")
            answer_and_display(mistral, model, question)


if __name__ == "__main__":
    main()
