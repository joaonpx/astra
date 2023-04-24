from art import tprint

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement

from response import generateResponse

import logging  

logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)

bot = ChatBot("Astra")

trainer = ChatterBotCorpusTrainer(bot)
trainer.train(
    "chatterbot.corpus.portuguese"
)

print("\n-------------------------------------------------------")
tprint("astra", font="sub-zero")
print("-------------------------------------------------------")

print('\nPara finalizar a conversa digite "tchau".\n')

while True:
    userMessage = input("Você: ")

    messageStatement = Statement(userMessage)

    response = generateResponse(messageStatement)

    if userMessage.upper() == "TCHAU":
        print("Astra: até mais!")
        break
    else:
        print(f"Astra: {response}")