import os
import pandas as pd
from masking.hashing import hash_value
from masking.tokenization import Tokenizer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, "input_data", "sample_data.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "output_data", "masked_data.csv")

def main():
    print("Looking for:", INPUT_FILE)
    print("Files in input_data:", os.listdir(os.path.join(BASE_DIR, "input_data")))

    df = pd.read_csv(INPUT_FILE)

    name_tokenizer = Tokenizer(prefix="NAME")

    df["name"] = df["name"].apply(name_tokenizer.tokenize)
    df["email"] = df["email"].apply(hash_value)
    df["phone"] = df["phone"].astype(str).apply(hash_value)

    df.to_csv(OUTPUT_FILE, index=False)
    print("Masking completed. Output saved to:", OUTPUT_FILE)

if __name__ == "__main__":
    main()
