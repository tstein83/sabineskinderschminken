#!/usr/bin/env python3
import os
import urllib.request
import hashlib
from pathlib import Path
from urllib.parse import urljoin

BASE_URL = "https://www.sabineskinderschminken.de/"
IMAGE_DIR = "/Users/D052167/sabines-kinderschminken/public/images/"

# Phase 2: Weitere gefundene Bilder
images_to_download = [
    # Baby Shower Party
    ("mediapool/99/998389/resources/36170785.jpg", "services"),

    # Kinderanimation
    ("mediapool/99/998389/resources/35967427.jpg", "services"),
    ("mediapool/99/998389/resources/35967428.JPG", "services"),
    ("mediapool/99/998389/resources/35967430.jpg", "services"),
    ("mediapool/99/998389/resources/53085032.jpg", "services"),
    ("mediapool/99/998389/resources/53085037.PNG", "services"),
    ("mediapool/99/998389/resources/53085052.jpg", "services"),
    ("mediapool/99/998389/resources/35967479.JPG", "services"),
    ("mediapool/99/998389/resources/big_35967481_0_510-340.JPG", "services"),

    # Kindergeburtstag
    ("mediapool/99/998389/resources/19805564.jpg", "services"),

    # Prominente
    ("mediapool/99/998389/resources/51990022.jpg", "gallery"),
    ("mediapool/99/998389/resources/51990027.jpg", "gallery"),
    ("mediapool/99/998389/resources/51989977.jpg", "gallery"),
    ("mediapool/99/998389/resources/51989967.jpg", "gallery"),
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
    print("BILDSUCHE UND DOWNLOAD - PHASE 2")
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
            existing_hashes[get_file_hash(result)] = result  # Füge zur Liste hinzu
        elif "SKIP" in str(result):
            skipped += 1
        else:
            errors += 1

    print()
    print("=" * 80)
    print("ZUSAMMENFASSUNG - PHASE 2")
    print("=" * 80)
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
    print("✓ Download Phase 2 abgeschlossen!")

    return len(downloaded)

if __name__ == "__main__":
    main()
