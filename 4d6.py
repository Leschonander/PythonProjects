import pygal
from random import randint

class Die():
    def __init__(self, sides = 6):
        self.sides = sides
    def roll(self):
        return randint(1, self.sides)

die1 = Die()
die2 = Die()
die3 = Die()
die4 = Die()

results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll() + die3.roll() + die4.roll()
    results.append(result)

freq = []
max_result = die1.sides + die2.sides + die3.sides + die4.sides
for value in range(4, max_result + 1):
    frequ = results.count(value)
    freq.append(frequ)
print(freq)
#
hist = pygal.Bar()

hist.title = ("Result of 1000 4d6 die rolls like in DnD")
hist.x_labels = ['1','2','3','4','5','6','7','8','9','10','11','12',
'13','14','15','16','17','18','19','20','21','22','23','24']
hist.x_title = 'Result'
hist.y_title = "Frequency of Results"

hist.add('D6 + D6 + D6 + D6', freq)
hist.render_to_file('Dnd_Die_Vis.svg')