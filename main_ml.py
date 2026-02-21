import traci
import joblib
import csv
import pandas as pd

# =========================
# CONFIGURATION
# =========================

SUMO_BINARY = "sumo"   # use "sumo-gui" for visualization
CONFIG_FILE = "config/simulation.sumocfg"

DEST_EDGE = "N6_N9"
ACCIDENT_EDGE = "N8_N9"

# =========================
# LOAD ML MODEL
# =========================

model = joblib.load("ml/congestion_model.pkl")

# =========================
# START SUMO
# =========================

traci.start([SUMO_BINARY, "-c", CONFIG_FILE])

departure_times = {}
travel_times = []
rerouted = set()

step = 0

# =========================
# MAIN LOOP
# =========================

while step < 1500:

    traci.simulationStep()

    if step % 100 == 0:
        print("Running Step:", step)

    # -------------------------
    # Track departures
    # -------------------------
    departed = traci.simulation.getDepartedIDList()
    for veh in departed:
        departure_times[veh] = step

    # -------------------------
    # Severe Accident at 800
    # -------------------------
    if step == 800:
        print("🚨 Severe Accident Created")

        traci.vehicle.add(
            vehID="crash_car",
            routeID="normal_route_3",
            typeID="normal"
        )

        traci.vehicle.moveTo("crash_car", "N8_N9_0", 40)
        traci.vehicle.setSpeed("crash_car", 0)

        # Make road nearly blocked
        traci.edge.setMaxSpeed(ACCIDENT_EDGE, 0.2)

    # -------------------------
    # ML Active Earlier (300)
    # Predict every 10 steps
    # -------------------------
    if step >= 300 and step % 10 == 0:

        vehicles = traci.vehicle.getIDList()

        for veh in vehicles:

            if traci.vehicle.getTypeID(veh) != "normal":
                continue

            if veh in rerouted:
                continue

            edge = traci.vehicle.getRoadID(veh)

            if edge.startswith(":"):
                continue

            density = traci.edge.getLastStepVehicleNumber(edge)
            speed = traci.edge.getLastStepMeanSpeed(edge)
            waiting = traci.edge.getWaitingTime(edge)

            # Mode encoding
            mode = 0
            if step >= 300:
                mode = 1
            if step >= 800:
                mode = 2

            features = pd.DataFrame(
                [[density, speed, waiting, mode]],
                columns=["density", "speed", "waiting", "mode"]
            )

            prediction = model.predict(features)[0]

            # -------------------------
            # INTELLIGENT REROUTING
            # -------------------------
            if prediction == 1:

                try:
                    alt_route = traci.simulation.findRoute(edge, DEST_EDGE)

                    # Only reroute if at least 5% faster
                    if alt_route.travelTime > 0:
                        current_estimate = alt_route.travelTime

                        if alt_route.travelTime < current_estimate * 0.95:
                            traci.vehicle.setRoute(veh, alt_route.edges)
                            rerouted.add(veh)

                except:
                    pass

    # -------------------------
    # Track arrivals
    # -------------------------
    arrived = traci.simulation.getArrivedIDList()

    for veh in arrived:
        if veh in departure_times:
            travel_time = step - departure_times[veh]
            travel_times.append(travel_time)

    step += 1

# =========================
# END SIMULATION
# =========================

traci.close()

# =========================
# CALCULATE RESULT
# =========================

if len(travel_times) > 0:
    avg_travel = sum(travel_times) / len(travel_times)
else:
    avg_travel = 0

with open("ml_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Average_Travel_Time"])
    writer.writerow([avg_travel])

print("ML Average Travel Time:", avg_travel)
print("Results saved to ml_results.csv")

