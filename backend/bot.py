# bot.py
from interactions import Client, Intents, slash_command, SlashContext, listen,slash_option,OptionType
from dotenv import load_dotenv
import os
import logging
import sys

from querying import data_querying
from manage_embedding import update_index


load_dotenv()
logging.basicConfig(stream=sys.stdout, level= logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

bot = Client(intents=Intents.ALL)


@listen()
async def on_ready():
    print("Ready")


@slash_command(name="query", description="Enter your question :)")
@slash_option(
    name="input_text",
    description="input text",
    required=True,
    opt_type=OptionType.STRING,
)

async def get_response(ctx: SlashContext, input_text: str):
    """from provided SlashContext with user input, send response from querying index

    Args:
        ctx (SlashContext): _description_
        input_text (str): _description_
    """
    await ctx.defer()
    response = await data_querying(input_text)
    response = f'**Input Query**: {input_text}\n\n{response}'
    await ctx.send(response)




# @slash_command(name="updatedb", description="Update your information database :)")
# async def updated_database(ctx: SlashContext):
#     """allows update of index from database

#     Args:
#         ctx (SlashContext): _description_
#     """
#     await ctx.defer()
#     update = await update_index()
#     if update:
#         response = f'Updated {sum(update)} document chunks'
#     else:
#         response = f'Error updating index'
#     await ctx.send(response)

def main():
    if "DISCORD_BOT_TOKEN" in os.environ:
        logging.info("Found DISCORD_BOT_TOKEN")
    if "OPENAI_API_KEY" in os.environ:
        logging.info("Found OPENAI_API_KEY")
    bot.start(os.getenv("DISCORD_BOT_TOKEN"))

if __name__ == '__main__':
    main()
