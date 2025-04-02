import matplotlib.pyplot as plt

# Imprta a blibioteca pandas
import pandas as pd

def exibirGrafico():
    #cria o dataframe
    df = pd.DataFrame({
        "Meses": ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
        "Temperaturas": [29, 31, 30, 28, 27, 25, 21, 24, 27, 28, 29, 33]
    })

    # Redimencionando o gráfico
    plt.figure(figsize=[10.0, 5.0])

    # Criação de gráfico
    plt.plot(df['Meses'], df['Temperatura'], color="Blue")

    # Definições dos titulos
    plt.title("Temperatura média ao longo do tempo")
    plt.xlabel("Meses")
    plt.ylabel("Temperatura")

    # Exibindo o gráfico
    plt.show()
    plt.savefig('chart2.png')

    # Exibe no console dados estatisticos
    print('Temperaturas: \n{df['Temperaturas'].describe()}')