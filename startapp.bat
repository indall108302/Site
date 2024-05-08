@echo off

REM Активация виртуального окружения
call .venv\Scripts\activate.bat

REM Переход в папку с проектом Django
cd gamecollector

REM Запуск сервера Django
start cmd /k "start "" "http://127.0.0.1:8000/" & python manage.py runserver --insecure"

REM Ожидание закрытия браузера
:LOOP
timeout /t 1 /nobreak >nul
tasklist | find "chrome.exe" >nul
if errorlevel 1 goto :LOOP

REM Деактивация виртуального окружения
deactivate.bat