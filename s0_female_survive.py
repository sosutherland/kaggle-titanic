import os
import pandas as pd


def submission() -> pd.DataFrame:
    df_test = pd.read_csv("data/test.csv")
    df_test["Survived"] = df_test["Sex"].map({"male": 0, "female": 1})
    return df_test[["PassengerId", "Survived"]]


def main() -> None:
    submission().to_csv(f"submissions/{os.path.basename(__file__)}.csv", index=False)


if __name__ == "__main__":
    main()
