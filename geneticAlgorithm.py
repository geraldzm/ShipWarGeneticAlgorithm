import math
import random
from chromosome import Chromosome

class GA:

    def __init__(self, ship, enemy):

        self.enemy_position = 0
        self.fire_position = 0
        self.current_position = 0

        self.accepted = 0.6 # amount accepted

        self._n_generations = 5
        self.population_size = 5

        self._ship = ship
        self._enemy = enemy

    def fitness(self, population):
        
        fit = []

        for gen in population:
            gen_n = gen.get_int() 
              
            heading = gen_n / 10
            rs = abs(heading - self.enemy_position) * (20 - abs(self.fire_position-self.enemy_position)) * abs(self.current_position - self.enemy_position)
            
            if gen_n != 0:
                rs -= math.trunc(200/ gen_n)

            fit.append((gen, rs))

        fit = sorted(fit, key=lambda tup: tup[1])      

        return [i[0] for i in fit[:int(self.accepted*len(fit))]] # return the first % accepted 

    def orgy(self, population):

        children = []

        for i in range(self.population_size):
            father = random.choice(population)
            mother = random.choice(population)
            
            child = father.sex(mother)
            
            children.append(child)

        return children

    def create_generations(self):

        spartan_babies = []

        #random initial population
        for i in range(self.population_size):
            ran = random.randrange(1, 254)
            spartan_babies.append(Chromosome(bytes([ran])))
        
        
        for i in range(self._n_generations):

            spartan_babies = self.fitness(spartan_babies) # save the fit ones, kill the others (this is sparta?)        
            spartan_babies = self.orgy(spartan_babies) # multiply

        return spartan_babies

    def take_decition(self):
        spartan_babies = self.create_generations() # create and get the elements of the last generation

        # getting the most common genotype
        count = {}

        for i in spartan_babies:
            try:
                count[i.get_int()] += 1
            except:
                count[i.get_int()] = 1

        max = 0
        the_one = 0

        for i in count:
            if count[i] > max:
                max = count[i]
                the_one = i

        # return the most common genotype
        return the_one

    # This method will be executed each frame
    def tick(self):
        
        self.current_position = int(self._ship._hit_box.x/40)
        self.enemy_position = int(self._enemy._hit_box.x/40)

        # if not bullet then fp = 0, if bullet then fp = bullet position on the x axis
        self._fire_position = 0 if len(self._enemy._bullets) == 0 else self._enemy._bullets[0]._hit_box.x

        selected = self.take_decition() # run N generations and get the comon genotype
        
        if selected >= 200: # fier bullet
            
            if len(self._ship._bullets) == 0: # one bullet at the time
                self._ship.fier()

        else: # move to a column
            col =  selected/10 # selected is a value > 0 and < 200
            
            self._ship._vel_x = col*40 - self._ship._hit_box.x # col*40 becouse there is 800px (width), each 40px represents one of the 20 columns

            n = 1

            if self._ship._vel_x < 0:
                n = -1
            
            if self._ship._vel_x != 0:
                self._ship._vel_x = n - (10/self._ship._vel_x)  # 10 is the max velocity

    def render(self, screen):
        pass