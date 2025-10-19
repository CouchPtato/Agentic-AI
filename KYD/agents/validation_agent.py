import re
import random
import pandas as pd

class DataValidationAgent:
    def __init__(self):
        pass

    def validate_phone(self, phone):
        return 0.9 if re.match(r"^[0-9\-\(\) ]{7,15}$", phone) else 0.4

    def validate_email(self, email):
        return 0.95 if re.match(r"[^@]+@[^@]+\.[^@]+", email) else 0.5

    def simulate_npi_check(self, name):
        return random.uniform(0.8, 0.98)

    def process(self, row):
        phone_conf = self.validate_phone(row["phone"])
        email_conf = self.validate_email(row["email"])
        npi_conf = self.simulate_npi_check(row["name"])
        avg_conf = round((phone_conf + email_conf + npi_conf) / 3, 2)

        return {
            "provider_id": row["provider_id"],
            "name": row["name"],
            "validation_score": avg_conf,
            "status": "Valid" if avg_conf > 0.7 else "Needs Review"
        }

    def run(self, df):
        results = [self.process(row) for _, row in df.iterrows()]
        return pd.DataFrame(results)
