import streamlit as st
import imaplib
import email

# ---------------- PRIORITY KEYWORDS ----------------

keywords = {
    "urgent": 20,
    "meeting": 10,
    "deadline": 15,
    "important": 10,
    "asap": 15,
    "issue": 10
}

# ---------------- STREAMLIT UI ----------------

st.title("AI Email Priority Agent")

email_user = st.text_input("Enter Gmail")

email_pass = st.text_input(
    "Enter App Password",
    type="password"
)

# ---------------- FETCH EMAILS ----------------

if st.button("Fetch Priority Emails"):

    # Connect Gmail
    mail = imaplib.IMAP4_SSL("imap.gmail.com")

    mail.login(email_user, email_pass)

    # Open inbox
    mail.select("inbox")

    # Get all emails
    status, messages = mail.search(None, "ALL")

    email_ids = messages[0].split()

    emails = []

    # Read latest 10 emails
    for e_id in email_ids[-10:]:

        status, data = mail.fetch(e_id, "(RFC822)")

        raw_email = data[0][1]

        msg = email.message_from_bytes(raw_email)

        # Get subject
        subject = str(msg["Subject"])

        # Get sender
        sender = str(msg["From"])

        # ---------------- GET EMAIL BODY ----------------

        body = ""

        if msg.is_multipart():

            for part in msg.walk():

                if part.get_content_type() == "text/plain":

                    try:
                        body = part.get_payload(decode=True).decode()
                    except:
                        body = ""

        else:

            try:
                body = msg.get_payload(decode=True).decode()
            except:
                body = ""

        # Convert body to lowercase
        content = body.lower()

        # ---------------- PRIORITY SCORE ----------------

        score = 0

        for word in keywords:

            if word in content:
                score += keywords[word]

        emails.append((score, subject, sender))

    # Sort emails
    emails.sort(reverse=True)

    # ---------------- DISPLAY OUTPUT ----------------

    st.subheader("Top Priority Emails")

    for score, subject, sender in emails[:5]:

        st.write(f"Sender: {sender}")
        st.write(f"Subject: {subject}")
        st.write("---")

    # Logout
    mail.logout()