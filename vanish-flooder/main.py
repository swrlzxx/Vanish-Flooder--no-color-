from assets import *
from assets.utility.util import *

async def spam(token, uid, message, count, rs, rm, em):
    inte = discord.Intents.all()
    client = discord.Client(intents=inte)

    @client.event
    async def on_ready():
        print(f"Logged in as {client.user.name}")
        await asyncio.sleep(1)
        tar = await client.fetch_user(int(uid))

        for _ in range(count):
            try:
                msg = message
                if rs:
                    msg += " -> " + ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=25))

                if rm:
                    msg += " -> " + ' '.join(random.choices(emojis, k=em))

                await tar.send(msg)
                await asyncio.sleep(0.5)
                print(f"Sent DM ~ {message} ({client.user.name})")

            except discord.Forbidden:
                print(f"{tar.name} DMs are closed ({client.user.name})")
                continue

    await client.start(token)

async def main():
    tokens = load_tokens()
    print(f"Loaded {len(tokens)} tokens")
    option = input("Choice? 1 for dm spam. 2 for exiting: ")

    if option == "1":
        tokens = open('input/tokens.txt', 'r').read().splitlines()

        uid = input("User Id: ")
        if not uid:
            await main()
        message = input("Message: ")
        if not message:
            await main()
        count = int(input("Amount: "))
        if not count:
            await main()        
        rs = input("Random String (y/n): ").strip().lower() == 'y'
        if rs == '':
            await main()        
        rm = input("Random Emojis (y/n): ").strip().lower() == 'y'
        if rm == '':
            await main()
        em = 5
        if rm:
            em = int(input("Emoji Amount: "))
        if em == '':
            await main()

        tasks = [spam(token, uid, message, count, rs, rm, em) for token in tokens]
        await asyncio.gather(*tasks)

    elif option == "2":
        print('Exiting...')
        exit()

if __name__ == "__main__":
    asyncio.run(main())
