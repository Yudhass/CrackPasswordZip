@echo off
REM Batch script untuk menjalankan ZIP Password Cracker di Windows
REM Double-click file ini untuk menjalankan program

title ZIP Password Cracker - 4 Digit Brute Force

echo ========================================
echo ZIP Password Cracker - Windows
echo ========================================
echo.

REM Check apakah Python terinstall
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python tidak ditemukan!
    echo.
    echo Silakan install Python terlebih dahulu:
    echo https://www.python.org/downloads/
    echo.
    echo Pastikan centang "Add Python to PATH" saat install
    echo.
    pause
    exit /b 1
)

REM Check apakah folder FileZip ada
if not exist "FileZip" (
    echo [INFO] Folder FileZip tidak ditemukan. Membuat folder...
    mkdir FileZip
    echo [INFO] Folder FileZip berhasil dibuat.
    echo.
    echo Silakan letakkan file ZIP di folder FileZip, lalu jalankan lagi script ini.
    echo.
    pause
    exit /b 0
)

REM Jalankan program
echo [INFO] Menjalankan ZIP Password Cracker...
echo.
python crack_zip_password.py

REM Pause untuk melihat hasil
echo.
echo ========================================
echo Program selesai!
echo ========================================
pause
