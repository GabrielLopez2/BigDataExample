import os
from kaggle.api.kaggle_api_extended import KaggleApi
from dotenv import load_dotenv

load_dotenv()

os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')

api = KaggleApi()
api.authenticate()

# ---------- Linea de codigo para busquedas ----------
search_term = 'big data'  #

print(f"🔍 Buscando datasets relacionados con '{search_term}'...\n")
datasets = api.dataset_list(search=search_term, sort_by='hottest')

# Mostrar los primeros 5 resultados
for i, d in enumerate(datasets[:5], 1):
    print(f"{i}. {d.title}\n   URL: https://www.kaggle.com/datasets/{d.ref}\n")


if datasets:
    selected = datasets[0]
    print(f"⬇️ Descargando dataset: {selected.title} ({selected.ref})\n")
    api.dataset_download_files(selected.ref, path='datasets', unzip=True)
    print("✅ ¡Dataset descargado en la carpeta 'datasets'!")
else:
    print("❌ No se encontraron datasets.")
