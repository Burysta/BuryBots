import openai
import telebot

openai.api_key = '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'
bot = telebot.TeleBot("5710210971:AAG0dtPq1pDgZ3kwzAG9-roAYaw35kLqeaM")



@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=message.text,
      temperature=0.5,
      max_tokens=1000,
      top_p=1.0,
      frequency_penalty=0.5,
      presence_penalty=0.0,
    )
    bot.send_message(chat_id=message. from_user.id, text=response['choices'][0]['text'])




bot.polling()

