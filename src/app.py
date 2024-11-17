import requests
from bs4 import BeautifulSoup
import time

URL = "https://eksempel.dk/bolig"  # Indsæt det korrekte link
HEADERS = {"User-Agent": "DinUserAgent"}  # Tilføj User-Agent for at undgå blokering

def tjek_om_lukket():
    try:
        # Hent siden
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()  # Tjek for HTTP-fejl
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Tjek om ordet "lukket" findes
        if "lukket" in soup.get_text().lower():
            return True
        return False
    except Exception as e:
        print(f"Fejl ved forespørgsel: {e}")
        return None

def send_besked():
    print("Opskrivningen er ÅBEN! Tjek hjemmesiden med det samme!")
    # Her kan du indsætte din beskedfunktion (e-mail, Telegram osv.)

# Loop til at holde øje med siden
while True:
    status = tjek_om_lukket()
    if status is not None:
        if not status:  # Hvis "lukket" IKKE findes
            send_besked()
            break  # Stop loopet, når beskeden er sendt
        else:
            print("Opskrivningen er stadig lukket.")
    else:
        print("Kunne ikke tjekke siden. Prøver igen...")
    
    time.sleep(300)  # Vent 5 minutter før næste tjek
