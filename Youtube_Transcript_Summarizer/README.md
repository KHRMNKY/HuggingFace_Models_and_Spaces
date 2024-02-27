# Video Summary Generator

This project retrieves the transcript of a YouTube video based on its URL and then summarizes the transcript using the Deepseek coder API. Users can input a YouTube video URL to obtain a summary of the video.

## How to Run

1. Clone this project locally:

    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd Youtube_Transcript_Summarizer
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3.Add your Deepseek coder API key to the `.env` file:
    
    ```
    api_key=your_openai_api_key 

    ```

4. Run the application:

    ```bash
    python app.py
    ```


## Usage

1. Upon starting the application, you'll see a text box under the "Enter Video URL" heading.
2. Paste the URL of the YouTube video into the text box.
3. Click the "Summarize" button.
4. The application will retrieve the video transcript and then generate a summary using the OpenAI API.
5. The result will appear under the "Summary" heading.

## Deepseek coder api

To access the Hugging Face interface for this project, use the following link:

[for taking your api key](https://platform.deepseek.com/api_keys)


## Hugging Face Interface

To access the Hugging Face interface for this project, use the following link:

[Hugging Face Interface](https://huggingface.co/spaces/KAHRAMAN42/youtube_transcript)



