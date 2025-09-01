# 🛡️ File Monitor with Email Alerts

A Python tool that monitors a directory for file changes (created, modified, deleted) and sends **real-time email alerts** when events occur.  
Built using [`watchdog`](https://pypi.org/project/watchdog/) and Python's built-in `smtplib`.

---

## ✨ Features
- 📂 Monitor any directory (recursive support included).
- 📧 Receive instant email notifications for:
  - File **created**
  - File **deleted**
  - File **modified**
- 🔐 Secure Gmail SMTP connection (SSL).

---

## 🚀 Installation

1. Clone this repository:
   ```
   git clone https://github.com/VarunSMenon/File_Integrity_Monitoring_Tool.git
   cd File_Integrity_Monitoring_Tool
