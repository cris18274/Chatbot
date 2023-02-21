from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the English corpus
trainer.train("chatterbot.corpus.english")

# Start a conversation with the chatbot
print("Hello, I am your AI ChatBot. Ask me anything!")
while True:
    try:
        user_input = input("You: ")
        bot_response = chatbot.get_response(user_input)
        print("Bot: ", bot_response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
