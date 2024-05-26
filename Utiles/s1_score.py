import json
import math
import numpy as np
from nltk import word_tokenize
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE
from rouge import Rouge
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import os
import sys

# Faild
def calculate_perplexity(texts, n):
    tokenized_text = [list(map(str.lower, word_tokenize(text))) for text in texts]
    train_data, padded_vocab = padded_everygram_pipeline(n, tokenized_text)
    model = MLE(n)
    model.fit(train_data, padded_vocab)
    perplexity = model.perplexity(tokenized_text)
    return perplexity

def ter(reference, hypothesis):
    """
    Calculate Translation Edit Rate (TER).

    Args:
    reference (str): The reference translation.
    hypothesis (str): The hypothesis translation.

    Returns:
    float: The TER score.
    """
    # Initialize the variables
    n = len(reference.split())
    m = len(hypothesis.split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize the DP table
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # Compute TER using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if reference.split()[i - 1] == hypothesis.split()[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i][j - 1] + 1, dp[i - 1][j] + 1)

    # Return the TER score
    return dp[n][m] / max(n, m)

def calculate_rouge(hypotheses, references):
    rouge = Rouge()
    scores = rouge.get_scores(hypotheses, references, avg=True)
    return scores

def calculate_bleu(hypotheses, references):
    smooth_fn = SmoothingFunction().method1
    scores = [sentence_bleu([ref.split()], hyp.split(), smoothing_function=smooth_fn) for hyp, ref in zip(hypotheses, references)]
    avg_score = np.mean(scores)
    return avg_score

def read_json_file(file_path):
    if not os.path.exists(os.path.abspath(file_path)):
        print(f'Not found: {os.path.abspath(file_path)}')

    with open(os.path.abspath(file_path), 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def process_responses(data, reference, hypotheses):
    processed_data = []

    for item in data:
        request_text = item.get('request', '')
        response_1 = item.get(reference, '')
        response_2 = item.get(hypotheses, '')

        score_bleu = calculate_bleu([response_2], [response_1]) # calculate_bleu(hypotheses, references)
        score_ter = ter(response_1, response_2) # ter(reference, hypothesis) TER
        calculated_rouge = calculate_rouge(response_2, response_1) # calculate_rouge(hypotheses, references) ROUGE
        score_roug_1_r = calculated_rouge['rouge-1']['r']
        score_roug_1_p = calculated_rouge['rouge-1']['p']
        score_roug_1_f = calculated_rouge['rouge-1']['f']
        score_roug_2_r = calculated_rouge['rouge-2']['r']
        score_roug_2_p = calculated_rouge['rouge-2']['p']
        score_roug_2_f = calculated_rouge['rouge-2']['f']
        score_roug_l_r = calculated_rouge['rouge-l']['r']
        score_roug_l_p = calculated_rouge['rouge-l']['p']
        score_roug_l_f = calculated_rouge['rouge-l']['f']

        processed_data.append({
            "request": request_text,
            "metrics": [
                {
                    "name": "BLEU",
                    "ref": reference,
                    "hyp": hypotheses,
                    "score": score_bleu
                },
                {
                    "name": "TER",
                    "ref": reference,
                    "hyp": hypotheses,
                    "score": score_ter
                },
                {
                    "name": "ROUGE",
                    "ref": reference,
                    "hyp": hypotheses,
                    "score": [
                        {
                            "name": "rouge-1",
                            "r": score_roug_1_r,
                            "p": score_roug_1_p,
                            "f": score_roug_1_f
                        },
                        {
                            "name": "rouge-2",
                            "r": score_roug_2_r,
                            "p": score_roug_2_p,
                            "f": score_roug_2_f
                        },
                        {
                            "name": "rouge-l",
                            "r": score_roug_l_r,
                            "p": score_roug_l_p,
                            "f": score_roug_l_f
                        }
                    ]
                }
            ]
        })

    return processed_data

def save_processed_data(file_path, processed_data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
     #\Utiles\telegram_messages_OkYasno\Datas\mv_result.json
    input_file_path = r'Utiles\telegram_messages_OkYasno\Datas\mv_result.json'
    output_file_path = r'Utiles\telegram_messages_OkYasno\Datas\mv_result_score_ref.json'
    
    data = read_json_file(input_file_path)
    processed_data = process_responses(data,'ref','ref')
    save_processed_data(output_file_path, processed_data)
#c:\Users\user\Documents\Yniver\Magistratura\Diplom_M\DDT\Development-of-a-digital-twin-using-artificial-intelligence-methods\Utiles

# import os

# def read_json_file(file_path):
#     # Проверка пути
#     print(f"Проверка пути: {file_path}")
#     absolute_path = os.path.abspath(file_path)
#     print(f"Абсолютный путь: {absolute_path}")

#     # Проверка существования файла
#     if not os.path.exists(file_path):
#         raise FileNotFoundError(f"Файл не найден по пути: {file_path}")
    
#     with open(file_path, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#     return data

# if __name__ == "__main__":
#     input_file_path = 'telegram_messages_OkYasno\\Datas\\mv_result.json'
    
#     try:
#         data = read_json_file(input_file_path)
#         print("Файл успешно прочитан.")
#     except FileNotFoundError as e:
#         print(e)
