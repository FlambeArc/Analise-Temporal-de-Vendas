import pandas as pd

df = pd.read_csv("data/data.csv")
df["data"] = pd.to_datetime(df["data"])
df = df.set_index("data")

df["media_movel"] = df["valor"].rolling(window=3).mean()
vendas_Mensais = df.resample("M")["valor"].sum()

df["mes"] = df.index.month
table = pd.pivot_table(
    df,
    values="valor",
    index="mes",
    columns="produto",
    aggfunc="sum"
)

Q1 = df["valor"].quantile(0.25)
Q3 = df["valor"].quantile(0.75)
IQR = Q3 - Q1
lim_inf = Q1 - 1.5 * IQR
lim_sup = Q3 + 1.5 * IQR
outliers = df[(df["valor"] < lim_inf) | (df["valor"] > lim_sup)]

print(df)
print("")
print(vendas_Mensais)
print("")
print(table)
print("")
print(outliers)

df.to_csv("resultado_completo.csv")
vendas_Mensais.to_csv("vendas_mensais.csv")
outliers.to_csv("outliers_detectados.csv")
