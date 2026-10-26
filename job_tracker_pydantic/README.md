# Job Application Tracker – Pydantic Validation

A small Python project that validates job applications with **Pydantic v2**.
It reads applications from a JSON file, rejects invalid entries with clear error
messages, and saves the clean, validated ones to a new file.

## Features

- **Type validation and coercion**: URLs, emails, dates and salaries are checked automatically (`"70000"` becomes `70000`)
- **Nested models**: each application contains a `Location` model
- **Field validator**: cleans company names (`"  revolut "` → `"Revolut"`) and rejects empty ones
- **Model validator**: an application with status `Offer` must include a salary
- **Computed field**: `days_since_applied` is calculated from the application date
- **Serialization**: valid applications are exported to JSON, with the recruiter email excluded for privacy

## Project structure

```
job_tracker_pydantic/
├── models.py                          # Pydantic models and validators
├── main.py                            # load → validate → report → save
└── data/
    ├── applications.json              # input (includes invalid entries on purpose)
    └── processed_applications.json    # output (valid entries only)
```

## How to run

```bash
uv add "pydantic[email]"
uv run python main.py
```

## Sample output

```
company='Revolut' role='Graduate Software Engineer (Java)' status='Applied' ... days_since_applied=6
Pinterest not a valid application
job_url
  Input should be a valid URL, relative URL without a base [type=url_parsing]
Mistral AI not a valid application
  Value error, Salary is required [type=value_error]
```

3 of 5 applications pass validation and are saved to `data/processed_applications.json`.

## What I learned

Building Pydantic models with field and model validators, computed fields,
nested models, and controlled serialization with `model_dump`.