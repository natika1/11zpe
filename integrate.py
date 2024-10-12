import os
import uuid
import requests
import json
from dotenv import load_dotenv
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

load_dotenv()

ELEVENLABS_API_KEY = "sk_f55dae6021ac30c7e36b2ef2e48c7101902f6930836ac947"

if not ELEVENLABS_API_KEY:
    raise ValueError("ELEVENLABS_API_KEY environment variable not set")

client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)



def get_posts():
    url = 'https://zpe.gov.pl/api/v1/document/D13MQOOrz/content'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:Cannot fetch the data', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None
    

def main() -> int:
       return 0        


if __name__ == '__main__':
    main()



def text_to_speech_file(text: str) -> str:
    """
    Converts text to speech and saves the output as an MP3 file.

    This function uses a specific client for text-to-speech conversion. It configures
    various parameters for the voice output and saves the resulting audio stream to an
    MP3 file with a unique name.

    Args:
        text (str): The text content to convert to speech.

    Returns:
        str: The file path where the audio file has been saved.
    """
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="S1JKkpuAQNsowB8ZvKRO",  # voice of Damian PL
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2",  # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # Generating a unique file name for the output MP3 file
    save_file_path = f"{uuid.uuid4()}.mp3"
    # Writing the audio stream to the file

    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"A new audio file was saved successfully at {save_file_path}")

    # Return the path of the saved audio file
    return save_file_path


if __name__ == "__main__":
        posts = get_posts()

        if posts:
             posts_string = json.dumps(posts)
             print(posts_string[2])
             docContain = json.loads(posts_string)
             
             #docContain[:docContain.index("section1")]

        else:
             print('Failed to fetch posts from API.')

        if posts:
            print("Here should be all to API for Audio transcription of text")
            #print(docContain)
            text_to_speech_file("Witaj świecie, może razem uda się ulepszyć Polską platformę edukacyjną!")
            #text_to_speech_file([posts_string])

            
