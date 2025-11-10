# 🔐 ZIP Password Cracker Suite - Windows Edition# 🪟 Panduan Instalasi & Penggunaan di Windows



**Version 2.0.0** - Panduan Lengkap untuk WindowsPanduan lengkap untuk menjalankan **ZIP Password Cracker** di Windows 10/11.



[![Windows](https://img.shields.io/badge/Windows-7%20%7C%208%20%7C%2010%20%7C%2011-blue?logo=windows)](https://www.microsoft.com/windows)---

[![Python](https://img.shields.io/badge/Python-3.6%2B-green?logo=python)](https://www.python.org/)

[![License](https://img.shields.io/badge/License-Educational-red)](LICENSE)## 📋 Requirement



> 🎯 **Tool profesional untuk recovery password ZIP yang terlupa**  - **Windows 10** atau **Windows 11**

> ✨ **Dilengkapi progress bar real-time dan auto-detection enkripsi**- **Python 3.6** atau lebih tinggi



------



## 📋 Daftar Isi## 🔧 Instalasi Python di Windows



- [Instalasi](#-instalasi)### 1. Download Python

- [3 Program Utama](#-3-program-utama)

- [Cara Penggunaan](#-cara-penggunaan)1. Buka browser dan kunjungi: https://www.python.org/downloads/

- [Fitur Windows Khusus](#-fitur-windows-khusus)2. Klik tombol **"Download Python 3.x.x"** (versi terbaru)

- [Troubleshooting Windows](#-troubleshooting-windows)3. Tunggu sampai file installer selesai didownload

- [Tips Windows](#-tips-windows)

### 2. Install Python

---

1. **Double-click** file installer yang sudah didownload (contoh: `python-3.11.5-amd64.exe`)

## 🚀 Instalasi2. ⚠️ **PENTING**: Centang **"Add Python to PATH"** di bagian bawah

   ```

### Langkah 1: Install Python   ☑ Add Python 3.x to PATH

   ```

1. **Download Python** dari [python.org](https://www.python.org/downloads/)3. Klik **"Install Now"**

2. ⚠️ **PENTING**: Centang **"Add Python to PATH"** saat install4. Tunggu proses instalasi selesai

3. Verifikasi instalasi:5. Klik **"Close"**



```cmd### 3. Verifikasi Instalasi

python --version

```1. Tekan tombol **Windows + R**

2. Ketik `cmd` lalu tekan **Enter**

Harus menampilkan: `Python 3.6.x` atau lebih tinggi3. Di Command Prompt, ketik:

   ```cmd

### Langkah 2: Install Dependencies   python --version

   ```

Buka **Command Prompt** (CMD) atau **PowerShell** dan jalankan:4. Jika muncul versi Python (contoh: `Python 3.11.5`), instalasi berhasil! ✅



```cmd---

pip install pyzipper

```## 📦 Setup Program



Output yang benar:### 1. Download Program

```

Successfully installed pycryptodomex-3.23.0 pyzipper-0.3.6Download semua file program ke folder (contoh: `C:\Users\YourName\Documents\CrackPasswordZIP`):

```

```

### Langkah 3: Setup FolderCrackPasswordZIP\

├── crack_zip_password.py     # File utama

```cmd├── run_cracker.bat           # Double-click untuk menjalankan

mkdir C:\ZipCracker├── FileZip\                  # Folder untuk file ZIP

cd C:\ZipCracker└── README_WINDOWS.md         # File ini

mkdir FileZip```

mkdir Extracted

```### 2. Buat Folder FileZip



✅ **Instalasi selesai!**Jika folder `FileZip` belum ada, buat folder baru:



---1. Buka **File Explorer** (Windows + E)

2. Masuk ke folder program (contoh: `C:\...\CrackPasswordZIP`)

## 🎯 3 Program Utama3. Klik kanan → **New** → **Folder**

4. Beri nama: `FileZip`

| Program | Character Set | Kecepatan | Cocok Untuk |

|---------|---------------|-----------|-------------|### 3. Copy File ZIP

| 🔢 **angka.py** | 0-9 | ⚡⚡⚡ | PIN, Tanggal |

| 🔤 **alpha.py** | a-z, A-Z | ⚡⚡ | Kata, Nama |Copy semua file ZIP yang ingin di-crack ke folder `FileZip`:

| 🔣 **alphanumeric.py** | a-z, A-Z, 0-9 | ⚡ | Kombinasi |

```

---CrackPasswordZIP\

└── FileZip\

## 💻 Cara Penggunaan    ├── archive1.zip

    ├── archive2.zip

### Program 1: Angka (0-9)    └── archive3.zip

```

```cmd

cd C:\ZipCracker---

python crack_zip_password_angka.py

```## 🚀 Cara Menggunakan



**Output:**### Metode 1: Double-Click (Paling Mudah) ⭐

```

[+] PASSWORD DITEMUKAN: 1234561. **Double-click** file `run_cracker.bat`

[+] File sudah diekstrak ke Extracted\locked2. Jendela Command Prompt akan terbuka otomatis

```3. Program akan berjalan dan menampilkan progress

4. Tunggu sampai selesai

### Program 2: Alpha (a-z, A-Z)5. Tekan tombol apapun untuk menutup jendela



```cmd### Metode 2: Via Command Prompt

python crack_zip_password_alpha.py

```1. Tekan **Windows + R**

2. Ketik `cmd` lalu tekan **Enter**

**Progress Bar:**3. Pindah ke folder program:

```   ```cmd

[*] Length 2: [████████████████████              ] 65.2% (1762/2704)   cd C:\Users\YourName\Documents\CrackPasswordZIP

```   ```

4. Jalankan program:

### Program 3: Alphanumeric   ```cmd

   python crack_zip_password.py

```cmd   ```

python crack_zip_password_alphanumeric.py

```### Metode 3: Via PowerShell



---1. Buka **PowerShell** (Windows + X → Windows PowerShell)

2. Pindah ke folder program:

## 🪟 Fitur Windows Khusus   ```powershell

   cd C:\Users\YourName\Documents\CrackPasswordZIP

### Auto-Detection AES   ```

3. Jalankan program:

Program otomatis detect ZIP dari Windows Explorer yang pakai **AES-256**:   ```powershell

   python crack_zip_password.py

```   ```

[*] Deteksi: AES encryption (Windows) - menggunakan pyzipper

```---



### Buat Shortcut## 📊 Contoh Output di Windows



```cmd```

echo python crack_zip_password_angka.py > run.bat============================================================

echo pause >> run.batZIP Password Cracker - 4 Digit Brute Force

```Cross-platform: Linux | Windows | macOS

============================================================

Double-click `run.bat` untuk jalankan![*] Ditemukan 2 file ZIP

[*] Memeriksa log.txt untuk file yang sudah di-crack...

---

[*] Memproses: archive1.zip

## 🔧 Troubleshooting Windows[*] File terenkripsi, mencoba crack password...

[*] Progress: mencoba password 0000...

### ❌ "python is not recognized"[*] Progress: mencoba password 1000...

[+] PASSWORD DITEMUKAN: 1234

**Solusi:**[*] Mengekstrak file...

1. Reinstall Python dengan centang "Add to PATH"[+] Ekstraksi selesai!

2. Atau tambah manual ke System Environment Variables

[*] Menulis hasil ke log.txt...

### ❌ "Permission denied"

============================================================

**Solusi:**RINGKASAN

1. Jalankan CMD **as Administrator**============================================================

2. Atau pindah folder ke `C:\` (bukan di Program Files)[OK] archive1.zip: 1234

[SKIP] archive2.zip: 5678

### ❌ Antivirus Block

[+] Selesai! Hasil disimpan di log.txt

**Solusi:**[+] File terekstrak di folder Extracted/

1. Add exception di Windows Defender

2. Settings → Security → Exclusions → Add `C:\ZipCracker`Press any key to continue . . .

```

---

---

## 💡 Tips Windows

## 📁 Lokasi Output

### Run di Background

### File Hasil

```bat

start /B python crack_zip_password_angka.py- **log.txt** - Berisi semua password yang berhasil ditemukan

```  ```

  Lokasi: C:\Users\YourName\Documents\CrackPasswordZIP\log.txt

### High Priority  ```



```cmd### Folder Extracted

start /HIGH python crack_zip_password_angka.py

```- **Extracted\** - Berisi file-file yang sudah diekstrak

  ```

### Auto-Notification  Lokasi: C:\Users\YourName\Documents\CrackPasswordZIP\Extracted\

  ```

```bat

python crack_zip_password_angka.pyContoh struktur:

msg %username% "Selesai! Cek log.txt"```

```Extracted\

├── archive1\

---│   ├── file1.txt

│   ├── image.jpg

## 📊 Estimasi Waktu Windows│   └── document.pdf

└── archive2\

### Program Angka    └── data.xlsx

```

| Digit | Time |

|-------|------|---

| 4 | 2-5 detik |

| 6 | 3-8 menit |## 🐛 Troubleshooting Windows

| 8 | 5-10 jam |

### ❌ Error: "Python is not recognized"

### Program Alpha

**Penyebab**: Python tidak ada di PATH

| Length | Time |

|--------|------|**Solusi**:

| 2 | < 1 detik |1. Install ulang Python

| 3 | 30-60 detik |2. ⚠️ Pastikan centang **"Add Python to PATH"**

| 4 | 25 menit - 1 jam |3. Atau tambahkan PATH manual:

   - Buka **System Properties** (Windows + Pause/Break)

### Program Alphanumeric   - Klik **Advanced system settings**

   - Klik **Environment Variables**

| Length | Time |   - Di **System variables**, cari **Path**

|--------|------|   - Klik **Edit**, lalu **New**

| 2 | 1-2 detik |   - Tambahkan path Python (contoh: `C:\Python311\`)

| 3 | 1-2 menit |   - Tambahkan path Scripts (contoh: `C:\Python311\Scripts\`)

| 4 | 1-3 jam |   - Klik **OK** semua dialog

   - Restart Command Prompt

---

### ❌ Error: "FileZip folder not found"

## 🎯 Best Practices

**Solusi**: Buat folder FileZip secara manual

1. **Letakkan ZIP di folder `FileZip\`**```cmd

2. **Pilih program sesuai jenis password**mkdir FileZip

3. **Monitor `log.txt` untuk hasil**```

4. **Backup hasil di folder `Extracted\`**

### ❌ Unicode/Encoding Error

---

**Solusi**: Program sudah handle otomatis, tapi jika masih error:

## 📱 Alternative Tools (Opsional)1. Buka Command Prompt

2. Jalankan dengan encoding UTF-8:

### Windows Store Python   ```cmd

   chcp 65001

Jika instalasi gagal, install dari **Microsoft Store**:   python crack_zip_password.py

1. Buka Store → Search "Python 3.10"   ```

2. Install

3. Restart CMD### ❌ Permission Denied



### PowerShell Script**Solusi**: Jalankan sebagai Administrator

1. Klik kanan `run_cracker.bat`

```powershell2. Pilih **"Run as administrator"**

cd C:\ZipCracker

python .\crack_zip_password_angka.py### ❌ Windows Defender Memblokir

```

**Catatan**: Windows Defender mungkin menganggap sebagai suspicious

---

**Solusi**:

## 🚀 Quick Start1. Klik **More info**

2. Klik **Run anyway**

```cmd3. Atau tambahkan folder ke exclusion list:

# 1. Setup   - Buka **Windows Security**

mkdir C:\ZipCracker   - **Virus & threat protection**

cd C:\ZipCracker   - **Manage settings**

pip install pyzipper   - **Add or remove exclusions**

   - Tambahkan folder program

# 2. Copy file ZIP ke FileZip\

copy "path\to\locked.zip" FileZip\---



# 3. Run program## ⚡ Tips Performa di Windows

python crack_zip_password_angka.py

### 1. Disable Windows Defender Sementara

# 4. Cek hasil

cd ExtractedUntuk kecepatan maksimal (hanya saat cracking):

```1. Buka **Windows Security**

2. **Virus & threat protection**

---3. **Manage settings**

4. Matikan **Real-time protection** (sementara)

**🎉 Selamat! Password ZIP Anda sudah di-recovery!**5. ⚠️ **Jangan lupa nyalakan kembali setelah selesai!**



*Windows Edition - Version 2.0.0*### 2. Priority Proses


Untuk memberikan prioritas lebih tinggi:
1. Buka **Task Manager** (Ctrl + Shift + Esc)
2. Tab **Details**
3. Cari `python.exe`
4. Klik kanan → **Set priority** → **High**

### 3. Background Mode

Untuk menjalankan di background:
```cmd
start /B python crack_zip_password.py > output.log 2>&1
```

---

## 🎯 Shortcut Keyboard Windows

Saat program berjalan:

- **Ctrl + C** - Stop program
- **Ctrl + Pause** - Pause terminal
- **Alt + Tab** - Switch window (program tetap jalan di background)
- **Windows + D** - Minimize semua window

---

## 📝 Scheduled Task (Jalankan Otomatis)

### Setup Task Scheduler

1. Tekan **Windows + R**
2. Ketik `taskschd.msc` lalu Enter
3. Klik **Create Basic Task**
4. Nama: `ZIP Password Cracker`
5. Trigger: Pilih jadwal (Daily, Weekly, dll)
6. Action: **Start a program**
7. Program: `python`
8. Arguments: `crack_zip_password.py`
9. Start in: `C:\Users\YourName\Documents\CrackPasswordZIP`
10. Klik **Finish**

---

## 🔐 Windows Firewall

Program ini **TIDAK** memerlukan akses internet atau network.

Jika Windows Firewall bertanya:
- **Pilih**: ❌ Cancel (tidak perlu akses network)

---

## 💾 Backup & Restore

### Backup Password Log

```cmd
copy log.txt log_backup_%date:~-4,4%%date:~-10,2%%date:~-7,2%.txt
```

### Export ke Excel

1. Buka **log.txt** di Notepad
2. Copy isi file
3. Buka **Excel**
4. Paste data
5. Format sesuai kebutuhan

---

## 🖥️ System Requirements

### Minimum
- **OS**: Windows 10 (64-bit)
- **RAM**: 2 GB
- **Storage**: 100 MB free space
- **Python**: 3.6+

### Recommended
- **OS**: Windows 11 (64-bit)
- **RAM**: 4 GB or more
- **Storage**: 1 GB free space
- **Python**: 3.10+
- **CPU**: Multi-core processor

---

## 🎨 Tampilan Console

### Mengganti Warna Console

Buat file `custom_run.bat`:
```batch
@echo off
color 0A
REM 0A = Black background, Green text
REM Pilihan lain: 0B (Cyan), 0C (Red), 0E (Yellow), 0F (White)
python crack_zip_password.py
pause
```

### Font Console

1. Klik kanan title bar Command Prompt
2. **Properties**
3. Tab **Font**
4. Pilih font yang diinginkan (recommend: Consolas, Cascadia Code)

---

## ❓ FAQ Windows

**Q: Apakah aman untuk Windows?**
A: Ya, 100% aman. Program tidak mengakses internet atau system files.

**Q: Perlu install library tambahan?**
A: Tidak! Semua library sudah built-in di Python.

**Q: Bisa jalan di Windows 7?**
A: Bisa, tapi install Python 3.8 atau lebih lama (Python 3.9+ tidak support Windows 7).

**Q: Konsumsi resource berapa?**
A: CPU: 10-30%, RAM: ~50 MB, Storage minimal.

**Q: File original aman?**
A: Ya! Program hanya membaca, tidak memodifikasi file ZIP original.

**Q: Bisa dijadikan .exe?**
A: Ya! Gunakan PyInstaller:
```cmd
pip install pyinstaller
pyinstaller --onefile crack_zip_password.py
```

---

## 🆘 Kontak Support

Jika mengalami masalah di Windows:

1. Cek **log.txt** untuk error details
2. Screenshot error message
3. Catat versi Python dan Windows
4. Buat issue di GitHub

---

## ✅ Checklist Setup Windows

- [ ] Python 3.x terinstall
- [ ] "Add Python to PATH" sudah dicentang
- [ ] Command `python --version` berfungsi
- [ ] Folder `FileZip` sudah dibuat
- [ ] File ZIP sudah dicopy ke folder `FileZip`
- [ ] File `crack_zip_password.py` ada di folder
- [ ] File `run_cracker.bat` ada di folder
- [ ] Sudah test double-click `run_cracker.bat`

---

## 🎉 Selamat!

Program ZIP Password Cracker sekarang siap digunakan di Windows!

**Happy Cracking! 🔓**

---

*Last Updated: November 10, 2025*
