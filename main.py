from art import tprint
from response import generateResponse

tprint("astra", font="sub-zero")

print('To end the conversation type "goodbye".')

while True:
    userMessage = input("You: ")

    response = generateResponse(userMessage)

    if userMessage.upper() == "GOODBYE":
        print("Astra: Goodbye! See you tomorow.")
        break
    elif userMessage.upper() == "ASTRA":
        print("Astra: Hi! How can I help you?")
    else:
        print(f"Astra: {response}")