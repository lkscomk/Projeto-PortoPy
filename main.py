from code import InteractiveConsole
import sys
from googletrans import Translator
import json

translator = Translator()


#essa função recebe o codigo .ppy (arquivo portopy) e retorna um codigo .py (python)
def codificacao(code, **options):
    compilacao = options.get('compilacao')

    #essa parte ira indentificar todos os aspas simples e duplos presentes no arquivo
    variaveis = []
    for x in range(len(code)):
        if code[x] == "'" or code[x] == '"':
            variaveis.append(x)

    #essa parte ira agrupar em duplas todos as aspas simples ou duplas do codigo e criarndo um codigo para cada dupla de aspas
    imutaveis = []
    for y in range(0, len(variaveis), 2):
        imutaveis.append(
            ['000' + str(y), [variaveis[y], variaveis[y + 1] + 1]])

    # essa parte sera responsavel por subistituir os strings pelos codigos criados
    codigoAlt = code
    for r in range(len(imutaveis)):
        codigoAlt = codigoAlt.replace(
            code[imutaveis[r][1][0]:imutaveis[r][1][1]], str(imutaveis[r][0]),
            1)

    # essa parte sera responsavel por subistituir os comandos PortoPy por os comandos python
    if compilacao == True or compilacao == None:
        #codigoAlt = codigoAlt.replace("escrever", "print").replace("entrar", "input").replace("e se", "elif").replace("se", "if").replace("ifnao", "else").replace("inteiro", "int").replace(" e ", " and ")
        codigoAlt = reposicionar(codigoAlt)
    else:
        codigoAlt = codigoAlt.replace("print", "escrever").replace(
            "input",
            "entrar").replace("if", "se").replace("elif", "e if").replace(
                "else", "ifnao").replace("int",
                                         "inteiro").replace(" and ", " e ")

    #essa parte sera responsavel por subistiuir os codigos criados por seus respectivos valores
    final = codigoAlt
    for r in range(len(imutaveis)):
        final = final.replace(str(imutaveis[r][0]),
                              code[imutaveis[r][1][0]:imutaveis[r][1][1]], 1)
    return final


def reposicionar(script):
    try:
        reservados = open('comandos.json')
        obj = json.loads(reservados.read())
        comandos = obj['reservadas']
    except FileNotFoundError as erro:
        nameErro = translator.translate("File Not Found Error", dest='pt')
        descricaoErro = translator.translate(erro, dest='pt')
        print(nameErro.text + ": " + codificacao(descricaoErro.text))
        sys.exit()
    else:
        for x in range(len(comandos)):
            #print(comandos[x][0], comandos[x][1])
            script = script.replace(comandos[x][1], comandos[x][0])
        return script


try:
    meuArquivo = open('scripts.txt')
    temp = open('temp.txt', 'w')
    code = meuArquivo.read()
except FileNotFoundError as erro:
    nameErro = translator.translate("File Not Found Error", dest='pt')
    descricaoErro = translator.translate(erro, dest='pt')
    print(nameErro.text + ": " + codificacao(descricaoErro.text))
    sys.exit()

try:
    exec(codificacao(code, compilacao=True))
    #InteractiveConsole().runcode(final)
except ValueError as erro:
    nameErro = translator.translate("Value Error", dest='pt')
    descricaoErro = translator.translate(erro, dest='pt')
    print(nameErro.text + ": " + codificacao(descricaoErro.text))
    sys.exit()
except NameError as erro:
    nameErro = translator.translate("Name Error", dest='pt')
    descricaoErro = translator.translate(erro, dest='pt')
    print(nameErro.text + ": " + codificacao(descricaoErro.text))
    sys.exit()
except IndentationError as erro:
    descricaoErro = translator.translate(erro, dest='pt')
    print("Erro de indentação: " + codificacao(descricaoErro.text))
    sys.exit()
except SyntaxError as erro:
    nameErro = translator.translate("Syntax Error", dest='pt')
    descricaoErro = translator.translate(erro, dest='pt')
    print(nameErro.text + ": " +
          codificacao(str("'") + descricaoErro.text + str("'")))
    sys.exit()
