import time
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def send_email_alert(subject, body, sender_email, receiver_email, smtp_server, port, login, password):
    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(login, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        print(f"📧 Email alert sent: {subject}")

    except Exception as e:
        print(f"⚠️ Failed to send email: {e}")


class FileMonitorHandler(FileSystemEventHandler):
    def __init__(self, sender_email, receiver_email, smtp_server, port, login, password):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.smtp_server = smtp_server
        self.port = port
        self.login = login
        self.password = password

    def on_created(self, event):
        message = f"File created: {event.src_path}"
        print(message)
        send_email_alert("File Created", message,
                         self.sender_email, self.receiver_email,
                         self.smtp_server, self.port, self.login, self.password)

    def on_deleted(self, event):
        message = f"File deleted: {event.src_path}"
        print(message)
        send_email_alert("File Deleted", message,
                         self.sender_email, self.receiver_email,
                         self.smtp_server, self.port, self.login, self.password)

    def on_modified(self, event):
        message = f"File modified: {event.src_path}"
        print(message)
        send_email_alert("File Modified", message,
                         self.sender_email, self.receiver_email,
                         self.smtp_server, self.port, self.login, self.password)


def start_monitoring(path, sender_email, receiver_email, smtp_server, port, login, password):
    event_handler = FileMonitorHandler(sender_email, receiver_email, smtp_server, port, login, password)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print(f"🔍 Monitoring started on: {path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("🛑 Monitoring stopped.")
    observer.join()


if __name__ == "__main__":
    path = input("Enter the path to monitor: ").strip()

    sender_email = "myemail@gmail.com"       
    receiver_email = "friendemail@gmail.com" 
    smtp_server = "smtp.gmail.com"
    port = 465
    login = "myemail@gmail.com"              
    password = "abcd efgh ijkl mnop"         

    start_monitoring(path, sender_email, receiver_email, smtp_server, port, login, password)
