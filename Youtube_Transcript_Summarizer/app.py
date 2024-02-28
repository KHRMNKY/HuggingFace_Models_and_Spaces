from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
import argparse


def parse_args():
  """
  A function to parse command-line arguments for the API key, model, and URL.
  Returns the parsed arguments.

  Returns:
  argparse.Namespace: The parsed arguments.
  """

  parser = argparse.ArgumentParser()
  parser.add_argument(
    dest = "api_key",
    type = str,
    help = "OpenAI api key or Deepseek coder api key"
  )

  parser.add_argument(
    dest = "model",
    type = str,
    help = "OpenAI model to use for summarization"
  )
  
  parser.add_argument(
    dest = "url",
    type = str,
    help = "YouTube video URL"
  )

  return parser.parse_args()


args = parse_args()
api_key = args.api_key
url = args.url
model = args.model


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



def summarization(prompt):
  """
  This function takes a prompt as input and uses the OpenAI API to generate a chat completion based on the prompt. It returns the summary of the chat completion.
  """

  system_msg = "you are a youtube transcript summarizer."
  

  if model == "deepseek-chat":
    base_url = "https://api.deepseek.com/v1"


  else:
    base_url = None

  client = OpenAI(api_key = api_key, base_url=base_url)
  completion = client.chat.completions.create(
    model = model,
    messages=[
      {"role": "system", "content": system_msg},
      {"role": "user", "content": prompt}
    ]
  )

  summary = completion.choices[0].message.content
  return summary



def main(url):
  """
  Function to
  summarize the transcript of a YouTube video using the provided URL.
  
  Parameters:
  url (str): The URL of the YouTube video.
  
  Returns:
  str: The summary of the video transcript.
  """

  transcript = youtube_url(url)
  query=f"summarize this {transcript} transcript"
  summary = summarization(query)
  return summary


if __name__ == "__main__":
    print(main(url))
