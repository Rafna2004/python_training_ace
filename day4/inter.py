def meeting__Rooms(intervals):
    start_times = sorted([i[0] for i in intervals])
    end_times = sorted([i[1] for i in intervals])
    rooms = 0
    max_rooms = 0
    s = 0
    e = 0

    while s < len(start_times):
        if start_times[s] < end_times[e]:
            rooms += 1
            s += 1
        else:
            rooms -= 1
            e += 1

        max_rooms = max(max_rooms, rooms)

    return max_rooms
print(meeting__Rooms([[0, 30], [5, 10], [15, 20]]))