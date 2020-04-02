from random import randint
import pdb

from config import NUM_PERSONS, MAX_LOCATION, NUM_ITERATION_PER_DAY, NUM_HOSPITALS, NUM_BEDS_PER_HOSPITAL, NUM_INITIAL_INFECTED, NUM_ITERATIONS_TO_RUN

from living_state import *
from person import Person
from hospital import Hospital
from covid19 import Covid19
from get_stats import get_people_stats
from contact import contact

def create_hospitals():
    all_hospitals = []
    for j in range(NUM_HOSPITALS):
        locations_x = []
        locations_y = []
        
        hospital_location_x = randint(10, MAX_LOCATION)
        hospital_location_y = randint(10, MAX_LOCATION)

        while (hospital_location_x in locations_x and hospital_location_y in locations_y):
            hospital_location_x = randint(10, MAX_LOCATION)
            hospital_location_y = randint(10, MAX_LOCATION)
        all_hospitals.append(Hospital(j, NUM_BEDS_PER_HOSPITAL, [hospital_location_x, hospital_location_y]))
    return all_hospitals

def create_people():
    all_people = []
    total_infected = 5
    infected_indices = []
    for j in range(total_infected):
        next_infected = randint(0, NUM_PERSONS)
        while(next_infected in infected_indices):
            next_infected = randint(0, NUM_PERSONS)
        infected_indices.append(next_infected)

    for j in range(NUM_PERSONS):
        if j in infected_indices:
            next_person = Person(j, MAX_LOCATION, INFECTED, active_probab = 0.6)
            next_person.infect(Covid19(), 0)      
            all_people.append(next_person)
        else:
            next_person = Person(j, MAX_LOCATION, UNINFECTED, active_probab = 0.6)
            all_people.append(next_person)

    return all_people

def run_iters(num_iterations):
    all_hospitals = create_hospitals()
    all_people = create_people()
    all_hospital_full = False
        
    for i in range(num_iterations):
        for j in range(NUM_PERSONS):
            all_people[j].move()
            all_people[j].are_symptoms_visible(i)
            if all_people[j].shows_symptom:

                # Checking if there is any space left in hospital
                all_hospital_full = True
                for a_hospital in all_hospitals:
                    if not a_hospital.is_full:
                        all_hospital_full = False
                        break
                
                # If all hospitals are not full then
                if not all_hospital_full:
                    for a_hospital in all_hospitals:
                        if not a_hospital.is_full:
                            hospital_location = a_hospital.location
                            a_hospital.occupy_bed()
                            break
                    all_people[j].hospitalize(hospital_location)
                
                # otherwise quarantine the person
                else:
                    all_people[j].no_hospital_quarantine()
        
        for j in range(NUM_PERSONS):
            for k in range(NUM_PERSONS):
                if j != k:
                    contact(all_people[j], all_people[k], i)
        
        for j in range(NUM_PERSONS):
            if all_people[j].status == NO_HOSPITAL_QUARANTINED or all_people[j].is_hospitalized:
                all_people[j].dead_immune_delay(i)
        
        get_people_stats(all_people, i)
        



if __name__ == "__main__":
    run_iters(NUM_ITERATIONS_TO_RUN)
