#!/bin/bash
# Drzewo rodu – uruchomienie jednym kliknięciem (macOS / Linux).
cd "$(dirname "$0")"
if ! python3 -c "import sys" 2>/dev/null; then
  echo "Brak Pythona 3. Zainstaluj go ze strony, która się otworzy, potem uruchom ten plik ponownie."
  (open https://www.python.org/downloads/ || xdg-open https://www.python.org/downloads/) 2>/dev/null
  read -p "Enter, aby zamknąć"; exit 1
fi
# biblioteka do „Odczytaj akt” – opcjonalna
python3 -c "import anthropic" 2>/dev/null || python3 -m pip install --user --quiet --disable-pip-version-check anthropic
python3 serwer.py
