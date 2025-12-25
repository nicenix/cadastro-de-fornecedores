import pandas as pd


lista_fornecedores = []

print("--- SISTEMA DE CADASTRO DE FORNECEDORES ---")
print("Digite 'S' para sair a qualquer momento.\n")

while True:
    nome = input("Nome da Empresa: ")
    if nome.upper() == 'S':
        break
    cnpj = input("CNPJ: ")
    categoria = input("Categoria (Ex: Elétrica, Hidráulica): ")

    fornecedor = {
        "Empresa": nome,
        "CNPJ": cnpj,
        "Categoria": categoria
    }
    lista_fornecedores.append(fornecedor)
    print("Cadastrado com sucesso!\n")

if lista_fornecedores:
    df = pd.to_excel(lista_fornecedores) # Cria a tabela
    df.to_excel("Base_Fornecedores.xlsx", index=False) # Salva o arquivo
    print("\n✅ Arquivo 'Base_Fornecedores.xlsx' gerado com sucesso!")
else:
    print("\nNenhum dado cadastrado.")