#!/usr/bin/env python3
"""
Script untuk crack password ZIP dengan huruf (a-z, A-Z)
Support: ZipCrypto (Linux) dan AES encryption (Windows)
Cross-platform: Linux, Windows, macOS
"""

import zipfile
import os
import sys
import time
import itertools
import string
from pathlib import Path

# Try import pyzipper for AES support
try:
    import pyzipper
    HAS_PYZIPPER = True
except ImportError:
    HAS_PYZIPPER = False

# Set encoding untuk Windows console
if sys.platform == 'win32':
    import codecs
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    if sys.stderr.encoding != 'utf-8':
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Konfigurasi
ZIP_FOLDER = "FileZip"
OUTPUT_FOLDER = "Extracted"
LOG_FILE = "log_alpha.txt"
MIN_LENGTH = 1
MAX_LENGTH = 999

# Character set: a-z dan A-Z
CHARSET = string.ascii_letters

def print_progress_bar(current, total, length, bar_length=50):
    """
    Menampilkan progress bar untuk setiap panjang karakter
    """
    percent = (current / total) * 100
    filled = int(bar_length * current / total)
    bar = '█' * filled + '░' * (bar_length - filled)
    print(f"\r[*] Length {length}: [{bar}] {percent:.1f}% ({current:,}/{total:,})", end='', flush=True)

def read_existing_log():
    """Membaca log untuk mendapatkan daftar file yang sudah di-crack"""
    cracked_files = {}
    
    if not os.path.exists(LOG_FILE):
        return cracked_files
    
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as log:
            lines = log.readlines()
            current_file = None
            
            for line in lines:
                line = line.strip()
                if line.startswith("File: "):
                    current_file = line.replace("File: ", "")
                elif line.startswith("Password: ") and current_file:
                    password = line.replace("Password: ", "")
                    if password != "N/A":
                        cracked_files[current_file] = password
                    current_file = None
    except Exception as e:
        print(f"[!] Warning: Tidak bisa membaca log file: {e}")
    
    return cracked_files


