import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')  # Download necessary NLTK data

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?",]
    ],

    [
        r"can you help me with the job?" ?",
        ["yes i can help you.what field you want to choose?",]
    ],

    
    [
        r"sorry (.*)",
        ["It's alright", "No problem",]
    ],
    [
        r"I am fine",
        ["Great to hear that!", "Awesome, how can I help you?",]
    ],
    [
        r"quit",
        ["Bye! Take care.",]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that. Can you please rephrase?",]
    ],
]

class Chatbot:
    def __init__(self, pairs, reflections):
        self.chat = Chat(pairs, reflections)
    
    def start(self):
        print("Hi, I am a chatbot. How can I help you today?")
        while True:
            user_input = input("> ")
            if user_input.lower() == "quit":
                print("Bye! Take care.")
                break
            response = self.chat.respond(user_input)
            print(response)

# Create a chatbot instance and start the conversation
chatbot = Chatbot(pairs, reflections)
chatbot.start()
