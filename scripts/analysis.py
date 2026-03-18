import pandas as pd
import numpy as np
import os

# Déterminer le chemin absolu du dossier du script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, '../data/raw/accessibilite-en-gare.csv')

# Charger le fichier CSV brut
df = pd.read_csv(csv_path, sep=';')

# Séparer les coordonnées
df[['lat', 'lon']] = df['stop_point_geopoint'].str.split(',', expand=True)
df['lat'] = df['lat'].astype(float)
df['lon'] = df['lon'].astype(float)

# Vérifier les valeurs manquantes
print('Valeurs manquantes par colonne :')
print(df.isnull().sum())

# Sauvegarder le DataFrame nettoyé
df.to_csv(os.path.join(script_dir, '../data/processed/cleaned_data.csv'), index=False)
print('Données nettoyées exportées dans data/processed/cleaned_data.csv')

# Analyse de la répartition de l’accessibilité
print('\nRépartition des niveaux d’accessibilité :')
print(df['accessibility_level_name'].value_counts())

# Pourcentages
distribution = df['accessibility_level_name'].value_counts(normalize=True) * 100
print('\nPourcentage de chaque niveau d’accessibilité :')
print(distribution)

# Gares non accessibles (correction du filtre)
print('\nGares non accessibles :')
df_non_access = df[df['accessibility_level_name'] == 'gare ou arrêt non accessible']
print(df_non_access[['stop_name', 'accessibility_level_name', 'lat', 'lon']])

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
else:
    print("Colonnes 'lat' et 'lon' non disponibles dans ce dataset.")

# Vérification du fichier exporté
print('\nFichier cleaned_data.csv existe :', os.path.exists(os.path.join(script_dir, '../data/processed/cleaned_data.csv')))
