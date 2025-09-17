#trabajar sobre este archivo
import pandas as pd
def imputar_outliers(df):
    df = df.copy()
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        # Definir límites
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR

        # Reemplazar outliers por la mediana de la columna
        mediana = df[col].median()
        df[col] = df[col].apply(
            lambda x: mediana if (x < limite_inferior or x > limite_superior) else x
        )
    return df

df = pd.read_csv('3. ciclismo.csv')
df_preprocesado = imputar_outliers(df)
print('Preprocesado')
print("Antes :\n", df.head(), "\n")
print("Después:\n", df_preprocesado.head())
