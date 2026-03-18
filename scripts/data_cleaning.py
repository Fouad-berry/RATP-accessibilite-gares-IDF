import pandas as pd

# Charger le fichier CSV brut
df = pd.read_csv('../data/raw/accessibilite-en-gare.csv', sep=';')

# Séparer les coordonnées
df[['lat', 'lon']] = df['stop_point_geopoint'].str.split(',', expand=True)
df['lat'] = df['lat'].astype(float)
df['lon'] = df['lon'].astype(float)

# Sauvegarder le DataFrame nettoyé
df.to_csv('../data/processed/cleaned_data.csv', index=False)
