from chatterbot import ChatBot # imports the constructor of the chatbot
from chatterbot.trainers import ListTrainer # responsible for allowing the usage of a list of strings
                                            # in the learning process


bot = ChatBot("My First Bot") # Initializes Chatbot and sets an alias

"""
Register 3 questions. Each answer refers to the previous item of the list. 
E.g.: "Fine" is the answer to the question "How are you doing?, and so on." 
"""
conversation = ["Hi", "Hello", "How are you doing?", "Fine", 
                "Do you like programming?", "Yes, I program in python"]

trainer = ListTrainer(bot) # Create a new trainer for the chatbot

trainer.train(conversation) # sets "conversation" as starting point for the Bot's learning

"""
Creation of an infinite loop that will capture an user's question.
Sets a confidence grade for answers. If it's lower than 0.5 the Bot is going to inform that
it doesn't know how to answer the respective question.
"""
while True:
    question = input("User: ")
    answer = bot.get_response(question)
    if float(answer.confidence) > 0.5:
        print("My First Bot: ", answer)
    else:
        print("My First Bot: I still don't know how to answer that question")