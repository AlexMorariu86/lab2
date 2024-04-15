class Animal:
    def mananca(self):
        print("Mananca")

class Pisica(Animal):
    print("Pisica mananca")


#animal = Animal()
#pisica = Pisica()

lista= [Pisica(), Pisica(), Animal(), Animal(), Animal()]
for animale in lista:
    animale.mananca()