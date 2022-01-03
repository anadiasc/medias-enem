# Programa que calcula a média aritimética e ponderada de notas obtidas no ENEM

invalid_input = True

def start() :

    print("Bem-vindo, vamos calcular médias? Insira as notas de cada disciplina abaixo:")

    notaling = float(input("Nota Linguagens = "))
    notaHum = float(input("Nota Humanas = "))
    notaNat = float(input("Nota Natureza = "))
    notaMat = float(input("Nota Matemática = "))
    notaRed = float(input("Nota Redação = "))


    escolha = int(input("Para cáculo de média aritimética, digite 1. Para cáculo de média ponderada, digite 2 = "))

    if escolha == 1:
        somaNotas = notaHum + notaling + notaMat + notaNat + notaRed
        
        mediaArit = (somaNotas) / 5
        
        print("Sua média aritimética é = %.2f " % mediaArit)
        invalid_input = False

    elif escolha == 2:
        pesoling = int(input("Peso Linguagens = "))
        pesoNat = int(input("Peso Natureza = "))
        pesoHum = int(input("Peso Humanas = "))
        pesoMat = int(input("Peso Matemática = "))
        pesoRed = int(input("Peso Redação = "))

        somaPesos = pesoling + pesoRed + pesoNat + pesoMat + pesoHum

        mediaPond = (notaHum * pesoHum + notaMat * pesoMat + notaNat * pesoNat + notaRed * pesoRed + notaling * pesoling) / somaPesos

        print("Sua média ponderada é = %.2f " % mediaPond)
        invalid_input = False

    else:
        print("Escolha uma opção válida")

while invalid_input:
    start()
    