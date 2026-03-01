# CmdEURL Payload Injector 🦆

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" alt="Python">
  <img src="https://img.shields.io/badge/Target-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows">
  <img src="https://img.shields.io/badge/Concept-LotL%20%2F%20Keystroke%20Injection-red?style=for-the-badge" alt="LotL">
</p>

---

## ⚠️ Disclaimer
**For educational and defensive research purposes only.** This script is a Proof of Concept (PoC) designed to simulate the delivery of a `curl`-based reverse shell (compatible with listeners like Hoaxshell). It was built to understand attacker execution flows and to develop SIEM/Sysmon detection rules. Do not use this on systems you do not own or do not have explicit permission to test.

---

## 🔍 What is CmdEURL?
CmdEURL is a Python-based payload delivery simulator. It acts as a software-based "BadUSB" by utilizing the `pyautogui` library to inject a malicious command directly into the active terminal window. 

The injected command leverages `curl.exe` (a native Windows binary - Living off the Land) to establish a beaconing reverse shell connection to a remote listener. 

### 🛡️ SOC / Blue Team Perspective
This project was developed as part of my **Red-to-Blue** learning path. By building the delivery mechanism and the payload itself, I gained hands-on experience in:
1. **LOLBins (Living off the Land Binaries):** Understanding how attackers abuse legitimate administrative tools like `curl` and `findstr` to bypass basic antivirus signatures.
2. **Command Line Obfuscation:** Observing how environment variables (`!protocol!!ip!`) are used in `cmd.exe` to hide the true destination IP from static analysis.
3. **Detection Engineering:** Creating a measurable event that can be hunted in **Sysmon Event ID 1 (Process Creation)** and **Event ID 3 (Network Connection)**.

---

## 🛑 2026 Update & Defender Efficacy (Historical Context)
**Note:** While this execution flow was highly effective around 2022-2023, modern Windows updates, Microsoft Defender, and AMSI now heavily signature Hoaxshell and this specific `curl` command line structure. 

This script is maintained as a **historical research tool** to demonstrate how LotL attacks evolved and to show exactly why modern AV/EDR solutions flag these specific execution chains today.

---

## ⚡ Execution Flow
1. The script prompts the user for the attacker's IP and Port.
2. It dynamically formats a `cmd.exe` payload containing a `curl` beacon loop.
3. Using `pyautogui`, it automatically types the crafted command into the active Command Prompt and executes it via the `Enter` key.
4. The target machine initiates an HTTP connection to the listener (e.g., Hoaxshell).

---

## 🛠️ Installation & Requirements

**Target Requirements:**
- Windows OS
- Python 3.x installed

**Setup via PowerShell:**
```powershell
# 1. Download the repository
curl -o nysch3ns_pload.zip [https://github.com/nysch3n/nysch3ns_pload/archive/refs/heads/main.zip](https://github.com/nysch3n/nysch3ns_pload/archive/refs/heads/main.zip)

# 2. Extract the archive
Expand-Archive .\nysch3ns_pload.zip

# 3. Navigate to the directory
cd nysch3ns_pload\nysch3ns_pload-main

# 4. Install dependencies
pip install -r requirements.txt
```
## 🚀 Usage
1. Start your listener on your attacking machine (e.g., using hoaxshell by t3l3machus).
2. Open a standard cmd.exe window on the target machine.
3. Run the Python script.
4. Enter the required IP and Port.
5. DO NOT close or minimize the terminal window! The script relies on pyautogui simulating keystrokes in the active window.
