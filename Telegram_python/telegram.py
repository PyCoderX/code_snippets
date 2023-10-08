from RestClient import RestClient
from credentials import TelegramCredentials


client = RestClient()  # Create an instance of the RestClient


class TelegramBot():
    """
    A class for interacting with the Telegram Bot API using TelegramCredentials.

    Attributes:
        base_url (str): The base URL for making API requests.
    """

    def __init__(self):

        # API
        self.base_url = f'https://api.telegram.org/bot{TelegramCredentials.token}/'

    @client.request
    def sendMessage(self, text):
        """
        Send a text message via the Telegram Bot API.

        Args:
            text (str): The text of the message.

        Returns:
            dict: The API request parameters.
        """
        inputs = {
            'method': 'POST',
            'url': f'{self.base_url}sendMessage',
            'params': {'chat_id': TelegramCredentials.chat_id, 'text': text}
        }
        return inputs

    @client.request
    def sendDocument(self, document_path, caption=''):
        """
        Send a document via the Telegram Bot API.

        Args:
            document_path (str): The path to the document file.
            caption (str, optional): The caption for the document (default is '').

        Returns:
            dict: The API request parameters.
        """
        try:
            inputs = {
                'method': 'POST',
                'url': f'{self.base_url}sendDocument',
                'params': {'chat_id': TelegramCredentials.chat_id, 'caption': caption},
                'files': {'document': open(document_path, 'rb')}
            }
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {str(e)}")
        except Exception as e:
            raise e
        return inputs

    @client.request
    def sendPhoto(self, photo_path, caption=''):
        """
        Send a photo via the Telegram Bot API.

        Args:
            photo_path (str): The path to the photo file.
            caption (str, optional): The caption for the photo (default is '').

        Returns:
            dict: The API request parameters.
        """
        try:
            inputs = {
                'method': 'POST',
                'url': f'{self.base_url}sendPhoto',
                'params': {'chat_id': TelegramCredentials.chat_id, 'caption': caption},
                'files': {'photo': open(photo_path, 'rb')}
            }
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {str(e)}")
        except Exception as e:
            raise e
        return inputs



