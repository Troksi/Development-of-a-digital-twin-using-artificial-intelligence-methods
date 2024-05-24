import math
import numpy as np
from nltk import word_tokenize
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE
from rouge import Rouge
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

def calculate_perplexity(texts, n):
    tokenized_text = [list(map(str.lower, word_tokenize(text))) for text in texts]
    train_data, padded_vocab = padded_everygram_pipeline(n, tokenized_text)
    model = MLE(n)
    model.fit(train_data, padded_vocab)
    perplexity = model.perplexity(tokenized_text)
    return perplexity

def calculate_rouge(hypotheses, references):
    rouge = Rouge()
    scores = rouge.get_scores(hypotheses, references, avg=True)
    return scores

def calculate_bleu(hypotheses, references):
    smooth_fn = SmoothingFunction().method1
    scores = [sentence_bleu([ref.split()], hyp.split(), smoothing_function=smooth_fn) for hyp, ref in zip(hypotheses, references)]
    avg_score = np.mean(scores)
    return avg_score

# Example usage
texts = ["This is a sample sentence for evaluation.", "Another sample sentence."]
hypotheses = ["This is a generated sentence for evaluation."]
references = ["This is a reference sentence for evaluation."]
n = 3

perplexity = calculate_perplexity(texts, n)
rouge_scores = calculate_rouge(hypotheses, references)
bleu_score = calculate_bleu(hypotheses, references)

print(f"Perplexity: {perplexity}")
print(f"ROUGE scores: {rouge_scores}")
print(f"BLEU score: {bleu_score}")
