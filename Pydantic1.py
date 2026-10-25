from pydantic import BaseModel
#Does also type coercian understands '30' is 30
class Patient(BaseModel):
    name: str
    age: int


patient = Patient(name="Shardul", age="30")

patient_info = {"name": "Pratik", "age": 26}

patient2 = Patient(**patient_info)

"""
** unpacks a dictionary into named arguments.

patient_info = {"name": "Pratik", "age": 26}

Patient(**patient_info)
# is exactly the same as
Patient(name="Pratik", age=26)
"""

def update_patient_data(patient: Patient):
    print("Inserting patient data")
    print("Name: ", patient.name)
    print("Age: ", patient.age)
    print("Patient data updated")


update_patient_data(patient2)

"""
OUTPUT 

(Pydantic) PS C:\Pratik\AI_Study\AgenticAI\Pydantic> py .\Pydantic1.py
C:\Pratik\AI_Study\AgenticAI\Pydantic\Pydantic1.py:26: SyntaxWarning: "\P" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\P"? A raw string is also an option.
  (Pydantic) PS C:\Pratik\AI_Study\AgenticAI\Pydantic> py .\Pydantic1.py
Inserting patient data
Name:  Pratik
Age:  26
Patient data updated   

"""