import random

R_EATING = "Eu amo pizza! e você?"

R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"

def unknown():

    response = ["Me desculpe, não te entendi. ",

                "...",

                "Pode repetir? não entendi",

                "Não entendi"][

        random.randrange(4)]

    return response
