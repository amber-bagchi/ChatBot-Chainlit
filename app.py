import chainlit as cl
from src.llm import ask_order
from src.prompt import system_instruction

@cl.on_message
async def main(user_message:cl.Message):

    response=ask_order(user_message.content,system_instruction)
    
    # Send a response back to the user
    await cl.Message(
        content=f"Received: {response}",
    ).send()

