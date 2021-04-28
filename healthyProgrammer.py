# 200 ml water = 3.5 litre water
import time
from pygame import mixer


def playMusic(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)  #-1 is used for making it indefinate loop
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

# def drinkWater(file,stopper):
#     # mixer.init()
#     # mixer.music.load(file)
#     # mixer.music.play(-1)  #-1 is used for making it indefinate loop
#     # while True:
#     #     a = input()
#     #     if a == stopper:
#     #         mixer.music.stop()
#     #         break
#     # i = "nd"
#     # while(i!="d"):
#     #     print("Drink Water")
#     #     i =input("Hit d for Done").lower()



# def eyeExer():
#     # mixer.init()
#     # mixer.music.load(file)
#     # mixer.music.play(-1)  #-1 is used for making it indefinate loop
#     # while True:
#     #     a = input()
#     #     if a == stopper:
#     #         mixer.music.stop()
#     #         break
#     # i = "nd"
#     # while(i!="d"):
#         # print("Eye Exercise")
#         # i =input("Hit d for Done").lower()

# def physicalActivity():
#     # mixer.init()
#     # mixer.music.load(file)
#     # mixer.music.play(-1)  #-1 is used for making it indefinate loop
#     # while True:
#     #     a = input()
#     #     if a == stopper:
#     #         mixer.music.stop()
#     #         break
#     # i = "nd"
#     # while(i!="d"):
#         # print("Physical activity")
#         # i =input("Hit d for Done").lower()

a = time.localtime()
b = 2
while (a.tm_min>18):
    a = time.localtime()
    if a.tm_min < 38:
        # main program is under here   
        if b == a.tm_sec:
            print("under loop  1")
            playMusic("drink.mp3","done")
            b = b+10
        elif b<a.tm_sec or b>a.tm_sec:
            print(f"iam a continue {a.tm_sec}")
            continue
    else:
        break

print("finished")
# time.sleep(2)
# eyeExer()
# time.sleep(3)
# physicalActivity()

