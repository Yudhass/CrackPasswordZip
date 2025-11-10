# 🔐 ZIP Password Cracker - Complete Suite# 🔐 ZIP Password Cracker - Complete Suite



**Version 2.0.0** - Full Cross-Platform Support (Linux & Windows)**Version 2.0.0** - Full Cross-Platform Support (Linux & Windows)



Kumpulan program Python untuk melakukan **crack password ZIP** secara otomatis menggunakan teknik brute force dengan **progress bar real-time**. Suite ini terdiri dari 3 program berbeda sesuai dengan tipe password yang ingin di-crack.Kumpulan program Python untuk melakukan **crack password ZIP** secara otomatis menggunakan teknik brute force dengan **progress bar real-time**. Suite ini terdiri dari 3 program berbeda sesuai dengan tipe password yang ingin di-crack.



------



## 📖 **Pilih Dokumentasi Sesuai Platform Anda:**## 📖 **Pilih Dokumentasi Sesuai Platform Anda:**



<table><table>

<tr><tr>

<td align="center" width="50%"><td align="center" width="50%">



### 🪟 **Pengguna Windows**### 🪟 **Pengguna Windows**



[![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](README_WINDOWS.md)[![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](README_WINDOWS.md)



**[📘 Buka Panduan Windows →](README_WINDOWS.md)****[📘 Buka Panduan Windows →](README_WINDOWS.md)**



Panduan lengkap untuk:Panduan lengkap untuk:

- ✅ Instalasi di Windows (CMD/PowerShell)- ✅ Instalasi di Windows (CMD/PowerShell)

- ✅ Cara penggunaan di Windows- ✅ Cara penggunaan di Windows

- ✅ Troubleshooting Windows- ✅ Troubleshooting Windows

- ✅ Tips & Tricks khusus Windows- ✅ Tips & Tricks khusus Windows

- ✅ Batch files & Task Scheduler- ✅ Batch files & Task Scheduler



</td></td>

<td align="center" width="50%"><td align="center" width="50%">



### 🐧 **Pengguna Linux**### 🐧 **Pengguna Linux**



[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](README_LINUX.md)[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](README_LINUX.md)



**[📗 Buka Panduan Linux →](README_LINUX.md)****[📗 Buka Panduan Linux →](README_LINUX.md)**



Panduan lengkap untuk:Panduan lengkap untuk:

- ✅ Instalasi di Linux (apt/yum/pacman)- ✅ Instalasi di Linux (apt/yum/pacman)

- ✅ Cara penggunaan di Linux- ✅ Cara penggunaan di Linux

- ✅ Troubleshooting Linux- ✅ Troubleshooting Linux

- ✅ Tips & Tricks khusus Linux- ✅ Tips & Tricks khusus Linux

- ✅ Screen/Tmux, Systemd, Cron- ✅ Screen/Tmux, Systemd, Cron



</td></td>

</tr></tr>

</table></table>



------



## 🎯 3 Program Utama



| Program | Character Set | Kombinasi | Log File | Kecepatan | Progress Bar |## 🎯 3 Program Utama

|---------|---------------|-----------|----------|-----------|--------------|

| **`crack_zip_password_angka.py`** | 0-9 | 1-9 digit | `log.txt` | ⚡ Tercepat | ✅ || Program | Character Set | Kombinasi | Log File | Kecepatan | Progress Bar |

| **`crack_zip_password_alpha.py`** | a-z, A-Z | Unlimited | `log_alpha.txt` | 🔶 Sedang | ✅ ||---------|---------------|-----------|----------|-----------|--------------|

| **`crack_zip_password_alphanumeric.py`** | a-z, A-Z, 0-9 | Unlimited | `log_alphanumeric.txt` | 🐌 Lambat | ✅ || **`crack_zip_password_angka.py`** | 0-9 | 1-9 digit | `log.txt` | ⚡ Tercepat | ✅ |

| **`crack_zip_password_alpha.py`** | a-z, A-Z | Unlimited | `log_alpha.txt` | 🔶 Sedang | ✅ |

---| **`crack_zip_password_alphanumeric.py`** | a-z, A-Z, 0-9 | Unlimited | `log_alphanumeric.txt` | 🐌 Lambat | ✅ |



## ✨ Fitur Utama



### 🔥 NEW in v2.0.0---| Program | Character Set | Kombinasi/Digit | Log File | Keterangan |- � **Multi-Digit Support**: Crack password dari 1 digit sampai 9 digit (0 - 999,999,999)



- 📊 **Progress Bar Real-time** - Visual progress bar untuk setiap panjang password

- 🎯 **Auto-Detection** - Otomatis deteksi tipe enkripsi (AES atau ZipCrypto)

- 🌐 **Cross-Platform** - Support file ZIP dari Windows dan Linux## ✨ Fitur Utama|---------|---------------|-----------------|----------|------------|- 🎯 **Custom Range**: Pilih range digit sesuai kebutuhan (misal: hanya 4-6 digit)

- 🔐 **Dual Encryption** - AES-256 (Windows) dan ZipCrypto (Linux)



### 🎨 Core Features

### 🔥 NEW in v2.0.0| `crack_zip_password_angka.py` | 0-9 | 1-9 digit | `log.txt` | **Hanya Angka** - Tercepat |- ⚡ **Optimasi Kecepatan**: Menggunakan CRC verification untuk pengecekan password yang lebih cepat

- ⚡ **Optimasi CRC**: Menggunakan CRC32 verification untuk kecepatan maksimal

- 📁 **Batch Processing**: Memproses semua file ZIP di folder secara otomatis

- 📝 **Logging Terpisah**: Setiap program punya log sendiri

- ⏭️ **Smart Skip**: Otomatis skip file yang sudah di-crack sebelumnya- 📊 **Progress Bar Real-time** - Visual progress bar untuk setiap panjang password| `crack_zip_password_alpha.py` | a-z, A-Z | Unlimited | `log_alpha.txt` | **Hanya Huruf** - Lambat untuk >4 char |- � **Real-time Statistics**: Menampilkan progress, speed (pwd/s), dan estimasi waktu

- 📤 **Auto Extract**: Otomatis mengekstrak file setelah password berhasil ditemukan

- 🎨 **User-Friendly**: Menu interaktif dengan tampilan yang rapi- 🎯 **Auto-Detection** - Otomatis deteksi tipe enkripsi (AES atau ZipCrypto)

- 🖥️ **Cross-Platform**: Berjalan di Linux, Windows, dan macOS

- 🔢 **Multi-Mode**: Angka, Huruf, atau Alphanumeric- 🌐 **Cross-Platform** - Support file ZIP dari Windows dan Linux| `crack_zip_password_alphanumeric.py` | a-z, A-Z, 0-9 | Unlimited | `log_alphanumeric.txt` | **Kombinasi Lengkap** - Paling lambat |- �📁 **Batch Processing**: Memproses semua file ZIP di folder secara otomatis



---- 🔐 **Dual Encryption** - AES-256 (Windows) dan ZipCrypto (Linux)



## 📊 Progress Bar Preview- 📝 **Logging Otomatis**: Menyimpan semua hasil crack ke file `log.txt`



```### 🎨 Core Features

[*] Mencoba password 2 karakter...

[*] Kombinasi untuk 2 karakter: 2,704---- ⏭️ **Smart Skip**: Otomatis skip file yang sudah pernah di-crack sebelumnya

[*] Length 2: [████████████████████              ] 65.2% (1762/2704)

```- ⚡ **Optimasi CRC**: Menggunakan CRC32 verification untuk kecepatan maksimal



Progress bar menampilkan:- 🔄 **Otomatis**: Tidak perlu input user, langsung jalan- 📤 **Auto Extract**: Otomatis mengekstrak file setelah password berhasil ditemukan

- **Visual bar**: Representasi grafis progress

- **Persentase**: Progress dalam persen (%)- 📁 **Batch Processing**: Memproses semua file ZIP di folder secara otomatis

- **Kombinasi**: Jumlah yang sudah dicoba / total

- 📝 **Logging Terpisah**: Setiap program punya log sendiri## ✨ Fitur Utama- 🖥️ **Cross-Platform**: Berjalan di Linux, Windows, dan macOS

---

- ⏭️ **Smart Skip**: Otomatis skip file yang sudah di-crack sebelumnya

## 📋 Requirement

- 📤 **Auto Extract**: Otomatis mengekstrak file setelah password berhasil ditemukan- 🎨 **User-Friendly**: Menu interaktif dengan tampilan yang rapi

### Sistem Operasi

- 🖥️ **Cross-Platform**: Berjalan di Linux, Windows, dan macOS

- ✅ **Linux** (Ubuntu, Debian, CentOS, dll)

- ✅ **Windows** (7, 8, 10, 11)- 🔢 **Multi-Mode**: Angka, Huruf, atau Alphanumeric

- ✅ **macOS** (10.14+)

---

### Software

- ⚡ **Optimasi CRC**: Menggunakan CRC32 verification untuk kecepatan maksimal---

- **Python 3.6** atau lebih tinggi

- **pyzipper** library untuk AES support## 📊 Progress Bar Preview



### 📦 Instalasi Dependencies- 🔄 **Otomatis**: Tidak perlu input user, langsung jalan



```bash```

pip3 install pyzipper

```[*] Mencoba password 2 karakter...- 📁 **Batch Processing**: Memproses semua file ZIP di folder secara otomatis## 📋 Requirement



**Auto-install:**[*] Kombinasi untuk 2 karakter: 2,704

- pyzipper 0.3.6

- pycryptodomex 3.23.0[*] Length 2: [████████████████████              ] 65.2% (1762/2704)- 📝 **Logging Terpisah**: Setiap program punya log sendiri



---```



## 🚀 Quick Start- ⏭️ **Smart Skip**: Otomatis skip file yang sudah di-crack sebelumnya- **Python 3.6** atau lebih tinggi



> **📖 Untuk panduan instalasi dan penggunaan lengkap, silakan pilih dokumentasi platform Anda:**Progress bar menampilkan:

> 

> - 🪟 **Windows**: [README_WINDOWS.md](README_WINDOWS.md)- **Visual bar**: Representasi grafis progress- 📊 **Real-time Progress**: Menampilkan progress, speed (pwd/s), dan password yang dicoba- Library standar Python (tidak perlu install tambahan):

> - 🐧 **Linux**: [README_LINUX.md](README_LINUX.md)

- **Persentase**: Progress dalam persen (%)

### Struktur Folder

- **Kombinasi**: Jumlah yang sudah dicoba / total- 📤 **Auto Extract**: Otomatis mengekstrak file setelah password berhasil ditemukan  - `zipfile` (bawaan Python)

```

CrackPasswordZIP/

├── crack_zip_password_angka.py       # Program numeric (0-9)

├── crack_zip_password_alpha.py       # Program alphabetic (a-z, A-Z)---- 🖥️ **Cross-Platform**: Berjalan di Linux, Windows, dan macOS  - `os` (bawaan Python)

├── crack_zip_password_alphanumeric.py # Program alphanumeric (full)

├── FileZip/                          # Tempat file ZIP yang ingin di-crack

├── Extracted/                        # Hasil ekstraksi (auto created)

├── log.txt                           # Log program angka## 📋 Requirement- 🎨 **User-Friendly**: Tampilan output yang rapi dan mudah dipahami  - `zlib` (bawaan Python)

├── log_alpha.txt                     # Log program alpha

├── log_alphanumeric.txt              # Log program alphanumeric

└── README.md                         # Dokumentasi ini

```### Sistem Operasi  - `pathlib` (bawaan Python)



### Penggunaan Dasar- ✅ **Linux** (Ubuntu, Debian, CentOS, dll)



**1. Letakkan file ZIP:**- ✅ **Windows** (7, 8, 10, 11)---

```bash

cp your-file.zip FileZip/- ✅ **macOS** (10.14+)

```

### ✅ Cek Versi Python

**2. Jalankan program:**

### Software

```bash

# Linux/macOS- **Python 3.6** atau lebih tinggi## 📋 Requirement

python3 crack_zip_password_angka.py

- **pyzipper** library untuk AES support

# Windows

python crack_zip_password_angka.py```bash

```

### 📦 Instalasi Dependencies

**3. Lihat hasil:**

```bash### Sistem Operasipython3 --version

cat log.txt

ls Extracted/```bash

```

pip3 install pyzipper- ✅ **Linux** (Ubuntu, Debian, CentOS, dll)```

> **💡 Untuk tutorial lengkap, lihat:**

> - 🪟 [README_WINDOWS.md](README_WINDOWS.md) - Panduan Windows```

> - 🐧 [README_LINUX.md](README_LINUX.md) - Panduan Linux

- ✅ **Windows** (7, 8, 10, 11)

---

**Auto-install:**

## 📊 Performa & Estimasi Waktu

- pyzipper 0.3.6- ✅ **macOS** (10.14+)---

### Program Angka (0-9) - 10 karakter

- pycryptodomex 3.23.0

| Digit | Kombinasi | Waktu Rata-rata | Worst Case | Progress Bar |

|-------|-----------|-----------------|------------|--------------|

| 1-3 | 1,110 | < 1 detik | < 1 detik | ✅ Real-time |

| 4 | 10,000 | 30 detik | 5 menit | ✅ Real-time |### ✅ Cek Versi Python

| 5 | 100,000 | 5 menit | 50 menit | ✅ Per 100k |

| 6 | 1,000,000 | 50 menit | 8 jam | ✅ Per 100k |### Software## 📦 Instalasi

| 7+ | 10,000,000+ | 8+ jam | 3+ hari | ✅ Per 100k |

**Linux/macOS:**

### Program Huruf (a-z, A-Z) - 52 karakter

```bash- **Python 3.6** atau lebih tinggi

| Length | Kombinasi | Waktu Rata-rata | Worst Case | Progress Bar |

|--------|-----------|-----------------|------------|--------------|python3 --version

| 1-2 | 2,756 | < 1 detik | ~2 detik | ✅ Real-time |

| 3 | 140,608 | ~1 menit | ~2 menit | ✅ Per 100k |```- Library standar Python (sudah built-in, tidak perlu install tambahan)### 1. Clone atau Download File

| 4 | 7,311,616 | ~1 jam | ~2 jam | ✅ Per 100k |

| 5+ | 380,204,032+ | ~2+ hari | Sangat lama | ✅ Per 100k |



### Program Alphanumeric (a-z, A-Z, 0-9) - 62 karakter**Windows:**



| Length | Kombinasi | Waktu Rata-rata | Worst Case | Progress Bar |```cmd

|--------|-----------|-----------------|------------|--------------|

| 1-2 | 3,906 | < 1 detik | ~3 detik | ✅ Real-time |python --version### ✅ Cek Versi Python```bash

| 3 | 238,328 | ~2 menit | ~3 menit | ✅ Per 100k |

| 4 | 14,776,336 | ~2 jam | ~4 jam | ✅ Per 100k |```

| 5+ | 916,132,832+ | ~5+ hari | Sangat lama | ✅ Per 100k |

# Jika menggunakan git

**Catatan:**

- Progress bar diupdate setiap mencoba password---

- Untuk kombinasi > 100k, progress bar update setiap 100k attempts

- AES encryption ~3x lebih lambat dari ZipCrypto**Linux/macOS:**git clone <repo-url>



---## 🚀 Cara Menggunakan



## 🔐 Tipe Enkripsi yang Didukung```bashcd CrackPasswordZIP



### 1️⃣ ZipCrypto (Traditional/Linux)### 📂 Setup Folder



**Dibuat dengan:**python3 --version

- Linux: `zip -e` atau `zip -P password`

- Older Windows tools1. Letakkan semua file ZIP yang ingin di-crack di folder **`FileZip/`**

- Legacy ZIP programs

2. Hasil ekstraksi akan disimpan di folder **`Extracted/`**```# Atau copy manual file crack_zip_password.py

**Karakteristik:**

- ⚡ Lebih cepat di-crack3. Log hasil akan disimpan sesuai program yang digunakan

- 🔓 Enkripsi lebih lemah

- 📦 Compress type: 0 atau 8```



**Contoh:**### Program 1️⃣: Crack Password Angka (0-9)

```bash

zip -P mypassword file.zip document.txt**Windows:**

```

**Cocok untuk:** Password pure numeric seperti PIN, tanggal, nomor

### 2️⃣ AES Encryption (Windows/Modern)

```cmd### 2. Verifikasi Struktur Folder

**Dibuat dengan:**

- Windows Explorer (Right-click → Compress)**Linux/macOS:**

- WinRAR dengan AES option

- 7-Zip dengan AES-256```bashpython --version

- Modern ZIP tools

python3 crack_zip_password_angka.py

**Karakteristik:**

- 🛡️ Enkripsi lebih kuat (AES-128/192/256)``````Pastikan struktur folder seperti ini:

- 🐌 Lebih lambat di-crack

- 📦 Compress type: 99



**Contoh:****Windows:**

```cmd

# Windows Explorer```cmd

Right-click → Send to → Compressed (zipped) folder

→ Set password with AES encryptionpython crack_zip_password_angka.py---```

```

```

### 🤖 Auto-Detection

CrackPasswordZIP/

Program **otomatis mendeteksi** tipe enkripsi dan menggunakan method yang sesuai:

**Contoh Output:**

```

[*] Deteksi: AES encryption (Windows) - menggunakan pyzipper```## 🚀 Cara Menggunakan├── crack_zip_password.py      # File script utama

```

============================================================

atau

ZIP Password Cracker - Numeric Brute Force├── FileZip/                   # Folder berisi file ZIP

```

[*] Deteksi: ZipCrypto (Linux/Traditional)Character Set: 0-9 (10 karakter)

```

Support: ZipCrypto (Linux) + AES (Windows)### Program 1️⃣: Crack Password Angka (0-9)│   ├── file1.zip

---

============================================================

## 📝 Format Log File

[*] Ditemukan 1 file ZIP│   ├── file2.zip

### log.txt (Program Angka)

[*] Memproses: test_angka.zip

```

============================================================[*] Deteksi: ZipCrypto (Linux/Traditional)**Linux/macOS:**│   └── ...

ZIP Password Cracking Results (Numeric)

Digit Range: 1-9[*] Mencoba password 1-9 digit (0 - 999,999,999)

Character Set: 0-9

============================================================```bash├── Extracted/                 # Folder output (auto created)



File: test_angka.zip[+] PASSWORD DITEMUKAN: 123

Password: 123

Status: SUCCESS[+] Panjang: 3 digitpython3 crack_zip_password_angka.py├── log.txt                    # File log (auto created)

---------------------------------------------------------------

```[+] Ditemukan setelah mencoba 124 kombinasi dalam 0.05 detik



### log_alpha.txt (Program Alpha)[+] File sudah diekstrak ke Extracted/test_angka```└── README.md                  # Dokumentasi ini



``````

============================================================

ZIP Password Cracking Results (Alphabetic)```

Length Range: 1-999 karakter

Character Set: a-z, A-Z### Program 2️⃣: Crack Password Huruf (a-z, A-Z)

============================================================

**Windows:**

File: test_alpha.zip

Password: ab**Cocok untuk:** Password pure alphabetic, kata-kata sederhana

Status: SUCCESS

------------------------------------------------------------```cmd### 3. Letakkan File ZIP

```

**Linux/macOS:**

### log_alphanumeric.txt (Program Alphanumeric)

```bashpython crack_zip_password_angka.py

```

============================================================python3 crack_zip_password_alpha.py

ZIP Password Cracking Results (Alphanumeric)

Length Range: 1-999 karakter``````Tempatkan semua file ZIP yang ingin di-crack ke dalam folder `FileZip/`:

Character Set: a-z, A-Z, 0-9

============================================================



File: test_alphanumeric.zip**Windows:**

Password: a1

Status: SUCCESS```cmd

------------------------------------------------------------

```python crack_zip_password_alpha.py### Program 2️⃣: Crack Password Huruf (a-z, A-Z)```bash



---```



## 🎯 Pemilihan Program yang Tepatmkdir -p FileZip



### 🤔 Program Mana yang Harus Digunakan?**Contoh Output:**



| Jenis Password | Program | Kecepatan | Contoh |```**Linux/macOS:**# Copy file ZIP ke folder FileZip

|----------------|---------|-----------|--------|

| Pure angka (PIN, tanggal) | `angka.py` | ⚡⚡⚡ Tercepat | 123, 2024, 0815 |============================================================

| Pure huruf | `alpha.py` | 🔶🔶 Sedang | abc, Password, ADMIN |

| Campuran huruf + angka | `alphanumeric.py` | 🐌 Lambat | abc123, Pass2024, user1 |ZIP Password Cracker - Alphabetic Brute Force```bashcp /path/to/file.zip FileZip/

| Tidak tahu jenisnya | Coba urut: angka → alpha → alphanumeric | - | - |

Character Set: a-z, A-Z (52 karakter)

### 💡 Tips Memilih:

Support: ZipCrypto (Linux) + AES (Windows)python3 crack_zip_password_alpha.py```

1. **Password pendek (<4 char)**: Coba alpha dulu

2. **Password pure numeric**: Gunakan angka (paling cepat)============================================================

3. **Password kompleks**: Gunakan alphanumeric (paling lengkap)

4. **Tidak yakin**: Mulai dari yang tercepat (angka → alpha → alphanumeric)[*] Ditemukan 1 file ZIP```



---[*] Memproses: test_alpha.zip



## 🧪 Testing[*] Deteksi: ZipCrypto (Linux/Traditional)---



Semua program sudah ditest dengan:



| Program | Test Password | Result | Time |[*] Mencoba password 1 karakter...**Windows:**

|---------|---------------|--------|------|

| `angka.py` | 123 | ✅ Success | 0.05s |[*] Kombinasi untuk 1 karakter: 52

| `alpha.py` | ab | ✅ Success | 0.02s |

| `alphanumeric.py` | a1 | ✅ Success | 0.06s |[*] Length 1: [██████████████████████████████████████████████████] 100.0% (52/52)```cmd## 🚀 Cara Menggunakan



**Test Coverage:**

- ✅ ZipCrypto encryption (Linux `zip -P`)

- ✅ AES encryption (Windows/modern tools)[*] Mencoba password 2 karakter...python crack_zip_password_alpha.py

- ✅ Progress bar display

- ✅ Log file creation[*] Kombinasi untuk 2 karakter: 2,704

- ✅ Auto-extract functionality

- ✅ Smart skip feature```### Menjalankan Program



---[+] PASSWORD DITEMUKAN: ab



## 🔒 Keamanan & Legal[+] Panjang: 2 karakter



### ⚠️ Program ini hanya boleh digunakan untuk:[+] Ditemukan setelah mencoba 54 kombinasi dalam 0.02 detik



- ✅ File ZIP milik sendiri yang lupa password```### Program 3️⃣: Crack Password Alphanumeric (a-z, A-Z, 0-9)**Linux/macOS:**

- ✅ Recovery data pribadi

- ✅ Testing keamanan dengan izin

- ✅ Pembelajaran dan penelitian

### Program 3️⃣: Crack Password Alphanumeric (a-z, A-Z, 0-9)```bash

### ❌ DILARANG KERAS untuk:



- ❌ File orang lain tanpa izin

- ❌ Aktivitas illegal**Cocok untuk:** Password kombinasi huruf dan angka**Linux/macOS:**python3 crack_zip_password_angka.py

- ❌ Bypass keamanan tanpa otorisasi

- ❌ Tujuan jahat atau merugikan



**Disclaimer:** Pengguna bertanggung jawab penuh atas penggunaan program ini. Developer tidak bertanggung jawab atas penyalahgunaan.**Linux/macOS:**```bash```



---```bash



## 📚 Dokumentasi Lengkap per Platformpython3 crack_zip_password_alphanumeric.pypython3 crack_zip_password_alphanumeric.py



Untuk panduan instalasi, penggunaan, dan troubleshooting yang lebih detail, silakan buka dokumentasi sesuai platform Anda:```



<table>```**Windows:**

<tr>

<td align="center" width="50%">**Windows:**



### 🪟 Windows Users```cmd```cmd



[![Windows Guide](https://img.shields.io/badge/📘_Complete_Windows_Guide-0078D6?style=for-the-badge&logo=windows)](README_WINDOWS.md)python crack_zip_password_alphanumeric.py



**[→ Buka README_WINDOWS.md](README_WINDOWS.md)**```**Windows:**python crack_zip_password_angka.py



Lengkap dengan:

- Instalasi Python di Windows

- Penggunaan CMD & PowerShell**Contoh Output:**```cmd```

- Batch file automation

- Task Scheduler setup```

- Troubleshooting khusus Windows

- Tips & tricks Windows============================================================python crack_zip_password_alphanumeric.py



</td>ZIP Password Cracker - Alphanumeric Brute Force

<td align="center" width="50%">

Character Set: a-z, A-Z, 0-9 (62 karakter)```### Menu Interaktif

### 🐧 Linux Users

Support: ZipCrypto (Linux) + AES (Windows)

[![Linux Guide](https://img.shields.io/badge/📗_Complete_Linux_Guide-FCC624?style=for-the-badge&logo=linux)](README_LINUX.md)

============================================================

**[→ Buka README_LINUX.md](README_LINUX.md)**

[*] Ditemukan 1 file ZIP

Lengkap dengan:

- Instalasi untuk berbagai distro[*] Memproses: test_alphanumeric.zip---Setelah program dijalankan, Anda akan melihat menu pilihan digit:

- Screen/Tmux untuk long-running

- Systemd service setup[*] Deteksi: ZipCrypto (Linux/Traditional)

- Cron job automation

- Troubleshooting khusus Linux

- Performance optimization

[*] Mencoba password 1 karakter...

</td>

</tr>[*] Kombinasi untuk 1 karakter: 62## 📊 Performa & Estimasi Waktu```

</table>

[*] Length 1: [██████████████████████████████████████████████████] 100.0% (62/62)

---

============================================================

## 🎓 FAQ

[*] Mencoba password 2 karakter...

### Q: Berapa lama waktu yang dibutuhkan untuk crack password?

[*] Kombinasi untuk 2 karakter: 3,844### Program Angka (0-9)PILIH JUMLAH DIGIT PASSWORD

**A:** Tergantung panjang dan kompleksitas password:

- 1-3 digit angka: < 1 detik

- 4 digit angka: ~30 detik

- 2 huruf: < 1 detik  [+] PASSWORD DITEMUKAN: a1============================================================

- 3 huruf: ~1 menit

- 4+ karakter: Bisa berjam-jam hingga berhari-hari[+] Panjang: 2 karakter



### Q: Apakah bisa crack password yang sangat panjang?[+] Ditemukan setelah mencoba 116 kombinasi dalam 0.06 detik| Digit | Kombinasi | Waktu Rata-rata | Worst Case |1. 1 digit  (0-9)          - Sangat Cepat



**A:** Secara teknis bisa, tapi:```

- Password > 8 karakter bisa memakan waktu tahun

- Password > 10 karakter praktis tidak mungkin dengan brute force|-------|-----------|-----------------|------------|2. 2 digit  (0-99)         - Sangat Cepat

- Gunakan dictionary attack atau hybrid attack untuk password panjang

---

### Q: Kenapa ada 3 program berbeda?

| 1-3 | 1,110 | < 1 detik | < 1 detik |3. 3 digit  (0-999)        - Cepat

**A:** Untuk optimasi kecepatan:

- Program angka hanya coba 0-9 (tercepat)## 📊 Performa & Estimasi Waktu

- Program alpha coba a-z, A-Z (sedang)

- Program alphanumeric coba semua kombinasi (lengkap tapi lambat)| 4 | 10,000 | 30 detik | 5 menit |4. 4 digit  (0-9999)       - Normal (~1-5 menit)



### Q: Apakah legal menggunakan program ini?### Program Angka (0-9) - 10 karakter



**A:** Legal jika digunakan untuk:| 5 | 100,000 | 5 menit | 50 menit |5. 5 digit  (0-99999)      - Lama (~10-50 menit)

- File milik sendiri yang lupa password

- Testing dengan izin| Digit | Kombinasi | Waktu Rata-rata | Worst Case | Progress Bar |

- Pembelajaran

|-------|-----------|-----------------|------------|--------------|| 6 | 1,000,000 | 50 menit | 8 jam |6. 6 digit  (0-999999)     - Sangat Lama (~1-8 jam)

Illegal jika untuk:

- File orang lain tanpa izin| 1-3 | 1,110 | < 1 detik | < 1 detik | ✅ Real-time |

- Aktivitas kriminal

- Bypass keamanan tanpa otorisasi| 4 | 10,000 | 30 detik | 5 menit | ✅ Real-time || 7+ | 10,000,000+ | 8+ jam | 3+ hari |7. 7 digit  (0-9999999)    - Ekstrim (~10-80 jam)



### Q: Bisa crack password dengan simbol (@, #, $, dll)?| 5 | 100,000 | 5 menit | 50 menit | ✅ Per 100k |



**A:** Saat ini belum support simbol. Untuk menambahkan:| 6 | 1,000,000 | 50 menit | 8 jam | ✅ Per 100k |8. 8 digit  (0-99999999)   - Sangat Ekstrim (~100-800 jam)

1. Edit `CHARSET` di program

2. Tambahkan: `+ string.punctuation`| 7+ | 10,000,000+ | 8+ jam | 3+ hari | ✅ Per 100k |

3. Note: Akan jauh lebih lambat!

### Program Huruf (a-z, A-Z - 52 char)9. 9 digit  (0-999999999)  - Ultra Ekstrim (~1000-8000 jam)

### Q: Program berhenti tiba-tiba, apa yang harus dilakukan?

### Program Huruf (a-z, A-Z) - 52 karakter

**A:** 

1. Cek log file - mungkin sudah berhasil10. Custom Range (min-max) - Pilih sendiri

2. Jalankan ulang - program akan skip file yang sudah berhasil

3. Cek error message untuk troubleshooting| Length | Kombinasi | Waktu Rata-rata | Worst Case | Progress Bar |



### Q: Bisa di-pause dan di-resume?|--------|-----------|-----------------|------------|--------------|| Length | Kombinasi | Waktu Rata-rata | Worst Case |============================================================



**A:** Saat ini belum ada fitur pause/resume otomatis. Workaround:| 1-2 | 2,756 | < 1 detik | ~2 detik | ✅ Real-time |

1. Tekan Ctrl+C untuk stop

2. Note password terakhir yang dicoba| 3 | 140,608 | ~1 menit | ~2 menit | ✅ Per 100k ||--------|-----------|-----------------|------------|

3. Edit program untuk mulai dari password tersebut

| 4 | 7,311,616 | ~1 jam | ~2 jam | ✅ Per 100k |

### Q: Kenapa progress bar kadang tidak smooth?

| 5+ | 380,204,032+ | ~2+ hari | Sangat lama | ✅ Per 100k || 1-2 | 2,756 | < 1 detik | ~2 detik |Pilih opsi (1-10): 4

**A:** Progress bar update berdasarkan kombinasi yang dicoba:

- Kombinasi kecil: Update setiap password

- Kombinasi besar: Update setiap 100k passwords

- Ini untuk menjaga kecepatan cracking tetap optimal### Program Alphanumeric (a-z, A-Z, 0-9) - 62 karakter| 3 | 140,608 | ~1 menit | ~2 menit |```



---



## 📋 Changelog| Length | Kombinasi | Waktu Rata-rata | Worst Case | Progress Bar || 4 | 7,311,616 | ~1 jam | ~2 jam |



### Version 2.0.0 (Current)|--------|-----------|-----------------|------------|--------------|



**🎉 Major Update:**| 1-2 | 3,906 | < 1 detik | ~3 detik | ✅ Real-time || 5+ | 380,204,032+ | ~2+ hari | Sangat lama |### Contoh Output

- ✅ Progress bar real-time untuk semua program

- ✅ Auto-detection encryption type (AES vs ZipCrypto)| 3 | 238,328 | ~2 menit | ~3 menit | ✅ Per 100k |

- ✅ Full cross-platform support (Linux & Windows ZIP)

- ✅ Dual-method cracking (zipfile + pyzipper)| 4 | 14,776,336 | ~2 jam | ~4 jam | ✅ Per 100k |

- ✅ Enhanced error handling

- ✅ Improved password verification| 5+ | 916,132,832+ | ~5+ hari | Sangat lama | ✅ Per 100k |

- ✅ Fixed "labas terus" bug

### Program Alphanumeric (a-z, A-Z, 0-9 - 62 char)```

**Dependencies:**

- Added: pyzipper 0.3.6**Catatan:**

- Added: pycryptodomex 3.23.0

- Progress bar diupdate setiap mencoba password============================================================

### Version 1.0.0

- Untuk kombinasi > 100k, progress bar update setiap 100k attempts

**Initial Release:**

- ✅ 3 program berbeda (angka, alpha, alphanumeric)- AES encryption ~3x lebih lambat dari ZipCrypto| Length | Kombinasi | Waktu Rata-rata | Worst Case |ZIP Password Cracker - Multi-Digit Brute Force

- ✅ Basic brute force functionality

- ✅ Smart skip feature

- ✅ Separate log files

- ✅ Auto-extract---|--------|-----------|-----------------|------------|Cross-platform: Linux | Windows | macOS



---



## 👨‍💻 Author & Credits## 🔐 Tipe Enkripsi yang Didukung| 1-2 | 3,906 | < 1 detik | ~3 detik |============================================================



**Created**: November 2025  

**Version**: 2.0.0  

**License**: Educational Use Only### 1️⃣ ZipCrypto (Traditional/Linux)| 3 | 238,328 | ~2 menit | ~3 menit |[*] Ditemukan 2 file ZIP



**Built with:**

- Python 3.6+

- zipfile (standard library)**Dibuat dengan:**| 4 | 14,776,336 | ~2 jam | ~4 jam |[*] Memeriksa log.txt untuk file yang sudah di-crack...

- pyzipper (AES support)

- itertools (combination generation)- Linux: `zip -e` atau `zip -P password`

- pathlib (path handling)

- Older Windows tools| 5+ | 916,132,832+ | ~5+ hari | Sangat lama |

---

- Legacy ZIP programs

## 📞 Support & Contributing

[*] Memproses: archive1.zip

### 🐛 Found a Bug?

**Karakteristik:**

Silakan report dengan informasi:

1. Program yang digunakan- ⚡ Lebih cepat di-crack---[*] Range: 4-4 digit

2. Pesan error lengkap

3. File ZIP sample (jika memungkinkan)- 🔓 Enkripsi lebih lemah

4. Python version

5. Operating system- 📦 Compress type: 0 atau 8[*] File terenkripsi, mencoba crack password...



### 💡 Feature Request?



Silakan submit request dengan deskripsi:**Contoh:**## 🔒 Keamanan & Legal[*] Total kombinasi yang akan dicoba: 10,000

1. Fitur yang diinginkan

2. Use case / contoh penggunaan```bash

3. Benefit yang didapat

zip -P mypassword file.zip document.txt

### 🤝 Want to Contribute?

```

Pull requests are welcome! Pastikan:

1. Code mengikuti style yang ada⚠️ **Program ini hanya boleh digunakan untuk:**[*] Mencoba password 4 digit (1000 - 9999)

2. Tambahkan test untuk fitur baru

3. Update dokumentasi### 2️⃣ AES Encryption (Windows/Modern)



---- ✅ File ZIP milik sendiri[*] Progress: 10,000/10,000 (100.00%) | Speed: 2500 pwd/s | Password: 2547



## 🌟 Star History**Dibuat dengan:**



Jika program ini membantu Anda, jangan lupa beri ⭐ star!- Windows Explorer (Right-click → Compress)- ✅ Recovery password yang lupa



---- WinRAR dengan AES option



**🎉 Happy Cracking! 🔓**- 7-Zip dengan AES-256- ✅ Testing & pembelajaran[+] PASSWORD DITEMUKAN: 2547



*Remember: With great power comes great responsibility. Use wisely!*- Modern ZIP tools



---[+] Ditemukan setelah mencoba 1,547 kombinasi dalam 0.62 detik



**Version:** 2.0.0  **Karakteristik:**

**Last Updated:** 10 November 2025  

**Platforms:** Linux, Windows, macOS- 🛡️ Enkripsi lebih kuat (AES-128/192/256)❌ **DILARANG untuk:**[*] Mengekstrak file...


- 🐌 Lebih lambat di-crack

- 📦 Compress type: 99- ❌ File orang lain tanpa izin[+] Ekstraksi selesai!



**Contoh:**- ❌ Aktivitas illegal

```cmd

# Windows Explorer- ❌ Bypass keamanan tanpa otorisasi[*] SKIP: archive2.zip (sudah di-crack, password: 1234)

Right-click → Send to → Compressed (zipped) folder

→ Set password with AES encryption

```

---============================================================

### 🤖 Auto-Detection

RINGKASAN

Program **otomatis mendeteksi** tipe enkripsi dan menggunakan method yang sesuai:

## 📚 Dokumentasi Lengkap============================================================

```

[*] Deteksi: AES encryption (Windows) - menggunakan pyzipper[*] File yang di-skip (sudah di-crack): 1

```

atauLihat file README ini untuk dokumentasi lengkap tentang:[*] File yang berhasil di-crack: 1

```

[*] Deteksi: ZipCrypto (Linux/Traditional)- ✅ Instalasi detail✓ archive1.zip: 2547

```

- ✅ Contoh penggunaan⊘ archive2.zip: 1234

---

- ✅ Troubleshooting

## 📝 Format Log File

- ✅ Tips & tricks[+] Selesai! Hasil disimpan di log.txt

### log.txt (Program Angka)

```- ✅ FAQ[+] File terekstrak di folder Extracted/

============================================================

ZIP Password Cracking Results (Numeric)

Digit Range: 1-9

Character Set: 0-9---Tekan ENTER untuk keluar...

============================================================

```

File: test_angka.zip

Password: 123## 👨‍💻 Author

Status: SUCCESS

---------------------------------------------------------------

```

**Created**: November 2025  

### log_alpha.txt (Program Alpha)

```**Version**: 1.0.0## 📊 Output & Result

============================================================

ZIP Password Cracking Results (Alphabetic)

Length Range: 1-999 karakter

Character Set: a-z, A-Z---### File `log.txt`

============================================================



File: test_alpha.zip

Password: ab**Happy Cracking! 🔓**Setelah program selesai, hasil akan disimpan di `log.txt`:

Status: SUCCESS

------------------------------------------------------------

``````

============================================================

### log_alphanumeric.txt (Program Alphanumeric)ZIP Password Cracking Results

```Digit Range: 4-4

========================================================================================================================

ZIP Password Cracking Results (Alphanumeric)

Length Range: 1-999 karakterFile: archive1.zip

Character Set: a-z, A-Z, 0-9Password: 2547

============================================================Status: SUCCESS

------------------------------------------------------------

File: test_alphanumeric.zipFile: archive2.zip

Password: a1Password: 1234

Status: SUCCESSStatus: SKIPPED (already cracked)

------------------------------------------------------------------------------------------------------------------------

```File: archive3.zip

Password: N/A

---Status: FAILED

------------------------------------------------------------

## 🎯 Pemilihan Program yang Tepat```



### 🤔 Program Mana yang Harus Digunakan?### Folder `Extracted/`



| Jenis Password | Program | Kecepatan | Contoh |File-file yang berhasil di-crack akan diekstrak ke folder `Extracted/`:

|----------------|---------|-----------|--------|

| Pure angka (PIN, tanggal) | `angka.py` | ⚡⚡⚡ Tercepat | 123, 2024, 0815 |```

| Pure huruf | `alpha.py` | 🔶🔶 Sedang | abc, Password, ADMIN |Extracted/

| Campuran huruf + angka | `alphanumeric.py` | 🐌 Lambat | abc123, Pass2024, user1 |├── archive1/

| Tidak tahu jenisnya | Coba urut: angka → alpha → alphanumeric | - | - |│   ├── file1.txt

│   ├── file2.jpg

### 💡 Tips Memilih:│   └── ...

└── archive2/

1. **Password pendek (<4 char)**: Coba alpha dulu    ├── document.pdf

2. **Password pure numeric**: Gunakan angka (paling cepat)    └── ...

3. **Password kompleks**: Gunakan alphanumeric (paling lengkap)```

4. **Tidak yakin**: Mulai dari yang tercepat (angka → alpha → alphanumeric)

---

---

## 🔍 Cara Kerja

## 🔍 Troubleshooting

### Algoritma Brute Force

### ❌ Error: "That compression method is not supported"

Program bekerja dengan langkah-langkah berikut:

**Penyebab:** File ZIP menggunakan AES encryption tapi `pyzipper` belum terinstall

1. **Scan Folder**: Mencari semua file `.zip` di folder `FileZip/`

**Solusi:**2. **Check Existing Log**: Membaca `log.txt` untuk melihat file yang sudah di-crack

```bash3. **Skip Files**: Melewati file yang sudah ada di log

pip3 install pyzipper4. **Pilih Digit**: User memilih range digit password (1-9 digit atau custom)

```5. **Brute Force**: Untuk setiap file ZIP baru:

   - Mengambil satu file dari dalam ZIP

### ❌ Error: "File tidak terproteksi password"   - Mencoba password dari digit minimum ke maksimum

   - Progress tracking dengan speed calculation

**Penyebab:** File ZIP tidak memiliki password   - Verifikasi dengan CRC checksum

6. **Extract**: Jika password ditemukan, ekstrak semua file

**Solusi:** Pastikan file ZIP yang ingin di-crack memang terproteksi password7. **Logging**: Simpan hasil ke `log.txt`



### ❌ Program berjalan sangat lambat### Optimasi CRC Verification



**Penyebab:** Password terlalu panjang atau character set terlalu besar- Menggunakan **CRC32 checksum** untuk verifikasi password

- Hanya membaca **1 file** untuk test (bukan semua file)

**Solusi:**- Lebih cepat ≈ **10-20x** dibanding ekstrak penuh

- Gunakan program yang sesuai dengan jenis password

- Password > 4 karakter akan memakan waktu lama### Smart Range Selection

- Pertimbangkan menggunakan hardware lebih kuat atau distributed cracking

Program mencoba password secara berurutan berdasarkan jumlah digit:

### ❌ Progress bar tidak muncul- **1 digit**: 0-9 (10 kombinasi)

- **2 digit**: 10-99 (90 kombinasi)  

**Penyebab:** Kombinasi terlalu kecil (< 100)- **3 digit**: 100-999 (900 kombinasi)

- **4 digit**: 1000-9999 (9,000 kombinasi)

**Solusi:** Progress bar hanya muncul untuk kombinasi yang cukup besar. Untuk password sangat pendek, hasil langsung muncul.- **5 digit**: 10000-99999 (90,000 kombinasi)

- Dan seterusnya...

---

**Contoh**: Jika pilih range 1-4 digit, program akan coba:

## 🔒 Keamanan & Legal```

0, 1, 2, ..., 9          (1 digit)

### ⚠️ Program ini HANYA boleh digunakan untuk:10, 11, 12, ..., 99      (2 digit)

100, 101, ..., 999       (3 digit)

- ✅ File ZIP milik sendiri yang lupa password1000, 1001, ..., 9999    (4 digit)

- ✅ Testing keamanan dengan izin```

- ✅ Recovery data pribadi

- ✅ Pembelajaran dan penelitian---



### ❌ DILARANG KERAS untuk:## ⚙️ Konfigurasi



- ❌ File orang lain tanpa izinAnda dapat mengubah konfigurasi di bagian atas file script:

- ❌ Aktivitas illegal

- ❌ Bypass keamanan tanpa otorisasi```python

- ❌ Tujuan jahat atau merugikan# Konfigurasi

ZIP_FOLDER = "FileZip"        # Folder ZIP input

**Disclaimer:** Pengguna bertanggung jawab penuh atas penggunaan program ini. Developer tidak bertanggung jawab atas penyalahgunaan.OUTPUT_FOLDER = "Extracted"   # Folder output ekstraksi

LOG_FILE = "log.txt"          # File log hasil

---MIN_DIGITS = 1                # Minimum digit password (default)

MAX_DIGITS = 9                # Maximum digit password (default)

## 📚 Struktur Folder```



```### Contoh: Mengubah Folder Input

CrackPasswordZIP/

├── FileZip/                          # Tempat file ZIP yang ingin di-crack```python

│   ├── file1.zip# Ubah ke folder yang berbeda

│   └── file2.zipZIP_FOLDER = "my_zip_files"

├── Extracted/                        # Hasil ekstraksiOUTPUT_FOLDER = "my_extracted_files"

│   ├── file1/```

│   └── file2/

├── crack_zip_password_angka.py       # Program numeric (0-9)### Contoh: Set Default Range Digit

├── crack_zip_password_alpha.py       # Program alphabetic (a-z, A-Z)

├── crack_zip_password_alphanumeric.py # Program alphanumeric (full)Jika ingin skip menu interaktif, edit fungsi `main()` dan ganti baris:

├── log.txt                           # Log program angka```python

├── log_alpha.txt                     # Log program alpha# Dari:

├── log_alphanumeric.txt              # Log program alphanumericmin_digits, max_digits = get_digit_choice()

├── README.md                         # Dokumentasi ini

└── CHANGELOG.md                      # Riwayat perubahan# Ke (contoh: selalu gunakan 4 digit):

```min_digits, max_digits = 4, 4

```

---

---

## 🎓 Tips & Tricks

## 📈 Performa

### 1️⃣ Optimasi Kecepatan

### Kecepatan Crack (Estimasi)

```bash

# Gunakan Python 3.9+ untuk performa terbaikKecepatan tergantung pada hardware CPU Anda. Berikut estimasi pada CPU rata-rata (2000-3000 pwd/s):

python3.9 crack_zip_password_angka.py

| Digit | Range | Total Kombinasi | Waktu Rata-rata | Worst Case |

# Atau gunakan PyPy untuk speed boost ~5x|-------|-------|-----------------|-----------------|------------|

pypy3 crack_zip_password_angka.py| 1 | 0-9 | 10 | < 1 detik | < 1 detik |

```| 2 | 0-99 | 100 | < 1 detik | < 1 detik |

| 3 | 0-999 | 1,000 | < 1 detik | 1 detik |

### 2️⃣ Background Processing| 4 | 0-9,999 | 10,000 | 30 detik | 5 menit |

| 5 | 0-99,999 | 100,000 | 5 menit | 50 menit |

```bash| 6 | 0-999,999 | 1,000,000 | 50 menit | 8 jam |

# Linux: Run di background dengan nohup| 7 | 0-9,999,999 | 10,000,000 | 8 jam | 3 hari |

nohup python3 crack_zip_password_angka.py &| 8 | 0-99,999,999 | 100,000,000 | 3 hari | 1 bulan |

| 9 | 0-999,999,999 | 1,000,000,000 | 1 bulan | 1 tahun |

# Monitor progress

tail -f nohup.out**Catatan**: 

```- Waktu rata-rata = password di tengah range

- Worst case = password di akhir range

### 3️⃣ Batch Processing- Kecepatan aktual akan ditampilkan saat proses berjalan



Letakkan multiple ZIP files di folder `FileZip/` - program akan memproses semuanya secara otomatis!### Memory Usage



### 4️⃣ Resume dari Crash- **RAM**: ~10-50 MB (tergantung ukuran file ZIP)

- **Disk**: Sesuai ukuran file yang diekstrak

Program otomatis skip file yang sudah berhasil di-crack (cek log file). Jika crash, jalankan ulang dan program akan continue dari file berikutnya.- **CPU**: Single-threaded (1 core)



### 5️⃣ Monitor Progress### Tips Meningkatkan Performa



Program menampilkan real-time progress:1. **Gunakan CPU yang lebih cepat** - Kecepatan crack sangat bergantung pada CPU

- **Progress bar**: Visual indicator2. **Tutup aplikasi lain** - Untuk mendapatkan CPU resources maksimal

- **Speed**: Passwords per second (pwd/s)3. **Pilih range digit yang tepat** - Jika tahu password ~4 digit, jangan pilih 1-9

- **Testing**: Password yang sedang dicoba4. **Gunakan SSD** - Lebih cepat untuk ekstraksi file

5. **Monitor speed** - Jika speed < 1000 pwd/s, kemungkinan sistem overload

---

---

## 🧪 Testing

## 🐛 Troubleshooting

Semua program sudah ditest dengan:

### ❌ Error: "Folder FileZip tidak ditemukan"

| Program | Test Password | Result | Time |

|---------|---------------|--------|------|**Solusi**: Buat folder terlebih dahulu

| `angka.py` | 123 | ✅ Success | 0.05s |

| `alpha.py` | ab | ✅ Success | 0.02s |```bash

| `alphanumeric.py` | a1 | ✅ Success | 0.06s |mkdir FileZip

```

**Test Coverage:**

- ✅ ZipCrypto encryption (Linux `zip -P`)### ❌ Error: "Tidak ada file ZIP di folder FileZip"

- ✅ AES encryption (Windows/modern tools)

- ✅ Progress bar display**Solusi**: Pastikan file ZIP sudah di-copy ke folder `FileZip/`

- ✅ Log file creation

- ✅ Auto-extract functionality```bash

- ✅ Smart skip featurels -la FileZip/

```

---

### ❌ Password tidak ditemukan (Status: FAILED)

## 📞 Support & Contributing

**Penyebab & Solusi**:

### 🐛 Found a Bug?- Password lebih dari jumlah digit yang dipilih → Pilih range digit yang lebih besar

- Password bukan angka murni (ada huruf/simbol) → Program ini hanya untuk numerik

Silakan report dengan informasi:- File ZIP corrupt → Coba dengan file ZIP lain

1. Program yang digunakan- Enkripsi berbeda → Beberapa tipe enkripsi tidak support

2. Pesan error lengkap

3. File ZIP sample (jika memungkinkan)### ❌ Proses terlalu lambat

4. Python version

5. Operating system**Solusi**:

- Tunggu sampai selesai (normal untuk jutaan kombinasi)

### 💡 Feature Request?- Cek speed (pwd/s) di progress indicator

- Gunakan CPU yang lebih cepat

Silakan submit request dengan deskripsi:- Tutup aplikasi lain yang membebani CPU

1. Fitur yang diinginkan- Untuk 7+ digit, siapkan waktu berjam-jam atau bahkan berhari-hari

2. Use case / contoh penggunaan

3. Benefit yang didapat### ❌ Program crash atau hang



### 🤝 Want to Contribute?**Solusi**:

- Pastikan ada cukup RAM (minimal 1GB free)

Pull requests are welcome! Pastikan:- Cek ukuran file ZIP tidak terlalu besar (>1GB)

1. Code mengikuti style yang ada- Restart komputer dan coba lagi

2. Tambahkan test untuk fitur baru- Update Python ke versi terbaru

3. Update dokumentasi

### ❌ Error: "Python3 tidak ditemukan"

---

**Solusi**: Install Python 3

## 📋 Changelog

```bash

### Version 2.0.0 (Current)# Ubuntu/Debian

sudo apt-get install python3

**🎉 Major Update:**

- ✅ Progress bar real-time untuk semua program# macOS

- ✅ Auto-detection encryption type (AES vs ZipCrypto)brew install python3

- ✅ Full cross-platform support (Linux & Windows ZIP)

- ✅ Dual-method cracking (zipfile + pyzipper)# Windows

- ✅ Enhanced error handling# Download dari https://www.python.org/downloads/

- ✅ Improved password verification```

- ✅ Fixed "labas terus" bug

---

**Dependencies:**

- Added: pyzipper 0.3.6## 📝 Contoh Penggunaan

- Added: pycryptodomex 3.23.0

### Scenario 1: Crack File ZIP dengan Password 4 Digit

### Version 1.0.0

```bash

**Initial Release:**# 1. Buat folder FileZip

- ✅ 3 program berbeda (angka, alpha, alphanumeric)mkdir FileZip

- ✅ Basic brute force functionality

- ✅ Smart skip feature# 2. Copy file ZIP

- ✅ Separate log filescp myarchive.zip FileZip/

- ✅ Auto-extract

# 3. Jalankan program

---python3 crack_zip_password_angka.py



## 👨‍💻 Author & Credits# 4. Pilih opsi 4 (4 digit)

Pilih opsi (1-10): 4

**Created**: November 2025  

**Version**: 2.0.0  # 5. Check hasil di Extracted/ dan log.txt

**License**: Educational Use Onlyls Extracted/

cat log.txt

**Built with:**```

- Python 3.6+

- zipfile (standard library)### Scenario 2: Crack dengan Custom Range (3-5 Digit)

- pyzipper (AES support)

- itertools (combination generation)```bash

- pathlib (path handling)# Jalankan program

python3 crack_zip_password_angka.py

---

# Pilih opsi 10 (Custom Range)

## 🎯 FAQPilih opsi (1-10): 10

Masukkan digit minimum (1-9): 3

### Q: Berapa lama waktu yang dibutuhkan untuk crack password?Masukkan digit maksimum (1-9): 5



**A:** Tergantung panjang dan kompleksitas password:# Program akan coba password dari 100 sampai 99999

- 1-3 digit angka: < 1 detik```

- 4 digit angka: ~30 detik

- 2 huruf: < 1 detik  ### Scenario 3: Batch Processing Multiple Files

- 3 huruf: ~1 menit

- 4+ karakter: Bisa berjam-jam hingga berhari-hari```bash

# 1. Copy semua file ZIP

### Q: Apakah bisa crack password yang sangat panjang?cp *.zip FileZip/



**A:** Secara teknis bisa, tapi:# 2. Jalankan program (akan process semua otomatis)

- Password > 8 karakter bisa memakan waktu tahunpython3 crack_zip_password_angka.py

- Password > 10 karakter praktis tidak mungkin dengan brute force

- Gunakan dictionary attack atau hybrid attack untuk password panjang# 3. Pilih digit sesuai perkiraan

Pilih opsi (1-10): 4

### Q: Kenapa ada 3 program berbeda?

# 4. Cek hasil

**A:** Untuk optimasi kecepatan:ls -R Extracted/

- Program angka hanya coba 0-9 (tercepat)```

- Program alpha coba a-z, A-Z (sedang)

- Program alphanumeric coba semua kombinasi (lengkap tapi lambat)### Scenario 4: Resume Cracking (File Sudah Pernah Di-crack)



### Q: Apakah legal menggunakan program ini?```bash

# Menambah file ZIP baru

**A:** Legal jika digunakan untuk:cp newfile.zip FileZip/

- File milik sendiri yang lupa password

- Testing dengan izin# Jalankan lagi (file lama otomatis di-skip)

- Pembelajaranpython3 crack_zip_password_angka.py



Illegal jika untuk:# Pilih digit

- File orang lain tanpa izinPilih opsi (1-10): 4

- Aktivitas kriminal

- Bypass keamanan tanpa otorisasi# Hanya newfile.zip yang diproses

# File lama akan muncul status SKIPPED

### Q: Bisa crack password dengan simbol (@, #, $, dll)?```



**A:** Saat ini belum support simbol. Untuk menambahkan:### Scenario 5: Crack Password Panjang (7+ Digit)

1. Edit `CHARSET` di program

2. Tambahkan: `+ string.punctuation````bash

3. Note: Akan jauh lebih lambat!# Untuk password panjang, siapkan waktu lama

python3 crack_zip_password_angka.py

### Q: Program berhenti tiba-tiba, apa yang harus dilakukan?

# Pilih opsi 7 (7 digit)

**A:** Pilih opsi (1-10): 7

1. Cek log file - mungkin sudah berhasil

2. Jalankan ulang - program akan skip file yang sudah berhasil# Biarkan berjalan di background (Linux/macOS)

3. Cek error message untuk troubleshootingnohup python3 crack_zip_password_angka.py &



### Q: Bisa di-pause dan di-resume?# Check progress

tail -f nohup.out

**A:** Saat ini belum ada fitur pause/resume otomatis. Workaround:```

1. Tekan Ctrl+C untuk stop

2. Note password terakhir yang dicoba---

3. Edit program untuk mulai dari password tersebut

## 🔒 Keamanan & Legal

### Q: Kenapa progress bar kadang tidak smooth?

⚠️ **PENTING**: Program ini hanya boleh digunakan untuk:

**A:** Progress bar update berdasarkan kombinasi yang dicoba:

- Kombinasi kecil: Update setiap password- ✅ Crack password file ZIP milik sendiri

- Kombinasi besar: Update setiap 100k passwords- ✅ Recover file yang password-nya lupa

- Ini untuk menjaga kecepatan cracking tetap optimal- ✅ Testing & pembelajaran



---❌ **DILARANG** untuk:

- Crack file ZIP milik orang lain tanpa izin

## 🌟 Star History- Aktivitas illegal atau tidak etis

- Bypass keamanan tanpa otorisasi

Jika program ini membantu Anda, jangan lupa beri ⭐ star!

**Pengguna bertanggung jawab penuh atas penggunaan program ini.**

---

---

**Happy Cracking! 🔓**

## 📚 Teknologi yang Digunakan

*Remember: With great power comes great responsibility. Use wisely!*

- **Language**: Python 3
- **Libraries**: `zipfile`, `zlib`, `pathlib`
- **Algorithm**: Brute Force dengan CRC32 Verification
- **Encryption Support**: 
  - ✅ Traditional ZIP encryption
  - ✅ Deflate compression
  - ⚠️ AES encryption (terbatas)

---

## 🎯 Roadmap Fitur

- [x] Support 1-9 digit password
- [x] Custom range selection
- [x] Real-time progress dan speed indicator
- [x] Cross-platform (Linux, Windows, macOS)
- [ ] Multi-threading untuk performa lebih cepat
- [ ] Support karakter alfanumerik (a-z, A-Z, 0-9)
- [ ] Support special characters
- [ ] Dictionary attack mode
- [ ] Resume function untuk process yang terganggu
- [ ] GUI (Graphical User Interface)
- [ ] Support untuk format archive lain (RAR, 7z)
- [ ] Export hasil ke CSV/JSON
- [ ] Distributed cracking (multiple computers)

---

## 📞 Support & Kontribusi

### Report Bug

Jika menemukan bug, silakan buat issue atau hubungi:

- Email: your-email@example.com
- GitHub Issues: [Buat Issue](link-ke-repo)

### Kontribusi

Kontribusi sangat diterima! Silakan:

1. Fork repository ini
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

---

## 📄 Lisensi

Project ini dilisensikan di bawah **MIT License** - lihat file `LICENSE` untuk detail lebih lanjut.

---

## 👨‍💻 Author

**Dibuat oleh**: [Your Name]  
**Created**: November 2025  
**Last Updated**: November 10, 2025

---

## 💡 Tips & Tricks

### 1. Jalankan di Background (Linux/macOS)

```bash
nohup python3 crack_zip_password.py > output.log 2>&1 &
```

### 2. Schedule dengan Cron (Linux/macOS)

```bash
# Edit crontab
crontab -e

# Jalankan setiap hari jam 2 pagi
0 2 * * * cd /path/to/project && python3 crack_zip_password.py
```

### 3. Monitor Progress Real-time

```bash
tail -f output.log
```

### 4. Count File di Extracted

```bash
find Extracted -type f | wc -l
```

### 5. Total Size Extracted

```bash
du -sh Extracted/
```

---

## ❓ FAQ

**Q: Berapa lama proses crack password?**
A: Tergantung jumlah digit. 1-4 digit: detik-menit. 5-6 digit: menit-jam. 7+ digit: jam-hari. Lihat tabel performa di atas.

**Q: Apakah program ini aman?**
A: Ya, program tidak memodifikasi file original. File original tetap aman di folder FileZip.

**Q: Bisakah di-pause dan dilanjutkan?**
A: Belum ada fitur pause built-in, tapi bisa di-stop (Ctrl+C) dan hasil yang sudah di-crack tidak akan di-proses ulang karena tersimpan di log.

**Q: Support password dengan huruf?**
A: Belum, untuk sekarang hanya numerik (0-9). Fitur alfanumerik akan ditambahkan di masa depan.

**Q: Bisa di-jalankan di Windows?**
A: Ya! Program sudah cross-platform. Install Python 3 dan jalankan seperti biasa.

**Q: Kenapa pilih 9 digit masih gagal?**
A: Kemungkinan password mengandung huruf atau simbol, bukan murni angka. Program ini khusus untuk numerik.

**Q: Berapa lama untuk crack 6 digit?**
A: Dengan speed 2500 pwd/s, worst case ~7 jam. Rata-rata ~3.5 jam. Kecepatan bervariasi tergantung CPU.

**Q: Apakah legal menggunakan program ini?**
A: Legal jika digunakan untuk file milik sendiri atau dengan izin. Illegal jika untuk crack file orang lain tanpa izin.

**Q: Bisa dipercepat dengan GPU?**
A: Saat ini belum support GPU. Versi future mungkin akan menambahkan GPU acceleration.

**Q: Program berhenti di tengah jalan, bagaimana?**
A: Jalankan ulang, file yang sudah berhasil di-crack akan di-skip otomatis. File yang gagal akan dilanjutkan dari awal range.

---

## 🎉 Terima Kasih

Terima kasih telah menggunakan **ZIP Password Cracker**!

Jika program ini membantu, silakan berikan star ⭐ di repository ini.

---

**Happy Cracking! 🔓**
