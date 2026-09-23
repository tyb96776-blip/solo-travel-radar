import sys
from src.travel.trip_generator import generate_trip_options
from src.scoring.deal_detector import detect_deal
from src.scoring.price_score import price_score

def run(mode):
    options = generate_trip_options()
    for option in options:
        option["price_score"] = price_score(option["total_cost"])
        option["deal"] = detect_deal(option)
    print(f"mode={mode}, generated_options={len(options)}")
    for item in options[:10]:
        print(item)

if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv) > 1 else "weekly")
