from chatterbot import ChatBot

bot = ChatBot("Astra")

def generateResponse(message):
    response = bot.generate_response(message)

    return response