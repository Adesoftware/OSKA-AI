import requests

def ask_oska(prompt):
    url = "http://127.0.0.1:11434/api/generate"

    payload = {
    "model": "qwen2.5:1.5b",
    "prompt": prompt,
    "stream": False,
      "options": {
        "num_predict": 250,
        "temperature": 0.4
    }
    
}

    try:
        response = requests.post(url, json=payload, timeout=120)

        data = response.json()

        print("DEBUG:", data)

        return data.get("response", "No response received.")

    except Exception as e:
        return f"Error: {e}"