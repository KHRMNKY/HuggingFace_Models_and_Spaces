from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
import gradio as gr
import os
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("api_key")

def youtube_url(url):
    
    """
    Function to retrieve the transcript of a YouTube video based on the provided URL.
    
    Parameters:
    url (str): The URL of the YouTube video.
    
    Returns:
    str: The transcript of the video.
    """

    transcript = ""
    list=url.split("=")
    video_id = list[1]
    list = YouTubeTranscriptApi.get_transcript(video_id, languages=['tr', 'en',"de"])
    for dict in list:
        transcript += dict["text"] + "\n"
    return transcript


def chat(prompt):

  """
  This function takes a prompt as input and uses the OpenAI API to generate a chat completion based on the prompt. It returns the summary of the chat completion.
  """

  system_msg = "you are a youtube transcript summarizer."

  client = OpenAI(api_key = api_key, base_url="https://api.deepseek.com/v1")

  completion = client.chat.completions.create(
  model="deepseek-chat",
  messages=[
      {"role": "system", "content": system_msg},
      {"role": "user", "content": prompt}
  ]
  )
  summary = completion.choices[0].message.content
  return summary


def main(url):

  """
  Function to summarize the transcript of a YouTube video using the provided URL.
  
  Parameters:
  url (str): The URL of the YouTube video.
  
  Returns:
  str: The summary of the video transcript.
  """
  
  transcript = youtube_url(url)
  query=f"summarize this {transcript} transcript"
  summary = chat(query)
  return summary


iface = gr.Interface(
    fn=main,
    inputs="text",
    outputs="text",
    
    title="Video Özeti Oluşturucu",
    description="Bir YouTube videosunun URL'sini girin ve özetini alın."
)

iface.launch(debug = True, share = True)
