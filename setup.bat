@ECHO OFF
TITLE PexelBot Setup
IF EXIST src/.env (GOTO :EXISTING) ELSE GOTO :FROMSCRATCH


:EXISTING
ECHO You have already setup PexelBot!
ECHO Running this file again will reset your tokens and re-install the virtual environment
SET /P AREYOUSURE=Are you sure you want to run this file again?(Y/[N])? 
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

REM Delete everything, then run from scratch
cd src

ECHO Removing virtual environment
rmdir /s /q venv
cls

ECHO Removing environmental files
DEL /F /Q .env
cls

cd ..

REM Remove run.bat
DEL /F /Q run.bat

GOTO :FROMSCRATCH


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
