import anthropic
from dotenv import load_dotenv
import os
from prompt_pascal import V4_RIGOUREUX

load_dotenv()

api_key= os.environ.get("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(api_key=api_key)


PASCAL_PROMPT_V1 = """Tu es Blaise Pascal, mathématicien et philosophe français du XVIIe siècle.
Réponds en restant dans le personnage."""

questions = [
    "Qui es-tu ?",
    "Que penses-tu de Dieu ?",
]
def ask_pascal(question):
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        system=V4_RIGOUREUX,
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return message.content[0].text

for  q in questions:
    print({"❓", q})
    print(ask_pascal(q))
