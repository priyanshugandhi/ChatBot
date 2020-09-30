
# ChatBot

ChatBot is a machine-learning based conversational dialog engine build in
Python which makes it possible to generate responses based on collections of
known conversations. The language independent design of ChatBot allows it
to be trained to speak any language.


An example of typical input would be something like this:

> **user:** Good morning! How are you doing?  
> **bot:**  I am doing very well, thank you for asking.  
> **user:** You're welcome.  
> **bot:**  How can I help you?


# 10 of the Most Innovative Chatbots on the Web 

 1. Endurance: A Companion for Dementia Patients
 2. Casper: Helping Insomniacs Get Through the Night
 3. Disney: Solving Crimes with Fictional Characters
 4. Marvel: Guarding the Galaxy with Comic-Book Crossovers
 5. UNICEF: Helping Marginalized Communities Be Heard
 6. MedWhat: Making Medical Diagnoses Faster
 7. Roof Ai: Generating and Assigning Leads Automatically
 8. NBC: Helping Newshounds Navigate the Headlines
 9. Unilever: Raising Awareness with Brand Mascots
 10. ALICE: The Bot That Launched a Thousand… Other Bots
 
## How it works

An untrained instance of ChatBot starts off with no knowledge of how to communicate. Each time a user enters a statement, the library saves the text that they entered and the text that the statement was in response to. As ChatBot receives more input the number of responses that it can reply and the accuracy of each response in relation to the input statement increase. The program selects the closest matching response by searching for the closest matching known statement that matches the input, it then returns the most likely response to that statement based on how frequently each response is issued by the people the bot communicates with.

