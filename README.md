# Drzewo rodu

![Drzewo rodu – darmowa aplikacja do drzewa genealogicznego](docs/promo-pl.svg)

🇬🇧 
![Drzewo rodu – free family tree app](docs/promo-en.svg)

*Family tree app for GEDCOM files (e.g. MyHeritage export). English interface: ☰ menu → Język / Language → English. Start: download ZIP, double-click `Uruchom.bat` (Windows) or `Uruchom.command` (macOS/Linux).*

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

**Odczyt aktów przez Claude (opcjonalnie):** w aplikacji ☰ → *Klucz Claude* wklej swój klucz z [console.anthropic.com](https://console.anthropic.com/settings/keys) (płacisz Anthropic za własne odczyty). Zaawansowani mogą zamiast tego użyć pliku `.env`.

Dla zaawansowanych: `python serwer.py [port]` (domyślnie 8770).

## Wsparcie / Support
Aplikacja jest darmowa. Jeśli Ci pomogła, możesz postawić autorowi kawę – przycisk jest też w menu ☰.

☕ [buycoffee.to/sebastian.garstka](https://buycoffee.to/sebastian.garstka) (BLIK, przelew) · [ko-fi.com/sebastiangarstka](https://ko-fi.com/sebastiangarstka)

## Licencja / License
Copyright © 2026 Sebastian Garstka. Program udostępniony na licencji **GNU AGPL v3** (plik [LICENSE](LICENSE)): możesz go używać, zmieniać i rozpowszechniać, także komercyjnie, pod warunkiem że zmieniony kod – również gdy udostępniasz program innym przez internet – udostępnisz na tej samej licencji, z informacją o autorze.

*Licensed under the GNU Affero General Public License v3.0.*
