SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

while True:
    adjective = input("Please type an adjective and press enter. ").strip()
    if adjective: break  # Ensure user enters something

while True:
    noun = input("Please type a noun and press enter. ").strip()
    if noun: break

while True:
    verb = input("Please type a verb and press enter. ").strip()
    if verb: break

print(f"{SENTENCE_START} {adjective} {noun} {verb}!")