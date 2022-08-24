from slackbot.bot import respond_to, listen_to
import re

#OPEN VALVE
@listen_to('(open)+.*(valve)+', re.IGNORECASE)
@respond_to('(open)+.*(valve)+', re.IGNORECASE)
def openValveOrder(message, *something):
	#if valve is close:
	message.reply('OK. Open valve.')
	#able to get the username who commands
	userID = message.channel._client.users[message.body['user']][u'name']
	print (userID + '\'s command to open valve.')

#CLOSE VALVE
@listen_to('(close)+.*(valve)+', re.IGNORECASE)
@respond_to('(close)+.*(valve)+', re.IGNORECASE)
def openValveOrder(message, *something):
	#if valve is open:
	message.reply('OK. Close valve.')
	#able to get the username who commands
	userID = message.channel._client.users[message.body['user']][u'name']
	print (userID + '\'s command to close valve.')
