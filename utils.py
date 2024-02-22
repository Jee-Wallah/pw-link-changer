from telethon.tl.types import ReplyKeyboardMarkup, KeyboardButtonRow, KeyboardButton
from telethon.tl.custom import Button


async def link_gen(link_hash, bot, event):
    async with bot.conversation(event.chat_id, timeout=200) as conv:
        try:
            await conv.send_message(
            'Choose quality',   
            buttons = ReplyKeyboardMarkup(
                rows=[
                    KeyboardButtonRow(
                        buttons=[
                            KeyboardButton(text="240"),
                            KeyboardButton(text="360"),
                            KeyboardButton(text="480"),
                            KeyboardButton(text="720"),
                        ]
                    )
                ],
                resize=True,
                persistent=True,
                placeholder="Choose quality"
            ))

            quality = await conv.get_response()
            await conv.send_message(
                "Give name of the lecture",
                buttons = Button.clear()
            )
            name = await conv.get_response()
            new_link = f"""
Here is your new link: 
`/yld https://psitoffers.store/testkey.php?vid={link_hash}&quality={quality.raw_text} -n {name.raw_text}`
    """
                        
            await conv.send_message(
                new_link
                
            )

        except TimeoutError:
            await event.respond(
                f"Timed out, try again",
                buttons = Button.clear()
                
            )
