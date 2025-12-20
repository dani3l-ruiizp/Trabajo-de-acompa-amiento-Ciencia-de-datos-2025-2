import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

def histograma(df, columna):
    plt.figure()
    sns.histplot(df[columna], kde=True)
    plt.title(f"Distribución de {columna}")
    plt.xlabel(columna)
    plt.ylabel("Frecuencia")
    plt.show()


def boxplot(df, columna):
    plt.figure()
    sns.boxplot(x=df[columna])
    plt.title(f"Boxplot de {columna}")
    plt.xlabel(columna)
    plt.show()


def grafico_barras(df, columna):
    plt.figure()
    df[columna].value_counts().plot(kind="bar")
    plt.title(f"Distribución por {columna}")
    plt.xlabel(columna)
    plt.ylabel("Frecuencia")
    plt.show()


def heatmap_correlaciones(df):
    plt.figure()
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Mapa de calor de correlaciones")
    plt.show()


def linea_tiempo(df, columna_tiempo, columna_valor):
    plt.figure()
    df.groupby(columna_tiempo)[columna_valor].mean().plot()
    plt.title("Evolución temporal")
    plt.xlabel(columna_tiempo)
    plt.ylabel(columna_valor)
    plt.show()