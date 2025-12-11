
import numpy as np

corpus = ["The quick brown fox jumped over the lazy dog.",
    "She sells seashells by the seashore.",
    "Peter Piper picked a peck of pickled peppers."]

unique_words = set()
for sent in corpus:
    for word in sent.split():
        unique_words.add(word.lower())

word_idx = {}
for i, word in enumerate(unique_words):
    word_idx[word] = i

one_hot_vector = []

for sent in corpus:
    sent_vectors = []
    for word in sent.split():
        vector = np.zeros(len(unique_words))
        vector[word_idx[word.lower()]] = 1
        sent_vectors.append(vector)
    one_hot_vector.append(sent_vectors)  # Fixed Indentation

# Verify Correctness
print(f"Number of sentences processed: {len(one_hot_vector)}")
assert len(one_hot_vector) == 3, f"Expected 3 sentences, got {len(one_hot_vector)}"

for i in range(len(corpus)): # Fixed Loop
    print(f"Sentence {i+1} length: {len(one_hot_vector[i])}")
    # Just checking first word match to be sure
    first_word = corpus[i].split()[0]
    first_vec = one_hot_vector[i][0]
    assert first_vec[word_idx[first_word.lower()]] == 1.0

print("Verification Passed!")
