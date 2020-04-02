from living_state import *
from random import randint
from config import NUM_ITERATION_PER_DAY

class Person(object):

    def __init__(self, uid, max_location, status, active_probab = 0.6):
        # unique id would be the index when the person was created
        self.uid = uid
        self.max_location = max_location
        self.status = status
        # probability of a person to move 
        self.active_probab = active_probab
        
        self.infection_cls = None
        self.shows_symptom = False
        self.days_from_infection = 0
        self.infected_day = 0
        self.is_hospitalized = False

        # function call
        self.move(force=True)
        
    def move(self, force = False):
        if (not self.is_hospitalized) and (self.status != DEAD) and (self.status != NO_HOSPITAL_QUARANTINED):
            will_move = self.active_probab*100
            # person will move 
            if randint(0, 100) < will_move or force:
                self.location = (randint(0, self.max_location), randint(0, self.max_location))
    
    def are_symptoms_visible(self, current_iter):
        if self.status == INFECTED and not self.is_hospitalized and not(self.status == NO_HOSPITAL_QUARANTINED):
            days_since_infection = int(current_iter/NUM_ITERATION_PER_DAY) - self.infected_day
            if days_since_infection >= self.infection_cls.delay_symptoms:
                self.shows_symptom = True
    
    def hospitalize(self, hospital_location):
        self.is_hospitalized = True
        self.location = hospital_location

    def infect(self, disease, current_iter):
        self.infection_cls = disease
        self.infected_day = int(current_iter/NUM_ITERATION_PER_DAY)
        self.status = INFECTED

    def dead_immune_delay(self, current_iter):
        if self.infected_day + self.infection_cls.delta_judment_day > (current_iter/NUM_ITERATION_PER_DAY): 
            if self.is_hospitalized:
                death_probab = randint(0,100)
                mortality_probab = self.infection_cls.mortality_rate*100
                if death_probab < mortality_probab:
                    self.status = DEAD
                    self.shows_symptom = False

                immune_probab = randint(0,100)
                std_immune_probab = self.infection_cls.immunity_probab*100
                if immune_probab < std_immune_probab:
                    self.status = IMMUNE
                    self.shows_symptom = False

            if self.status == NO_HOSPITAL_QUARANTINED:
                death_probab = randint(0,100)
                mortality_probab = self.infection_cls.saturated_mortality_rate*100
                if death_probab < mortality_probab:
                    self.status = DEAD
                    self.shows_symptom = False

                immune_probab = randint(0,100)
                std_immune_probab = self.infection_cls.saturated_immune_probab*100
                if immune_probab < std_immune_probab:
                    self.status = IMMUNE
                    self.shows_symptom = False
                

    def no_hospital_quarantine(self):
        self.status = NO_HOSPITAL_QUARANTINED
        self.is_hospitalized = False
        

