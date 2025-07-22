import chainlit as cl
from engine.langgraph_engine import run_engine

@cl.on_message
async def on_message(message: cl.Message):
    user_prompt = message.content
    result = await run_engine(user_prompt)
    await cl.Message(content=result).send()