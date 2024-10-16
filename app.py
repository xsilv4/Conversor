import os
from tkinter import *
import yt_dlp

#caminho da área de downloads 
if os.name == 'nt':  # Para Windows
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

def downloadvideo():
    videourl = url_video.get()  # Pega a URL do vídeo
    quality = video_quality.get()  # Pega a qualidade selecionada
    if videourl:
        # Define a qualidade com base na seleção do usuário
        if quality == '1080p':
            video_format = 'bestvideo[height<=1080]'
        else:  # '144p'
            video_format = 'worstvideo[height<=144]'

        ydl_opts = {
            'format': f'{video_format}+bestaudio/best',  # Mantém o melhor áudio disponível
            'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),  # Direciona o download para a área de downloads
            'merge_output_format': 'mp4',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
            'postprocessor_args': [
                '-c:a', 'aac',
                '-b:a', '192k',
            ],
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([videourl])
            texto_resultado['text'] = 'Download de vídeo concluído!'
        except Exception as e:
            texto_resultado['text'] = f"Erro: {e}"

def downloadaudio():
    musicaurl = url_musica.get()  # Pega a URL da música
    if musicaurl:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
            'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),  # Direciona o download para a área de downloads
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([musicaurl])
            texto_resultado['text'] = 'Download de áudio concluído!'
        except Exception as e:
            texto_resultado['text'] = f"Erro: {e}"

janela = Tk()
janela.title('Downloader Video e Música')
janela.geometry('600x400')
janela.config(bg='#6a89ba')

# Seção de download de vídeo
texto_orientacao = Label(janela, text="Digite a URL para download do vídeo:", bg='#6a89ba', font=('Times New Roman', 16)) 
texto_orientacao.grid(column=2, row=1)

url_video = Entry(janela, width=50)
url_video.grid(column=2, row=2, padx=10, pady=10)

# Opções de qualidade de vídeo
video_quality = StringVar(value='1080p')  # Qualidade padrão
Label(janela, text="Escolha a qualidade do vídeo:", bg='#6a89ba').grid(column=2, row=3)
OptionMenu(janela, video_quality, '1080p', '144p').grid(column=2, row=4)

download_video = Button(janela, text='Download Vídeo', bg='#D3D3D3', command=downloadvideo)
download_video.grid(column=2, row=5, padx=250, pady=10)

# Seção de download de música
texto_orientacao2 = Label(janela, text="Digite a URL para download da música:", bg='#6a89ba', font=('Times New Roman', 16))
texto_orientacao2.grid(column=2, row=6, pady=20)

url_musica = Entry(janela, width=50)
url_musica.grid(column=2, row=7)

download_musica = Button(janela, text='Download Música', bg='#D3D3D3', command=downloadaudio)
download_musica.grid(column=2, row=8, pady=12)

# Exibe o resultado
texto_resultado = Label(janela, text='', bg='#6a89ba')
texto_resultado.grid(column=2, row=9, pady=13)

janela.mainloop()
