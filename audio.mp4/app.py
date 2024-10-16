import yt_dlp  # type: ignore import para baixar coisas do youtube
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/executar', methods=['POST'])
def executar():
    videourl = request.form['video']
    downloadvideo(videourl)
    resultado = "Download e conversão concluídos!"
    return render_template('index.html', resultado=resultado)

def downloadvideo(videourl):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Baixa o melhor vídeo e o melhor áudio
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',  # Mescla o vídeo e o áudio em MP4
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Converte para MP4
        }],
        'postprocessor_args': [
            '-c:a', 'aac',  # Codec de áudio AAC
            '-b:a', '192k',  # Taxa de bits para o áudio
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([videourl])

if __name__ == '__main__':
    app.run(debug=True)
