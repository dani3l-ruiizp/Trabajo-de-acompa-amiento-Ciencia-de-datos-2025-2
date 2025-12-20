import pandas as pd
import numpy as np

def cargar_datos_json(ruta_json):
    """
    Carga el dataset desde un archivo JSON
    """
    return pd.read_json(ruta_json)


def limpiar_datos(df):
    """
    Limpieza básica del dataset:
    - Manejo de valores nulos
    - Eliminación de duplicados
    - Conversión de tipos
    """
    df = df.copy()

    df.drop_duplicates(inplace=True)

    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].fillna("No reportado")

    for col in df.select_dtypes(include=[np.number]).columns:
        df[col] = df[col].fillna(df[col].median())

    return df


def filtrar_criterio_farmaceutico(df, columna, valor):
    """
    Filtra el DataFrame por un criterio farmacéutico específico
    """
    return df[df[columna] == valor]