def quadrado(x): #Funcao que ira retornar o quadrado de um nuemro 'x' que passei
    return x * x

def main():
    for i in range(10):
        print("{} ao quadrado é: {}".format(i, quadrado(i)))


if __name__ == "__main__": #Em outras palavras, essa linha quer dizer "Se eu estiver rodando esse arquivo em particular, execute a funcao main, caso contrario, nao execute"
    main()
