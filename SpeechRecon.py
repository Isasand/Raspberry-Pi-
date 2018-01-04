import speech_recognition as sr
import subprocess 

bashCommand = "python test.py"
#bashComTwo = "play testsound.wav"
r = sr.Recognizer()
m = sr.Microphone() 

try: 
	print("A moment of silence please..") 
	with m as source: r.adjust_for_ambient_noise(source)
	while True: 
		print("say something")
		with m as source: audio = r.listen(source) 
		print("got it") 
		try: 
			value = r.recognize_google(audio) 
			
			if str is bytes: 
				print(u"You said{}".format(value).encode("utf-8"))
				if value == "hello pie": 
					process = subprocess.Popen(bashCommand.split(), stdout = subprocess.PIPE)
					process.communicate()
					#process = subprocess.Popen(bashComTwo.split(), stdout = subprocess.PIPE)
					#process.communicate()

			else: 
				print("you said {}".format(value))
				print("not utf8") 
		except sr.UnknownValueError: 
			print("oups didnt catch that") 
		except sr.RequestError as e: 
			print("uh! Coulnt request results from Google speach recon servce; {0}".format(e))

except KeyboardInterrupt: 
	pass
