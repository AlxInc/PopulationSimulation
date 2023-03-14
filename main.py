import random
import math
import matplotlib.pyplot as plt
import csv

startPopulation = 50
food = 25
agriculture = 5

peopleDictionary = []
peopleDictionaryHistory = []


fertilityx = 18
fertilityy = 40
infantMortality = 5
workingx = 14
workingy = 65
lastNames = ['Smith',
'Jones',
'Williams',
'Brown',
'Wilson',
'Taylor',
'Anderson',
'Johnson',
'White',
'Thompson',
'Lee',
'Martin',
'Thomas',
'Walker',
'Kelly',
'Young',
'Harris',
'King',
'Ryan',
'Roberts',
'Hall',
'Evans',
'Davis',
'Wright',
'Baker',
'Campbell',
'Edwards',
'Clark',
'Robinson',
'McDonald',
'Hill',
'Scott',
'Clarke',
'Mitchell',
'Stewart',
'Moore',
'Turner',
'Miller',
'Green',
'Watson',
'Bell',
'Wood',
'Cooper',
'Murphy',
'Jackson',
'James',
'Lewis',
'Allen',
'Bennett',
'Robertson']

#graphing
born_this_year = 0
died_this_year = 0
line_year = [1]
line_population = [0]
line_avg_age = [0]
line_deaths = [0]
line_children_born = [0]
line_food = [0]

class God:
    def __init__(self):
        self.name = 'God'

