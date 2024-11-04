# Rubber Ducky in Cybersecurity: Antivirus Deactivation / Data Extraction / Backdoor

## Description

This project explores the use of the USB Rubber Ducky in cybersecurity, demonstrating techniques such as antivirus deactivation, data extraction, and backdoor installation. It showcases the potential of such attacks in a controlled environment to raise awareness of risks and to help develop defensive measures.

> **Warning:** This project is intended strictly for educational purposes and should only be used in authorized environments with the necessary permissions. Using these techniques outside of a legal framework is strictly prohibited.

## Contributors

- Maël PLARD
- Alice VIVET
- Alexandre FOURNET

## Context

Rubber Ducky devices are often used in penetration testing scenarios to simulate attacks based on automated command injection. Due to their USB-like appearance, they are commonly used in **social engineering** attack demonstrations. The objective of this project is to explore and document various attack techniques, focusing on three main areas:

1. **Antivirus Deactivation**: Demonstrates methods to bypass or temporarily disable antivirus software.
2. **Data Extraction**: Techniques to extract sensitive data from the target machine using automated scripts.
3. **Backdoor Installation**: Methods for installing a backdoor to allow persistent access to the target system.

## Project Overview

This project leverages a Raspberry Pi to emulate a "Bad USB" device, similar to a Rubber Ducky, in a cybersecurity context. Upon connection to a Windows computer, the Raspberry Pi mounts a storage space named "CIRCUITPY" containing a `code.py` script and necessary libraries for executing automated commands. The objectives include disabling antivirus software, extracting sensitive data, and setting up a backdoor for future access.

## Setup and Components

1. **CIRCUITPY Setup**: 
   - When connected, the Raspberry Pi creates a storage space named `CIRCUITPY` containing:
     - A `code.py` file for payload execution.
     - A `lib` folder with the `adafruit_hid` library and a custom AZERTY keyboard layout.
   - The initial `code.py` script displays "Hello World!" on power-up, confirming that the necessary libraries are installed and functioning.

2. **Libraries**:
   - **adafruit_hid** library: Enables keyboard emulation to send keystrokes.
   - **Custom AZERTY Layout**: Adjusts the keyboard mapping for French keyboards.

## Attack Steps

The `code.py` script executes the following steps:

### Initial Payload: Antivirus Deactivation and Command Line Access
1. Opens "Virus & Threat Protection" settings.
2. Disables antivirus through recorded keystrokes.
3. Opens a command prompt for further commands.

### Primary Script: Automated Antivirus Deactivation and Data Extraction
1. **Disables Antivirus**: Executes commands to disable the Windows Defender antivirus.
2. **Data Extraction**: Uses command-line commands to extract sensitive data, specifically the SAM, SECURITY, and SYSTEM registry files.
3. **Data Transfer**: Transfers extracted data to an FTP server for analysis.

### Secondary Script: Backdoor Setup
1. **Creates an Administrator Account**: Adds a new user to the administrator group.
2. **Configures WinRM Service**: Enables Windows Remote Management to facilitate remote access.
3. **Disables UAC Remote Restrictions**: Allows remote administrative actions.
4. **Hides Malicious User**: Prevents the new user from appearing on the login screen.
5. **Exploitation**: Enables remote access through **evil-winrm** from a Kali Linux machine to the victim’s system.

> **Note:** Success depends on OS version compatibility, network stability, and ensuring no modifications create infinite execution loops within CIRCUITPY.

## Challenges and Solutions

- **Boot Failure on Raspberry Pi**: Initial issues with booting were resolved by installing a stable version of CircuitPython.
- **CIRCUITPY Infinite Loops**: Modifications to the `code.py` script needed careful handling to avoid repeated execution loops upon each reconnection.

## Attack Scenarios

1. **File Theft**: Successfully extracted registry files and transferred them via an FTP server for analysis.
2. **Backdoor Installation**: The backdoor provided persistent administrative access, allowing further data extraction or follow-up attacks.

> **FTP Note:** An insecure FTP server was used for simplicity, although more secure protocols would be ideal for real-world applications.

## Project Insights

This project offered practical experience in using the Raspberry Pi within Windows environments, highlighting both the strengths and limitations of a custom-built Bad USB device. While more affordable than commercial options like the Rubber Ducky, building and configuring a custom device presents complexities.

## Limitations and Future Enhancements

- **OS Compatibility**: Success varies by OS version and settings; expanding compatibility would increase reliability.
- **Network Accessibility**: Ensuring backdoor accessibility across different networks could be improved by installing malware to manage remote connections.
- **OS Detection**: Incorporating OS detection could allow tailored attacks on Linux or other platforms.

## Security Recommendations

1. **Admin Account Separation**: Limit administrative rights to essential users and accounts to reduce risk.
2. **USB Security Awareness**: Train users on the risks of connecting unknown USB devices to critical systems.

---

This project emphasizes the importance of understanding potential USB-based attack vectors and highlights the need for vigilance in USB device management and security practices.
