import matplotlib.pyplot as plt

def gerar_graficos(data):
    """
    Gera os gráficos solicitados: gráfico de dispersão, gráfico de barras e gráfico de pizza.
    """
    # Gráfico de dispersão (Horas de sono vs Nota final)
    plt.scatter(data['sleep_hours'], data['final_score'])
    plt.title("Horas de sono vs Nota final")
    plt.xlabel("Horas de sono")
    plt.ylabel("Nota final")
    plt.show()

    # Gráfico de barras (Idade vs Média das notas intermediárias)
    age_groups = data.groupby('age')['midterm_Score'].mean()
    age_groups.plot(kind='bar')
    plt.title("Idade vs Média das Notas Intermediárias")
    plt.xlabel("Idade")
    plt.ylabel("Média das Notas")
    plt.show()

    # Gráfico de pizza para as idades
    age_bins = pd.cut(data['age'], bins=[0, 17, 21, 24, 100], labels=["Até 17", "18-21", "21-24", "25 ou mais"])
    age_groups_pie = age_bins.value_counts()
    age_groups_pie.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title("Distribuição de Idades")
    plt.show()
