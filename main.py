import pandas as pd

dados = {
    "Nome": ["João", "Maria", "Pedro"],
    "Cargo": ["Dev", "Analista", "Suporte"],
    "Salário": [4000, 4500, 3000]
}

df = pd.DataFrame(dados)
print(df)