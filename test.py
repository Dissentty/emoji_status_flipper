import asyncio, os
from random import randint
from telethon import TelegramClient, functions, types
from dotenv import load_dotenv

load_dotenv()
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

statuses = [
    5404333301034927124,
    5839434146912407382,
    5246772116543512028,
    5247100325059370738,
    5404333301034927124
]

interval = 10

async def set_status(client, status_id):
    try:
        result = await client(functions.account.UpdateEmojiStatusRequest(
            emoji_status=types.EmojiStatus(
                document_id=status_id
            )
        ))
        print("Status update:", "ok" if result else "fail")
    except Exception as e:
        print("Error updating status:", e)

async def start_swapping():
    async with TelegramClient('anon', api_id, api_hash) as client:
        await client.start()
        while True:
            random_index = randint(0, len(statuses) - 1)
            print("Setting status to index:", random_index)
            await set_status(client, statuses[random_index])
            await asyncio.sleep(interval)

if __name__ == "__main__":
    asyncio.run(start_swapping())
