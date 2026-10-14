# Drzewo rodu

🇬🇧 *Family tree app for GEDCOM files (e.g. MyHeritage export). English interface: ☰ menu → Język / Language → English. Start: download ZIP, double-click `Uruchom.bat` (Windows) or `Uruchom.command` (macOS/Linux).*

Przeglądarkowa aplikacja do prowadzenia drzewa genealogicznego z pliku GEDCOM (.ged, np. eksport z MyHeritage).

**Funkcje:** drzewo z rozwijaniem gałęzi w miejscu, profil osoby, edycja, zdjęcia, notatki badawcze, mapa z animacją migracji, detektyw sprzeczności dat, sieć powiązań, życie na tle historii, „gdzie szukać dalej”, wyszukiwanie w serwisach genealogicznych, odczyt aktów przez Claude.

## Uruchomienie – jedno kliknięcie
1. Pobierz projekt (zielony przycisk **Code → Download ZIP**) i rozpakuj.
2. **Windows:** kliknij dwukrotnie **`Uruchom.bat`**.
   **macOS / Linux:** kliknij dwukrotnie **`Uruchom.command`** (za pierwszym razem: prawy klik → Otwórz).
3. Aplikacja sama otworzy się w przeglądarce. Wczytaj swój plik .ged (☰ → Otwórz plik).

Plik startowy sam sprawdza, czego brakuje:
- gdy nie ma Pythona – na Windows instaluje go automatycznie (winget), na macOS otwiera stronę pobierania,
- doinstalowuje bibliotekę do odczytu aktów,
- uruchamia serwer i otwiera przeglądarkę (ponowne kliknięcie tylko otwiera przeglądarkę).

Nie zamykaj czarnego okna, dopóki korzystasz z aplikacji. Najlepiej działa w **Chrome lub Edge** (zapis do pliku .ged i listów).

**Odczyt aktów przez Claude (opcjonalnie):** skopiuj `.env.example` jako `.env` i wpisz w nim swój klucz Anthropic API.

Dla zaawansowanych: `python serwer.py [port]` (domyślnie 8770).
