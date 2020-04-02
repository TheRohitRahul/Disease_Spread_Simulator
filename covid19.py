from config import *

class Covid19(object):
    def __init__(self):
        # in days
        self.delay_symptoms = DAYS_TILL_SYMPTOMS_APPEAR
        self.infect_area = INFECTION_AREA
        self.person_infect_probab = PROBABILITY_OF_PERSON_GETTING_INFECTED
        self.mortality_rate = MORTALITY_RATE
        self.saturated_mortality_rate = MORTALITY_RATE_WHEN_HOSPITALS_ARE_SATURATED
        self.immunity_probab = PROBABILITY_OF_GETTING_IMMMUNE
        self.saturated_immune_probab = PROBABILITY_OF_GETTING_IMMMUNE_WHEN_HOSPITALS_ARE_SATURATED
        self.delta_judment_day = DELTA_SINCE_JUDGEMENT_DAY