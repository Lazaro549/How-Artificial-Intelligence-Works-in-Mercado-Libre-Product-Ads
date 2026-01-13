def calculate_ad_rank(ad_score: float, target_acos: float) -> float:
    """
    Simplified ad-rank model for educational purposes.

    Higher ad-score and competitive ACOS improve ranking.
    """
    if target_acos == 0:
        return 0.0

    return round(ad_score / target_acos, 4)


if __name__ == "__main__":
    ad_score = 8.5      # Listing quality
    target_acos = 0.12 # 12%

    ad_rank = calculate_ad_rank(ad_score, target_acos)
    print(f"Ad Rank Score: {ad_rank}")
