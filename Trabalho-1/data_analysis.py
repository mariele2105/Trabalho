import pandas as pd

def realizar_analise(data):
    """
    Realiza a análise estatística da coluna selecionada pelo usuário.
    Calcula média, mediana, moda e desvio padrão.
    """
    column = input("Escolha uma coluna para análise (ex: 'midterm_Score'): ")
    
    # Validar se a coluna existe e é numérica
    if column in data.columns and pd.api.types.is_numeric_dtype(data[column]):
        mean = data[column].mean()
        median = data[column].median()
        mode = data[column].mode()[0]  # Pega o primeiro valor da moda
        std_dev = data[column].std()
        
        print(f"Média: {mean}")
        print(f"Mediana: {median}")
        print(f"Moda: {mode}")
        print(f"Desvio Padrão: {std_dev}")
    else:
        print("Coluna não encontrada ou não é numérica.")
