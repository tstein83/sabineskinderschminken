#!/usr/bin/env python3
import os
import urllib.request
import hashlib
from pathlib import Path
from urllib.parse import urljoin

BASE_URL = "https://www.sabineskinderschminken.de/"
IMAGE_DIR = "/Users/D052167/sabines-kinderschminken/public/images/"

# Alle gefundenen Bilder aus den gescannten Seiten
# Format: (relative_url, category)
images_to_download = [
    # Hauptseite
    ("mediapool/99/998389/resources/big_35965930_0_82-150.jpg", "gallery"),
    ("mediapool/99/998389/resources/55481139.jpg", "gallery"),
    ("mediapool/99/998389/resources/55477329.jpg", "gallery"),
    ("mediapool/99/998389/resources/55481149.jpg", "gallery"),
    ("mediapool/99/998389/resources/big_28935202_0_1024-640.jpg", "gallery"),
    ("mediapool/99/998389/resources/52012392.jpg", "services"),
    ("mediapool/99/998389/resources/44697416.jpg", "services"),

    # Team Seite
    ("mediapool/99/998389/resources/52012137.JPG", "team"),
    ("mediapool/99/998389/resources/52012142.jpg", "team"),
    ("mediapool/99/998389/resources/52012227.jpg", "team"),
    ("mediapool/99/998389/resources/52007952.PNG", "team"),

    # Galerie Seite
    ("ci_14387787/small_24899187_1_1285-1920.JPG", "gallery"),
    ("ci_14387787/small_29516341_1_1285-1920.JPG", "gallery"),
    ("ci_14387787/small_25309661.jpg", "gallery"),
    ("ci_14387787/small_30010226_1_1440-1920.JPG", "gallery"),

    # Kinderschminken
    ("mediapool/99/998389/resources/big_55477204_0_263-350.jpg", "services"),
    ("mediapool/99/998389/resources/55477249.jpg", "services"),
    ("mediapool/99/998389/resources/big_55477229_0_263-350.jpg", "services"),
    ("mediapool/99/998389/resources/big_28939642_0_1024-685.JPG", "services"),

    # Ballon-Figuren
    ("mediapool/99/998389/resources/51990137.jpg", "services"),
    ("mediapool/99/998389/resources/51990147.jpg", "services"),
    ("mediapool/99/998389/resources/51990237.jpg", "services"),
    ("mediapool/99/998389/resources/33696789.JPG", "services"),
    ("mediapool/99/998389/resources/36225464.JPG", "services"),
    ("mediapool/99/998389/resources/36225485.JPG", "services"),
    ("mediapool/99/998389/resources/33696912.JPG", "services"),
    ("mediapool/99/998389/resources/33714602.JPG", "services"),
    ("mediapool/99/998389/resources/big_33714687_0_600-450.JPG", "services"),
    ("mediapool/99/998389/resources/33714750.JPG", "services"),
    ("mediapool/99/998389/resources/33696955.JPG", "services"),
    ("mediapool/99/998389/resources/36225471.JPG", "services"),
    ("mediapool/99/998389/resources/big_33697122_0_450-300.JPG", "services"),
    ("mediapool/99/998389/resources/big_33696975_0_450-300.JPG", "services"),
    ("mediapool/99/998389/resources/33699891.JPG", "services"),
    ("mediapool/99/998389/resources/36225499.JPG", "services"),
    ("mediapool/99/998389/resources/36225531.JPG", "services"),
    ("mediapool/99/998389/resources/44697436.jpg", "services"),
    ("mediapool/99/998389/resources/44697461.jpg", "services"),
    ("mediapool/99/998389/resources/44697786.jpg", "services"),

    # Facepainting
    ("mediapool/99/998389/resources/51994412.jpg", "services"),
    ("mediapool/99/998389/resources/51994427.jpg", "services"),
    ("mediapool/99/998389/resources/51994442.jpg", "services"),
    ("mediapool/99/998389/resources/big_30011222_1_450-600.JPG", "services"),
    ("mediapool/99/998389/resources/29561637.JPG", "services"),
    ("mediapool/99/998389/resources/51345277.jpg", "services"),
    ("mediapool/99/998389/resources/big_29562248_1_450-600.JPG", "services"),
    ("mediapool/99/998389/resources/big_29562260_1_450-600.JPG", "services"),

    # Bodypainting
    ("mediapool/99/998389/resources/36224669.jpg", "services"),
    ("mediapool/99/998389/resources/36171098.jpg", "services"),

    # Halloween Effects
    ("mediapool/99/998389/resources/55476979.jpg", "services"),
    ("mediapool/99/998389/resources/55476974.jpg", "services"),
    ("mediapool/99/998389/resources/55476989.jpg", "services"),
    ("mediapool/99/998389/resources/55477014.jpg", "services"),
    ("mediapool/99/998389/resources/55477119.jpg", "services"),
    ("mediapool/99/998389/resources/55477124.jpg", "services"),
    ("mediapool/99/998389/resources/55477129.jpg", "services"),
    ("mediapool/99/998389/resources/big_24384781_0_646-457.jpg", "services"),
    ("mediapool/99/998389/resources/big_29341972_0_500-335.JPG", "services"),
    ("mediapool/99/998389/resources/29516841.jpg", "services"),
    ("mediapool/99/998389/resources/big_29341936_3_401-600.JPG", "services"),
    ("mediapool/99/998389/resources/big_29341947_1_401-600.JPG", "services"),

    # Galerie-1
    ("mediapool/99/998389/resources/big_35516270_0_543-768.jpg", "gallery"),
    ("mediapool/99/998389/resources/big_35516272_0_543-768.jpg", "gallery"),
    ("mediapool/99/998389/resources/big_35516275_0_543-768.jpg", "gallery"),

    # Bellypainting
    ("ci_14502607/small_36170692.jpg", "services"),
    ("ci_14502607/small_25298391_0_1500-1231.jpg", "services"),
    ("ci_14502607/small_25353884_0_1500-1111.jpg", "services"),
    ("ci_14502607/small_25298993_0_1500-1004.jpg", "services"),

    # Schminkstand
    ("mediapool/99/998389/resources/52011382.jpg", "services"),
    ("mediapool/99/998389/resources/52011387.jpg", "services"),
    ("mediapool/99/998389/resources/52011407.jpg", "services"),
    ("mediapool/99/998389/resources/52011532.jpg", "services"),
    ("mediapool/99/998389/resources/52011567.jpg", "services"),
    ("mediapool/99/998389/resources/52011542.jpg", "services"),
    ("mediapool/99/998389/resources/52011942.jpg", "services"),

    # Ballons im Einsatz
    ("mediapool/99/998389/resources/55477254.jpg", "services"),
    ("mediapool/99/998389/resources/55477274.jpg", "services"),
    ("mediapool/99/998389/resources/55477279.jpg", "services"),
    ("mediapool/99/998389/resources/big_35967086_0_482-600.JPG", "services"),
    ("mediapool/99/998389/resources/35967090.JPG", "services"),
    ("mediapool/99/998389/resources/35967093.JPG", "services"),

    # Glitzertattoos
    ("mediapool/99/998389/resources/big_30853786_0_400-300.JPG", "services"),
    ("mediapool/99/998389/resources/big_29361727_1_450-600.JPG", "services"),
    ("mediapool/99/998389/resources/big_29361733_1_450-600.JPG", "services"),
    ("mediapool/99/998389/resources/big_29361736_1_450-600.JPG", "services"),

    # Airbrushtattoos
    ("mediapool/99/998389/resources/big_28914740_0_1024-640.jpg", "services"),
    ("mediapool/99/998389/resources/36321089.jpg", "services"),
]

