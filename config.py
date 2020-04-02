
# Number of iteration to run the simulation for
NUM_ITERATIONS_TO_RUN = 10000

# number of people with which to conduct this simulation
NUM_PERSONS = 400

# size of the area where simulations will run
MAX_LOCATION = 1000

# We will say a day has passed when this many iterations have run
NUM_ITERATION_PER_DAY = 4

# Initial number of infected people
NUM_INITIAL_INFECTED = 5

# Hospital Related
NUM_HOSPITALS = 5
NUM_BEDS_PER_HOSPITAL = 5

#specific to covid19
DAYS_TILL_SYMPTOMS_APPEAR = 10
INFECTION_AREA = 10
PROBABILITY_OF_PERSON_GETTING_INFECTED = 0.5
MORTALITY_RATE = 0.05
MORTALITY_RATE_WHEN_HOSPITALS_ARE_SATURATED = 0.1
PROBABILITY_OF_GETTING_IMMMUNE = 0.07
PROBABILITY_OF_GETTING_IMMMUNE_WHEN_HOSPITALS_ARE_SATURATED = 0.02

# The number of days after which the disease will either kill people or they will become immune to the disease
DELTA_SINCE_JUDGEMENT_DAY = 25