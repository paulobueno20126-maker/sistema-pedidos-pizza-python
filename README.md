# 🍕 Sistema de Pedidos de Pizzaria

Este projeto foi desenvolvido em 1hora durante o meu curso de **Python**, focado em aplicar lógica de programação para resolver um problema do mundo real: a gestão de pedidos de uma pizzaria.

## 📋 Funcionalidades
- Escolha de tamanho (Pequena, Média, Grande).
- Adição de ingredientes extras dinâmicos.
- Inclusão de bebidas ao pedido.
- Cálculo automático de totais e sub-totais.
- Sistema de loop para múltiplos pedidos na mesma sessão.

## 💰 Tabela de Preços
| Item | Valor Base |
| :--- | :--- |
| **Pizza Pequena** | R$ 20,00 |
| **Pizza Média** | R$ 30,00 |
| **Pizza Grande** | R$ 40,00 |
| **Ingrediente Extra** | R$ 5,00 (cada) |
| **Refrigerante** | R$ 8,00 |

## 💻 Código Fonte (Resumo da Lógica)
O algoritmo utiliza estruturas `while True` para manter o atendimento ativo e `if/elif/else` para precificação precisa.

```python
# Exemplo da lógica de decisão de preços
if tamanho == 'pequena':
    valor_pizza = 20
elif tamanho == 'media':
    valor_pizza = 30
# ... lógica continua para extras e bebidas

