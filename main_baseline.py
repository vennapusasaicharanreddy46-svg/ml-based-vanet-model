import traci
import csv

SUMO_BINARY = "sumo"
CONFIG_FILE = "config/simulation.sumocfg"

traci.start([SUMO_BINARY, "-c", CONFIG_FILE])

ACCIDENT_EDGE = "N8_N9"

departure_times = {}
travel_times = []

step = 0

while step < 1500:

    traci.simulationStep()

    # Record departure times
    departed = traci.simulation.getDepartedIDList()
    for veh in departed:
        departure_times[veh] = step

    # Create accident
    if step == 800:
        traci.vehicle.add(
            vehID="crash_car",
            routeID="normal_route_3",
            typeID="normal"
        )
        traci.vehicle.moveTo("crash_car", "N8_N9_0", 40)
        traci.vehicle.setSpeed("crash_car", 0)
        traci.edge.setMaxSpeed(ACCIDENT_EDGE, 1)

    # Record arrival times
    arrived = traci.simulation.getArrivedIDList()
    for veh in arrived:
        if veh in departure_times:
            travel_time = step - departure_times[veh]
            travel_times.append(travel_time)

    step += 1

traci.close()

avg_travel = sum(travel_times) / len(travel_times)

with open("baseline_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Average_Travel_Time"])
    writer.writerow([avg_travel])

print("Baseline Average Travel Time:", avg_travel)

