import json

from pydantic import ValidationError

from models import JobApplication, Location
with open("data/applications.json", "r") as file:
    data = json.load(file)

valid_applications = []
for application in data:
    try:
        application_draft = JobApplication(**application)
        print(application_draft)
        valid_applications.append(application_draft)

    except ValidationError as e:
        print(f"{application["company"]} not a valid application")
        print(e)

with open("data/processed_applications.json", "w", encoding="utf-8") as file:
    json.dump([application.model_dump(mode="json") for application in valid_applications],file,indent=2)


"""
OUTPUT 

(Pydantic) PS C:\Pratik\AI_Study\AgenticAI\Pydantic\job_tracker_pydantic> python .\main.py
company='Revolut' role='Graduate Software Engineer (Java)' job_url=AnyUrl('https://www.revolut.com/careers') recruiter_email='talent@revolut.com' status='Applied' salary=None applied_on=datetime.date(2026, 10, 20) location=Location(city='Lisbon', country='Portugal') days_since_applied=6
Wrote to data/processed_applications.json
company='Imc Trading' role='Graduate Software Engineer (2027)' job_url=AnyUrl('https://www.imc.com/eu/careers') recruiter_email=None status='Assessment' salary=None applied_on=datetime.date(2026, 10, 15) location=Location(city='Amsterdam', country='Netherlands') days_since_applied=11
Wrote to data/processed_applications.json
company='Bending Spoons' role='Graduate Software Engineer' job_url=AnyUrl('https://jobs.bendingspoons.com/') recruiter_email='hr@bendingspoons.com' status='Offer' salary=70000 applied_on=datetime.date(2026, 9, 1) location=Location(city='Milan', country='Italy') days_since_applied=55
Wrote to data/processed_applications.json
Pinterest not a valid application
1 validation error for JobApplication
job_url
  Input should be a valid URL, relative URL without a base [type=url_parsing, input_value='not-a-valid-url', input_type=str]
    For further information visit https://errors.pydantic.dev/2.14/v/url_parsing
Mistral AI not a valid application
1 validation error for JobApplication
  Value error, Salary is required [type=value_error, input_value={'company': 'Mistral AI',...', 'country': 'France'}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.14/v/value_error
"""