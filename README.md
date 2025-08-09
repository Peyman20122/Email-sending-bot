
# EmailBot - Python Email Sending Bot

This project provides a simple Python class to send emails with optional file attachments.
It uses Python's built-in `smtplib` and `email` libraries.

---

## Features

* Send emails to a specified recipient
* Send plain text email body
* Attach a file (e.g., PDF, image) to the email
* Support for multiple email services (Gmail, Outlook, Yahoo, and custom SMTP servers)
* Uses TLS encryption for secure email transmission

---

## How to Use

1. Include or import the `EmailBot` class in your project.

2. Create an instance of `EmailBot` with the following parameters:

* `email_address`: Sender's email address
* `email_password`: Sender's email password or app-specific password (recommended for Gmail)
* `attachment_path`: Path to the attachment file (use `None` if no attachment)
* `email_service`: Email service provider (`gmail`, `outlook`, `yahoo`, or `custom`)
* `body`: Email body text
* `subject`: Email subject
* `receiver_email`: Recipient's email address

3. Call the `send_email()` method to send the email.

---

## Example Code

```python
bot = EmailBot(
    email_address="youremail@gmail.com",
    email_password="your-app-password",
    attachment_path="path/to/file.pdf",
    email_service="gmail",
    body="Hello, this is a test email.",
    subject="Test Email",
    receiver_email="receiver@example.com"
)

bot.send_email()
```

---

## Important Notes

* For Gmail, it is recommended to use an [App Password](https://support.google.com/accounts/answer/185833) instead of your main password for better security.
* If using a custom SMTP server, add the server details (address and port) in the `SMTP_CONFIGS` dictionary inside the class or use the `"custom"` option and specify the details accordingly.
* Ensure the attachment file path is correct; otherwise, the attachment will not be sent.
* An active internet connection and open SMTP ports are required.
* Any errors during sending will be printed to the console for debugging.

---

## Possible Improvements

* Support sending HTML formatted emails
* Send emails to multiple recipients at once
* Support SMTP servers requiring SSL connections
* Improved error handling and logging


