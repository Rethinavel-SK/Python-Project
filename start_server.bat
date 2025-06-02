@echo off
echo Starting Tamil Music Platform Server...
echo.

REM Try different Python commands
echo Trying python3...
python3 manage.py runserver 2>nul
if %errorlevel% equ 0 goto :success

echo Trying python...
python manage.py runserver 2>nul
if %errorlevel% equ 0 goto :success

echo Trying with virtual environment...
call venv\Scripts\activate.bat
python manage.py runserver 2>nul
if %errorlevel% equ 0 goto :success

echo Trying with full path...
venv\Scripts\python.exe manage.py runserver 2>nul
if %errorlevel% equ 0 goto :success

:error
echo.
echo ERROR: Could not start Django server!
echo Please check:
echo 1. Python is installed
echo 2. Django is installed (pip install django)
echo 3. You are in the correct directory
echo.
pause
goto :end

:success
echo Server started successfully!

:end
