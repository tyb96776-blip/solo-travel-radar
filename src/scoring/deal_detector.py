def detect_deal(option, historical_price=None):
    if historical_price and historical_price > 0:
        drop = (historical_price - option["total_cost"]) / historical_price * 100
        return {"sudden_drop_percent": round(drop, 1), "is_sudden_drop": drop >= 20}
    return {"sudden_drop_percent": None, "is_sudden_drop": False}
