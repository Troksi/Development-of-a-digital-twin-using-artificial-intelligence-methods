from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

def calculate_bleu(hypotheses, references):
    smooth_fn = SmoothingFunction().method1
    scores = [sentence_bleu([ref.split()], hyp.split(), smoothing_function=smooth_fn) for hyp, ref in zip(hypotheses, references)]
    avg_score = np.mean(scores)
    return avg_score

# Example usage
hypotheses = ["This is a generated sentence for evaluation."]
references = ["This is a reference sentence for evaluation."]
bleu_score = calculate_bleu(hypotheses, references)
print(f"BLEU score: {bleu_score}")
