from bs4 import BeautifulSoup
import requests
import smtplib

url = "https://geizhals.de/razer-viper-v3-hyperspeed-schwarz-rz01-04910100-r3m1-a3022623.html"

def getPrice(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit /537.36'
    }
    try:
        response = requests.get(url, headers=headers)
    except requests.RequestException:
        return -1

    soup = BeautifulSoup(response.content, "html.parser")

    price = soup.find('span', class_='gh_price')

    price_value = 0

    if price:
        price_string = price.get_text(strip=True)

        price_value = price_string.replace("€", "").replace(",", ".").strip()
        return float(price_value)
    else:
        return -1

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    #create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # connect to SMPT server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()   
        server.login(sender_email, sender_password)   
        server.send_message(msg)   
        server.quit()
        print("E-Mail erfolgreich gesendet!")
    except Exception as e:
        print("Fehler beim Senden:", e)


def checkPrice(url):
    price = getPrice(url)

    password = "xqho buum szxh ayjp"
    email = "nguyenlekevin2006@gmail.com"
    subject = "Price has fallen"
    product = "Razer Viper"
    body = f"The Price is for {product} has fallen to {price}€ !\n Click the link to buy it now: \n" + url

    if price == -1:
        return
    if price < 60:
        send_email(email, password, email, subject, body)

checkPrice(url)