
# ChatBot

ChatBot is a machine-learning based conversational dialog engine build in
Python which makes it possible to generate responses based on collections of
known conversations. The language independent design of ChatBot allows it
to be trained to speak any language.


An example of typical input would be something like this:

> **user:** Good morning! How are you doing?  
> **bot:**  I am doing very well, thank you for asking.  
> **user:** You're welcome.  
> **bot:** Do you like hats?  

## How it works

An untrained instance of ChatBot starts off with no knowledge of how to communicate. Each time a user enters a statement, the library saves the text that they entered and the text that the statement was in response to. As ChatBot receives more input the number of responses that it can reply and the accuracy of each response in relation to the input statement increase. The program selects the closest matching response by searching for the closest matching known statement that matches the input, it then returns the most likely response to that statement based on how frequently each response is issued by the people the bot communicates with.


## Basic Usage

```
from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")
```

# Training data

ChatBot comes with a data utility module that can be used to train chat bots.
At the moment there is three languages, English, Spanish and Portuguese training data in this module. Contributions
of additional training data or training data in other languages would be greatly
appreciated. 

```
# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# Train based on english greetings corpus
chatbot.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
chatbot.train("chatterbot.corpus.english.conversations")
```



