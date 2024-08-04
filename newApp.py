import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests

URL = "https://newsapi.org/v2/everything"
API_KEY = "e588f6955eca4fb3b5cceacf5e50f56a"
topic = "tesla"
params = {
    "q": topic,
    "apiKey": API_KEY,
    "language": 'en',
    "sortBy": "publishedAt"
}
response = requests.get(URL, params=params)


def send_email(email_body):
    host = "smtp.gmail.com"
    port = 465

    username = "ashistripathy897@gmail.com"
    password = "ofqb ooir rzbg pktj"

    receiver = "ashistripathy897@gmail.com"
    context = ssl.create_default_context()

    # Create a MIMEMultipart message to add subject and email headers
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = receiver
    msg['Subject'] = "Subject: Today's News"

    # Attach the HTML body to the message
    msg.attach(MIMEText(email_body, 'html'))

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.send_message(msg)


response_json = response.json()["articles"]

# Create HTML email body
body = """
<html>
<head></head>
<body>
    <h2>Latest Tesla News</h2>
"""

for article in response_json[:21]:
    if (article['title'] is not None) and (article['description'] is not None) and (article['url'] is not None):
        body += f"""
        <h3>{article['title']}</h3>
        <p>{article['description']}</p>
        <a href="{article['url']}">Read more</a>
        <br><br>
        """

# Close HTML tags
body += """
</body>
</html>
"""

print(body)

# Encode body as UTF-8
# body = body.encode('utf-8')

# Send email
send_email(email_body=body)
