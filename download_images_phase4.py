#!/usr/bin/env python3
import os
import urllib.request
import hashlib
from pathlib import Path
from urllib.parse import urljoin

BASE_URL = "https://www.sabineskinderschminken.de/"
IMAGE_DIR = "/Users/D052167/sabines-kinderschminken/public/images/"

# Phase 4: Letzte gefundene Bilder
images_to_download = [
    # Hochzeitsdekoration
    ("mediapool/99/998389/resources/52008487.jpg", "services"),
    ("mediapool/99/998389/resources/52010022.JPG", "services"),
    ("mediapool/99/998389/resources/52010147.JPG", "services"),
    ("mediapool/99/998389/resources/52010267.jpg", "services"),
    ("mediapool/99/998389/resources/35509200.JPG", "services"),
    ("mediapool/99/998389/resources/34764806.JPG", "services"),
    ("mediapool/99/998389/resources/35509613.JPG", "services"),
    ("mediapool/99/998389/resources/34764861.JPG", "services"),
    ("mediapool/99/998389/resources/35508979.JPG", "services"),
    ("mediapool/99/998389/resources/35508982.JPG", "services"),
    ("mediapool/99/998389/resources/35509010.JPG", "services"),
    ("mediapool/99/998389/resources/35509013.JPG", "services"),
    ("mediapool/99/998389/resources/35509175.jpg", "services"),
    ("mediapool/99/998389/resources/35509581.jpg", "services"),

    # Verpackungsballon
    ("mediapool/99/998389/resources/36280079.JPG", "services"),
    ("mediapool/99/998389/resources/36280068.jpg", "services"),
    ("mediapool/99/998389/resources/35967640.JPG", "services"),
    ("mediapool/99/998389/resources/33715048.JPG", "services"),
    ("mediapool/99/998389/resources/33715119.jpg", "services"),
    ("mediapool/99/998389/resources/33715124.jpg", "services"),
    ("mediapool/99/998389/resources/33715135.JPG", "services"),
    ("mediapool/99/998389/resources/33715137.jpg", "services"),
    ("mediapool/99/998389/resources/33715189.JPG", "services"),
    ("mediapool/99/998389/resources/33715225.JPG", "services"),
    ("mediapool/99/998389/resources/33838628.jpg", "services"),
    ("mediapool/99/998389/resources/33715254.JPG", "services"),
    ("mediapool/99/998389/resources/33838643.JPG", "services"),

    # Ballongeschenke
    ("mediapool/99/998389/resources/33507730.JPG", "services"),
    ("mediapool/99/998389/resources/33507817.JPG", "services"),
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
            print(f"  SKIP (bereits vorhanden)")
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
        print(f"  ERROR: {str(e)}")
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return None

def main():
    print("=" * 80)
    print("BILDSUCHE UND DOWNLOAD - PHASE 4 (FINAL)")
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
        filename_short = os.path.basename(relative_url)[:40]
        print(f"Prüfe: {filename_short}...")

        result = download_image(full_url, category, existing_hashes)
        if result:
            downloaded.append((result, category, relative_url))
            existing_hashes[get_file_hash(result)] = result  # Füge zur Liste hinzu
        elif result is None:
            skipped += 1
        else:
            errors += 1

    print()
    print("=" * 80)
    print("ZUSAMMENFASSUNG - PHASE 4 (FINAL)")
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
    print("=" * 80)
    print("ALLE DOWNLOADS ABGESCHLOSSEN!")
    print("=" * 80)

    return len(downloaded)

if __name__ == "__main__":
    main()
