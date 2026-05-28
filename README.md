## AI Email Priority Agent

### 📌 Overview
- AI Email Priority Agent is a simple AI-based email analyzer built using Python and Streamlit.
- The application connects to a Gmail inbox using IMAP and prioritizes emails based on important keywords found inside the email body.
- The main goal of this project is to reduce email overload by helping users quickly identify important emails.

---

### 🚀 Features
- Connects securely to Gmail using IMAP
- Reads latest emails from inbox
- Extracts email subject, sender, and body
- Assigns priority scores using keyword analysis
- Displays top priority emails
- Simple Streamlit user interface

---

### 🛠️ Technologies Used
- Python
- Streamlit
- Imaplib
- Email Module

---

### ▶️ Run the Application
```bash
pip install -r requirements.txt
```

```bash
streamlit run main.py
```
---

### 🔐 Gmail Setup

To use this project with Gmail:

- Enable 2-Step Verification in Gmail
- Generate an App Password
- Use the Gmail address and App Password inside the app

---

### 📂 Project Structure

```bash
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```
---