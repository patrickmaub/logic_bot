import re
import json


def process_file(file_path, answers=False):
    with open(file_path, "r") as file:
        content = file.read()

    if (answers == False):
        chapters = content.split("EXERCISES FOR CHAPTER")
    if(answers):
        chapters = content.split("ANSWERS TO EXERCISES FOR CHAPTER")

    exercise_sets = []
   # print(len(chapters))
    for i, chapter in enumerate(chapters):

        if chapter:
            if len(chapter) < 100:
                continue
            splitted = chapter.split("EXERCISE SET")
            # print(len(splitted
            for j, exercise_set in enumerate(splitted):

                if exercise_set:
                    if len(exercise_set) < 100:
                        continue
                    # print(exercise_set)
                    problems = {}
                    for match in re.finditer(r'(\d+)\.\s*[\r\n]*(.*?)(?=\s*\d+\. |\n|$)', exercise_set, re.DOTALL):
                        problem_number = int(match.group(1))
                        problem_text = match.group(2).strip()
                        problems[problem_number] = problem_text
                    exercise_sets.append(problems)

    return exercise_sets


def write_to_json_file(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)


exercises_data = process_file("exercises.txt")
answers_data = process_file("answers.txt", answers=True)

for i in range(len(exercises_data)):

    print(exercises_data[i])
