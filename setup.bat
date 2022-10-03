@ECHO OFF
IF EXIST src/.env (GOTO :EXISTING) ELSE GOTO :FROMSCRATCH


:EXISTING
echo file exists
GOTO :END


:FROMSCRATCH
Rem Create .env file
python setup/install_and_setup.py -env

Rem Setup the venv
echo Setting up virtual environment...
cd src
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install --disable-pip-version-check -q -r ../setup/requirements.txt
cd ..

echo Deactivating virtual environment...
deactivate

GOTO :END


:END
echo end
PAUSE
