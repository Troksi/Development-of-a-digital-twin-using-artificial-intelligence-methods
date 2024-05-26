import math
import numpy as np
from nltk import word_tokenize
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE
from rouge import Rouge
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

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

# import sacrebleu

# def calculate_bleu(refs, hyps):
#     return sacrebleu.corpus_bleu(hyps, refs)


# # Example usage
# texts = ["This is a sample sentence for evaluation.", "Another sample sentence."]
hypotheses = "This is a generated sentence for evaluation."
references = "This is a reference sentence for evaluation."
# n = 2

# # perplexity = calculate_perplexity(texts, n)

# # print(f"Perplexity: {perplexity}")
res_roug = calculate_rouge(hypotheses, references)['rouge-1']
print(f'ROUGE scores: {res_roug}')
print(f'ROUGE scores: {calculate_rouge(hypotheses, hypotheses)}')
print(f"BLEU score: {calculate_bleu(hypotheses, references)}")
print(f"BLEU score: {calculate_bleu([hypotheses], [hypotheses])}")

# Example usage:
reference = "the cat sat on the mat"
hypothesis = "a cat sat on a mat"
print("TER:", ter(reference, hypothesis))
print("TER:", ter(reference, reference))


# import nltk
# nltk.download('punkt')