class Person:
    def __init__(self, age, name, mother, father):
        self.gender = random.randint(0, 1)
        self.age = age
        self.name = name
        self.pregnant = False

        #reproduction
        self.mother = mother
        self.father = father
        self.children = []
        self.married = False
        self.partner = object

        #profession
        # self.workCapacity = wc

    def marraige(self):
        if self.age > 14:
            possible_partners = [p for p in peopleDictionary if p.name != self.name]
            partner = random.choice(possible_partners)
            # print(f'Name {self.name}, Partner chosen {partner.name}')
            if self.married is True:
                pass

            elif self.married is not True and partner.married is not True:
                self.married = True
                self.partner = partner
                partner.married = True
                partner.partner = self
            else:
                self.partner = partner
                if partner.partner.married is not True:
                    partner.partner = self

            self.have_child()

    def generate_name(self):
        n = random.randint(0, 2)
        new_name = ''
        if n == 0:
            new_name = random.choice(lastNames)
        elif n == 1:
            new_name = random.choice(lastNames)
            new_name = new_name[::-1].lower().title()
            lastNames.append(new_name)
        else:
            new_name = self.name[:len(self.name) // 2] + self.partner.name[len(self.partner.name) // 2:]
            lastNames.append(new_name)
        return new_name

    def have_child(self):
        global born_this_year
        if self.gender == 1 and self.partner.gender == 0:
            if self.age > 14:
                if self.pregnant is False:
                    if self.age > fertilityx and self.age < fertilityy:
                        if random.randint(0, 2) == 1:
                            self.pregnant = True

                elif self.pregnant is True:
                    self.pregnant = False
                    if random.randint(0, 100) > infantMortality:
                        new_name = self.generate_name()
                        peopleDictionary.append(Person(age=0,
                                                       name=new_name,
                                                       mother=self,
                                                       father=self.partner))
                        peopleDictionaryHistory.append(Person(age=0,
                                                       name=new_name,
                                                       mother=self,
                                                       father=self.partner))
                        self.children.append(peopleDictionary[-1])
                        self.partner.children.append(peopleDictionary[-1])
                        born_this_year += 1

def plot_graph():
    global line_year, line_population, line_avg_age, line_max_workers, line_deaths, line_children_born, born_this_year, died_this_year
    line_deaths.append(died_this_year)
    line_children_born.append(born_this_year)
    line_year.append(line_year[-1] + 1)
    line_population.append(len(peopleDictionary))
    avg = []
    for people in peopleDictionary:
        avg.append(people.age)
    try:
        line_avg_age.append(sum(avg) / len(peopleDictionary))
    except ZeroDivisionError:
        line_avg_age.append(0)
    line_food.append(food)
    born_this_year = 0
    died_this_year = 0

def harvest(food, agriculture):
    ablePeople = 0
    global peopleDictionary
    global died_this_year


    for person in peopleDictionary:
        if person.age > workingx and person.age < workingy:
            ablePeople += 1


    food += ablePeople * agriculture

    food -= len(peopleDictionary)

    if food < len(peopleDictionary):
        # peopleToStarve = random.choices(peopleDictionary, k=int(len(peopleDictionary)) - food)

        peopleToStarve = []
        for i in range(0, len(peopleDictionary) - food):
            personToStarve = random.choice(peopleDictionary)
            while True:
                if personToStarve not in peopleToStarve:
                    peopleToStarve.append(personToStarve)
                    False
                else:
                    continue


        print(f'going to die {peopleToStarve}')
        for person in peopleToStarve:
            peopleDictionary.remove(person)
        died_this_year = len(peopleToStarve)
        food = 0

    else:

        food -= len(peopleDictionary)
    print(f'able bodies = {ablePeople} food {food} down from {food + len(peopleDictionary)}')








# for x in lastNames:
#     print(x, end=', ')

# name = random.choice(peopleDictionary).name
# partner = random.choice(peopleDictionary).name
# print(f'person {name1}, partner {name2}')
# name3 = name1[:len(name1)//2] + partner[len(name2)//2:]
# print(name3)
# lastNames.append(name3)

# for x in lastNames:
#     print(x, end=', ')

def runYear():
    harvest(food=food, agriculture=agriculture)
    for person in peopleDictionary:
        if person.age > 80:
            peopleDictionary.remove(person)
            continue
        elif person.age > 13:
            person.marraige()
        person.age += 1

    current_last_names = [p.name for p in peopleDictionary]
    for name in lastNames:
        if name not in current_last_names:
            del name

    # print(f'year {line_year[-1]}')
    plot_graph()

def beginSim():
    for x in range(0, startPopulation):
        peopleDictionary.append(Person(age=random.randint(18, 50),
                                       name=lastNames[x],
                                       mother=God(),
                                       father=God()))
        peopleDictionaryHistory.append(Person(age=random.randint(18, 50),
                                       name=lastNames[x],
                                       mother=God(),
                                       father=God()))

def faimilyTree():
    ft_list = [{'Person 1': 'God', 'Relation': 'Ancestor', 'Person 2': '', 'Gender': 'M', 'Details': 'Start'}]
    csv_columns = ['Person 1', 'Relation', 'Person 2', 'Gender', 'Details']
    ft = open('FamilyTree.csv', 'a', newline="")
    for person in peopleDictionary:
        if len(person.children) > 0:
            for child in person.children:
                person1 = {"Person 1": child.name}
                relation = {"Relation": "Child"}
                person2 = {"Person 2": person.name}
                gender = {"Gender": 'M' if child.gender == 0 else 'F'}
                details = {"Details": f'{person.name} has {len(person.children)} children'}
                comple = person1
                comple.update(relation)
                comple.update(person2)
                comple.update(gender)
                comple.update(details)
                ft_list.append(comple)
            else:
                person1 = {"Person 1": person.name}
                relation = {"Relation": "Married" if person.married == True else "Partnered"}
                try:
                    person2 = {"Person 2": person.partner.name}
                except AttributeError:
                    person2 = {"Person 2": "No Partner"}
                gender = {"Gender": 'M' if person.gender == 0 else 'F'}
                details = {"Details": 'none'}
                comple = person1
                comple.update(relation)
                comple.update(person2)
                comple.update(gender)
                comple.update(details)
                ft_list.append(comple)
        else:
            person1 = {"Person 1": person.name}
            relation = {"Relation": "Married" if person.married == True else "Partnered"}
            try:
                person2 = {"Person 2": person.partner.name}
            except AttributeError:
                person2 = {"Person 2": "No Partner"}
            gender = {"Gender": 'M' if person.gender == 0 else 'F'}
            details = {"Details": 'none'}
            comple = person1
            comple.update(relation)
            comple.update(person2)
            comple.update(gender)
            comple.update(details)
            ft_list.append(comple)

    writer = csv.DictWriter(ft, fieldnames=csv_columns)
    writer.writeheader()

    for data in ft_list:
        writer.writerow(data)

    ft.close()

beginSim()

while len(peopleDictionary) < 1000 and len(peopleDictionary) > 1:
    runyear = runYear()
else:
    plt.plot(line_year, line_population, label= "Population")
    plt.plot(line_year, line_deaths, label="Deaths")
    plt.plot(line_year, line_children_born, label="Births")
    plt.plot(line_year, line_avg_age, label="Average Age")
    plt.plot(line_year, line_food, label="Food")
    plt.xlabel('Years')
    plt.ylabel('Amount')
    plt.title('Population Simulation')
    plt.legend()
    faimilyTree()

    plt.show()





# for x in peopleDictionary:
#     if x.age > 14:
#         print(f'{x.name} is {x.age} years old {"Male" if x.gender == 0 else "Female"} and is {"Married" if x.married == True else "Partnered"} to ', end='')
#         try:
#             print(f'{x.partner.name} has {len(x.children)} children, father {x.father.name if x.father != "God" else "God"}, mother {x.mother.name if x.mother != "God" else "God"}')
#         except AttributeError:
#             continue
#
# print(f'Alive: {len(peopleDictionary)}, deaths {died_this_year}, births {born_this_year}')



# for x in peopleDictionary:
#     print(f'{x.name} \t\t\t  {"Male" if x.gender == 0 else "Female"} \t\t {"Married" if x.married == True else "Partnered"} to ', end='')
#     try:
#         print(x.partner.name)
#     except AttributeError:
#         print('no one')