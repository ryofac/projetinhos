from funtions import *
from time import sleep

def main():
    chatbot('Olá, sou o Olá bot , gostaria de conhecer melhor!')
    nome = str(input('Qual o seu nome?'))
    chatbot(f'Olá, {nome} prazer em te conhecer!')

def chatbot(texto):
    printslow("OLABOT: " + texto)
    
def printslow(texto, velocidade = 0.06): # função para escrever o texto lentamente
    for letra in texto: # loop for: variável letra recebe cada letra em texto
        print(letra, end='', flush=True) # end ='': não quebra a linha e não tem espaço entre as letras
        # flush: Não deixa o buffer renderizar a string toda
        sleep(velocidade) # Atraso de 0.04seg entre cada letra
    print('\n')
if __name__ == '__main__':
    main()