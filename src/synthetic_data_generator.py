import random
import pandas as pd

def generate_campaign_data(rows=50):
    data = []

    for i in range(rows):
        impressions = random.randint(5000, 20000)
        clicks = int(impressions * random.uniform(0.01, 0.04))
        sales = int(clicks * random.uniform(0.02, 0.06))
        revenue = sales * random.randint(8000, 15000)
        ad_spend = clicks * random.uniform(20, 60)

        data.append([
            f"MLA{i+1000}",
            impressions,
            clicks,
            sales,
            revenue,
            round(ad_spend, 2)
        ])

    return pd.DataFrame(
        data,
        columns=["product_id", "impressions", "clicks", "sales", "revenue", "ad_spend"]
    )


if __name__ == "__main__":
    df = generate_campaign_data()
    df.to_csv("synthetic_campaign_data.csv", index=False)
