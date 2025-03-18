import pytest
from exercicios_revisao import (
    saudacao, area_circulo, fahrenheit_para_celsius,
    calculo_multa, calcular_tinta, maior_numero, validar_usuario_senha,
    verificar_letra, maior_tres_numeros, produto_mais_barato,
    saudacao_turno, caixa_eletronico, classificar_participacao,
    calcular_preco_carne, potencia, estatisticas_numeros,
    validar_nota, media_notas,
    calcular_serie, calcular_media_ginastica,
    piramide_esquerda, piramide_direita, piramides_lado_a_lado,
    calcular_troco, validar_cartao
)

def test_saudacao():
    assert saudacao("Samuel") == "Boa tarde, Samuel. Seja bem vindo!"

def test_area_circulo():
    assert area_circulo(2) == pytest.approx(12.5664, rel=1e-3)

def test_fahrenheit_para_celsius():
    assert fahrenheit_para_celsius(32) == 0
    assert fahrenheit_para_celsius(212) == 100

def test_calculo_multa():
    assert calculo_multa(60) == "Excesso de peso: 10 kg.\nMulta a pagar: R$ 40.00."
    assert calculo_multa(30) == "Peso dentro do limite. Nenhuma multa aplicada."

def test_calcular_tinta():
    resultado = calcular_tinta(125)

    esperado = (
        "Quantidade de latas de 18L: 2\n"
        "Preço total: R$ 160.00\n\n"
        
        "Quantidade de galões de 3,6L: 7\n"
        "Preço total: R$ 175.00\n\n"

        "Quantidade de latas: 1, Quantidade de galões: 2\n"
        "Preço total: R$ 130.00"
    )

    assert resultado == esperado



def test_maior_numero():
    assert maior_numero(5, 10) == 10

def test_verificar_letra():
    assert verificar_letra("a") == "Vogal"
    assert verificar_letra("b") == "Consoante"

def test_maior_tres_numeros():
    assert maior_tres_numeros(3, 7, 5) == 7

def test_produto_mais_barato():
    assert produto_mais_barato(10, 15, 20) == 10

def test_saudacao_turno():
    assert saudacao_turno("M") == "Bom Dia!"
    assert saudacao_turno("X") == "Valor Inválido!"

def test_caixa_eletronico():
    resultado = caixa_eletronico(256)
    esperado = (
        "Notas fornecidas:\n"
        "2 nota(s) de R$ 100\n"
        "1 nota(s) de R$ 50\n"
        "1 nota(s) de R$ 5\n"
        "1 nota(s) de R$ 1\n"
    )
    assert resultado == esperado

    resultado = caixa_eletronico(399)
    esperado = (
        "Notas fornecidas:\n"
        "3 nota(s) de R$ 100\n"
        "1 nota(s) de R$ 50\n"
        "4 nota(s) de R$ 10\n"
        "1 nota(s) de R$ 5\n"
        "4 nota(s) de R$ 1\n"
    )
    assert resultado == esperado


def test_classificar_participacao():
    assert classificar_participacao(["sim", "sim", "não", "não", "não"]) == "Suspeita"

def test_calcular_preco_carne():
    assert calcular_preco_carne("Picanha", 6, False) == 46.8

def test_potencia():
    assert potencia(2, 3) == 8

def test_estatisticas_numeros():
    assert estatisticas_numeros([3, 7, 5]) == (3, 7, 15)

def test_validar_nota(monkeypatch):
    # Simula entradas do usuário: ["abc", "-1", "11", "8"]
    entradas = iter(["abc", "-1", "11", "8"])  # O usuário tentará entradas erradas antes de acertar
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    resultado = validar_nota()
    assert resultado == "Nota válida: 8.00"


def test_validar_usuario_senha(monkeypatch):
    # Simula entradas do usuário: ["ana", "ana", "ana123"]
    entradas = iter(["ana", "ana", "ana123"])  # O usuário tenta repetir antes de acertar
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    resultado = validar_usuario_senha()
    assert resultado == "Usuário e senha cadastrados com sucesso!"



def test_media_notas():
    assert media_notas([7, 8, 9]) == 8

def test_calcular_serie():
    assert calcular_serie(3) == pytest.approx(2.27, rel=1e-2)

import pytest

def test_calcular_media_ginastica():
    nome = "Aparecido Parente"
    notas = [9.9, 7.5, 9.5, 8.5, 9.0, 8.5, 9.7]
    
    esperado = (
        "Atleta: Aparecido Parente\n"
        "Nota: 9.9\n"
        "Nota: 7.5\n"
        "Nota: 9.5\n"
        "Nota: 8.5\n"
        "Nota: 9.0\n"
        "Nota: 8.5\n"
        "Nota: 9.7\n\n"
        "Resultado final:\n"
        "Atleta: Aparecido Parente\n"
        "Melhor nota: 9.9\n"
        "Pior nota: 7.5\n"
        "Média: 9.04"
    )

    resultado = calcular_media_ginastica(nome, notas)
    assert resultado == esperado


def test_piramide_esquerda():
    assert piramide_esquerda(3) == "#\n##\n###\n"

def test_piramide_direita():
    assert piramide_direita(3) == "  #\n ##\n###\n"

def test_piramides_lado_a_lado():
    assert piramides_lado_a_lado(3) == "  # #\n ## ##\n### ###\n"

def test_calcular_troco():
    assert calcular_troco(99) == {50: 1, 25: 1, 10: 2, 1: 4}


@pytest.mark.parametrize(
    "numero, esperado",
    [
        ("378282246310005", "Cartão Válido - Bandeira: American Express"),  # Amex válido
        ("5555555555554444", "Cartão Válido - Bandeira: MasterCard"),       # MasterCard válido
        ("4111111111111111", "Cartão Válido - Bandeira: Visa"),             # Visa válido (16 dígitos)
        ("4012888888881881", "Cartão Válido - Bandeira: Visa"),             # Outro Visa válido
        ("4003600000000014", "Cartão Válido - Bandeira: Visa"),             # O número que estava falhando
        ("123456789012345", "Número inválido."),  # Número inválido (corrigido)
        ("6011111111111117", "Bandeira não reconhecida."), # Bandeira inválida
    ]
)
def test_validar_cartao(numero, esperado):
    assert validar_cartao(numero) == esperado

