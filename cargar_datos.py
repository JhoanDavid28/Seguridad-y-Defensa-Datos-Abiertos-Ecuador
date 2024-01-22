import pandas as pd
import os


directorio = str(os.getcwd())


# selecciona el directorio de los archivos
# muestra la ubicación de los archivos
path_armas_ilicitas = directorio + "/Datos_proyecto_telefónica/mdi_armasilicitas_pm_2023_enero_noviembre.csv"
path_detenidos_aprehendidos = directorio + "/Datos_proyecto_telefónica/mdi_detenidosaprehendidos_pm_2023_enero_noviembre.csv"
path_personas_desaparecidas = directorio + "/Datos_proyecto_telefónica/mdi_personasdesaparecidas_pm_2023_enero_noviembre.csv"

# cargar los archivos
df_armas_ilicidas = pd.read_csv(path_armas_ilicitas, delimiter=';', encoding='iso-8859-1', low_memory=False)
df_detenidos_aprehendidos = pd.read_csv(path_detenidos_aprehendidos, delimiter=';', encoding='iso-8859-1', low_memory=False)
df_personas_desaparecidas = pd.read_csv(path_personas_desaparecidas, delimiter=';', encoding='iso-8859-1', low_memory=False)

# Limpieza de datos
df_detenidos_aprehendidos = df_detenidos_aprehendidos.drop(df_detenidos_aprehendidos.columns[37:61], axis = 1)
df_armas_ilicidas = df_armas_ilicidas.drop(df_armas_ilicidas.columns[37:61], axis = 1)
    

