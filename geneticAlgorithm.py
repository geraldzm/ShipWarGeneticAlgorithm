import math
import random
from chromosome import Chromosome

class GA:

    def __init__(self, ship, enemy):

        self.enemy_position = 14
        self.fire_position = 0
        self.current_position = 2

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

        return [i[0] for i in fit[:int(self.accepted*len(fit))]] #[a_tuple[0] for a_tuple in tuple_list]

    def orgy(self, population):
        #print('')

        children = []

        for i in range(self.population_size):
            father = random.choice(population)
            mother = random.choice(population)
            
            child = father.sex(mother)
            
            children.append(child)
          #  print('father:', father, ' |\tmother:', mother, ' |\tchild:', child)

            # 0001 0110
        return children

    def create_generations(self):

        #spartan_babies = [Chromosome(b'\x8F'), Chromosome(b'\xF5'), Chromosome(b'\x19'), Chromosome(b'\x76'),Chromosome(b'\x48')]

        spartan_babies = []

        for i in range(self.population_size):
            ran = random.randrange(1, 254)
            spartan_babies.append(Chromosome(bytes([ran])))
        
        for i in range(self._n_generations):

            spartan_babies = self.fitness(spartan_babies)
            
            #print("\nGen",i)
            #for bb in spartan_babies:
                #print(bb)
            
            spartan_babies = self.orgy(spartan_babies)

        return spartan_babies

    def take_decition(self):
        spartan_babies = self.create_generations()

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

          #  print(i, count[i]) 


      #  print('the one:', the_one, '\tGen:', self._n_generations) #sellected

        return the_one

    def tick(self):
        
        self.current_position = int(self._ship._hit_box.x/40)
        self.enemy_position = int(self._enemy._hit_box.x/40)

        selected = self.take_decition()
        
        # mapping:
        if selected >= 200:
            print("fire")
            self._ship.fier()
        else:
            col =  selected/10
            
            self._ship._vel_x = col*40 - self._ship._hit_box.x

            n = 1

            if self._ship._vel_x < 0:
                n = -1
            
            if self._ship._vel_x != 0:
                self._ship._vel_x = n - (10/self._ship._vel_x) #10 max vel

          #  print("move to column", col, 'vel:',self._ship._vel_x)


    def render(self, screen):
        pass