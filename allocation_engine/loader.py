import json

def load_cost_data(file_path):
    """
    Load cost data from a JSON file.
    """

    with open(file_path, "r") as f:
        data = json.load(f)

    return data
