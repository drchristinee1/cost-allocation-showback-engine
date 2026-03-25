import json
from allocation_engine.loader import load_cost_data
from allocation_engine.allocator import allocate_costs

def main():
    print("=== Cost Allocation & Showback Engine ===")

    input_file = "data/sample_costs.json"

    try:
        cost_data = load_cost_data(input_file)
    except FileNotFoundError:
        print(f"Input file not found: {input_file}")
        return

    result = allocate_costs(cost_data)

    print("\n=== Allocation Result ===\n")
    print(json.dumps(result, indent=4))

    output_file = "outputs/allocation_output.json"
    with open(output_file, "w") as f:
        json.dump(result, f, indent=4)

    print(f"\nOutput saved to {output_file}")

if __name__ == "__main__":
    main()
