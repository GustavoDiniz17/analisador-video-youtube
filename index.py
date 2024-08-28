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