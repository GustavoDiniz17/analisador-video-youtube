import os
import pytube
import ffmpeg
import openai
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import os
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv('API_TOKEN')

def download_youtube_video(url, output_path='video.mp4'):
    yt = pytube.YouTube(url)
    stream = yt.streams.get_highest_resolution()
    print(f"Baixando o vídeo: {stream.title}")
    stream.download(filename=output_path)

def extract_audio_from_video(video_path, audio_path='audio.wav'):
    print("Extraindo áudio...")
    ffmpeg_extract_audio(video_path, audio_path)

def transcribe_audio(audio_path):
    with open(audio_path, 'rb') as audio_file:
        transcription = openai.Audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcription['text']

def summarize_text(text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Resuma o seguinte texto:\n\n{text}",
        max_tokens=150
    )
    return response.choices[0].text.strip()
def main():
    video_url = input("Insira a URL do vídeo do YouTube: ")
    
    # Baixar o vídeo
    download_youtube_video(video_url)
    
    # Extrair áudio do vídeo
    extract_audio_from_video('video.mp4', 'audio.wav')
    
    # Transcrever o áudio
    transcript = transcribe_audio('audio.wav')
    
    # Resumir o texto
    summary = summarize_text(transcript)
    
    # Mostrar o resumo
    print("\nResumo do vídeo:")
    print(summary)
    
    # Limpar arquivos temporários
    os.remove('video.mp4')
    os.remove('audio.wav')

if _name_ == '_main_':
    main()
    