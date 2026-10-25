#Case 1 : Basic typehinting, but still no enforcement

def insert_patient_data(name: str, age: int):
    if type(name) is str and type(age) is int:
        print("Inserting patient data")
        print("Name: ", name)
        print("Age: ", age)
        print("Patient data inserted")
    else:
        raise TypeError("Not valid format")



def update_patient_data(name: str, age: int):
    if type(name) is str and type(age) is int:
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
Traceback (most recent call last):
  File "C:\Pratik\AI_Study\AgenticAI\Pydantic\typehinting_and_validation.py", line 25, in <module>
    insert_patient_data("Shardul", "twenty-six")
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Pratik\AI_Study\AgenticAI\Pydantic\typehinting_and_validation.py", line 10, in insert_patient_data
    raise TypeError("Not valid format")
TypeError: Not valid format
"""