# tanimlamalar 
from flask import Flask, render_template, request , send_file
from gtts import gTTS
import os

# flaskin icindeki bu zimbirtiyi routerlari kullanmak ve de portu calistirmak icin cagiriyorum(opsiyonel)
app = Flask(__name__)
# router

 #ana sayfa
@app.route('/')
def index():
    return render_template('index.html', audio_file=None)

  #istek attiktan sonra vesselam 
@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    tts = gTTS(text)
    tts.save('static/output.mp3')
    return render_template('index.html', audio_file='output.mp3')

  #dosyayi oynatma
@app.route('/play')
def play():
    return send_file('static/output.mp3')

  # dosyayi indirme
@app.route('/download')
def download():
    return send_file('static/output.mp3', as_attachment=True)
  

  #portta calistirma
app.run(host='0.0.0.0', port=81)
