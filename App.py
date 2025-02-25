# Inicializando o inventário de produtos como um dicionário vazio
inventario = {}

# Função para adicionar um produto ao inventário
def adicionar_produto(nome, preco, quantidade):
    inventario[nome] = {"preço": preco, "quantidade": quantidade}
    printf("Produto {nome} adicionado com sucesso!")

# Função para remover um produto do inventário
def remover_produto(nome):
    if nome in inventario:
        del inventario[nome]
        printf("Produto {nome} removido com sucesso!")
    else:
        printf("Produto {nome} não encontrado no inventário.")

# Função para listar todos os produtos do inventário
def listar_produtos():
    if inventario:
        printf("Inventário de Produtos:")
        for nome, detalhes in inventario.items():
            printf("Nome: {nome}, Preço: {detalhes['preço']}, Quantidade: {detalhes['quantidade']}")
    else:
        printf("O inventário está vazio.")

# Função principal para o menu de opções
def menu():
    while True:
        printf("\n1. Adicionar produto")
        printf("2. Remover produto")
        printf("3. Listar produtos")
        printf("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade do produto: "))
            adicionar_produto(nome, preco, quantidade)
        elif opcao == "2":
            nome = input("Nome do produto a ser removido: ")
            remover_produto(nome)
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            printf("Opção inválida. Tente novamente.")

# Chamando a função principal do menu
menu()
