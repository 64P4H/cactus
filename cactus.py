import speech_recognition as sr
import os
import sys



#пиши распознавания и функции к ним здесь
command_by_recognize={
	('вот', 'бот', 'both', 'what'):'.\shortcuts\\runbot.bat.lnk',
	('дискорд', 'дискорт', 'discord', 'escort'):'.\shortcuts\Discord.lnk',
	('стим', 'steam', 'tsum', 'jim'):'.\shortcuts\Steam.lnk',
	('aimp', "i'm", 'плеер', 'player', 'blair'):'.\shortcuts\AIMP.lnk'#ты заполнял этот словарик
}
#и запиши что чему пренадлежит сюда комментами
#bot = ('вот', 'бот', 'both', 'what')
#steam = ('','','','','')
#discord = ('дискорд', 'дискорт', 'discord', 'escort')


def get_speech():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Ready')
		r.adjust_for_ambient_noise(source, duration=2)
		audio = r.listen(source)
	try:
		speechRU = list(r.recognize_google(audio, language='ru-RU').lower().split(' '))
		speechENG = list(r.recognize_google(audio, language='en-US').lower().split(' '))
	except sr.UnknownValueError:
		print('Nope, try again.')
		speechRU, speechENG = get_speech()
	return speechRU, speechENG

def get_key_words(speechRU, speechENG):
	flow_of_key_words=list(command_by_recognize.keys())
	recognized_key_words=[]
	for words_to_recognize in flow_of_key_words:
		for word_to_recognize in words_to_recognize:
			if ((word_to_recognize in speechRU) or (word_to_recognize in speechENG)) and (words_to_recognize not in recognized_key_words):
				recognized_key_words.append(words_to_recognize)
				break
	if len(recognized_key_words)>0:
		return recognized_key_words
	else:
		print('I could not recognize anything')
		return []


def main():
	while True:
		try:
			inp = input()
			speechRU, speechENG = get_speech()
			print(speechRU, '\n', speechENG)
			key_words = get_key_words(speechRU, speechENG)
			print(key_words)
			for key_word in key_words:
				os.startfile(command_by_recognize[key_word])



		except KeyboardInterrupt:
			break


if __name__=='__main__':
	main()