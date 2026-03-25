def allocate_costs(cost_data):
    """
    Allocate direct and shared cloud costs to teams.
    Shared cost is distributed proportionally based on direct cost.
    """

    direct_costs = {}
    shared_cost = 0

    # Step 1: separate direct and shared cost
    for item in cost_data:
        team = item["team"]
        cost = item["cost"]

        if team == "shared":
            shared_cost += cost
        else:
            direct_costs[team] = direct_costs.get(team, 0) + cost

    # Step 2: total direct cost
    total_direct_cost = sum(direct_costs.values())

    # Step 3: allocate shared cost proportionally
    final_allocation = {}

    for team, cost in direct_costs.items():
        if total_direct_cost > 0:
            shared_allocation = (cost / total_direct_cost) * shared_cost
        else:
            shared_allocation = 0

        final_allocation[team] = round(cost + shared_allocation, 2)

    return final_allocation
