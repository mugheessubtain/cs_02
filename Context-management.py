from agents import Agent,Runner,function_tool,RunContextWrapper
from my_config.config import llm_model
import asyncio
from dataclasses import dataclass


@dataclass
class BookContext:
    title: str
    author: str
    year: int

    
# @function_tool
# async def summary_generator(ctx:RunContextWrapper[BookContext],agent:Agent)->str:
#     """"Generate Summary of the book name from the context"""
#     return f"The Book name is '{ctx.context.title}' by {ctx.context.author}, published in {ctx.context.year}.Summary is {agent.final_output if agent.final_output else 'No summary available yet.'}"

<<<<<<< HEAD
def dynammic_instructions(ctx:RunContextWrapper[BookContext],agent:Agent[BookContext])->str:
=======
def dynammic_instructions(ctx:RunContextWrapper[BookContext],agent:Agent)->str:
>>>>>>> 14d3ad9909952ed792e0060b323a761ea7ef8502
    return f"You are a summary generator for the book '{ctx.context.title}' by {ctx.context.author}, published in {ctx.context.year}. Provide a concise summary."
async def main():
    book=BookContext(
        title="Rich Dad Poor Dad",
        author="Robert T. Kiyosaki",
        year=1997
    )
<<<<<<< HEAD
    context_writer=Agent[BookContext](
=======
    context_writer=Agent(
>>>>>>> 14d3ad9909952ed792e0060b323a761ea7ef8502
        name="Assistant agent",
        instructions=dynammic_instructions,
        model=llm_model,
        # tools=[summary_generator]
    )

    result=await Runner.run(
        context_writer,
        input="Write a short summary of the book ?",
        context=book,
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())



