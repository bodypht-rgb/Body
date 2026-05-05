# IoT-Sentinel: Asynchronous Protocol Resilience Auditor

## 🛡️ Project Overview
**IoT-Sentinel** is a high-performance, asynchronous security research tool designed to audit the resilience of IoT devices (specifically tailored for Windows IoT Core environments like ATMs). It evaluates how these systems handle concurrent requests across multiple protocols including **SSH, MQTT, and HTTP**.

The core philosophy of this project is **"Safety-First Auditing"**, utilizing advanced concurrency control to prevent accidental service disruption during security assessments.

## ✨ Key Engineering Features
- **Asynchronous Orchestration:** Built with `asyncio` to handle high-concurrency probing with minimal CPU/RAM overhead, making it ideal for low-power IoT hardware.
- **Adaptive Throttling:** Implements `asyncio.Semaphore` to strictly control the number of simultaneous connections, mimicking "Human-like" interaction and preventing Rate-Limit triggers.
- **Multi-Protocol Support:** Modular architecture supporting specialized auditing for:
  - **Secure Shell (SSH):** Credential and command execution resilience.
  - **MQTT:** Broker injection and topic-level access control.
  - **Web Services:** Endpoint exposure and HTTP header hardening.

## 🏗️ Architecture Diagram


## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- `pip install -r requirements.txt`

### Configuration
1. Clone the repository.
2. Rename `.env.example` to `.env`.
3. Set your **Authorized** target IP and parameters.

## ⚖️ Legal & Ethical Disclosure
This tool is strictly for **educational purposes** and **authorized security auditing**. Accessing or attempting to audit any system without explicit, written consent from the owner is illegal. The developer of this tool promotes **Ethical Hacking** and assumes no responsibility for misuse or damage caused by this software.

## 👨‍💻 Author
**Abdelrahman Mahmoud**
*Backend & Security Research Engineer*
[GitHub](https://github.com/bodypht-rgb) | [LinkedIn](https://www.linkedin.com/in/abdelrahman-mahmoud-655395405)
