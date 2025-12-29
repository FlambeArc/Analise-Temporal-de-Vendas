import pandas as pd

vendas = {
    "data": ["2025-01-10", "2025-01-15", "2025-01-20", "2025-02-02", "2025-02-11", "2025-02-28", "2025-03-23", "2025-03-24", "2025-03-25"],
    "produto": ["caneta", "papel", "caneta", "borracha", "papel", "caneta", "borracha", "papel", "cola"],
    "valor": [2.5, 10, 3, 0.5, 15, 2.5, 0.5, 5, 7]
}

df = pd.DataFrame(vendas)
df.to_csv("data.csv", index=False)