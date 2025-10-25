# Web Application Vulnerability Scanner

**Internship Project by Suriya Kumaran**  
Paavai Engineering College — B.E. Cybersecurity

---

## 🧠 Overview

The **Web Application Vulnerability Scanner** is a Python-based security tool developed as part of my cybersecurity internship.  
It automatically detects common web vulnerabilities such as **Cross-Site Scripting (XSS)** and **SQL Injection (SQLi)** by crawling target URLs, testing payloads, and analyzing responses.

This project aims to demonstrate practical understanding of **OWASP Top 10** concepts, web security testing, and secure software development principles.

---

## ⚙️ Key Features

- 🌐 **Automated Crawling:** Discovers links, forms, and input fields on a target website.  
- 💉 **Vulnerability Detection:** Injects safe XSS and SQLi payloads and inspects responses.  
- 📊 **Report Generation:** Logs results with URL, parameter, payload, and severity level.  
- 🧩 **Flask Web Dashboard:** Manage scans, view vulnerabilities, and export results.  
- 🧱 **SQLite Database:** Stores scan results locally for later review.  
- 🛡️ **Ethical Scope:** Designed strictly for learning and testing authorized targets.

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| Programming Language | Python 3 |
| Libraries | requests, BeautifulSoup4, Flask, sqlite3, regex |
| UI Framework | Flask + HTML (Jinja2 templates) |
| Database | SQLite |
| OS Compatibility | Windows / Linux |

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/suriyakumaran6/ElevateLabs.git
cd ElevateLabs/Project
