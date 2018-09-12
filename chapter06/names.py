def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def lookup(data, label, name):
    return data[label].get(name)


def store(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2: names.insert(1, '')
        labels = 'first', 'middle', 'last'
        for name, label in zip(names, labels):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]


MyNames = {}
init(MyNames)
store(MyNames, "Magnus Lie Hetland")
store(MyNames, "Anne Lie Hetland")
store(MyNames, "Jun Zheng", "Luke Skywalker", "Anakin Skywalker")
lookup1 = lookup(MyNames, 'middle', "Lie")
print(f"{lookup1} found!")
print(MyNames)
# zhengjuns-MacBook-Pro:chapter06 zhengjun$ python3 names.py
# ['Magnus Lie Hetland', 'Anne Lie Hetland'] found!
# {'first': {'Magnus': ['Magnus Lie Hetland'], 'Anne': ['Anne Lie Hetland'], 'Jun': ['Jun Zheng']}, 'middle': {'Lie': ['Magnus Lie Hetland', 'Anne Lie Hetland'], '': ['Jun Zheng']}, 'last': {'Hetland': ['Magnus Lie Hetland', 'Anne Lie Hetland'], 'Zheng': ['Jun Zheng']}}
