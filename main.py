import os
import random

path = 'C:/Users/salom/Documents/Test'

recup = os.listdir(path)
for liste_images in recup:
    if liste_images.endswith(".png"):
        print(liste_images)
    elif liste_images.endswith("jpg"):
        print("Ok")


for liste_videos in recup:
    if liste_videos.endswith("mp3"):
        print(liste_videos)
    elif liste_videos.endswith("mp4"):
        print("Ok")


point = ""
tr_point = point.find(".")
sep = ""
liste_images = list(liste_images)
liste_videos = list(liste_videos)
tr_point = str(tr_point)
nb =  {
    for i in range(10):
}


debut = liste_images[0]
fin = tr_point

for liste_images in sep:
    trouver = sep.find(tr_point, debut, fin)
    if trouver == -1:
        print("Probleme")
    elif



