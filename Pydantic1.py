from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int


patient = Patient(name="Shardul", age="thirty")

def update_patient_data(patient: Patient):
    print("Inserting patient data")
    print("Name: ", patient.name)
    print("Age: ", patient.age)
    print("Patient data updated")


update_patient_data(patient)

"""
OUTPUT 

(Pydantic) PS C:\Pratik\AI_Study\AgenticAI\Pydantic> py .\Pydantic1.py
Traceback (most recent call last):
  File "C:\Pratik\AI_Study\AgenticAI\Pydantic\Pydantic1.py", line 8, in <module>
    patient = Patient(name="Shardul", age="thirty")
  File "C:\Pratik\AI_Study\AgenticAI\Pydantic\.venv\Lib\site-packages\pydantic\main.py", line 280, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for Patient
age                                                                                                                                                                                 
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='thirty', input_type=str]                                                    
    For further information visit https://errors.pydantic.dev/2.14/v/int_parsing      

"""