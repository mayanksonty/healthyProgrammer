# 200 ml water = 3.5 litre water
from datetime import datetime
from time import time
from pygame import mixer

def isOfficeTime(currentTime):
    if isOfficeTime > '09:00:00' and isOfficeTime < '17:00:01':
        return True
    else:
        return False
     


def playMusic(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)  #-1 is used for making it indefinate loop
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log(msg):
    with open("mayank.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    waterSec = 5
    exerciseSec = 10
    eyesSec = 20
    currentTime = time.strftime('%H:%M:%S')
    
    while (isOfficeTime(currentTime)):
        if time() - init_water > waterSec:
            print("Water Drinking time 'done' for stopping")
            playMusic("drink.mp3","done")
            init_water = time()
            log("Drank Water at")
        elif time() - init_exercise > exerciseSec:
            print("Excercise time 'done' for stopping")
            playMusic("drink.mp3","done")
            init_exercise = time()
            log("Done Excercise at")
        elif time() - init_eyes > eyesSec:
            print("Eye Excercise time 'done' for stopping")
            playMusic("drink.mp3","done")
            init_eyes = time()
            log("Done Eyes exercise at")














