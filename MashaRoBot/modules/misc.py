from MashaRoBot.modules.helper_funcs.chat_status import user_admin
from MashaRoBot.modules.disable import DisableAbleCommandHandler
from MashaRoBot import dispatcher

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ParseMode, Update
from telegram.ext.dispatcher import run_async
from telegram.ext import CallbackContext, Filters, CommandHandler

MARKDOWN_HELP = f"""
Markdown is a very powerful formatting tool supported by telegram. {dispatcher.bot.first_name} has some enhancements, to make sure that \
saved messages are correctly parsed, and to allow you to create buttons.

• <code>_italic_</code>: wrapping text with '_' will produce italic text
• <code>*bold*</code>: wrapping text with '*' will produce bold text
• <code>`code`</code>: wrapping text with '`' will produce monospaced text, also known as 'code'
• <code>[sometext](someURL)</code>: this will create a link - the message will just show <code>sometext</code>, \
and tapping on it will open the page at <code>someURL</code>.
<b>Example:</b><code>[test](example.com)</code>

• <code>[buttontext](buttonurl:someURL)</code>: this is a special enhancement to allow users to have telegram \
buttons in their markdown. <code>buttontext</code> will be what is displayed on the button, and <code>someurl</code> \
will be the url which is opened.
<b>Example:</b> <code>[This is a button](buttonurl:example.com)</code>

If you want multiple buttons on the same line, use :same, as such:
<code>[one](buttonurl://example.com)
[two](buttonurl://google.com:same)</code>
This will create two buttons on a single line, instead of one button per line.

Keep in mind that your message <b>MUST</b> contain some text other than just a button!
"""


@run_async
@user_admin
def echo(update: Update, context: CallbackContext):
    args = update.effective_message.text.split(None, 1)
    message = update.effective_message

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            args[1], parse_mode="MARKDOWN", disable_web_page_preview=True
        )
    else:
        message.reply_text(
            args[1], quote=False, parse_mode="MARKDOWN", disable_web_page_preview=True
        )
    message.delete()


def markdown_help_sender(update: Update):
    update.effective_message.reply_text(MARKDOWN_HELP, parse_mode=ParseMode.HTML)
    update.effective_message.reply_text(
        "Try forwarding the following message to me, and you'll see, and Use #test!"
    )
    update.effective_message.reply_text(
        "/save test This is a markdown test. _italics_, *bold*, code, "
        "[URL](example.com) [button](buttonurl:github.com) "
        "[button2](buttonurl://google.com:same)"
    )


@run_async
def markdown_help(update: Update, context: CallbackContext):
    if update.effective_chat.type != "private":
        update.effective_message.reply_text(
            "Contact me in pm",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Markdown help",
                            url=f"t.me/{context.bot.username}?start=markdownhelp",
                        )
                    ]
                ]
            ),
        )
        return
    markdown_help_sender(update)


__help__ = """
*Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:*
*Mᴀʀᴋᴅᴏᴡɴ:*
 ❍ /markdownhelp*:* ϙᴜɪᴄᴋ sᴜᴍᴍᴀʀʏ ᴏғ ʜᴏᴡ ᴍᴀʀᴋᴅᴏᴡɴ ᴡᴏʀᴋs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ - ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴄᴀʟʟᴇᴅ ɪɴ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛs
*Pᴀsᴛᴇ:*
 ❍ /paste*:* Sᴀᴠᴇs ʀᴇᴘʟɪᴇᴅ ᴄᴏɴᴛᴇɴᴛ ᴛᴏ `ɴᴇᴋᴏʙɪɴ.ᴄᴏᴍ` ᴀɴᴅ ʀᴇᴘʟɪᴇs ᴡɪᴛʜ ᴀ ᴜʀʟ
*Rᴇᴀᴄᴛ:*
 ❍ /react*:* Rᴇᴀᴄᴛs ᴡɪᴛʜ ᴀ ʀᴀɴᴅᴏᴍ ʀᴇᴀᴄᴛɪᴏɴ 
*Uʀʙᴀɴ Dɪᴄᴛᴏɴᴀʀʏ:*
 ❍ /ud <ᴡᴏʀᴅ>*:* Tʏᴘᴇ ᴛʜᴇ ᴡᴏʀᴅ ᴏʀ ᴇxᴘʀᴇssɪᴏɴ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴇᴀʀᴄʜ ᴜsᴇ
*Wɪᴋɪᴘᴇᴅɪᴀ:*
 ❍ /wiki <ϙᴜᴇʀʏ>*:* ᴡɪᴋɪᴘᴇᴅɪᴀ ʏᴏᴜʀ ϙᴜᴇʀʏ
*Wᴀʟʟᴘᴀᴘᴇʀs:*
 ❍ /wall <ϙᴜᴇʀʏ>*:* ɢᴇᴛ ᴀ ᴡᴀʟʟᴘᴀᴘᴇʀ ғʀᴏᴍ ᴡᴀʟʟ.ᴀʟᴘʜᴀᴄᴏᴅᴇʀs.ᴄᴏᴍ
*Cᴜʀʀᴇɴᴄʏ ᴄᴏɴᴠᴇʀᴛᴇʀ:* 


 




"""

ECHO_HANDLER = DisableAbleCommandHandler("echo", echo, filters=Filters.group)
MD_HELP_HANDLER = CommandHandler("markdownhelp", markdown_help)

dispatcher.add_handler(ECHO_HANDLER)
dispatcher.add_handler(MD_HELP_HANDLER)

__mod_name__ = "Ꭼ-ᏆͲᎬᎷ🪁"
__command_list__ = ["id", "echo"]
__handlers__ = [
    ECHO_HANDLER,
    MD_HELP_HANDLER,
]
