import argparse
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

# === Configuration ===
MODEL_PATH = "task2_model.pkl"
SCALER_PATH = "task2_scaler.pkl"
SKEWED_FEATURES = [
    "Search Count", "Survey", "Google Sense", "Branch Counts"
]


def load_artifacts():
    print("Loading model and scaler...")
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    return model, scaler


def preprocess(df):
    print("Preprocessing input data...")

    # Drop non-feature columns if present
    if 'ID' in df.columns:
        df = df.drop(columns=['ID'])

    # Apply log1p to skewed features
    for col in SKEWED_FEATURES:
        if col in df.columns:
            df[col] = np.log1p(df[col])

    return df


def main(input_path, output_path):
    # Load new data
    df_new = pd.read_csv(input_path)
    print(f"Loaded {len(df_new)} rows from {input_path}")

    # Preprocess
    df_features = preprocess(df_new.copy())

    # Load model and scaler
    model, scaler = load_artifacts()

    # Scale features
    X_scaled = scaler.transform(df_features)

    # Predict
    print("Making predictions...")
    predictions = model.predict(X_scaled)
    df_new["Predicted_Grade"] = predictions

    # Save output
    df_new.to_csv(output_path, index=False)
    print(f"Predictions saved to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict restaurant grades using trained model.")
    parser.add_argument("--input", "-i", type=Path, required=True, help="Path to input CSV file")
    parser.add_argument("--output", "-o", type=Path, required=True, help="Path to output CSV file")

    args = parser.parse_args()
    main(args.input, args.output)
