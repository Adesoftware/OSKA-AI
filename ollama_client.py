import requests

def ask_oska(prompt):
    url = "http://127.0.0.1:11434/api/generate"

    payload = {
        "model": "qwen2.5:3b",
        "prompt": prompt,
        "stream": True
    }

    try:
        response = requests.post(url, json=payload, timeout=300)

        data = response.json()

        return data.get("response", "No response received.")

    except Exception as e:
        return f"Error: {e}"