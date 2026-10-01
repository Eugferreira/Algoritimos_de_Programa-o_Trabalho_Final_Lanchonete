# -*- coding: utf-8 -*-
# =============================================================================
# SISTEMA DE ATENDIMENTO E PEDIDOS - LANCHONETE
# Disciplina: Algoritmos e Programação (ADS - Unilavras)
# Aluno: Eugênio Ferreira Nogueira
#
# O que o programa faz:
#   1. Pede o nome do cliente
#   2. Mostra o cardápio e recebe pedidos (código + quantidade) em repetição
#   3. Acumula o total da compra
#   4. Calcula o desconto conforme o valor total
#   5. Pede a forma de pagamento
#   6. Mostra um resumo final
#
# Só foram usados recursos vistos em aula: variáveis, input/print, operadores,
# if/elif/else, match/case, while, funções e f-strings.
# NÃO foram usadas listas, tuplas, dicionários ou outras estruturas de dados.
# =============================================================================


# -----------------------------------------------------------------------------
# FUNÇÕES DO CARDÁPIO
# -----------------------------------------------------------------------------

def mostrar_cardapio():
    """Mostra na tela os produtos disponíveis (código, nome e preço)."""
    print()
    print("=" * 40)
    print(f"{'CARDÁPIO':^40}")        # ^40 = centraliza o texto em 40 espaços
    print("=" * 40)
    print(f"{'1 - X-Burger':<28} R$ 18.00")
    print(f"{'2 - X-Salada':<28} R$ 20.00")
    print(f"{'3 - Batata Frita':<28} R$ 12.00")
    print(f"{'4 - Refrigerante':<28} R$  7.00")
    print(f"{'5 - Suco Natural':<28} R$  9.00")
    print(f"{'6 - Sobremesa':<28} R$ 10.00")
    print("-" * 40)
    print("0 - Finalizar pedido")
    print("=" * 40)


def buscar_preco(codigo):
    """Recebe o código digitado e devolve o preço do produto.
    Se o código não existir, devolve 0 (usado como sinal de 'inválido')."""
    match codigo:
        case "1":
            return 18.00
        case "2":
            return 20.00
        case "3":
            return 12.00
        case "4":
            return 7.00
        case "5":
            return 9.00
        case "6":
            return 10.00
        case _:                # qualquer outro valor = código inexistente
            return 0


def buscar_nome(codigo):
    """Recebe o código digitado e devolve o nome do produto."""
    match codigo:
        case "1":
            return "X-Burger"
        case "2":
            return "X-Salada"
        case "3":
            return "Batata Frita"
        case "4":
            return "Refrigerante"
        case "5":
            return "Suco Natural"
        case "6":
            return "Sobremesa"
        case _:
            return "Desconhecido"


# -----------------------------------------------------------------------------
# FUNÇÕES DE ENTRADA E VALIDAÇÃO
# -----------------------------------------------------------------------------

def ler_quantidade():
    """Pede a quantidade e repete a pergunta até o usuário digitar um
    número maior que zero. Devolve a quantidade válida."""
    quantidade = 0
    while quantidade <= 0:                      # repete enquanto for inválida
        quantidade = int(input("Quantidade: "))
        if quantidade <= 0:
            print("Quantidade inválida! Digite um número maior que zero.")
    return quantidade


def escolher_pagamento():
    """Pede a forma de pagamento e repete até a opção ser válida.
    Devolve o nome da forma de pagamento escolhida."""
    forma = ""
    while forma == "":                          # enquanto não escolheu nada válido
        print()
        print("Forma de pagamento:")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão")
        opcao = input("Escolha (1, 2 ou 3): ")
        match opcao:
            case "1":
                forma = "Dinheiro"
            case "2":
                forma = "PIX"
            case "3":
                forma = "Cartão"
            case _:
                print("Forma de pagamento inválida!")
    return forma


# -----------------------------------------------------------------------------
# FUNÇÕES DE CÁLCULO
# -----------------------------------------------------------------------------

def calcular_percentual_desconto(total):
    """Devolve o percentual de desconto de acordo com o total da compra:
       abaixo de R$ 50,00      -> 0%
       de R$ 50,00 a R$ 99,99  -> 5%
       R$ 100,00 ou mais       -> 10%"""
    if total >= 100:
        return 10
    elif total >= 50:
        return 5
    else:
        return 0


# -----------------------------------------------------------------------------
# FUNÇÃO DO RESUMO FINAL
# -----------------------------------------------------------------------------

def mostrar_resumo(cliente, total, percentual, desconto, valor_final, pagamento):
    """Mostra o resumo organizado do atendimento."""
    print()
    print("=" * 40)
    print(f"{'RESUMO DO ATENDIMENTO':^40}")
    print("=" * 40)
    print(f"Cliente:             {cliente}")
    print(f"Valor original:      R$ {total:.2f}")
    print(f"Desconto aplicado:   {percentual}%")
    print(f"Valor do desconto:   R$ {desconto:.2f}")
    print(f"Valor final:         R$ {valor_final:.2f}")
    print(f"Forma de pagamento:  {pagamento}")
    print("=" * 40)
    print("Obrigado pela preferência, " + cliente + "!")


# -----------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# -----------------------------------------------------------------------------

def main():
    print("=== BEM-VINDO À LANCHONETE ===")
    cliente = input("Qual é o seu nome? ")

    total = 0                  # ACUMULADOR: soma o subtotal de cada item
    atendendo = True           # controla o laço: False = encerra os pedidos

    # Laço principal: repete enquanto o cliente não escolher finalizar (código 0)
    while atendendo:
        mostrar_cardapio()
        codigo = input("Código do produto: ")

        if codigo == "0":                      # cliente quer finalizar
            atendendo = False
        else:
            preco = buscar_preco(codigo)
            if preco == 0:                     # código inexistente -> não calcula nada
                print("Código inválido! Escolha uma opção do cardápio.")
            else:
                nome = buscar_nome(codigo)
                quantidade = ler_quantidade()
                subtotal = preco * quantidade  # subtotal deste item
                total = total + subtotal       # acumula no total da compra
                print(f"Adicionado: {quantidade}x {nome} = R$ {subtotal:.2f}")
                print(f"Total parcial: R$ {total:.2f}")

    # Depois do laço: se não comprou nada, encerra sem pedir pagamento
    if total == 0:
        print()
        print("Nenhum item foi pedido. Até a próxima, " + cliente + "!")
    else:
        percentual = calcular_percentual_desconto(total)
        desconto = total * percentual / 100    # valor do desconto em reais
        valor_final = total - desconto
        pagamento = escolher_pagamento()
        mostrar_resumo(cliente, total, percentual, desconto, valor_final, pagamento)


main()
