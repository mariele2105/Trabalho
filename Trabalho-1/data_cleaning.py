def limpar_dados(data):
    """
    Limpa os dados removendo registros com dados faltantes na coluna 'parent_education'
    e substituindo valores nulos na coluna 'attendance' pela mediana.
    """
    # Remover registros com educação dos pais vazia
    data_cleaned = data.dropna(subset=['parent_education'])
    
    # Substituir valores nulos na coluna 'attendance' pela mediana
    attendance_median = data_cleaned['attendance'].median()
    data_cleaned['attendance'].fillna(attendance_median, inplace=True)
    
    # Log da limpeza
    print("Dados limpos com sucesso!")
    return data_cleaned
