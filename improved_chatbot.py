import nltk
from nltk.chat.util import Chat, reflections


pairs =[
    ['hello' ,[' hey there how can i help you today?']],
    ['how are you', ['well, am just a bot, but am doing great']],
    ['name',[" am Mason,you ai bot assistant"]],
    ['exit',['goodbye!']]
]




chatbot =Chat(pairs,reflections)
chatbot.converse()
          
