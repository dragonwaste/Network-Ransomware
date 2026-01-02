# Network Ransomware (Educational Simulation)

## ⚠️ Disclaimer
This project is **strictly for educational and research purposes**.  
It is intended to demonstrate how ransomware-style attacks may operate in a **controlled, isolated lab environment** in order to better understand, detect, and defend against them.

**Do NOT deploy this code on real networks or systems.**

---

## 📌 Project Overview

Network Ransomware is a Python-based educational simulation that models the behavior of a ransomware attack within a networked environment. The project focuses on:

- Attack orchestration
- Configuration-driven execution
- Encryption/decryption workflows
- Victim and attacker setup automation
- Demonstrating common ransomware lifecycle stages

This project is useful for students and researchers studying:
- Malware behavior
- Cybersecurity defense strategies
- Incident response
- Network security fundamentals

---

## 🧩 Project Structure

Network_Ransomware/
│
├── main.py # Main controller for the ransomware workflow
├── attack.py # Core ransomware logic and attack behavior
├── dycryptor.py # Decryption logic (recovery simulation)
├── config.conf # Configuration file (key-value format)
├── victim_setup.bat # Simulated victim environment setup
├── cleanup_setup.bat # Cleanup and reset script


---

## ⚙️ Key Features

- Modular ransomware simulation architecture
- Configurable execution using a `.conf` file
- Encryption and decryption logic separation
- Automated setup and cleanup scripts
- Designed for safe testing in isolated environments

---

## 🛠️ Technologies Used

- Python 3
- File I/O
- Configuration parsing
- Modular code design
- Batch scripting (Windows)

---

## 📚 Educational Use Cases

- Malware analysis labs
- Blue team / SOC training
- Understanding ransomware kill chains
- Practicing detection and mitigation strategies

---

## 🚫 Ethical Use Notice

This project must **only** be used:
- On systems you own
- In sandboxed or virtual environments
- For defensive security education

Misuse of this code may be illegal and unethical.

