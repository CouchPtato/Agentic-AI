# create_dataset.py
import pandas as pd
from faker import Faker
import random

fake = Faker()
specialties = ["Cardiology", "Dermatology", "Pediatrics", "Orthopedics", "Neurology", 
               "Gynecology", "General Medicine", "Psychiatry", "Urology", "Ophthalmology"]

records = []
for i in range(1000):
    name = fake.name()
    phone = fake.phone_number()
    address = fake.address().replace("\n", ", ")
    specialty = random.choice(specialties)
    license_no = f"LIC{random.randint(10000,99999)}"
    email = fake.email()
    website = f"https://www.{name.split()[0].lower()}clinic.com"
    records.append([i+1, name, phone, email, address, specialty, license_no, website])

df = pd.DataFrame(records, columns=[
    "provider_id", "name", "phone", "email", "address", "specialty", "license_no", "website"
])

df.to_csv("providers.csv", index=False)
print("✅ Synthetic dataset created: providers.csv")
