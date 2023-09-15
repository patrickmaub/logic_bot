import csv
from ast import literal_eval
from typing import List, Dict
import PyPDF2
import json
import openai
import numpy as np
import re
imoprt os
openai.api_key = os.environ.get("OPENAI_API_KEY")


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def turbo(prompt, tokens=2000, messages=[], temperature=0.7, system="", model="gpt-4", stream=False):
    response = openai.ChatCompletion.create(
        model=model, messages=[{"role": "system", "content": system}] + messages + [{"role": "user", "content": prompt}], temperature=temperature, stream=stream)
    if stream:
        return response
    return response['choices'][0]['message']['content']


def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    try:
        return openai.Embedding.create(input=[text], model=model)['data'][0]['embedding']
    except Exception as e:
        print(f'Error getting embedding for {text}: {e}')
        return None


def split_content(content, enc, max_length=2048):
    import time
    time_start = time.time()
    # Split the content into chunks of max_length tokens
    content_tokens = enc.encode(content)
    content_chunks = [content_tokens[i:i+max_length]
                      for i in range(0, len(content_tokens), max_length)]
    content_text_chunks = [enc.decode(chunk) for chunk in content_chunks]
    time_end = time.time()
    print(
        f'Splitting content into {len(content_text_chunks)} chunks took {time_end - time_start} seconds.')
    return content_text_chunks


def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        content = file.read()
    return content


textbook = literal_eval(read_file("embeddings.txt"))

# accept a user input

messages = [{"role": "system",
             "content": "You are an expert in logic. You are a professional tutor as well. You are teaching a user who has a strong background in computer science so you know that you can often explain things in computer science terms to have the user understand faster. You need to help the user learn all of the content from Logic_1.pdf through Logic_7.pdf. You cite your context with its file_name and page_number."}]

while True:
    user_input = input("Enter a question: ")

    input_embedding = get_embedding(user_input)

# compare the user input to the textbook embeddings

# find the closest match

# return the answer

# print(input_embedding)
    similarity_scores = []

    for i in range(len(textbook)):
        similarity_scores.append(
            cosine_similarity(input_embedding, textbook[i]['embedding']))

# sort the similarity scores
    sorted_similarity_scores = sorted(similarity_scores, reverse=True)

# find the index of the highest 2 scores and then put them into a string
    index1 = similarity_scores.index(sorted_similarity_scores[0])
    combined = "From file:" + textbook[index1]['file_name'] + \
        '\n' + 'Page: ' + str(textbook[index1]['page_number'])  # + \

    while len(messages) > 10:
        messages.pop(0)
    messages.append(
        {"role": "user", "content": f"Context: {combined}\nQuestion: {user_input}"})
    final_response = ''
    response = turbo(user_input, tokens=256, messages=messages,
                     model="gpt-4", stream=True)
    for resp in response:
       # print(resp)
        try:
            rsp = resp['choices'][0]['delta']['content'].replace('\n', ' ')

            final_response += resp['choices'][0]['delta']['content']
            print('\n\n' + final_response + '\n\n')
        except:
            pass
    messages.append({"role": "user", "content": final_response})
