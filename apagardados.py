import csv
import random

def apagar_dados_aleatoriamente(arquivo_entrada, arquivo_saida, porcentagem):
    with open(arquivo_entrada, 'r', newline='') as entrada, open(arquivo_saida, 'w', newline='') as saida:
        leitor_csv = csv.reader(entrada)
        escritor_csv = csv.writer(saida)

        # Copie o cabeçalho do arquivo original
        cabeçalho = next(leitor_csv)
        escritor_csv.writerow(cabeçalho)

        for linha in leitor_csv:
            nova_linha = []
            for campo in linha:
                if random.random() > porcentagem:
                    nova_linha.append(campo)
                else:
                    nova_linha.append("")
            escritor_csv.writerow(nova_linha)

def main():
    arquivo_entrada = input("Digite o nome do arquivo CSV de entrada: ")
    arquivo_saida = input("Digite o nome do arquivo de saída CSV: ")
    porcentagem = float(input("Digite a porcentagem de dados a serem apagados (0-1): "))

    if porcentagem < 0 or porcentagem > 1:
        print("Porcentagem inválida. Deve estar entre 0 e 1.")
        return

    apagar_dados_aleatoriamente(arquivo_entrada, arquivo_saida, porcentagem)
    print(f"Dados modificados foram salvos em '{arquivo_saida}'.")

if __name__ == "__main__":
    main()
