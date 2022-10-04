@echo off

IF EXIST src/.env (GOTO :SETUPDONE) ELSE GOTO :SETUPNOTDONE

:SETUPDONE
REM Set the path to the directory where the main script is located
cd src

Rem activate the virtual environment
call venv\Scripts\activate

Rem run the main script
python main.py

GOTO :END

:SETUPNOTDONE
ECHO You have not setup PexelBot yet!
ECHO Please run the setup.bat file first
PAUSE

:END