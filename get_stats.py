from living_state import *
import cv2
import numpy as np

from config import MAX_LOCATION, NUM_ITERATION_PER_DAY

def display_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(500)
    # cv2.destroyAllWindows() 

def get_people_stats(all_people, iter):
    
    map_ = np.zeros((MAX_LOCATION, MAX_LOCATION, 3), dtype=np.uint8)
    
    uninfected = 0
    infected = 0
    immune = 0
    dead = 0
    no_hospital_quarantined = 0

    for a_person in all_people:
        x, y = a_person.location

        if a_person.status == UNINFECTED:
            cv2.circle(map_, (x, y), 2, (255,255,255), -1)
            uninfected +=1
        elif a_person.status == INFECTED:
            cv2.circle(map_, (x, y), 2, (0,255,0), -1)
            infected += 1
        elif a_person.status == IMMUNE:
            cv2.circle(map_, (x, y), 2, (255,0,0), -1)
            immune += 1
        elif a_person.status == DEAD:
            cv2.circle(map_, (x, y), 2, (0,0,255), -1)
            dead += 1
        elif a_person.status == NO_HOSPITAL_QUARANTINED:
            cv2.circle(map_, (x, y), 2, (0,128,128), -1)
            no_hospital_quarantined += 1

    print("\nday : {}".format(iter/NUM_ITERATION_PER_DAY))
    print("\nUninfected : {}\nInfected : {}\nImmune : {}\nDead : {}\nQuarantined : {}".format(uninfected, infected, immune, dead, no_hospital_quarantined))
    display_image("person stats", map_) 