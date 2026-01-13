import pandas as pd
from sklearn.linear_model import LinearRegression

def train_sales_prediction_model(df: pd.DataFrame):
    X = df[["clicks", "impressions", "ad_spend"]]
    y = df["sales"]

    model = LinearRegression()
    model.fit(X, y)

    return model


if __name__ == "__main__":
    data = pd.read_csv("data_sample.csv")
    model = train_sales_prediction_model(data)

    prediction = model.predict([[300, 14000, 22000]])
    print(f"Predicted sales: {int(prediction[0])}")
