import math
import numpy as np
from nltk import word_tokenize
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE

def calculate_perplexity(texts, n):
    # Tokenize the text
    tokenized_text = [list(map(str.lower, word_tokenize(text))) for text in texts]
    
    # Prepare the data for the language model
    train_data, padded_vocab = padded_everygram_pipeline(n, tokenized_text)
    
    # Train the language model
    model = MLE(n)
    model.fit(train_data, padded_vocab)
    
    # Compute perplexity
    perplexity = model.perplexity(tokenized_text)
    return perplexity

# Example usage
texts = ["This is a sample sentence for evaluation.", "Another sample sentence."]
n = 3
perplexity = calculate_perplexity(texts, n)
print(f"Perplexity: {perplexity}")
