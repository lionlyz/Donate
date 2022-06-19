# Developed By : Abhishek Kumar (https://telegram.me/TheTeleRoid) 

import os
from pyrogram import Client, filters
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InputTextMessageContent
from pyrogram.types import InlineQueryResultArticle


Bot = Client(
    "Donate",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_TEXT = """Hey! {}

☞ Sangat Senang mengetahui bahwa Anda menyumbangkan kami.

Terima kasih telah menggunakan [bot kami](https://t.me/+ku2kx0h4KRFkOTll).
"""

DONATE_BUTTONS = [
    InlineKeyboardButton(
        text='Donasi 💳',
        callback_data='donateme'
    )
]

DONATE_TEXT = """Hey! {}
Anda dapat berdonasi kepada kami menggunakan dana

Dana - `085796582392`

Atau hubungi kami :- [leon](https://telegram.me/divmas). """

BUTTON_TEXT = """ Click the Below Buttons To Donate Us. """

UPI_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(" Back ", callback_data="back"),
            InlineKeyboardButton(" PayPal ", url="https://paypal.me/diivmas")
        ],
        [
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

PAY_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(" Dana ", callback_data="upidata"),
            InlineKeyboardButton(" PayPal ", url="https://paypal.me/diivmas")
        ],
        [
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup([DONATE_BUTTONS]),
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.command(["donate"]))
async def donate(bot, update):
    await bot.send_message(
        text="Click the Following Button to Donate Us.",
        reply_markup=InlineKeyboardMarkup([PAY_BUTTONS]),
        disable_web_page_preview=True,
        quote=True
    )

@Bot.on_message(filters.private & filters.command(["bots"]))
async def bots(bot, update):
    await bot.send_message(
        text="https://t.me/dlksyz",
        reply_markup=InlineKeyboardMarkup([PAY_BUTTONS]),
        disable_web_page_preview=True,
        quote=True
    )

@Bot.on_inline_query()
async def answerX(bot, update):

    answer = list()
    answer.append(InlineQueryResultArticle(title="This is My Donation Or Payment Bot", description="You Can Donate Us Using Inline.",
    input_message_content=InputTextMessageContent(message_text="Please donate us any amount you like, to support the services."),
    reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton("Donasi 💳", url="https://paypal.me/diivmas") ] ] ),
    thumb_url="https://paypal.me/diivmas") )
    try:
        await update.answer(results=answer, cache_time=0)
    except Exception as e:
        print(f"🚸 ERROR : {e}")
    except QueryIdInvalid:
        pass

@Bot.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "donateme":
        await update.message.edit_text(
            text=BUTTON_TEXT.format(update.from_user.mention),
            reply_markup=PAY_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "upidata":
        await update.message.edit_text(
            text=DONATE_TEXT.format(update.from_user.mention),
            reply_markup=UPI_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "back":
        await update.message.edit_text(
            text=BUTTON_TEXT.format(update.from_user.mention),
            reply_markup=PAY_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()

Bot.run()
