# Sistema de Atendimento e Pedidos — Lanchonete

**Aluno:** Eugênio Ferreira Nogueira
**Disciplina:** Algoritmos e Programação — Análise e Desenvolvimento de Sistemas (Unilavras)
**Projeto:** Sistema de Atendimento e Pedidos em Python

## Descrição

Programa em Python, executado no terminal, que registra os pedidos de uma lanchonete. O cliente informa o nome, escolhe produtos do cardápio por código, informa as quantidades e pode continuar pedindo até decidir finalizar. Ao final, o sistema calcula o desconto de acordo com o valor da compra, pede a forma de pagamento e mostra um resumo organizado do atendimento.

O programa foi feito usando apenas o conteúdo visto em aula (variáveis, `input`/`print`, operadores, `if`/`elif`/`else`, `match`/`case`, `while` e funções).

## Principais funcionalidades

- Identificação do cliente pelo nome.
- Cardápio com 6 produtos (código, nome e preço).
- Seleção de produto por código e quantidade, com repetição até o cliente digitar `0` para finalizar.
- Cálculo do subtotal de cada item e acúmulo no total da compra.
- Validação das entradas: código de produto inexistente, quantidade menor ou igual a zero e forma de pagamento inválida. Em caso de erro, nenhum cálculo é feito com valores incorretos.
- Regra de desconto automática:

  | Valor da compra | Desconto |
  |---|---|
  | Abaixo de R$ 50,00 | 0% |
  | De R$ 50,00 a R$ 99,99 | 5% |
  | R$ 100,00 ou mais | 10% |

- Escolha da forma de pagamento (Dinheiro, PIX ou Cartão).
- Resumo final com nome do cliente, valor original, percentual de desconto, valor do desconto, valor final e forma de pagamento.
- Se o cliente finalizar sem pedir nada, o programa encerra sem pedir pagamento.

## Organização do código

| Função | Responsabilidade |
|---|---|
| `mostrar_cardapio()` | Exibe os produtos disponíveis |
| `buscar_preco(codigo)` | Devolve o preço do produto (ou `0` se o código não existir) |
| `buscar_nome(codigo)` | Devolve o nome do produto |
| `ler_quantidade()` | Lê a quantidade e repete até ser maior que zero |
| `escolher_pagamento()` | Lê e valida a forma de pagamento |
| `calcular_percentual_desconto(total)` | Define o percentual de desconto pelo total |
| `mostrar_resumo(...)` | Exibe o resumo final |
| `main()` | Controla o fluxo geral do atendimento |

## Como executar

1. Tenha o **Python 3.10 ou superior** instalado (o `match`/`case` exige essa versão).
2. Baixe o arquivo `lanchonete.py`.
3. No terminal, dentro da pasta do arquivo, execute:
4. Siga as instruções na tela: digite o nome, escolha os produtos pelo código e digite `0` para finalizar.

## Exemplo de execução

```
Qual é o seu nome? Ana
Código do produto: 2
Quantidade: 3
Adicionado: 3x X-Salada = R$ 60.00
Total parcial: R$ 60.00
Código do produto: 0

Forma de pagamento:
1 - Dinheiro
2 - PIX
3 - Cartão
Escolha (1, 2 ou 3): 2

========================================
         RESUMO DO ATENDIMENTO
========================================
Cliente:             Ana
Valor original:      R$ 60.00
Desconto aplicado:   5%
Valor do desconto:   R$ 3.00
Valor final:         R$ 57.00
Forma de pagamento:  PIX
========================================