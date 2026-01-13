import pandas as pd

def load_campaign_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def calculate_ctr(clicks: int, impressions: int) -> float:
    if impressions == 0:
        return 0.0
    return round((clicks / impressions) * 100, 2)


def calculate_conversion_rate(sales: int, clicks: int) -> float:
    if clicks == 0:
        return 0.0
    return round((sales / clicks) * 100, 2)


if __name__ == "__main__":
    df = load_campaign_data("data_sample.csv")

    df["CTR (%)"] = df.apply(
        lambda row: calculate_ctr(row["clicks"], row["impressions"]), axis=1
    )

    df["Conversion Rate (%)"] = df.apply(
        lambda row: calculate_conversion_rate(row["sales"], row["clicks"]), axis=1
    )

    print(df)
