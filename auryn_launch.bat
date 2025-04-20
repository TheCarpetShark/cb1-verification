@echo off
SETLOCAL ENABLEEXTENSIONS

REM --- Define paths ---
SET AURYN_DIR=D:\NEURAL_CORE\auryn_core
SET VENV_PATH=%AURYN_DIR%\venv\Scripts\activate.bat
SET PYTHON_SCRIPT=%AURYN_DIR%\auryn_seed_startup.py
SET POWERSHELL_INJECT=%AURYN_DIR%\inject_memory_and_launch.ps1
SET GPT4ALL_GUI=D:\GPT4ALL\bin\chat.exe

REM --- Activate venv and run seed script ---
call "%VENV_PATH%"
python "%PYTHON_SCRIPT%"

REM --- Inject memory using PowerShell silently ---
powershell -ExecutionPolicy Bypass -File "%POWERSHELL_INJECT%" -WindowStyle Hidden

REM --- Open GPT4All GUI ---
start "" "%GPT4ALL_GUI%"

REM --- Optional: Log that launch completed ---
echo [%DATE% %TIME%] Aurnis Launched Successfully >> "%AURYN_DIR%\auryn_launch.log"

ENDLOCAL
