import threading
import itertools
import time
from ollama_client import ask_oska
from prompts import business_letter_prompt, memo_prompt, summarize_prompt

def thinking_animation():
    for c in itertools.cycle([".", "..", "..."]):
        if stop_animation:
            break
        print(f"\rOSKA is thinking{c}", end="", flush=True)
        time.sleep(0.5)

print("=" * 50)
print("OSKA AI")
print("Offline Smart Knowledge Assistant")
print("Enterprise Intelligence Without the Cloud")
print("=" * 50)

print("\n1. Business Letter")
print("2. Memo Generator")
print("3. Text Summarizer")
print("4. General AI Chat")

choice = input("\nSelect option (1-4): ")

if choice == "1":
    topic = input("Enter letter topic: ")
    prompt = business_letter_prompt(topic)

elif choice == "2":
    topic = input("Enter memo topic: ")
    prompt = memo_prompt(topic)

elif choice == "3":
    text = input("Paste text to summarize: ")
    prompt = summarize_prompt(text)

elif choice == "4":
    prompt = input("Ask OSKA: ")

else:
    print("Invalid option.")
    exit()

stop_animation = False

animation_thread = threading.Thread(target=thinking_animation)
animation_thread.start()

answer = ask_oska(prompt)

stop_animation = True
animation_thread.join()
print("\r" + " " * 40, end="")  # clear line
print("\rOSKA:")
print(answer)
input("\nPress Enter to exit...")