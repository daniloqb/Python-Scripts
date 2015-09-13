__author__ = 'danilqb'


class Robot:

    population = 0    # Variaveis de classe nao precisam ser declaradas como static

    def __init__(self, name):
        self.name = name
        print "(Initializing {}.)".format(self.name)

        Robot.population +=1  # self.__class__.population

    def die(self):
        print "({} is being destroyed!)".format(self.name)
        Robot.population -= 1

        if Robot.population == 0:
            print "({} was the last one)".format(self.name)
        else:
            print "There ares still {:d} robots working".format(Robot.population)


    def say_hi(self):

        print "Greetings, my master call me {}".format(self.name)

    @classmethod
    def how_many(cls):   # @classmethod decorator   ==  how_many = classmethod(how_many)
        print "Whe have {:d} robots.".format(cls.population)


droid1 = Robot('R2-D2')
droid1.say_hi()
droid1.how_many()


droid2 = Robot('C-3PO')
droid2.say_hi()
droid2.how_many()



droid1.die()
droid2.die()

Robot.how_many()