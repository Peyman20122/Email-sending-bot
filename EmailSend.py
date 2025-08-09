import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

class EmailBot:

    SMTP_CONFIGS = {
        "gmail": {"server": "smtp.gmail.com", "port": 587, "use_tls": True},
        "outlook": {"server": "smtp-mail.outlook.com", "port": 587, "use_tls": True},
        "yahoo": {"server": "smtp.mail.yahoo.com", "port": 587, "use_tls": True},
        "custom": {"server": "your.smtp.server", "port": 587, "use_tls": True}
    }

    def __init__(self, email_address, email_password, attachment_path, email_service, body, subject, receiver_email):
        self.smtp_config = self.SMTP_CONFIGS.get(email_service, self.SMTP_CONFIGS["custom"])
        self.email_address = email_address
        self.email_password = email_password
        self.attachment_path = attachment_path
        self.body = body
        self.subject = subject
        self.receiver_email = receiver_email

    def send_email(self):
        sender_email = self.email_address
        receiver_email = self.receiver_email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = self.subject
        message.attach(MIMEText(self.body, "plain"))

        if self.attachment_path and os.path.exists(self.attachment_path):
            with open(self.attachment_path, "rb") as f:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={os.path.basename(self.attachment_path)}"
            )
            message.attach(part)

        try:
            server = smtplib.SMTP(self.smtp_config["server"], self.smtp_config["port"], timeout=30)
            if self.smtp_config.get("use_tls"):
                server.starttls()
            server.login(sender_email, self.email_password)
            text = message.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print("ایمیل با موفقیت ارسال شد")
        except Exception as e:
            print(f"خطا در ارسال ایمیل: {e}")
        finally:
            server.quit()


bot = EmailBot(
    email_address="peimandaii2012@gmail.com",
    email_password="AppPassword",
    attachment_path="p.pdf",
    email_service="gmail",
    body="این متن ایمیل تستی است",
    subject="ایمیل تست",
    receiver_email="peymandr2012@gmail.com"
)

bot.send_email()



