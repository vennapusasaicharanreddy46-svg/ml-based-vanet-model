import traci
import random

SUMO_BINARY = "sumo-gui"
CONFIG_FILE = "config/simulation.sumocfg"

traci.start([SUMO_BINARY, "-c", CONFIG_FILE])

ACCIDENT_EDGE = "N8_N9"
MODE = "NORMAL"
step = 0

while step < 1500:

    traci.simulationStep()

    # ---------------- CREATE ACCIDENT ----------------
    if step == 800:
        MODE = "ACCIDENT"
        print("🚨 ACCIDENT AT N8 → N9")

        traci.vehicle.add(
            vehID="crash_car_1",
            routeID="normal_route_3",
            typeID="normal"
        )

        traci.vehicle.add(
            vehID="crash_car_2",
            routeID="normal_route_3",
            typeID="normal"
        )

        # Move crash vehicles to accident location
        traci.vehicle.moveTo("crash_car_1", "N8_N9_0", 40)
        traci.vehicle.moveTo("crash_car_2", "N8_N9_0", 42)

        # Stop crash vehicles
        traci.vehicle.setSpeed("crash_car_1", 0)
        traci.vehicle.setSpeed("crash_car_2", 0)

        # Color them red
        traci.vehicle.setColor("crash_car_1", (255, 0, 0))
        traci.vehicle.setColor("crash_car_2", (255, 0, 0))

        # Reduce speed of accident edge
        traci.edge.setMaxSpeed(ACCIDENT_EDGE, 1)

    vehicles = traci.vehicle.getIDList()

    for veh in vehicles:

        if traci.vehicle.getTypeID(veh) != "normal":
            continue

        current_edge = traci.vehicle.getRoadID(veh)

        # ---------------- REROUTE VEHICLES ----------------
        if MODE == "ACCIDENT":

            if current_edge == "N7_N8":

                decision = random.random()

                if decision < 0.5:
                    # Route 1: N7-N8-N5-N6-N3
                    new_route = [
                        "N7_N8",
                        "N8_N5",
                        "N5_N6",
                        "N6_N3"
                    ]
                else:
                    # Route 2: N7-N8-N5-N6-N9
                    new_route = [
                        "N7_N8",
                        "N8_N5",
                        "N5_N6",
                        "N6_N9"
                    ]

                traci.vehicle.setRoute(veh, new_route)

    step += 1

traci.close()
print("Simulation Finished Successfully")