def detect_encryption_type(zip_path):
    """
    Deteksi tipe enkripsi ZIP
    Returns: 'aes', 'zipcrypto', 'none', atau None jika error
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            encrypted_members = [info for info in zf.infolist() if info.flag_bits & 0x1]
            if not encrypted_members:
                return 'none'
            
            # Check compress_type: 99 = AES, lainnya = ZipCrypto
            if encrypted_members[0].compress_type == 99:
                return 'aes'
            else:
                return 'zipcrypto'
    except Exception as e:
        print(f"[!] Error detecting encryption: {e}")
        return None


def crack_with_zipfile(zip_path, min_length, max_length):
    """Crack menggunakan standard zipfile (untuk ZipCrypto)"""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            encrypted_members = [info for info in zip_file.infolist() if info.flag_bits & 0x1]
            test_member_name = encrypted_members[0].filename
            print(f"[*] File test: {test_member_name}")
            
            start_time = time.time()
            tried = 0
            
            for length in range(min_length, max_length + 1):
                print(f"\n[*] Mencoba password {length} karakter...")
                combinations_for_length = len(CHARSET) ** length
                print(f"[*] Kombinasi untuk {length} karakter: {combinations_for_length:,}")
                
                tried_for_length = 0
                for password_tuple in itertools.product(CHARSET, repeat=length):
                    password = ''.join(password_tuple)
                    tried += 1
                    tried_for_length += 1
                    
                    # Update progress bar every 1000 attempts or at intervals
                    if tried_for_length % 1000 == 0 or tried_for_length == combinations_for_length:
                        print_progress_bar(tried_for_length, combinations_for_length, length)
                    
                    if tried % 100000 == 0:
                        elapsed = time.time() - start_time
                        speed = tried / elapsed if elapsed > 0 else 0
                        print(f"\n[*] Speed: {speed:.0f} pwd/s | Testing: {password}")
                    
                    try:
                        pw_bytes = password.encode('utf-8')
                        _ = zip_file.read(test_member_name, pwd=pw_bytes)
                        
                        zip_file.extractall(
                            path=os.path.join(OUTPUT_FOLDER, Path(zip_path).stem),
                            pwd=pw_bytes
                        )
                        
                        elapsed = time.time() - start_time
                        print(f"\n\n[+] PASSWORD DITEMUKAN: {password}")
                        print(f"[+] Panjang: {len(password)} karakter")
                        print(f"[+] Ditemukan setelah mencoba {tried:,} kombinasi dalam {elapsed:.2f} detik")
                        print(f"[+] File sudah diekstrak ke {OUTPUT_FOLDER}/{Path(zip_path).stem}")
                        return password
                        
                    except (RuntimeError, zipfile.BadZipFile):
                        continue
                    except Exception:
                        continue
                
                # Print newline setelah progress bar selesai untuk length ini
                print()  
            
            elapsed = time.time() - start_time
            print(f"\n[-] Password tidak ditemukan setelah mencoba {tried:,} kombinasi dalam {elapsed:.2f} detik")
            return None
            
    except Exception as e:
        print(f"[-] Error: {e}")
        return None


def crack_with_pyzipper(zip_path, min_length, max_length):
    """Crack menggunakan pyzipper (untuk AES encryption)"""
    try:
        with pyzipper.AESZipFile(zip_path, 'r') as zip_file:
            encrypted_members = [info for info in zip_file.infolist() if info.flag_bits & 0x1]
            test_member_name = encrypted_members[0].filename
            print(f"[*] File test: {test_member_name}")
            
            start_time = time.time()
            tried = 0
            
            for length in range(min_length, max_length + 1):
                print(f"\n[*] Mencoba password {length} karakter...")
                combinations_for_length = len(CHARSET) ** length
                print(f"[*] Kombinasi untuk {length} karakter: {combinations_for_length:,}")
                
                tried_for_length = 0
                for password_tuple in itertools.product(CHARSET, repeat=length):
                    password = ''.join(password_tuple)
                    tried += 1
                    tried_for_length += 1
                    
                    # Update progress bar every 1000 attempts or at intervals
                    if tried_for_length % 1000 == 0 or tried_for_length == combinations_for_length:
                        print_progress_bar(tried_for_length, combinations_for_length, length)
                    
                    if tried % 100000 == 0:
                        elapsed = time.time() - start_time
                        speed = tried / elapsed if elapsed > 0 else 0
                        print(f"\n[*] Speed: {speed:.0f} pwd/s | Testing: {password}")
                    
                    try:
                        pw_bytes = password.encode('utf-8')
                        _ = zip_file.read(test_member_name, pwd=pw_bytes)
                        
                        zip_file.extractall(
                            path=os.path.join(OUTPUT_FOLDER, Path(zip_path).stem),
                            pwd=pw_bytes
                        )
                        
                        elapsed = time.time() - start_time
                        print(f"\n\n[+] PASSWORD DITEMUKAN: {password}")
                        print(f"[+] Panjang: {len(password)} karakter")
                        print(f"[+] Ditemukan setelah mencoba {tried:,} kombinasi dalam {elapsed:.2f} detik")
                        print(f"[+] File sudah diekstrak ke {OUTPUT_FOLDER}/{Path(zip_path).stem}")
                        return password
                        
                    except (RuntimeError, Exception):
                        continue
                
                # Print newline setelah progress bar selesai untuk length ini
                print()
            
            elapsed = time.time() - start_time
            print(f"\n[-] Password tidak ditemukan setelah mencoba {tried:,} kombinasi dalam {elapsed:.2f} detik")
            return None
            
    except Exception as e:
        print(f"[-] Error: {e}")
        return None


def crack_zip_password(zip_path, min_length, max_length):
    """
    Main function untuk crack password
    Otomatis deteksi tipe enkripsi dan gunakan method yang sesuai
    """
    print(f"\n[*] Memproses: {os.path.basename(zip_path)}")
    print(f"[*] Range: {min_length}-{max_length} karakter")
    print(f"[*] Character set: a-z, A-Z ({len(CHARSET)} karakter)")
    
    # Deteksi tipe enkripsi
    enc_type = detect_encryption_type(zip_path)
    
    if enc_type == 'none':
        print("[!] File tidak terproteksi password")
        return None
    elif enc_type is None:
        print("[!] Error membaca file ZIP")
        return None
    elif enc_type == 'aes':
        if HAS_PYZIPPER:
            print(f"[*] Deteksi: AES encryption (Windows) - menggunakan pyzipper")
            return crack_with_pyzipper(zip_path, min_length, max_length)
        else:
            print(f"[!] ERROR: File menggunakan AES encryption tetapi pyzipper tidak terinstall")
            print(f"[!] Install dengan: pip3 install pyzipper")
            return None
    else:  # zipcrypto
        print(f"[*] Deteksi: ZipCrypto (Linux/Traditional)")
        return crack_with_zipfile(zip_path, min_length, max_length)


def main():
    """Main function untuk memproses semua file ZIP di folder"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("="*60)
    print("ZIP Password Cracker - Alphabetic Brute Force")
    print("Character Set: a-z, A-Z (52 karakter)")
    print("Support: ZipCrypto (Linux) + AES (Windows)")
    print("Cross-platform: Linux | Windows | macOS")
    print("="*60)
    
    # Buat folder output jika belum ada
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    # Cari semua file ZIP di folder
    zip_folder_path = Path(ZIP_FOLDER)
    if not zip_folder_path.exists():
        print(f"[-] Folder {ZIP_FOLDER} tidak ditemukan!")
        print(f"[*] Membuat folder {ZIP_FOLDER}...")
        os.makedirs(ZIP_FOLDER, exist_ok=True)
        print(f"[!] Silakan letakkan file ZIP di folder {ZIP_FOLDER} dan jalankan lagi")
        input("\nTekan ENTER untuk keluar...")
        return
    
    zip_files = list(zip_folder_path.glob("*.zip"))
    
    if not zip_files:
        print(f"[-] Tidak ada file ZIP di folder {ZIP_FOLDER}")
        input("\nTekan ENTER untuk keluar...")
        return
    
    print(f"[*] Ditemukan {len(zip_files)} file ZIP")
    
    # Baca log untuk melihat file yang sudah di-crack
    print(f"[*] Memeriksa {LOG_FILE} untuk file yang sudah di-crack...")
    cracked_files = read_existing_log()
    
    if cracked_files:
        print(f"[*] Ditemukan {len(cracked_files)} file yang sudah di-crack sebelumnya")
    
    print(f"\n[*] Mode: Otomatis mencoba password dari {MIN_LENGTH} karakter tanpa batas")
    print(f"[*] Character set: a-z, A-Z ({len(CHARSET)} karakter)")
    
    # Proses setiap file ZIP
    results = []
    skipped_count = 0
    success_count = 0
    failed_count = 0
    
    for zip_file in zip_files:
        # Cek apakah file sudah pernah di-crack
        if zip_file.name in cracked_files:
            print(f"\n[*] SKIP: {zip_file.name} (sudah di-crack, password: {cracked_files[zip_file.name]})")
            results.append({
                'filename': zip_file.name,
                'password': cracked_files[zip_file.name],
                'status': 'SKIPPED (already cracked)'
            })
            skipped_count += 1
            continue
        
        password = crack_zip_password(str(zip_file), MIN_LENGTH, MAX_LENGTH)
        
        if password:
            results.append({
                'filename': zip_file.name,
                'password': password,
                'status': 'SUCCESS'
            })
            success_count += 1
        else:
            results.append({
                'filename': zip_file.name,
                'password': 'N/A',
                'status': 'FAILED'
            })
            failed_count += 1
    
    # Tulis hasil ke log
    print(f"\n[*] Menulis hasil ke {LOG_FILE}...")
    with open(LOG_FILE, 'w', encoding='utf-8') as log:
        log.write("="*60 + "\n")
        log.write("ZIP Password Cracking Results (Alphabetic)\n")
        log.write(f"Length Range: {MIN_LENGTH}-{MAX_LENGTH} karakter\n")
        log.write(f"Character Set: a-z, A-Z\n")
        log.write("="*60 + "\n\n")
        
        for result in results:
            log.write(f"File: {result['filename']}\n")
            log.write(f"Password: {result['password']}\n")
            log.write(f"Status: {result['status']}\n")
            log.write("-"*60 + "\n")
    
    # Tampilkan ringkasan
    print("\n" + "="*60)
    print("RINGKASAN")
    print("="*60)
    
    if skipped_count > 0:
        print(f"[*] File yang di-skip (sudah di-crack): {skipped_count}")
    if success_count > 0:
        print(f"[*] File yang berhasil di-crack: {success_count}")
    if failed_count > 0:
        print(f"[*] File yang gagal di-crack: {failed_count}")
    
    print("\nDetail:")
    for result in results:
        if result['status'] == 'SKIPPED (already cracked)':
            status_symbol = "[SKIP]" if os.name == 'nt' else "⊘"
        elif result['status'] == 'SUCCESS':
            status_symbol = "[OK]" if os.name == 'nt' else "✓"
        else:
            status_symbol = "[FAIL]" if os.name == 'nt' else "✗"
        print(f"{status_symbol} {result['filename']}: {result['password']}")
    
    print(f"\n[+] Selesai! Hasil disimpan di {LOG_FILE}")
    print(f"[+] File terekstrak di folder {OUTPUT_FOLDER}/")
    
    input("\nTekan ENTER untuk keluar...")


if __name__ == "__main__":
    main()
