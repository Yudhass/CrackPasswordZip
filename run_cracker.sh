#!/bin/bash
# Shell script untuk menjalankan ZIP Password Cracker di Linux/macOS
# Jalankan: chmod +x run_cracker.sh && ./run_cracker.sh

echo "========================================"
echo "ZIP Password Cracker - Linux/macOS"
echo "========================================"
echo ""

# Check apakah Python3 terinstall
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 tidak ditemukan!"
    echo ""
    echo "Silakan install Python3 terlebih dahulu:"
    echo "Ubuntu/Debian: sudo apt-get install python3"
    echo "macOS: brew install python3"
    echo ""
    exit 1
fi

# Check apakah folder FileZip ada
if [ ! -d "FileZip" ]; then
    echo "[INFO] Folder FileZip tidak ditemukan. Membuat folder..."
    mkdir FileZip
    echo "[INFO] Folder FileZip berhasil dibuat."
    echo ""
    echo "Silakan letakkan file ZIP di folder FileZip, lalu jalankan lagi script ini."
    echo ""
    exit 0
fi

# Jalankan program
echo "[INFO] Menjalankan ZIP Password Cracker..."
echo ""
python3 crack_zip_password.py

# Tampilkan hasil
echo ""
echo "========================================"
echo "Program selesai!"
echo "========================================"
