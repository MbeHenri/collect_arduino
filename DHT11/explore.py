import pandas as pd
import matplotlib.pyplot as plt

path_data = "output.txt"
df = pd.read_csv(
    path_data, sep=";", header=None, names=["Temperature", "Humidity", "Time"]
)

# Néttoyage
df["Time"] = pd.to_datetime(df["Time"])
df["Temperature"] = pd.to_numeric(df["Temperature"], errors="coerce")
df["Humidity"] = pd.to_numeric(df["Humidity"], errors="coerce")
df = df.dropna(subset=["Temperature", "Humidity"])


# Fonction de suppréssion de valeurs abérantes
def remove_outliers(df: pd.DataFrame, column: str):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]


# Suppression des valeurs aberrantes pour les colonnes 'Temperature' et 'Humidity'
df = remove_outliers(df, "Temperature")
df = remove_outliers(df, "Humidity")

# Tracer les graphes de la température et de l'humidité en fonction du temps sur le même graphique
plt.figure(figsize=(10, 5))
plt.plot(df["Time"], df["Temperature"], label="Temperature (°C)", color="red")
plt.plot(df["Time"], df["Humidity"], label="Humidity (%)", color="blue")
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("Temperature and Humidity vs Time")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
