from ollama_client import ask_oska

print("OSKA AI")
print("Enterprise Intelligence Without the Cloud")

question = input("\nAsk OSKA: ")

print("\nThinking...")

answer = ask_oska(question)

print("\nOSKA:")
print(answer)