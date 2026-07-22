from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/stsb-roberta-base")

pairs = [
    # Financials
    ("Regional Banks: retail banking lending deposits customers",
     "Deposits from customers"),
    ("Regional Banks: retail banking lending deposits customers",
     "Allowance account for credit losses of financial assets"),
    # Energy
    ("Oil Gas Drilling: drilling exploration production",
     "Revenue from sale of crude oil"),
    ("Oil Gas Drilling: drilling exploration production",
     "Fuel and energy expense"),
    # Consumer
    ("Consumer Electronics: televisions phones laptops tablets",
     "Research and development expense"),
    ("Consumer Electronics: televisions phones laptops tablets",
     "Warranty provision"),
]
scores = model.predict(pairs)
for (si, tag), score in zip(pairs, scores):
    print(f"{score:.3f}  {si[:35]} → {tag[:40]}")