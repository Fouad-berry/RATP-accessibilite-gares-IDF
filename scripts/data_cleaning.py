import pandas as pd
import os

# Déterminer le chemin absolu du dossier du script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construire le chemin absolu du CSV
csv_path = os.path.join(script_dir, '../data/raw/accessibilite-en-gare.csv')

# Charger le fichier CSV brut
df = pd.read_csv(csv_path, sep=';')

# Séparer les coordonnées
df[['lat', 'lon']] = df['stop_point_geopoint'].str.split(',', expand=True)
df['lat'] = df['lat'].astype(float)
df['lon'] = df['lon'].astype(float)

# Sauvegarder le DataFrame nettoyé
df.to_csv(os.path.join(script_dir, '../data/processed/cleaned_data.csv'), index=False)
