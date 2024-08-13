import requests
import os
from dotenv import load_dotenv

from src.prompt import system_instruction
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage


# Load environment variables
load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')


def ask_order(user_message, instruction):
    
    model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True, verbose=True, temperature=0.9)
    
    
    respones=model(
    [
        SystemMessage(content=system_instruction),
        HumanMessage(content=user_message),
    ]
)
    
    return respones.content

if __name__=="__main__":
    user_message = input("Enter your message: ")
    respones=ask_order(user_message)
    print(respones)