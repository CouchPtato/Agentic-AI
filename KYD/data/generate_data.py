import pandas as pd
from faker import Faker
import random

fake = Faker()
specialties = ["Cardiology", "Dermatology", "Pediatrics", "Orthopedics", "Neurology", 
               "Gynecology", "General Medicine", "Psychiatry", "Urology", "Ophthalmology"]

records = []
num_records = 1000
invalid_fraction = 0.28

for i in range(num_records):
    name = fake.name()
    phone = fake.phone_number()
    address = fake.address().replace("\n", ", ")
    specialty = random.choice(specialties)
    license_no = f"LIC{random.randint(10000,99999)}"
    email = fake.email()
    website = f"https://www.{name.split()[0].lower()}clinic.com"

    if random.random() < invalid_fraction:
        choice = random.choice(["phone", "email", "license_no"])
        if choice == "phone":
            phone = "invalid_phone"
        elif choice == "email":
            email = "invalid_email"
        elif choice == "license_no":
            license_no = ""

    records.append([i+1, name, phone, email, address, specialty, license_no, website])

df = pd.DataFrame(records, columns=[
    "provider_id", "name", "phone", "email", "address", "specialty", "license_no", "website"
])

# import os
# os.makedirs("data", exist_ok=True)

df.to_csv("providers.csv", index=False)
print("✅ Synthetic dataset created with some invalid entries: data/providers.csv")
