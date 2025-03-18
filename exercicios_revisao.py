import math

# 1. Faça uma função que receba o nome de uma pessoa como entrada e retorne uma saudação.
# Exemplo:
# Boa tarde, Samuel. Seja bem vindo!
def saudacao(nome):
   msg = f"Boa tarde, {nome}. Seja bem vindo!"
   return msg
# 2. Faça uma função que peça o raio de um círculo e retorne sua área.
def area_circulo(raio):
    area = math.pi*math.pow(raio, 2)
    return area

# 3. Faça uma função que converta a temperatura de Fahrenheit para Celsius.
# C = 5 * ((F-32) / 9).
def fahrenheit_para_celsius(F):
    C = (F - 32) * 5/9
    return C

F = 32
C = fahrenheit_para_celsius(F)

# 4. Faça uma função que calcule a multa por excesso de peso de peixes.
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça uma funçao que receba como 
# entrada o peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite 
# e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
# Exemplos de saidas para os parâmetros 70 e 25 respectivamente:
#
# Excesso de peso: 20 kg.
# Multa a pagar: R$ 80.00.
#
# Peso dentro do limite. Nenhuma multa aplicada.
def calculo_multa(peixe_peso):
    limite = 50  
    multa_por_kg = 4  

    if peixe_peso > limite:
        excesso = peixe_peso - limite
        multa = excesso * multa_por_kg
        return f"Excesso de peso: {excesso} kg.\nMulta a pagar: R$ {multa:.2f}."
    else:
        return "Peso dentro do limite. Nenhuma multa aplicada."


# 5. Faça uma função para calcular a quantidade de tinta necessária para pintar uma área.
# O função deverá receber o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é 
# de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
# galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
# os valores para cima, isto é, considere latas cheias.

## Exemplo de saída para uma área de 100 metros quadrados
# Quantidade de latas de 18L: 2
# Preço total: R$ 160.00
# 
# Quantidade de galões de 3,6L: 6
# Preço total: R$ 150.00
#
# Quantidade de latas: 1, Quantidade de galões: 1
# Preço total: R$ 105.00

def calcular_tinta(area):
    cobertura_por_litro = 6 
    lata_capacidade = 18  
    galoes_capacidade = 3.6  
    preco_lata = 80.00  
    preco_galao = 25.00  
    folga = 0.1 

    area_com_folga = area * (1 + folga)
    litros_necessarios = area_com_folga / cobertura_por_litro

    latas_necessarias = math.ceil(litros_necessarios / lata_capacidade)
    preco_latas = latas_necessarias * preco_lata

    galoes_necessarios = math.ceil(litros_necessarios / galoes_capacidade)
    preco_galoes = galoes_necessarios * preco_galao

    latas_mistas = math.floor(litros_necessarios / lata_capacidade)
    litros_restantes = litros_necessarios - (latas_mistas * lata_capacidade)
    galoes_mistos = math.ceil(litros_restantes / galoes_capacidade)
    preco_misto = (latas_mistas * preco_lata) + (galoes_mistos * preco_galao)

    resultado = (
        f"Quantidade de latas de 18L: {latas_necessarias}\n"
        f"Preço total: R$ {preco_latas:.2f}\n\n"
        
        f"Quantidade de galões de 3,6L: {galoes_necessarios}\n"
        f"Preço total: R$ {preco_galoes:.2f}\n\n"

        f"Quantidade de latas: {latas_mistas}, Quantidade de galões: {galoes_mistos}\n"
        f"Preço total: R$ {preco_misto:.2f}"
    )

    return resultado


