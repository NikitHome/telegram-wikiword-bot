import telebot
import re
import wikipedia


bot = telebot.TeleBot('#')


# set ru language on wikipedia
wikipedia.set_lang("ru")


# clear wiki text & set max length 1000 symbols
def getwiki(s):
	try:
		ny = wikipedia.page(s)
		wikitext = ny.content[:1000] # max lenght
		wikimas = wikitext.split('.') # dot split
		wikimas = wikimas[:-1] # cut all after last dot

		wikitext_2 = ''
		for x in wikimas: 
			if not('==' in x):
				if (len((x.strip()))>3):
					wikitext_2 = wikitext_2 + x + '.'
			else:
				break

		wikitext_2 = re.sub('\([^()]*\)', '', wikitext_2)
		wikitext_2 = re.sub('\([^()]*\)', '', wikitext_2)
		wikitext_2 = re.sub('\{[^\{\}]*\}', '', wikitext_2)

		return wikitext_2

	except Exception as e:
		return 'Об этом нет информации'


# handler command /start
@bot.message_handler(commands = ["start"])
def start(m, res = False):
	bot.send_message(m.chat.id, 'Отправь мне любое слово и я найду его значение на Wikipedia')


# user message handler
@bot.message_handler(content_types = ["text"])
def handle_text(message):
	bot.send_message(message.chat.id, getwiki(message.text))


bot.polling(none_stop = True, interval = 0)