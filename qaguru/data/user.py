from dataclasses import dataclass


@dataclass
class NewUser:
    first_name: str
    last_name: str
    gender: str
    user_email: str
    user_phone_number: str
    subjects: str
    hobbies: str
    address: str
    photo: str
    day_of_birth: str
    month_of_birth: str
    year_of_birth: str
    state: str
    city: str


userFemaleRegistration = NewUser(first_name="Olga",
                                 last_name="Kutuzova",
                                 gender="Female",
                                 user_email="olga_kuz@gmail.com",
                                 user_phone_number="1234567891",
                                 subjects="Computer Science",
                                 hobbies="Reading",
                                 photo="foto.jpg",
                                 address="India",
                                 day_of_birth="05",
                                 month_of_birth="Mar",
                                 year_of_birth="2000",
                                 state="Uttar Pradesh",
                                 city="Lucknow")


@dataclass
class NewUserTextBox:
    full_name: str
    user_email: str
    current_address: str
    permanent_address: str


userTextBox = NewUserTextBox(full_name="Alex",
                             user_email="alex@gmail.com",
                             current_address="India",
                             permanent_address="Pakistan"
                             )
