from flask import Flask, render_template, request, redirect, url_for
import mail


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(debug=True)