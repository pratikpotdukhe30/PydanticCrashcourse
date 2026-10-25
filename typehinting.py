#Case 1 : Basic typehinting, but still no enforcement

def insert_patient_data(name: str, age: int):
    print("Inserting patient data")
    print("Name: ", name)
    print("Age: ", age)
    print("Patient data inserted")


def update_patient_data(name: str, age: int):
    print("Inserting patient data")
    print("Name: ", name)
    print("Age: ", age)
    print("Patient data updated")


insert_patient_data("Shardul", 26)


insert_patient_data("Shardul", "twenty-six")

""" Output
Inserting patient data
Name:  Shardul
Age:  26
Patient data inserted
Inserting patient data
Name:  Shardul
Age:  twenty-six
Patient data inserted
"""