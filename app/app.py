
import chainlit as cl
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

llm = ChatOllama(model="llama3:8b")

@cl.on_message
async def main(message: cl.Message):
	# Stream response from Ollama
	msg = cl.Message(content="")
	await msg.send()
	async for chunk in llm.astream([HumanMessage(content=message.content)]):
		if hasattr(chunk, "content") and chunk.content:
			await msg.stream_token(chunk.content)
