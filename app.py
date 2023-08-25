import datetime
from email.mime.text import MIMEText
import hashlib
import os
from flask import Flask
import psycopg2
from werkzeug.utils import secure_filename

import random
import string
from MySQLdb import connect
from flask import Flask, redirect, render_template, request, session, url_for 




import hashlib
app = Flask(__name__)
import mail


app = Flask(__name__)

def get_connection():
    url = os.environ['DATABASE_URL']
    connection = psycopg2.connect(url)
    return connection

@app.route('/')
def index():
    sql = "SELECT * FROM himekami_news ORDER BY contentday DESC LIMIT 5"
  
    
    # try :
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute(sql)
    news = cursor.fetchall()


    # except psycopg2.DatabaseError :
    #     flg = False

    # finally :
    cursor.close()
    connection.close()

    return render_template('index.html',news=news)

@app.route('/inquiry')
def inquiry():
    return render_template('inquiry.html')

@app.route('/inquiry_mail', methods=['POST'])
def inquiry_mail():
    companyname = request.form.get('companyname')
    name = request.form.get('name')
    furigana = request.form.get('furigana')
    id = request.form.get('mail')
    tel = request.form.get('tel')
    postcode = request.form.get('postcode')
    address = request.form.get('address')
    content = request.form.get('content')
    # メール送信
    mail.send_mail(companyname, name, furigana, id, tel, postcode, address, content)
    return redirect(url_for('index'))


@app.route('/post_news')
def post_news():
    return render_template('post_news.html')


@app.route('/post_news_result',methods = ["POST"])
def post_news_result():

      UPLOAD_FOLDER = 'C:/Users/itou/Documents/GitHub/project_e/static/img'
      file = request.files['img']
      charset = string.ascii_letters + string.digits
      ran = ''.join(random.choices(charset, k=5))
      f_name = secure_filename(file.filename)
      up_fail=ran+f_name
      title=request.form.get("title")
      content=request.form.get("content")
      connection = get_connection()
      cursor = connection.cursor()

        # SQLの実行
      sql = "INSERT INTO himekami_news(title, content, image) VALUES(%s, %s, %s)"
      cursor.execute(sql,(title,content,up_fail))
      count = cursor.rowcount # 更新件数を取得
      connection.commit()
        # except:
            #  count=0
        # finally: # 成功しようが、失敗しようが、close する。
      cursor.close()
      connection.close()

        
      if count==1:
            file.save(os.path.join(UPLOAD_FOLDER , up_fail))
            return render_template('postnews_result.html')
      else:
            return render_template('post_news.html')

@app.route('/adoption')
def adoption():
    return render_template('adoption.html')


@app.route('/profile')
def profile():
    return render_template('companyprofile.html')


if __name__ == '__main__':
    app.run(debug=True)