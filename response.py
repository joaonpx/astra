from textblob import TextBlob

def generateResponse(message):
    testimonial = TextBlob(message)

    if testimonial.sentiment.polarity > 0.5:
        return "I'm happy for that!"
    elif testimonial.sentiment.polarity < -0.5:
        return "Sinto muito que você esteja se sentindo assim."
    else:
        return "Não entendi o que você quis dizer. Poderia reformular a sua pergunta?"