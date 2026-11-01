# File Hashing in Digital Forensics

## 1. What is File Hashing?
File hashing is the process of converting file data into a fixed-length value called a hash.

## 2. What is SHA-256?
SHA-256 is a cryptographic hash algorithm that produces a 256-bit hash value.

## 3. Importance of File Hashing
- Helps verify file integrity.
- Detects accidental or unauthorized changes.
- Supports digital evidence verification.
- Helps compare original files with working copies.

## 4. How It Works
1. Select a file.
2. Calculate its hash value.
3. Record the hash.
4. Calculate the hash again when verification is needed.
5. Compare both values.

If the hash values match, the files have matching contents with extremely high confidence.

## 5. Common Hash Algorithms
- MD5
- SHA-1
- SHA-256
- SHA-512

SHA-256 is generally preferred over MD5 and SHA-1 for integrity verification.

## 6. Python Library
Python provides the hashlib library for calculating file hashes.

Example:
import hashlib

with open("sample.txt", "rb") as file:
    data = file.read()

hash_value = hashlib.sha256(data).hexdigest()

print("SHA-256:", hash_value)

