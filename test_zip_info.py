#!/usr/bin/env python3
import zipfile
import sys

zip_path = sys.argv[1] if len(sys.argv) > 1 else "FileZip/50+ Preset Alam Aesthetic (XMP) - BANG ZECK1.zip"

print(f"Analyzing: {zip_path}\n")

with zipfile.ZipFile(zip_path, 'r') as zf:
    print(f"Total files: {len(zf.infolist())}\n")
    
    for info in zf.infolist()[:5]:  # Show first 5 files
        print(f"File: {info.filename}")
        print(f"  Compressed size: {info.compress_size}")
        print(f"  Uncompressed size: {info.file_size}")
        print(f"  Flag bits: {info.flag_bits} (0x{info.flag_bits:04x})")
        print(f"  Is encrypted (bit 0): {bool(info.flag_bits & 0x1)}")
        print(f"  Compress type: {info.compress_type}")
        print()
    
    # Test berbagai password
    test_passwords = ['a', 'aa', 'aaa', 'AAA', 'test', 'password']
    
    encrypted_files = [info for info in zf.infolist() if info.flag_bits & 0x1]
    if encrypted_files:
        test_file = encrypted_files[0]
        print(f"\nTesting passwords on: {test_file.filename}")
        print(f"File is encrypted: {bool(test_file.flag_bits & 0x1)}")
        
        for pwd in test_passwords:
            try:
                data = zf.read(test_file.filename, pwd=pwd.encode('utf-8'))
                print(f"✓ Password '{pwd}' WORKS! (read {len(data)} bytes)")
            except RuntimeError as e:
                print(f"✗ Password '{pwd}' failed: {e}")
            except Exception as e:
                print(f"✗ Password '{pwd}' error: {type(e).__name__}: {e}")
