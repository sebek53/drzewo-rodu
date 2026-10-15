@echo off
rem Drzewo rodu – uruchomienie jednym kliknieciem (Windows).
rem Gdy jest Python: doinstalowuje biblioteke do odczytu aktow, startuje serwer. Gdy brak Pythona: otwiera drzewo.html wprost.
chcp 65001 >nul
cd /d "%~dp0"
title Drzewo rodu

set "PY="
where py >nul 2>nul && py -3 -c "import sys" >nul 2>nul && set "PY=py -3"
if not defined PY python -c "import sys" >nul 2>nul && set "PY=python"
if not defined PY if exist "%LocalAppData%\Programs\Python\Python312\python.exe" set "PY=%LocalAppData%\Programs\Python\Python312\python.exe"

rem bez Pythona aplikacja tez dziala - otwieramy ja wprost w przegladarce
if not defined PY (
  start "" "%~dp0drzewo.html"
  exit /b 0
)

rem biblioteka do „Odczytaj akt” (Claude) – opcjonalna, reszta aplikacji dziala bez niej
%PY% -c "import anthropic" >nul 2>nul || (
  echo Doinstalowuje biblioteke do odczytu aktow...
  %PY% -m pip install --user --quiet --disable-pip-version-check anthropic
)

%PY% serwer.py
pause
