from living_state import *
from random import randint
import pdb

def contact(person1, person2, current_iter):
    
    xp1, yp1 = person1.location
    xp2, yp2 = person2.location

    if (person1.status == INFECTED or person1.status == NO_HOSPITAL_QUARANTINED) and person2.status == UNINFECTED:
        
        if (xp2 >= xp1 - person1.infection_cls.infect_area and xp2 <= xp1 + person1.infection_cls.infect_area) and (yp2 >= yp1 - person1.infection_cls.infect_area and yp2 <= yp1 + person1.infection_cls.infect_area):

            infection_probab = person1.infection_cls.person_infect_probab*100
            prob = randint(0,100)
            if prob < infection_probab:
                person2.infect(person1.infection_cls, current_iter)

    if (person2.status == INFECTED or person2.status == NO_HOSPITAL_QUARANTINED) and person1.status == UNINFECTED:
        
        if (xp1 >= xp2 - person2.infection_cls.infect_area and xp1 <= xp2 + person2.infection_cls.infect_area) and (yp1 >= yp2 - person2.infection_cls.infect_area and yp1 <= yp2 + person2.infection_cls.infect_area):

            infection_probab = person2.infection_cls.person_infect_probab*100
            prob = randint(0,100)
            if prob < infection_probab:
                person1.infect(person2.infection_cls, current_iter)
