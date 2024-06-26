import os 
import sys
import base64
import datetime
from gtts import gTTS
from text_to_speech.constants import *
from text_to_speech.entity.config_entity import TTSConfig
from text_to_speech.logging import logger
from text_to_speech.exceptions import TTSException


class TTSapplication:
    def __init_(self, app_config=TTSConfig()):
        """
        Initializs the application by loading the application configurartion.
        """
        try:
            self.app_config = app_config
            self.artifact_dir = app_config.artifact_dir
            self.audio_dir = app_config.audio_dir
            self.text_dir = app_config.text_dir

            logger.info(f"Loaded all application configurations")
        except Exception as e:
            raise TTSException(e,sys) from e
        

    def text2Speech(self, text, accent):
        """
        It takes in a text string and an accent, writes the string to a text file, creates a gTTS object,
        saves the gTTS object as a mp3 file, and then returns the mp3 file as a base64 encoded string.

        Args:
            data: The text that you want to convert to speech.
            accent: This is the accent of the voice

        Returns:
            The return value is the base64 encoded string
        """

        try:
            
            text_filename = TEXT_FILENAME
            text_file_path = os.path.join(self.text_dir, TEXT_FILENAME)
            #os.makedirs(self.text_dir, exist_ok=True)
            with open(text_file_path, "+a") as file:
                file.write(f'\n{text}')

            # Create object for text to speech
            tts = gTTS(text=text, lang='en', slow=False, tld=accent)

            

            filename = f"converted_file_{CURRENT_TIME_STAMP}.mp3"
            #os.makedirs(self.audio_dir, exist_ok=True)
            audio_path = os.path.join(self.audio_dir, filename)

            # save tts object as mp3
            tts.save(audio_path)

            with open(audio_path, "rb") as file:
                my_string = base64.b64encode(file.read())
            return my_string
        except Exception as e:
            raise TTSException(e, sys)from e