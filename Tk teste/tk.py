import tkinter as tk

def main():
    global coelho
    global textozinho
    janela = tk.Tk()
    janela.title('Janelinha fofa')
    txt = tk.Label(janela, text='Aqui é uma janelinha fofa', font='Arial')
    txt2 = tk.Label(janela, text= 'Clique no botão para uma surpresa! ')
    txt.grid(column=0, row=0, padx= 200, pady= 20)
    txt2.grid(column=0, row=1)
    textozinho = tk.Label(janela, text= "")
    textozinho.grid(column=0, row=5, pady= 10)
    coelho = tk.Label(janela, text= "")
    coelho.grid(column=0, row=3, pady= 40, padx= 50)
    botao = tk.Button(janela, text= 'Botão Surpresa',command= coelha)
    botao.grid(column=0, row=2, padx= 40, pady= 10)    
    janela.mainloop()
    
def texto_fofo():
    txt = "Te amo mais que tudo, coelhosa <3"
    textozinho["text"] = txt

def coelha():
    coelhosa = '''         
                              __
                     /\    .-" /
                    /  ; .'  .' 
                   :   :/  .'   
                    \  ;-.'     
       .--""""--..__/     `.    
     .'           .'    `o  \   
    /                    `   ;  
   :                  \      :  
 .-;        -.         `.__.-'  
:  ;          \     ,   ;       
'._:           ;   :   (        
    \/  .__    ;    \   `-.     
     ;     "-,/_..--"`-..__)    
     '""--.._:                   '''
   
    coelho["text"] = coelhosa
    botao2 = tk.Button(text= "Clica de novo <3", command= texto_fofo)
    botao2.grid(column= 0, row= 4)
main()