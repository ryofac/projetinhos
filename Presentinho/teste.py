from transformers import pipeline

frase_legal = str(input('Diga uma coisa massa: '))

classificador = pipeline("sentiment-analysis")
print(classificador(frase_legal))
     