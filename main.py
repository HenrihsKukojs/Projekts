import requests
from bs4 import BeautifulSoup
import json
import os

def skrapet_imdb_top250_filmas():
    filmas = []
    vietnes_adrese = "https://www.imdb.com/chart/top/"
    
    galvenes = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    try:
        atbilde = requests.get(vietnes_adrese, headers=galvenes, timeout=10)
        atbilde.raise_for_status()
    except requests.exceptions.RequestException as e:
        return []

    zupa = BeautifulSoup(atbilde.content, "html.parser")
    
    filmu_saraksta_bloks = zupa.find("ul", class_="ipc-metadata-list") 
    
    if not filmu_saraksta_bloks:
        return []

    filmu_elementi = filmu_saraksta_bloks.find_all("li", class_="ipc-metadata-list-summary-item")

    for ieraksts in filmu_elementi:
        try:
            virsraksta_tags = ieraksts.find("h3", class_="ipc-title__text")
            nosaukums = virsraksta_tags.get_text(strip=True).split('.', 1)[-1].strip() if virsraksta_tags else "Nezināms nosaukums"

            info_tagi = ieraksts.find_all("span", class_="sc-b0901df4-7") 
            
            gads = "Nav gada"
            reitings = "Nav reitinga"

            if len(info_tagi) >= 1:
                gada_teksts = info_tagi[0].get_text(strip=True)
                if gada_teksts.isdigit() and len(gada_teksts) == 4:
                    gads = gada_teksts
            
            reitinga_bloks = ieraksts.find("span", class_="ipc-rating-star--rating")
            if reitinga_bloks:
                 reitings = reitinga_bloks.get_text(strip=True).split('(')[0].strip()

            filmas.append({
                "Nosaukums": nosaukums,
                "Gads": gads,
                "Reitings": reitings
            })
        except Exception:
            continue

    return filmas

if __name__ == "__main__":
    visas_filmas = skrapet_imdb_top250_filmas()

    if visas_filmas:
        print("\n--- IMDb Top 250 Filmas ---")
        for filma in visas_filmas:
            print(f"Nosaukums: {filma['Nosaukums']}")
            print(f"Gads: {filma['Gads']}")
            print(f"Reitings: {filma['Reitings']}")
            print("-" * 30)
    else:
        print("\nNav atrasti filmu dati.")

    izvades_direktorija = "dati"
    os.makedirs(izvades_direktorija, exist_ok=True)
    izvades_faila_cels = os.path.join(izvades_direktorija, "imdb_top250_filmas.json")

    with open(izvades_faila_cels, "w", encoding="utf-8") as f:
        json.dump(visas_filmas, f, ensure_ascii=False, indent=4)
    
    print(f"\nSaglabāti {len(visas_filmas)} filmu dati failā {izvades_faila_cels}")
