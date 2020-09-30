def verbola (*valores):      # funcao(lista,bola), se tiver dentro retorna True
    if (valores[1] in valores[0]):
        return True
    
def insbola (*valores):     # funcao(bola,lista)
    valores[1].append(valores[0])
    
def delbola (*valores):     # funcao(bola, lista)
    valores[1].remove(valores[0])

def copiarlista (*valores): #funcao(lista a ser copiado,inicio do laço, linhas para pular a lista)
    lista = []
    for x in range (valores[1],len(valores[0]),valores[2]):
        lista.append(valores[0][x])
    return lista

def abrireinserir (numcartela): #funcao(numero da caretla) e retorna o (numero da cartela, a cartela, e a pontuação zerada).
    arquivo = open('cartela' + numcartela + '.txt', 'r')  
    for x in arquivo:
        lista = x.split()
    arquivo.close()
    return [numcartela,lista,0]

def maisponto(*valores): #funcao(bola,lista das compradas[[cartela,lista,pontos]])
    for x in valores[1]:
        if (verbola(x[1],valores[0])== True):
            x[2]+=1
            if x[2]>=2:
                print (f'A Cartela = {x[0]} falta {4-x[2]}  ')

def menosponto(*valores): #funcao(bola,lista das compradas[[cartela,lista,pontos]]) PRONTO.. 
    for x in valores[1]:
        if (verbola(x[1],valores[0])== True):
            x[2]-=1

def pergunta (*valores):  #funcão(resposta com S ou N)
    if valores[0].upper() == 'N': # se considerar como não comprada, apenas continue
        return False
    elif valores[0].upper() == 'S':
        return True
    else:
        x = input('Escreva um S(para sim) ou um N(para não).')
        pergunta(x)

def compras(*valores): #funcao(compra,compradas)
    if valores[0] in valores[1]:
        resposta = (input('Esta já foi comprada, deseja excluir?(S/N)'))
        if (pergunta(resposta) == True):
            delbola(valores[0],valores[1])
            
##################### inicio #####################

compradas=[] # lista de compradas zerada

# laço for para inserir as compradas
for cartela in range (1,6):
    resposta = (input(f'A cartela de numero {cartela} está comprada?(S/N)'))
    if (pergunta(resposta) == True):
        compradas.append(abrireinserir(str(cartela)))
       
###     formato da lista de compradas = [ [num, lista,pont] , [num, lista,pont]...]

sorteio=[] #zerar sorteio
print (compradas)

try:
    while True:
        bola = (input('Bola sorteada: '))
        if (verbola(sorteio,bola) == True):
            resposta = (input ('Bola já existe, deseja excluir?'))
            if (pergunta(resposta)== True):
                menosponto(bola,compradas)
                delbola(bola,sorteio)
            else:
                continue             
        else:
            insbola(bola,sorteio)
            maisponto(bola,compradas)
                
except KeyboardInterrupt:
    pass

print(sorteio,'\n',compradas)



