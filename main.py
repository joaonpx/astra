from art import tprint

import pyttsx3

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement

from response import generateResponse

# -*- coding: utf-8 -*-

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

    messageStatement = Statement(userMessage.capitalize())

    response = generateResponse(messageStatement)

    if userMessage.upper() == "TCHAU":
        print("Astra: até mais!")

        # en = pyttsx3.init() 
        # en.say("até mais!")
        # en.runAndWait()

        break
    else:
        print(f"Astra: {response}")

        # en = pyttsx3.init() 
        # en.say(response)
        # en.runAndWait()