# 6. Faça uma função que receba dois números e retorne o maior deles.
def maior_numero(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    return n1 
    
# 7. Faça uma função que verifique se uma letra é vogal ou consoante.
def verificar_letra(letra):
    if letra.lower() in "aeiou":
        return "Vogal"
    else:
        return "Consoante"

# 8. Faça um Programa que receba três números e retorne o maior deles.
def maior_tres_numeros(n1, n2, n3):
    return max(n1, n2, n3)

# 9. Faça uma função que retorne o menor valor entre três numeros informados.
def produto_mais_barato(p1, p2, p3):
    return min(p1, p2, p3)

# 10. Faça uma funçao que retorne uma saudação com base no turno de estudo.
# A entrada deverá ser M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
def saudacao_turno(turno):
    if turno == "M":
        return "Bom Dia!"
    elif turno == "V":
        return "Boa Tarde!"
    elif turno == "N":
        return "Boa Noite!"
    else:
        return "Valor Inválido!"

# 11. Faça uma função para um caixa eletrônico que informe quantas notas de cada valor serão fornecidas
# ao ser solicitado um saque.
# A função receberá como entrada o valor do saque e e retornará quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo de saída para uma entrada de 346
# Notas fornecidas:
# 3 nota(s) de R$ 100
# 4 nota(s) de R$ 10
# 1 nota(s) de R$ 5
# 1 nota(s) de R$ 1

def caixa_eletronico(valor):
    notas = [100, 50, 10, 5, 1]
    resultado = "Notas fornecidas:\n"
    
    for nota in notas:
        qtd = valor // nota
        if qtd > 0:
            resultado += f"{qtd} nota(s) de R$ {nota}\n"
        valor -= qtd * nota
    
    return resultado

# 12. Desenvolva uma lógica que classifique uma pessoa com base nas respostas sobre um crime.
# A função deverá receber receba a resposta as seguintes perguntas:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
def classificar_participacao(respostas):
    positiva = respostas.count("sim")
    
    if positiva == 2:
        return "Suspeita"
    elif 3 <= positiva <= 4:
        return "Cúmplice"
    elif positiva == 5:
        return "Assassino"
    else:
        return "Inocente"

# 13. Faça um Programa que calcule o preço da carne em uma promoção com desconto opcional.
# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
# receberá ainda um desconto de 5% sobre o total da compra. Escreva uma função que receba o tipo e a quantidade de
# carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de
# carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

def calcular_preco_carne(tipo, quantidade, no_cartao):
    # Preços para carnes com base na quantidade
    precos = {
        "File Duplo": (4.90, 5.80),  # Até 5 Kg e Acima de 5 Kg
        "Alcatra": (5.90, 6.80),
        "Picanha": (6.90, 7.80)
    }
    
    # Determinando o preço por kg de acordo com a quantidade
    preco_por_kg = precos[tipo][0] if quantidade <= 5 else precos[tipo][1]
    
    # Calculando o preço total
    total = preco_por_kg * quantidade
    
    # Aplicando desconto de 5% se o pagamento for no cartão Tabajara
    if no_cartao:
        total -= total * 0.05
    
    return round(total, 2)
# 14. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem.
def potencia(base, expoente):
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado
# 15. Faça um Programa que retorne o menor, maior e a soma de um conjunto de números.
def estatisticas_numeros(lista):
    return min(lista), max(lista), sum(lista)

# 16. Função que valida se uma nota está entre 0 e 10.
def validar_nota():
    while True:
        nota = float(input("Informe a nota: "))
        if 0 <= nota <= 10:
            return f"Nota válida: {nota:.2f}"
        else:
            print("Erro: A nota deve estar entre 0 e 10. Tente novamente.")

# 17. Função que lê um nome de usuário e senha e verifica se a senha é igual ao nome do usuário.
def validar_usuario_senha():
    while True:
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        if usuario == senha:
            print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")
        else:
            return "Usuário e senha cadastrados com sucesso!"

# 18. Função que calcula a média aritmética de um conjunto de N notas.
def media_notas(notas):
    return sum(notas) / len(notas)

# 19. Função que calcula a soma da série S = 1/1 + 2/3 + 3/5 + ... até n/m.
def calcular_serie(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i / (2 * i - 1)
    return soma

# 20. Função que calcula a média de ginástica, retirando as melhores e piores notas.
def calcular_media_ginastica(nome, notas):
    melhor_nota = max(notas)
    pior_nota = min(notas)
    notas.remove(melhor_nota)
    notas.remove(pior_nota)
    media = sum(notas) / len(notas)
    
    resultado = f"Atleta: {nome}\n"
    for nota in notas:
        resultado += f"Nota: {nota}\n"
    resultado += f"\nResultado final:\nAtleta: {nome}\nMelhor nota: {melhor_nota}\nPior nota: {pior_nota}\nMédia: {media:.2f}"
    
    return resultado

# 21. Função para desenhar uma pirâmide alinhada à esquerda.
def piramide_esquerda(n):
    return "\n".join("#" * i for i in range(1, n + 1)) + "\n"

# 22. Função para desenhar uma pirâmide alinhada à direita.
def piramide_direita(n):
    return "\n".join(" " * (n - i) + "#" * i for i in range(1, n + 1)) + "\n"

# 23. Função para desenhar duas pirâmides lado a lado.
def piramides_lado_a_lado(n):
    return "\n".join(" " * (n - i) + "#" * i + " " * 1 + " " * (n - i) + "#" * i for i in range(1, n + 1)) + "\n"

# 24. Função que calcula o troco com a menor quantidade de moedas possível.
def calcular_troco(valor):
    moedas = {50: 0, 25: 0, 10: 0, 5: 0, 1: 0}
    for moeda in moedas.keys():
        moedas[moeda], valor = divmod(valor, moeda)
    return moedas

# 25. Função que valida um número de cartão de crédito utilizando o algoritmo de Luhn.
def validar_cartao(numero):
    numero = numero.replace(" ", "")  # Remover espaços
    if not numero.isdigit() or len(numero) < 13 or len(numero) > 19:
        return "Número inválido."
    
    soma = 0
    inverter = numero[::-1]
    for i, digito in enumerate(inverter):
        n = int(digito)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        soma += n
    
    if soma % 10 == 0:
        bandeira = ""
        if numero.startswith(("34", "37")):
            bandeira = "American Express"
        elif numero.startswith("5"):
            bandeira = "MasterCard"
        elif numero.startswith("4"):
            bandeira = "Visa"
        else:
            bandeira = "Bandeira não reconhecida."
        
        return f"Cartão Válido - Bandeira: {bandeira}"
    else:
        return "Número inválido."

