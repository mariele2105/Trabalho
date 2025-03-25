import pandas as pd

def carregar_dados(file_path):
    """
    Carrega os dados de um arquivo CSV ou JSON e retorna um DataFrame.
    """
    try:
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        elif file_path.endswith('.json'):
            data = pd.read_json(file_path)
        else:
            print("Formato de arquivo não suportado!")
            return None
        print("Dados carregados com sucesso!")
        return data
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {str(e)}")
        return None
