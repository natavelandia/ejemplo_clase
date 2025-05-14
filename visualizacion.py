# Librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Seaborn para visualizaciones más estilizadas
import seaborn as sns
import os
from analisis import DataAnalyzer

data = pd.read_csv("adult.csv")
analizar = DataAnalyzer(data)
analizar.summary()
analizar.correlation_matrix()
analizar.categorical_analisis()


data = pd.read_csv("vehicles.csv")
analizar = DataAnalyzer(data)
analizar.summary()
analizar.correlation_matrix()
analizar.categorical_analisis()