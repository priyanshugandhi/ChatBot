
# ChatBot

ChatBot is a machine-learning based conversational dialog engine build in
Python which makes it possible to generate responses based on collections of
known conversations. The language independent design of ChatBot allows it
to be trained to speak any language.


An example of typical input would be something like this:

> **User:** Good morning! How are you doing?  
> **Bot:**  I am doing very well, thank you for asking.  
> **User:** You're welcome.  
> **Bot:**  How can I help you?



## How it works

An untrained instance of ChatBot starts off with no knowledge of how to communicate. Each time a user enters a statement, the library saves the text that they entered and the text that the statement was in response to. As ChatBot receives more input the number of responses that it can reply and the accuracy of each response in relation to the input statement increase. The program selects the closest matching response by searching for the closest matching known statement that matches the input, it then returns the most likely response to that statement based on how frequently each response is issued by the people the bot communicates with.

