# Changelog - ZIP Password Cracker Suite

## Version 2.0.0 - Cross-Platform Support (10 November 2025)

### 🎉 Major Update: Full Cross-Platform Compatibility

Semua 3 program sekarang **mendukung file ZIP dari Windows dan Linux**!

### ✨ Fitur Baru

#### 1. Auto-Detection Encryption Type
- Otomatis deteksi **AES encryption** (dari Windows/WinRAR/7-Zip)
- Otomatis deteksi **ZipCrypto** (dari Linux zip command)
- Tidak perlu manual pilih - program pintar memilih method yang tepat

#### 2. Dual-Method Support
- **ZipCrypto**: Menggunakan Python standard `zipfile` library
- **AES**: Menggunakan `pyzipper` library untuk AES-128/192/256

#### 3. Enhanced Error Handling
- Deteksi file tanpa password
- Deteksi AES tanpa pyzipper installed
- Informasi jelas tentang tipe enkripsi yang digunakan

### 📦 Dependencies Baru

```bash
pip3 install pyzipper
```

**Otomatis install dependencies:**
- pyzipper 0.3.6
- pycryptodomex 3.23.0

### 🔧 Program yang Di-update

1. **crack_zip_password_angka.py**
   - ✅ Support AES + ZipCrypto
   - Character set: 0-9 (10 chars)
   - Log file: `log.txt`

2. **crack_zip_password_alpha.py**
   - ✅ Support AES + ZipCrypto
   - Character set: a-z, A-Z (52 chars)
   - Log file: `log_alpha.txt`

3. **crack_zip_password_alphanumeric.py**
   - ✅ Support AES + ZipCrypto
   - Character set: a-z, A-Z, 0-9 (62 chars)
   - Log file: `log_alphanumeric.txt`

### 🐛 Bug Fixes

- Fixed false-positive password detection pada ZipCrypto
- Fixed program "labas terus" (tidak berhenti) - sekarang berhenti saat password ditemukan
- Improved password verification dengan `zip_file.read()` sebelum `extractall()`

### 📝 Output Improvements

Program sekarang menampilkan:
```
[*] Deteksi: AES encryption (Windows) - menggunakan pyzipper
```
atau
```
[*] Deteksi: ZipCrypto (Linux/Traditional)
```

### 🧪 Tested With

- ✅ ZIP dengan password "aa" (AES encryption) - **BERHASIL**
- ✅ 51 files .xmp diekstrak dari AES ZIP
- ✅ Syntax check passed untuk semua program

### 📚 Compatibility

- **Windows**: ZIP dari Explorer, WinRAR, 7-Zip (AES)
- **Linux**: ZIP dari `zip -e` atau `zip -P` command (ZipCrypto)
- **macOS**: ZIP dari Archive Utility atau command line

### 🚀 Migration Guide

Tidak perlu perubahan! Program otomatis detect dan gunakan method yang sesuai.

Jika belum install pyzipper:
```bash
pip3 install pyzipper
```

### 💡 Notes

- AES encryption ~3x lebih lambat dari ZipCrypto karena algoritma lebih complex
- Program otomatis gunakan method tercepat untuk tipe enkripsi masing-masing
- Backup files tersimpan dengan ekstensi `.backup`

---

**Previous Version**: 1.0.0 (ZipCrypto only)
