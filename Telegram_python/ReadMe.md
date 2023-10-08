# Telegram Bot Using RestClient

This Python script demonstrates how to interact with the Telegram Bot API.

## Prerequisites

Before using this script, ensure you have the following:

- Python installed on your system.
- Install required libraries: 
```python
  pip install -r requirements.txt
```
## Usage

1. Clone this repository or download the `TelegramBot.py` file.

2. Update `credentials.py` file:

   ```python
   # credentials.py

   class TelegramCredentials:
       token = 'YOUR_BOT_TOKEN'
       chat_id = 'YOUR_CHAT_ID'
   ```
3. Use `TelegramBot.py` as following:
   ```python
    if __name__ == '__main__':
        bot = TelegramBot()

        bot.sendMessage('Hello, World!')
        bot.sendPhoto('/home/Desktop/test.jpg')
   ```
## Functions
1. `sendMessage(text)` Send a text message via the Telegram Bot API.
2. `sendDocument(document_path, caption='')` Send a document via the Telegram Bot API.
3. `sendPhoto(photo_path, caption='')` Send a photo via the Telegram Bot API.


## Credits
This script uses the RestClient library for making HTTP requests to the Telegram Bot API.

## License
This project is licensed under the MIT License - see the LICENSE file for details.