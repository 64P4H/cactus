import speech_recognition as sr
import os
import keyboard
from commands import *
from winsound import PlaySound as PS
from winsound import SND_ALIAS


def get_speech():
	rec = sr.Recognizer()
	with sr.Microphone() as source:
		print('I am listenning')
		rec.adjust_for_ambient_noise(source, duration=2)
		audio = rec.listen(source)
	try:
		speechRU = list(rec.recognize_google(audio, language='ru-RU').lower().split(' '))
		try:
			speechENG = list(rec.recognize_google(audio, language='en-US').lower().split(' '))
		except sr.UnknownValueError:
			speechENG = []
	except sr.UnknownValueError:
		PS('SystemHand', SND_ALIAS)
		speechRU = []
		speechENG = []
		#print('I could not recognize anything\n')
		#speechRU, speechENG = get_speech()
	return speechRU, speechENG

def get_key_words(speechRU, speechENG):
	flow_of_key_words=list(command_to_recognize.keys())
	recognized_key_words=[]
	if (len(speechRU)==0) and (len(speechENG)==0):
		return []
	else:
		for words_to_recognize in flow_of_key_words:
			for word_to_recognize in words_to_recognize:
				if ((word_to_recognize in speechRU) or (word_to_recognize in speechENG)) and (words_to_recognize not in recognized_key_words):
					recognized_key_words.append(words_to_recognize)
					break
		if len(recognized_key_words)>0:
			return recognized_key_words
		else:
			PS('SystemHand', SND_ALIAS)
			#print('I could not detect any key words\n')
			return []


def main():
	while True:
		try:
			print('Press "ctrl+shift+v" to start')
			keyboard.wait('ctrl+shift+v')
			PS('SystemAsterisk', SND_ALIAS)
			speechRU, speechENG = get_speech()
			#print(speechRU, '\n', speechENG)
			key_words = get_key_words(speechRU, speechENG)
			#print(key_words)
			for key_word in key_words:
				if len(command_to_recognize[key_word])==0:
					#print('Command not entered')
					PS('SystemHand', SND_ALIAS)
				else:
					if str(type(command_to_recognize[key_word]))=="<class 'str'>":
						try:
							shortcut = command_to_recognize[key_word]
							os.startfile(shortcut)
							PS('SystemAsterisk', SND_ALIAS)
						except FileNotFoundError:
							PS('SystemHand', SND_ALIAS)
							#print('File not found')
							break
					else:
						for shortcut in command_to_recognize[key_word]:
							try:
								os.startfile(shortcut)
								PS('SystemAsterisk', SND_ALIAS)
							except FileNotFoundError:
								PS('SystemHand', SND_ALIAS)
								#print('File not found')
								break



		except KeyboardInterrupt:
			break



if __name__=='__main__':
	main()