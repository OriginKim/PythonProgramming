import os
import pickle

def input_scores():
    scores = []
    i = 1
    while True:
        score = int(input(f"#{i}? "))
        if score < 0:
            break
        scores.append(score)
        i += 1
    return scores

def get_average(scores):
    return sum(scores) / len(scores)

def show_scores(scores):
    print("\n[점수 출력]")
    print("개인점수:", *scores)
    print(f"평균: {get_average(scores):.1f}")

def save_scores(scores, filename="score.bin"):
    with open(filename, "wb") as file:
        pickle.dump(scores, file)

def load_scores(filename="score.bin"):
    with open(filename, "rb") as file:
        return pickle.load(file)


FILENAME = "score.bin"

if os.path.exists(FILENAME):
    print("[파일 읽기]")
    scores = load_scores(FILENAME)
else:
    scores = input_scores()
    save_scores(scores, FILENAME)

show_scores(scores)
