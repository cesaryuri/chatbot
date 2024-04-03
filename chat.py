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

    def reset(self):

        self._pairs = []

    def lerarray(self, entrada):
        for texto in self._pairs:
            if texto[0].pattern.lower() == entrada.lower():
                print(''.join(texto[1]))

f = FociChatbot()

f.add_response('Oi', 'Digite Tarefas ou Compromissos')
f.add_response('Tarefas', 'Refatorar código do robô sumô')
f.add_response('Tarefas', 'Estudar e resolver exercícios da lista de Sinais e Sistemas')
f.add_response('Tarefas', 'Desenvolver chatbot baseado no código fornecido')
f.add_response('Compromissos', 'Ir a UABJ para reunião do PPE')
f.add_response('Compromissos', 'Aula de IA na AEB as 8h')
f.add_response('Compromissos', 'Aula de Sinais e Sistemas na AEB de 10h')
f.add_response('Compromissos', 'Ir a aula de sistemas embarcados na AEB de 8h as 10h')
f.add_response('Compromissos', 'Ir a aula de IA na AEB de 10h as 12h')

while True:
    user_input = input("Você: ")
    if user_input.lower() == "quit":
        break

    f.lerarray(user_input)