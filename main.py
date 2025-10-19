import pandas as pd
from KYD.agents.validation_agent import DataValidationAgent

def main():
    print("\n🚀 Starting Provider Validation Pipeline...\n")

    df = pd.read_csv("KYD/data/providers.csv")
    print(f"Loaded {len(df)} provider records\n")

    val_agent = DataValidationAgent()

    validated = val_agent.run(df)
    
    print(validated)

    valid_count = (validated["status"] == "Valid").sum()
    print("Valid entries :", valid_count)
    invalid_count = (validated["status"] == "Needs Review").sum()
    print("Needs review :", invalid_count)

if __name__ == "__main__":
    main()