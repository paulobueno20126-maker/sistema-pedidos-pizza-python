def sistema_pedidos():
    total_geral = 0
    
    while True:
        print("\n--- NOVO PEDIDO DE PIZZA ---")
        tamanho = input("Qual tamanho de pizza gostaria (pequena/media/grande)? ").lower()
        
        # [span_5](start_span)Define valor base pelo tamanho[span_5](end_span)
        if tamanho == 'pequena':
            valor_pizza = 20
        elif tamanho == 'media':
            valor_pizza = 30
        elif tamanho == 'grande':
            valor_pizza = 40
        else:
            print("Tamanho inválido.")
            continue

        valor_extras = 0
        ingredientes_extras = 0
        
        # [span_6](start_span)[span_7](start_span)Pergunta por extras[span_6](end_span)[span_7](end_span)
        gosta_extras = input("Gostaria de adicionar ingredientes extras (sim/nao)? ").lower()
        if gosta_extras == 'sim':
            print("Extras disponíveis: Calabresa, Mussarela, Tomate, Cebola, Bacon (R$ 5,00 cada)")
            lista_extras = ['cebola', 'mussarela', 'calabresa', 'tomate', 'bacon']
            
            for item in lista_extras:
                adicionar = input(f"Gostaria de adicionar {item}? (sim/nao): ").lower()
                if adicionar == 'sim':
                    valor_extras += 5
                    ingredientes_extras += 1

        # [span_8](start_span)[span_9](start_span)Bebida[span_8](end_span)[span_9](end_span)
        refrigerante = input("Gostaria de adicionar um refrigerante (R$ 8,00)? (sim/nao): ").lower()
        if refrigerante == 'sim':
            valor_extras += 8

        total_pedido = valor_pizza + valor_extras
        print(f"\nValor desta pizza: R$ {total_pedido:.2f}")
        print(f"Total de ingredientes extras: {ingredientes_extras}")
        
        total_geral += total_pedido
        
        continuar = input("\nGostaria de fazer outro pedido? (sim/nao): ").lower()
        if continuar == 'nao':
            break

    print(f"\nTOTAL FINAL DE TODOS OS PEDIDOS: R$ {total_geral:.2f}")

if __name__ == "__main__":
    sistema_pedidos()
