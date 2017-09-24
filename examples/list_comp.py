#!/usr/bin/python


class Patient():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


if __name__ == '__main__':
    patients = [
        Patient('John', 'Doe'),
        Patient('Jan', 'Kowalski')
    ]

    # it doesn't say anything to me
    print(patients)

    # classic way
    result = []
    for patient in patients:
        result.append(patient.name)
    print(result)

    # list comprehension
    print([patient.name for patient in patients])
