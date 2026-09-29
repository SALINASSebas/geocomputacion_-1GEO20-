import numpy as np
import xarray as xr
from scipy.stats import kendalltau, theilslopes

def cargar_historico(modelo, carpeta, variable):
    ruta = carpeta + modelo + f"/{variable}_{modelo}_1950-2014_historical.nc"
    return xr.open_dataset(ruta)[variable]

def cargar_escenario(modelo, escenario, carpeta, variable):
    carpeta_modelo = carpeta + modelo + "/"
    tramo1 = xr.open_dataset(carpeta_modelo + f"{variable}_{modelo}_2015-2049_{escenario}.nc")[variable]
    tramo2 = xr.open_dataset(carpeta_modelo + f"{variable}_{modelo}_2050-2099_{escenario}.nc")[variable]
    return xr.concat([tramo1, tramo2], dim="time")