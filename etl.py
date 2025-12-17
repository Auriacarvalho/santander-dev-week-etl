import pandas as pd
import json

# ===== EXTRACT (MOCK) =====

df = pd.read_csv("SDW2023.csv")
user_ids = df["UserID"].tolist()

users = [
    {
        "id": 1,
        "name": "Ana",
        "news": []
    },
    {
        "id": 2,
        "name": "Carlos",
        "news": []
    },
    {
        "id": 3,
        "name": "Marina",
        "news": []
    }
]

print("Usuários simulados:")
print(json.dumps(users, indent=2, ensure_ascii=False))

# ===== TRANSFORM =====

def generate_news(user):
    return f"{user['name']}, investir hoje é o caminho para um futuro financeiro seguro."

for user in users:
    user["news"].append({
        "icon": "credit.svg",
        "description": generate_news(user)
    })

print("\nUsuários após transformação:")
print(json.dumps(users, indent=2, ensure_ascii=False))

# ===== LOAD (SIMULADO) =====

print("\nCarga simulada concluída com sucesso.")

