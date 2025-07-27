import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot pairs (patterns and responses)
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I am an AI chatbot created using NLTK."]
    ],
    [
        r"how are you ?",
        ["I'm doing great! How can I assist you today?"]
    ],
    [
        r"(.*) your creator?",
        ["I was created as part of a CodTech internship project."]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye!", "See you later!", "Bye! Have a nice day!"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Can you rephrase it?"]
    ]
]

# Create and start the chatbot
def chatbot():
    print("Welcome to CodTech NLP Chatbot! (Type 'quit' to exit)")
    chat = Chat(pairs, reflections)
    chat.converse()

chatbot()
