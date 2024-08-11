from openai import OpenAI
from dotenv import load_dotenv, find_dotenv, dotenv_values
from pathlib import Path

config = dotenv_values(find_dotenv())

class OpenAIClient:
    def __init__(self) -> None:
        self.client = OpenAI(
            api_key=config.get("OPENAI_API_KEY"),
        )

    def chat(self, messages, json_mode, model="gpt-4o", temperature=1):
        if json_mode:
            chat_completion = self.client.chat.completions.create(
                messages=messages,
                model=model,
                response_format={"type": "json_object"},
                temperature=temperature
            )
        else:
            chat_completion = self.client.chat.completions.create(
                messages=messages,
                model=model,
                temperature=temperature
            )
        response = chat_completion.choices[0].message.content
        return response

    def get_embedding(self, text: str, model="text-embedding-ada-002"):
        text = text.replace("\n", " ")
        resp = self.client.embeddings.create(input=[text], model=model)
        return resp.data[0].embedding
    
    def output_narration_voice(self, input_text, openai_voice = 'onyx'):
        """creates an mp3 file called "speech.mp3" into local dir from input text and openai voice chosen

        Args:
            input_text (_type_): what is narrated
            openai_voice (str, optional): _description_. Defaults to 'onyx'.
        """

        #! https://platform.openai.com/docs/guides/text-to-speech/streaming-real-time-audio
        #! for real-time streaming
        
        speech_file_path = Path('__file__').parent / "speech.mp3"

        response = self.client.audio.speech.create(
            model="tts-1",
            voice=openai_voice,
            input=input_text
        )
        response.stream_to_file(speech_file_path)
        return response