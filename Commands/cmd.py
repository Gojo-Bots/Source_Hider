from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ParseMode
from config import Config

#Inline Keyboard Button
keyboard = [
[
 InlineKeyboardButton("Source Code", url=Config.SOURCE)
],
[
 InlineKeyboardButton("How To Create A Bot Like Me",url="https://telegra.ph/Captain-03-24")
]
]

#The Keyboard On Up👆
reply_markup = InlineKeyboardMarkup(keyboard)

#Send Start Message
def startMessage(update,context):
 msg = Config.START_TEXT.format(update.message.from_user.full_name,update.message.chat.id)
 try:
  update.message.reply_photo(photo = "https://te.legra.ph/file/dc6e0b631938b66e38626.jpg", caption = msg,reply_markup=reply_markup,
parse_mode=ParseMode.MARKDOWN)
 except Exception as e:
 	update.message.reply_text(e)

#Help Message
def helpMessage(update,context):
 msg = Config.HELP_TEXT
 try:
   update.message.reply_text(photo = "https://te.legra.ph/file/785e57bcd78ac4634b6d5.jpg" ,reply_markup=reply_markup,parse_mode=ParseMode.MARKDOWN)
 except Exception as e:
  	update.message.reply_text(e)

