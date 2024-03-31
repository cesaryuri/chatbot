import re
import random
from nltk.chat.util import Chat, reflections

class FociChatbot(Chat):
    def __init__(self):
        super().__init__([], reflections)

    def add_response(self, input, output):
        if isinstance(output, str):
            o = [output]
        else:
            o = output
        self._pairs.append((re.compile(input, re.IGNORECASE), o))

    def converse(self):
        super().converse()

    def respond(self, input):
        return super().respond(input)

    def reset(self):
        self._pairs = []

f = FociChatbot()

f.add_response('Oi', 'Escolha o que quer fazer')
f.add_response('Tarefas', 'Refatorar código do robô sumô')
f.add_response('Tarefas', 'Estudar e resolver exercícios da lista de Sinais e Sistemas')
f.add_response('Compromissos', 'Ir a UABJ para reunião do PPE')
f.add_response('Compromissos', 'Aula de IA na AEB as 8h')
f.add_response('Compromissos', 'Aula de Sinais e Sistemas na AEB de 10h')

while True:
    user_input = input("Você: ")
    if user_input.lower() == "quit":
        break
    response = f.respond(user_input)
    print("Bot:", response)
