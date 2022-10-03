@echo off

REM Set the path to the directory where the main script is located
cd src

Rem activate the virtual environment
call venv\Scripts\activate

Rem run the main script
python main.py
