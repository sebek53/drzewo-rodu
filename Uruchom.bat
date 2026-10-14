@echo off
rem Drzewo rodu – uruchomienie jednym kliknieciem (Windows).
rem Sprawdza Pythona (gdy brak – instaluje przez winget), doinstalowuje biblioteke do odczytu aktow, startuje serwer i otwiera przegladarke.
chcp 65001 >nul
cd /d "%~dp0"
title Drzewo rodu

set "PY="
where py >nul 2>nul && py -3 -c "import sys" >nul 2>nul && set "PY=py -3"
if not defined PY python -c "import sys" >nul 2>nul && set "PY=python"
if not defined PY if exist "%LocalAppData%\Programs\Python\Python312\python.exe" set "PY=%LocalAppData%\Programs\Python\Python312\python.exe"

if not defined PY (
  echo Nie znaleziono Pythona - instaluje go automatycznie, to potrwa chwile...
  winget install -e --id Python.Python.3.12 --scope user --silent --accept-package-agreements --accept-source-agreements
  if exist "%LocalAppData%\Programs\Python\Python312\python.exe" set "PY=%LocalAppData%\Programs\Python\Python312\python.exe"
)
if not defined PY (
  echo.
  echo Nie udalo sie zainstalowac Pythona automatycznie.
  echo Zainstaluj go ze strony, ktora sie otworzy ^(zaznacz "Add python.exe to PATH"^), potem uruchom ten plik ponownie.
  start "" https://www.python.org/downloads/
  pause
  exit /b 1
)

rem biblioteka do „Odczytaj akt” (Claude) – opcjonalna, reszta aplikacji dziala bez niej
%PY% -c "import anthropic" >nul 2>nul || (
  echo Doinstalowuje biblioteke do odczytu aktow...
  %PY% -m pip install --user --quiet --disable-pip-version-check anthropic
)

%PY% serwer.py
pause
