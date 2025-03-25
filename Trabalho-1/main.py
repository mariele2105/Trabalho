import os
import logging
from data_processing import carregar_dados
from data_cleaning import limpar_dados
from data_analysis import realizar_analise
from data_visualization import gerar_graficos

# Configuração do logging
logging.basicConfig(filename='logfile.log', level=logging.INFO)

def main():
    # Perguntar ao usuário o caminho do arquivo
    file_path = input("Digite o caminho do arquivo CSV ou JSON: ")
    
    # Verificar se o caminho existe
    if not os.path.exists(file_path):
        print("Caminho do arquivo inválido!")
        logging.error(f"Erro: Caminho inválido {file_path}")
        return
    
    # Carregar os dados
    data = carregar_dados(file_path)
    if data is None:
        return
    
    # Limpeza de dados
    data_cleaned = limpar_dados(data)
    
    # Realizar análise estatística
    realizar_analise(data_cleaned)
    
    # Gerar gráficos
    gerar_graficos(data_cleaned)

if __name__ == "__main__":
    main()

