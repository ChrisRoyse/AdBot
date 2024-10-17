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

        # Process !ask command with GPT-4
        if message.content.startswith('!ask'):
            prompt = message.content[5:]  # Remove the command part
            response = get_gpt4_response(prompt)
            await message.channel.send(response)

# Run the bot
bot = Bot()
bot.run()
