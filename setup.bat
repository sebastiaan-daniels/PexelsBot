@ECHO OFF
TITLE PexelBot Setup
IF EXIST src/.env (GOTO :EXISTING) ELSE GOTO :FROMSCRATCH


:EXISTING
ECHO file exists
GOTO :END


:FROMSCRATCH
REM Create .env file
python setup/install_and_setup.py -env
cls

REM Setup the venv
ECHO Setting up virtual environment...
cd src
python -m venv venv
cls

ECHO Activating virtual environment...
call venv\Scripts\activate
cls

ECHO Installing dependencies...
pip install --disable-pip-version-check -q -r ../setup/requirements.txt
cd ..
cls

REM copy the run file to the root
copy setup\run.bat . >nul
cls

REM deactivate the venv
deactivate

GOTO :END


:END
ECHO Done!
PAUSE
