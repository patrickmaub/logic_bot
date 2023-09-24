# Logic Bot

Logic Bot is an intelligent question-answering program designed to help users learn all of the content from a series of logic-related textbook files (Logic_1.pdf through Logic_7.pdf). The program uses OpenAI's GPT-4 model and cosine similarity measures to find the most relevant answers to users' questions.

## Features
- Utilizes the GPT-4 model to generate text responses based on user input
- Computes cosine similarity between input questions and textbook embeddings to find closest match
- Provides contextual references (file name and page number) for the generated answers
- Automatically trims message history to maintain a manageable chat environment

## Dependencies
- numpy
- PyPDF2
- openai
- re
- ast (used for 'literal_eval' function)

You must install these via `pip install` to use Logic Bot.

## How to Use
1. Make sure all dependencies have been installed.
2. Provide your OpenAI API key by setting the `OPENAI_API_KEY` environment variable.
3. Ensure that the textbook embeddings are available in "embeddings.txt" file format.
4. Run the script (make sure the file names have the correct extensions), and start asking questions.

When you run the program, a message history will be saved to facilitate further discussion and context. You can interact with the bot by entering questions into the terminal.

### Example Usage

```python
Enter a question: What is a tautology?

From file: Logic_2.pdf
Page: 11
A tautology is a statement that is true no matter what its terms are. In other words, it is always true under every interpretation. In contrast, a contradiction is a statement that is false no matter what its terms are. Examples of tautologies include "P or ~P" and "P implies P," where P stands for a propositional variable.
```

## Functions

The code consists of multiple functions to handle different tasks:

- **cosine_similarity(a, b)**: Calculate the cosine similarity between two vectors 'a' and 'b'.
- **turbo(prompt, tokens=2000, messages=[], temperature=0.7, system="", model="gpt-4", stream=False)**: Call OpenAI API with the given parameters to generate a response (used GPT-4) based on the user's input.
- **get_embedding(text, model="text-embedding-ada-002")**: Get the embedding of the given text using the specified OpenAI model.
- **split_content(content, enc, max_length=2048)**: Split the given content into chunks of 'max_length' tokens.
- **read_text_file(file_path)**: Read text from a file and return the contents.
- **read_file(file_path: str) -> str**: Read a file and return the content.

## Limitations
- Make sure the file names have the correct extensions, otherwise the program may not work properly.
- The quality of the answer depends on the accuracy and relevance of the textbook embeddings.
- Cosine similarity has its limitations for understanding semantic relationships between embeddings; more advanced techniques might improve the relevance of the generated response.
- The program has a token limit of 2000 tokens, so longer and more detailed answers might be truncated or not generate the best explanation.

## Final Thoughts

Logic Bot is an example of utilizing natural language processing (NLP) and artificial intelligence (AI) for providing automated support in learning a subject. The program can be modified and improved based on the user's preferences, educational materials, and desired outcomes. Please ensure you have the appropriate API Key and permission to use GPT-4 for educational support purposes.