def get_file_hash(filepath):
    """Berechne MD5 Hash einer Datei"""
    if not os.path.exists(filepath):
        return None
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def get_existing_files():
    """Sammle alle existierenden Bilddateien mit ihren Hashes"""
    existing = {}
    for root, dirs, files in os.walk(IMAGE_DIR):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                filepath = os.path.join(root, file)
                file_hash = get_file_hash(filepath)
                if file_hash:
                    existing[file_hash] = filepath
    return existing

def sanitize_filename(filename):
    """Bereinige Dateinamen"""
    # Entferne 'big_' Prefix
    filename = filename.replace('big_', '')
    # Entferne Größenangaben am Ende (z.B. _0_1024-640)
    import re
    filename = re.sub(r'_\d+_\d+-\d+\.', '.', filename)
    filename = re.sub(r'_\d+\.', '.', filename)
    return filename

def download_image(url, category, existing_hashes):
    """Lade ein Bild herunter, wenn es noch nicht existiert"""
    try:
        # Temporärer Download
        temp_path = "/tmp/temp_image"
        urllib.request.urlretrieve(url, temp_path)

        # Hash berechnen
        file_hash = get_file_hash(temp_path)

        # Prüfe ob bereits vorhanden
        if file_hash in existing_hashes:
            print(f"  SKIP (bereits vorhanden): {url}")
            os.remove(temp_path)
            return None

        # Dateinamen erstellen
        filename = os.path.basename(url)
        filename = sanitize_filename(filename)

        # Zielverzeichnis
        target_dir = os.path.join(IMAGE_DIR, category)
        os.makedirs(target_dir, exist_ok=True)

        # Zieldatei
        target_path = os.path.join(target_dir, filename)

        # Wenn Datei bereits existiert, füge Nummer hinzu
        base_name, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(target_path):
            target_path = os.path.join(target_dir, f"{base_name}_{counter}{ext}")
            counter += 1

        # Verschiebe die Datei
        os.rename(temp_path, target_path)
        print(f"  DOWNLOADED: {filename} -> {category}/")
        return target_path

    except Exception as e:
        print(f"  ERROR: {url} - {str(e)}")
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return None

def main():
    print("=" * 80)
    print("BILDSUCHE UND DOWNLOAD FÜR SABINES KINDERSCHMINKEN")
    print("=" * 80)
    print()

    # Existierende Dateien laden
    print("Scanne existierende Bilder...")
    existing_hashes = get_existing_files()
    print(f"✓ {len(existing_hashes)} existierende Bilder gefunden")
    print()

    # Download-Statistik
    downloaded = []
    skipped = 0
    errors = 0

    print(f"Prüfe {len(images_to_download)} Bilder...")
    print()

    for relative_url, category in images_to_download:
        full_url = urljoin(BASE_URL, relative_url)
        print(f"Prüfe: {relative_url}")

        result = download_image(full_url, category, existing_hashes)
        if result:
            downloaded.append((result, category, relative_url))
        elif "SKIP" in str(result):
            skipped += 1
        else:
            errors += 1

    print()
    print("=" * 80)
    print("ZUSAMMENFASSUNG")
    print("=" * 80)
    print(f"Bereits vorhanden: {len(existing_hashes)}")
    print(f"Neu heruntergeladen: {len(downloaded)}")
    print(f"Übersprungen (Duplikate): {skipped}")
    print(f"Fehler: {errors}")
    print(f"Gesamt geprüft: {len(images_to_download)}")
    print()

    if downloaded:
        print("NEU HERUNTERGELADENE BILDER:")
        print("-" * 80)
        for filepath, category, url in downloaded:
            filename = os.path.basename(filepath)
            print(f"  {category:12} | {filename}")

    print()
    print("✓ Download abgeschlossen!")

    return len(downloaded)

if __name__ == "__main__":
    main()
