import os
import pandas as pd
from masking.hashing import hash_value
from masking.tokenization import Tokenizer
from masking.partial_masking import mask_phone, mask_email
from masking.fake_data import FakeNameGenerator

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, "input_data", "sample_data.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "output_data", "masked_data.csv")

def main():
    df = pd.read_csv(INPUT_FILE)

    # Preserving raw values for derived masking
    raw_name = df["name"]
    raw_email = df["email"]
    raw_phone = df["phone"].astype(str)

    name_tokenizer = Tokenizer(prefix="NAME")
    fake_name_gen = FakeNameGenerator()

    # Additional masking strategies
    df["name_fake"] = raw_name.apply(fake_name_gen.get_fake_name)
    df["phone_partial"] = raw_phone.apply(mask_phone)
    df["email_partial"] = raw_email.apply(mask_email)

    # Primary anonymization
    df["name"] = raw_name.apply(name_tokenizer.tokenize)
    df["email"] = raw_email.apply(hash_value)
    df["phone"] = raw_phone.apply(hash_value)

    df.to_csv(OUTPUT_FILE, index=False)
    print("Masking completed. Output saved to:", OUTPUT_FILE)

if __name__ == "__main__":
    main()
