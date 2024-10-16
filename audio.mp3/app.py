import yt_dlp  # type: ignore
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/executar', methods=['POST'])
def executar():
    videourl = request.form['video']
    downloadaudio(videourl)  
    resultado = "Download e conversão concluídos!"
    return render_template('index.html', resultado=resultado)

def downloadaudio(videourl, outputformat='mp3'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': outputformat,
        }],
        'outtmpl': '%(title)s.%(ext)s',  
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([videourl])

if __name__ == '__main__':
    app.run(debug=True)
