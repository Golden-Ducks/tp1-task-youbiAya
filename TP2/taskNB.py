vocab = ["feel", "good", "better", "thank", "happened"]

docs = {
    "D1": (["feel", "good"], "Positive"),
    "D2": (["feel", "better", "thank"], "Positive"),
    "D3": (["happened", "good"], "Negative")
}


counts = {"Positive": {w:0 for w in vocab}, "Negative": {w:0 for w in vocab}}
totals = {"Positive":0, "Negative":0}

for words, label in docs.values():
    for w in words:
        counts[label][w] += 1
        totals[label] += 1


priors = {"Positive": 2/3, "Negative": 1/3}


def naive_bayes(doc):
    scores = {}

    for label in ["Positive", "Negative"]:
        prob = priors[label]

        for w in doc:
            likelihood = (counts[label][w] + 1) / (totals[label] + len(vocab))
            prob *= likelihood

        scores[label] = prob

    return max(scores, key=scores.get), scores


tests = [
    ["feel", "good"],
    ["feel", "better", "thank"],
    ["happened", "good"]
]

for t in tests:
    label, scores = naive_bayes(t)
    print("Predicted:", label)
    print("Scores:", scores)