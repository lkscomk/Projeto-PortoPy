# !/usr/bin/python3
from tkinter import *
import json


root = Tk()
text = Text(root, font=('Courier New', 10))
butt = Button(root, text='Rodar')
text.insert(END, "Bye Bye.....\nBye Bye.....\nBye print.....\nBye Bye.....\nBye Bye.....\n")
text.pack()
butt.pack()
global tags
tags = []

def escrevendo(e=''):
    texto = text.get('1.0', END)
    code = text.get('1.0', END)
    local = 0
    colunas = []

    variaveis = []
    for x in range(len(code)):
        if code[x] == "'" or code[x] == '"':
            variaveis.append(x)

    #essa parte ira agrupar em duplas todos as aspas simples ou duplas do codigo e criarndo um codigo para cada dupla de aspas
    imutaveis = []
    for y in range(0, len(variaveis), 2):
        imutaveis.append(['000' + str(y), [variaveis[y], variaveis[y + 1] + 1]])

    # essa parte sera responsavel por subistituir os strings pelos codigos criados
    codigoAlt = code
    for r in range(len(imutaveis)):
        codigoAlt = codigoAlt.replace(code[imutaveis[r][1][0]:imutaveis[r][1][1]], str(imutaveis[r][0]), 1)

    for x in range(len(codigoAlt)):
        if codigoAlt[x:x+1] == "\n":
            colunas.append([codigoAlt[local:x+1]])
            local = x + 1

        for y in range(len(colunas)):
            reservados = open('comandos.json')
            obj = json.loads(reservados.read())
            comandos = obj['reservadas']
            for x in range(len(comandos)):
                try:
                    text.tag_config(comandos[x][0], foreground = "#000000")
                except:
                    pass
            for x in range(len(comandos)):
                text.configure(foreground = "#000000")
                linhas = colunas[y][0].find(comandos[x][0])
                if linhas != -1:
                    ini = str(y+1)+"."+str(linhas)
                    fim = str(y+1)+"."+str(linhas + len(comandos[x][0]))
                    text.tag_add(str('ab'+str(x)), ini, fim)
                    text.tag_config(str('ab')+str(x), foreground = "#ff7700")
                    
    for r in range(len(imutaveis)):
        codigoAlt = codigoAlt.replace(str(imutaveis[r][0]), code[imutaveis[r][1][0]:imutaveis[r][1][1]], 1)
    print(codigoAlt)
            
def alteracoes(e):
    root.after(1, lambda: escrevendo())



text.bind("<Any-KeyPress>", alteracoes)
root.mainloop()
