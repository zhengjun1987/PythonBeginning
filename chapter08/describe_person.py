def describe_person(person):
    print(f"Description of {person['name']}")
    print(f"Age: {person['age']}")
    # if 'occupation' in person:
    #     print(f"Occupation: {person['occupation']}")
    try:
        print(f"Occupation: {person['occupation']}")
    except KeyError:
        pass