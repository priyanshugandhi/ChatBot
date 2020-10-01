
# HelperBot

HelperBot(ChatBot) is a machine-learning based conversational dialog engine build in
Python which makes it possible to generate responses based on collections of
known conversations. The language independent design of ChatBot allows it
to be trained to speak any language.

The main aim of HelperBot is to help the humanbeing. To give him the required information that the person need.
It is effective because the person got the information easily and in a less time.

Today Chatbots are smarter,more responsive,more useful and we're likely to see even more of them in the coming years.

An example of typical input would be something like this:

> **user:** Good morning! How are you doing?  
> **bot:**  I am doing very well, thank you for asking.  
> **user:** You're welcome.  
> **bot:**  How can I help you?



## How Do HelperBots works

An untrained instance of ChatBot starts off with no knowledge of how to communicate. Each time a user enters a statement, the library saves the text that they entered and the text that the statement was in response to. As ChatBot receives more input the number of responses that it can reply and the accuracy of each response in relation to the input statement increase. The program selects the closest matching response by searching for the closest matching known statement that matches the input, it then returns the most likely response to that statement based on how frequently each response is issued by the people the bot communicates with.

