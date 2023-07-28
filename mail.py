from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_mail(companyname, name, furigana, id, tel, postcode, address, content):

    to = 'a.togasawa.sys22@morijyobi.ac.jp' #宛先
    PASS = os.environ['MAIL_PASS']
    HOST = 'smtp.gmail.com'
    PORT = 587
    subject = '依頼'

    body = f'<p>会社名:{companyname}</p><p>名前:{name}</p><p>フリガナ:{furigana}</p><p>メールアドレス:{id}</p><p>電話番号:{tel}</p><p>住所:〒{postcode}</p><p>{address}</p><br><p>{content}</p>'

    # MIME インスタンスを生成
    msg = MIMEMultipart()
    # HTML 形式の本文を設定
    msg.attach(MIMEText(body, 'html'))
    # 件名、送信元アドレス、送信先アドレスを設定
    msg['Subject'] = subject
    msg['From'] = id
    msg['To'] = to

    # SMTP サーバへ接続
    server = SMTP(HOST, PORT)
    server.starttls()
    server.login(to, PASS) # ログイン認証
    server.send_message(msg) # 送信！！！
    server.quit() # サーバ切断