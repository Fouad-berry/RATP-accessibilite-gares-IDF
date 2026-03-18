import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Charger les données nettoyées
df = pd.read_csv('../data/processed/cleaned_data.csv')

# Analyse de la répartition de l’accessibilité
print(df['accessibility_level_name'].value_counts())

# Pourcentages
distribution = df['accessibility_level_name'].value_counts(normalize=True) * 100
print(distribution)

# Gares non accessibles
print(df[df['accessibility_level_name'] == 'Non accessible'])

# Nombre d’arrêts par ligne
if 'ligne' in df.columns:
    print('\nNombre d’arrêts par ligne :')
    arrets_par_ligne = df['ligne'].value_counts()
    print(arrets_par_ligne)
    print('\nTop 5 des lignes les plus desservies :')
    print(arrets_par_ligne.head(5))
else:
    print("Colonne 'ligne' non disponible dans ce dataset.")

# Zones mal couvertes (quadrillage simple)
if 'lat' in df.columns and 'lon' in df.columns:
    lat_min, lat_max = df['lat'].min(), df['lat'].max()
    lon_min, lon_max = df['lon'].min(), df['lon'].max()
    n_bins = 20
    grid, xedges, yedges = np.histogram2d(df['lat'], df['lon'], bins=n_bins)
    print('\nDensité de gares par zone (grille) :')
    print(grid)
    # Optionnel : afficher la carte si exécuté en local
    # plt.figure(figsize=(8, 6))
    # plt.imshow(grid.T, origin='lower', extent=[lat_min, lat_max, lon_min, lon_max], aspect='auto', cmap='Reds')
    # plt.colorbar(label='Nombre de gares')
    # plt.title('Densité de gares par zone (quadrillage)')
    # plt.xlabel('Latitude')
    # plt.ylabel('Longitude')
    # plt.show()
else:
    print("Colonnes 'lat' et 'lon' non disponibles dans ce dataset.")
