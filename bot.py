import json
import requests
import pygame.mixer
from time import sleep


pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
list_Tuples = []
link = "http://www.reddit.com/r/magicArena/new.json?limit=25"
while(True):
	controll = True
	while(controll == True):
		try:
			controll = False
			response = requests.get(link, headers = {'User-agent': 'your bot 0.2'})
		except:
			print("Server error")
			sleep(20)
			controll = True 

	all_resp = json.loads(response.text)
	num_max = all_resp['data']['dist']
	for i in range (0,num_max):
		title = all_resp['data']['children'][i]['data']['title']
		title.lower()
		if "code" in title:
			id_post = all_resp['data']['children'][i]['data']['id']
			author_name = all_resp['data']['children'][i]['data']['author_fullname']
			tuple_test = (title,id_post,author_name) 
			if tuple_test not in list_Tuples:
				list_Tuples.append(tuple_test)
				pygame.mixer.music.play(0)
				print("https://www.reddit.com" + all_resp['data']['children'][i]['data']['permalink'])
				while pygame.mixer.music.get_busy():
					sleep(10)
				
	sleep(30)
			