from pydantic_ai import Agent
import asyncio
from pydantic_ai.models.anthropic import AnthropicModel
from dotenv import load_dotenv
import os

#Load variable from .env
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

anthropic_model = AnthropicModel("claude-3-5-sonnet-latest")

#Model Selection
basic_agent = Agent(
    system_prompt='You are a helpful e-commerce support agent. Be concise and friendly.',
    model=anthropic_model
)

#Example Run 1: Synchronous Execution
prompt= "Say hello to the customer and ask how you can help with their order today."
print("\n=== Synchronous Execution===")
result = basic_agent.run_sync(prompt)
print(result.output)

#Example 2: Asynchronous execution (method 1- inside async function)
print("\n=== Asynchronous Execution===")
async def run_async():
    result= await basic_agent.run(prompt)
    print(result.output)

asyncio.run(run_async())

#Example 3: Asynchronous execution (method 2- using asyncio.run directly)
print("\n===Asynchronous Execution Method 2===")
result = asyncio.run(basic_agent.run(prompt))
print(result.output)