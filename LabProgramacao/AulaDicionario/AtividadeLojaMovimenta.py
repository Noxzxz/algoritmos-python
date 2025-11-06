def atualizar(estoque, movimentacao):
    for mov in movimentacao:
        produto = mov[0]
        quantidade = mov[1]
        
        if produto not in estoque:
            estoque[produto] = {"saldo": quantidade, "min": 0, "preco": 0}
        else:
            estoque[produto]["saldo"] += quantidade

def main():
    estoque = {
        "cafe": {"saldo": 10, "min": 12, "preco": 12.50},
        "pao": {"saldo": 30, "min": 25, "preco": 2.00},
        "queijo": {"saldo": 5, "min": 12, "preco": 34.00},
    }

    movimentacao = [
        ["cafe", -3],
        ["pao", -10],
        ["cafe", 5],
        ["leite", 8]
    ]
    
    atualizar(estoque, movimentacao)
    print(estoque)
    
if __name__ == "__main__":
    main()
