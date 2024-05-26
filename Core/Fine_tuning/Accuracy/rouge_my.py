from rouge import Rouge

def calculate_rouge(hypotheses, references):
    rouge = Rouge()
    scores = rouge.get_scores(hypotheses, references, avg=True)
    return scores

# Example usage
hypotheses = ["This is a generated sentence for evaluation."]
references = ["This is a reference sentence for evaluation."]
rouge_scores = calculate_rouge(hypotheses, references)
print(f"ROUGE scores: {rouge_scores}")
