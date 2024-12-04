# Twitch FAQ Bot

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/yourusername/twitch-faq-bot/CI)
![License](https://img.shields.io/github/license/yourusername/twitch-faq-bot)
![Stars](https://img.shields.io/github/stars/yourusername/twitch-faq-bot?style=social)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview

Twitch FAQ Bot is a Python-based chatbot designed to enhance your Twitch channel's interactivity by automatically responding to frequently asked questions (FAQs) using OpenAI's GPT-4. When a viewer asks a question similar to predefined FAQs, the bot responds with a relevant YouTube video link(advertisement), providing quick and consistent answers without interrupting your stream.

## Features

- **Automated FAQ Responses:** Uses GPT-4 to determine if a message matches predefined FAQs.
- **Customizable FAQ List:** Easily update the list of frequently asked questions.
- **Seamless Integration:** Built with TwitchIO for smooth integration with Twitch chat.
- **AI-Powered Understanding:** Leverages OpenAI's GPT-4 for accurate message similarity detection.
- **Easy Configuration:** Simple setup for API keys and tokens.

## Demo

![Twitch FAQ Bot Demo](https://www.example.com/demo-screenshot.png)

*Watch the bot in action on our [YouTube Channel](https://www.youtube.com/watch?v=LKRkqZsGvGM&ab_channel=TheNumberOneLLC).*

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.7 or higher** is installed on your machine. You can download it [here](https://www.python.org/downloads/).
- **Twitch account** with the ability to create a bot.
- **OpenAI API key**. Sign up or log in to [OpenAI](https://platform.openai.com/) to obtain your API key.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/twitch-faq-bot.git
   cd twitch-faq-bot
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   *If you don't have a `requirements.txt`, you can install the necessary packages manually:*

   ```bash
   pip install openai twitchio
   ```

## Configuration

1. **Set Up API Keys and Tokens**

   Open the `main.py` file and replace the placeholder strings with your actual credentials:

   ```python
   # Set your API keys here
   TWITCH_TOKEN = 'your_twitch_oauth_token'
   TWITCH_CLIENT_ID = 'your_twitch_client_id'
   OPENAI_API_KEY = 'your_openai_api_key'
   ```

   - **Twitch Token:** You can generate an OAuth token [here](https://twitchapps.com/tmi/).
   - **Twitch Client ID:** Obtain this from your [Twitch Developer Console](https://dev.twitch.tv/console).
   - **OpenAI API Key:** Available in your [OpenAI account](https://platform.openai.com/account/api-keys).

2. **Customize FAQs and Response**

   Modify the `faq_list` and `video_link` variables in `main.py` to suit your channel's needs:

   ```python
   # List of frequently asked questions and the video link
   faq_list = [
       "What is a good credit score?",
       "How do I get good credit?",
       "What credit do I need for a loan?",
       "How do I remove negative items from my credit report?"
   ]
   video_link = "https://www.youtube.com/watch?v=LKRkqZsGvGM&ab_channel=TheNumberOneLLC"
   ```

## Usage

Run the bot using the following command:

```bash
python main.py
```

Upon successful launch, you should see a message indicating that the bot has logged in. The bot will now monitor your Twitch chat and respond to messages that match your FAQs with the specified YouTube video link.

## Contributing

Contributions are welcome! If you'd like to contribute to Twitch FAQ Bot, please follow these steps:

1. **Fork the Repository**

2. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add YourFeature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

Please ensure your contributions adhere to the [code of conduct](https://github.com/yourusername/twitch-faq-bot/blob/main/CODE_OF_CONDUCT.md) and follow the project's coding standards.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the [LICENSE](https://github.com/yourusername/twitch-faq-bot/blob/main/LICENSE) file for details.

## Acknowledgements

- [TwitchIO](https://github.com/TwitchIO/TwitchIO) - An asynchronous Python wrapper for the Twitch API.
- [OpenAI](https://openai.com/) - For providing the powerful GPT-4 language model.
- [TheNumberOneLLC](https://www.youtube.com/channel/TheNumberOneLLC) - Inspiration for the video content.

---

*Feel free to reach out via [GitHub Issues](https://github.com/yourusername/twitch-faq-bot/issues) for any questions or support.*

# Full Code

Create a file named `main.py` and paste the following code:

```python
import os
import openai
from twitchio.ext import commands

# Set your API keys here
TWITCH_TOKEN = 'TWITCH_TOKEN'
TWITCH_CLIENT_ID = 'TWITCH_CLIENT_ID'
OPENAI_API_KEY = 'OPENAI_API_KEY'

openai.api_key = OPENAI_API_KEY

# List of frequently asked questions and the video link
faq_list = [
    "What is a good credit score?",
    "How do I get good credit?",
    "What credit do I need for a loan?",
    "How do I remove negative items from my credit report?"
]
video_link = "https://www.youtube.com/watch?v=LKRkqZsGvGM&ab_channel=TheNumberOneLLC"

# Function to check if a message is similar to any of the frequently asked questions using GPT-4
def is_similar_to_faq(message):
    prompt = f"Is the following message similar to any of these frequently asked questions?\n\nFAQs:\n" \
             f"1. {faq_list[0]}\n" \
             f"2. {faq_list[1]}\n" \
             f"3. {faq_list[2]}\n" \
             f"4. {faq_list[3]}\n\n" \
             f"Message: {message}\n\n" \
             f"Respond with 'yes' or 'no'."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=10,
        temperature=0.0,
    )
    return response.choices[0].message['content'].strip().lower() == 'yes'

# Define a function to get a response from GPT-4 using the chat endpoint
def get_gpt4_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].message['content'].strip()

# Create a bot class using TwitchIO
class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=TWITCH_TOKEN, prefix='!', initial_channels=['Cabdru'])

    async def event_ready(self):
        print(f'Logged in as {self.nick}')

    async def event_message(self, message):
        if message.author.name.lower() == self.nick.lower():
            return

        # Check if the message is similar to any FAQ
        if is_similar_to_faq(message.content):
            await message.channel.send(video_link)
            return

# Run the bot
bot = Bot()
bot.run()
```

---

Create a `requirements.txt` file to manage your dependencies:

```
openai
twitchio
```

# Getting Started

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/twitch-faq-bot.git
   cd twitch-faq-bot
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys**

   - Open `main.py` and replace the placeholder strings with your actual `TWITCH_TOKEN`, `TWITCH_CLIENT_ID`, and `OPENAI_API_KEY`.

4. **Run the Bot**

   ```bash
   python main.py
   ```

Your Twitch FAQ Bot should now be up and running, ready to assist your viewers with their frequently asked questions!
