def gas_stations(distance, tank_size, stations):
    current_diesel = tank_size
    stop_stations = []
    stations.append(distance)

    for i in range(len(stations)):

        if i == 0:
            current_diesel -= stations[i]
            if current_diesel <= 0:
                return []
            continue

        current_diesel -= (stations[i] - stations[i - 1])

        if current_diesel <= 0:
            current_diesel = tank_size - (stations[i] - stations[i - 1])
            if current_diesel <= 0:
                return stop_stations
            stop_stations.append(stations[i - 1])

    return stop_stations


tests = [
    ((320, 90, [50, 80, 140, 180, 220, 290]), [80, 140, 220, 290]),
    ((390, 80, [70, 90, 140, 210, 240, 280, 350]), [70, 140, 210, 280, 350]),
    ((100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150]), [40, 80]),
    ((100, 101, [200]), []),
    ((100, 50, [200]), []),
    ((100, 50, [10, 90]), []),
    ((100, 50, [10, 30]), []),
]

for args, answer in tests:
    if answer == gas_stations(*args):
        print(True)
    else:
        print(False)
