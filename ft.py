import matplotlib.pyplot as plt
from treelib import Node, Tree
import webbrowser
import sys, pathlib, os, csv


line_year = [1]
line_population = [0]
line_avg_age = [0]
line_deaths = [0]
line_children_born = [0]
line_food = [0]

def plot_graph(people, child, death, food):
    global line_year, line_population, line_avg_age, line_max_workers, line_deaths, line_children_born, born_this_year, died_this_year
    # line_deaths.append(death)
    # line_children_born.append(child)
    line_year.append(line_year[-1] + 1)
    line_population.append(len(people))
    line_food.append(food)

    avg = []
    for person in people:
        avg.append(person.age)
    try:
        line_avg_age.append(sum(avg) / len(people))
    except ZeroDivisionError:
        line_avg_age.append(0)



def show_graph():
    plt.plot(line_year, line_population, label="Population", color=[0, 1, 0])
    # plt.plot(line_year, line_deaths, label="Deaths", color=[1, 0, 0])
    # plt.plot(line_year, line_children_born, label="Births", color=[0, 0, 0])
    plt.plot(line_year, line_avg_age, label="Average Age", color=[1, 1, 0])
    plt.plot(line_year, line_food, label="Food", color=[0, 0, 1])
    plt.xlabel('Years')
    plt.ylabel('Amount')
    plt.title('Population Simulation')
    plt.legend()
    plt.show()

def familyTree(peopleDictionaryHistory):
    tree = Tree()
    tree.create_node("THE CREATOR", "God")  #root node

    for x in range(0, len(peopleDictionaryHistory)):
        tree.create_node(peopleDictionaryHistory[x][0], peopleDictionaryHistory[x][1], peopleDictionaryHistory[x][2])
    with open('output.txt', 'a', encoding='utf-8') as f:
        sys.stdout = f
        tree.show()

    url = pathlib.Path(f'{os.path.dirname(os.path.abspath(__file__))}\output.txt')
    webbrowser.open_new_tab(url)

def faimilyTree_Spreadsheet(peopleDictionary, id):
    ft_list = []
    csv_columns = ['Person 1', 'Relation', 'Person 2', 'Gender', 'Details']
    ft = open(f'FamilyTree_{id}.csv', 'a', newline="")
    for person in peopleDictionary:
        if person.id == id:
            person1 = {"Person 1": person.name}
            relation = {"Relation": "Married" if person.married == True else "Partnered"}
            try:
                person2 = {"Person 2": person.partner.name}
            except AttributeError:
                person2 = {"Person 2": "No Partner"}
            gender = {"Gender": 'M' if person.gender == 0 else 'F'}
            details = {"Details": f'Children Below, age {person.age}' if len(person.children) > 0 else f'age {person.age}'}
            comple = person1
            comple.update(relation)
            comple.update(person2)
            comple.update(gender)
            comple.update(details)
            ft_list.append(comple)
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




    writer = csv.DictWriter(ft, fieldnames=csv_columns)
    writer.writeheader()

    for data in ft_list:
        writer.writerow(data)

    ft.close()

def faimilyTreeAll_Spreadsheet(peopleDictionary):
    ft_list = []
    csv_columns = ['Person 1', 'Relation', 'Person 2', 'Gender', 'Details']
    ft = open('FamilyTree.csv', 'a', newline="")
    for person in peopleDictionary:
        person1 = {"Person 1": person.name}
        relation = {"Relation": "Married" if person.married == True else "Partnered"}
        try:
            person2 = {"Person 2": person.partner.name}
        except AttributeError:
            person2 = {"Person 2": "No Partner"}
        gender = {"Gender": 'M' if person.gender == 0 else 'F'}
        details = {"Details": f'Children Below, age {person.age}' if len(person.children) > 0 else f'age {person.age}'}
        compile = person1
        compile.update(relation)
        compile.update(person2)
        compile.update(gender)
        compile.update(details)
        ft_list.append(compile)
        if len(person.children) > 0:
            for child in person.children:
                person1 = {"Person 1": child.name}
                relation = {"Relation": "Child"}
                person2 = {"Person 2": person.name}
                gender = {"Gender": 'M' if child.gender == 0 else 'F'}
                details = {"Details": f'{person.name} has {len(person.children)} children'}
                compile = person1
                compile.update(relation)
                compile.update(person2)
                compile.update(gender)
                compile.update(details)
                ft_list.append(compile)

    writer = csv.DictWriter(ft, fieldnames=csv_columns)
    writer.writeheader()

    for data in ft_list:
        writer.writerow(data)

    ft.close()