import pandas as pd
from acos_calculator import calculate_acos
from campaign_decision_engine import campaign_decision
from acos_optimizer import optimize_acos

def run_campaign_simulation(data_path, target_acos):
    df = pd.read_csv(data_path)

    results = []

    for _, row in df.iterrows():
        acos = calculate_acos(row["ad_spend"], row["revenue"])
        decision = campaign_decision(
            acos=acos,
            target_acos=target_acos,
            conversion_rate=(row["sales"] / row["clicks"]) * 100
        )

        optimized_acos = optimize_acos(
            current_acos=target_acos,
            performance_trend="improving" if acos <= target_acos else "declining"
        )

        results.append({
            "product_id": row["product_id"],
            "current_acos": acos,
            "decision": decision,
            "next_target_acos": optimized_acos
        })

    return pd.DataFrame(results)


if __name__ == "__main__":
    output = run_campaign_simulation(
        data_path="data_sample.csv",
        target_acos=10
    )
    print(output)
