day_lst = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
time_lst = ["Morning", "Afternoon"]
# =======================
# starting read all files
# =======================
f = open("busy.csv", 'r')
f_containment = f.read().splitlines()
f.close()
busy = [f_containment[i].split(';') for i in range(len(f_containment))]
busy = [[int(busy[i][j]) if busy[i][j].isnumeric() else busy[i][j] for j in range(len(busy[i]))] for i in
        range(len(busy))]
f = open("classroom.csv", 'r')
f_containment = f.read().splitlines()
f.close()
classroom = [f_containment[i].split(';') for i in range(len(f_containment))]
classroom = [
    [int(classroom[i][j]) if classroom[i][j].isnumeric() else classroom[i][j] for j in range(len(classroom[i]))] for i
    in range(len(classroom))]
f = open("service.csv", 'r')
f_containment = f.read().splitlines()
f.close()
service = [f_containment[i].split(';') for i in range(len(f_containment))]
service = [[int(service[i][j]) if service[i][j].isnumeric() else service[i][j] for j in range(len(service[i]))] for i in
           range(len(service))]
f = open("Courses.csv", 'r')
f_containment = f.read().splitlines()
f.close()
courses = [f_containment[i].split(';') for i in range(len(f_containment))]
courses = [[int(courses[i][j]) if courses[i][j].isnumeric() else courses[i][j] for j in range(len(courses[i]))] for i in
           range(len(courses))]
# =================================
# sorting and parsing initial files
# =================================
courses_dict = []
elective_dict = []
busy_dict = []
service_dict = []
# cleanup courses:

for i in range(len(courses)):  # Parsing Courses to 2 dict arrays, courses_dict and elective_dict
    if courses[i][5] == 'S':
        index = [service[i][0] for i in range(len(service))].index(courses[i][0])
        service_dict.append(
            {
                "l_name": "".join([i for i in courses[i][0] if not i.isnumeric()]),
                "l_code": int("".join([i for i in courses[i][0] if i.isnumeric()])),
                "day": service[index][1],
                "time": service[index][2],
                "t_name": courses[i][6]
            }
        )
    elif courses[i][4] == 'C':  # if this is a Course:
        courses_dict.append(
            {
                # t_name attribute -> teacher name
                # l_name is lesson name (code)
                # l_code is lesson code
                # so, for "CENG101", l_name is "CENG" and l_code is 101
                "l_name": "".join([i for i in courses[i][0] if not i.isnumeric()]),
                "l_code": int("".join([i for i in courses[i][0] if i.isnumeric()])),
                "t_name": courses[i][6]
            }
        )
    else:  # or if this is a Elective
        elective_dict.append(
            {
                "l_name": "".join([i for i in courses[i][0] if not i.isnumeric()]),
                "l_code": int("".join([i for i in courses[i][0] if i.isnumeric()])),
                "t_name": courses[i][6]
            }
        )
for i in range(len(busy)):
    busy_dict.append(
        {
            "t_name": busy[i][0],
            "day": busy[i][1],
            "time": busy[i][2]
        }
    )
# sort
courses_dict.sort(key=lambda x: x['l_code'], reverse=True)
elective_dict.sort(key=lambda x: x['l_code'], reverse=True)


# ====================
# teacher availability
# ====================
def t_isAvailable(t_name, day, time):
    b = True  # boolean
    for i in range(len(busy_dict)):
        tmp_lst = list(busy_dict[i].values())
        if tmp_lst.__contains__(t_name) and tmp_lst.__contains__(day) and tmp_lst.__contains__(time):
            b = False
    return b


# ==================================
# amount of grades for proper output
# ==================================
def getLeastGrades():
    _1st = 0
    _2nd = 0
    _3rd = 0
    _4th = 0
    for c in courses_dict:
        if c["l_code"] // 100 == 1:
            _1st += 1
        if c["l_code"] // 100 == 2:
            _2nd += 1
        if c["l_code"] // 100 == 3:
            _3rd += 1
        if c["l_code"] // 100 == 4:
            _4th += 1
    for s in service_dict:
        if s["l_code"] // 100 == 1:
            _1st += 1
        if s["l_code"] // 100 == 2:
            _2nd += 1
        if s["l_code"] // 100 == 3:
            _3rd += 1
        if s["l_code"] // 100 == 4:
            _4th += 1
    for e in elective_dict:
        if e["l_code"] // 100 == 1:
            _1st += 1
        if e["l_code"] // 100 == 2:
            _2nd += 1
        if e["l_code"] // 100 == 3:
            _3rd += 1
        if e["l_code"] // 100 == 4:
            _4th += 1
    tmp = [_1st, _2nd, _3rd, _4th]
    tmp_sorted = sorted(tmp, reverse=True)
    tmp_indexes = []
    for i in range(4):
        tmp_indexes.append(tmp.index(tmp_sorted[i]) + 1)
        tmp[tmp_indexes[-1] - 1] = 99
    return tmp_indexes  # note: this is actually a list of grades in descending order of their amount


# ===================
# lesson availability
# ===================
def getLessonBig(day, time, *locked):
    # parse for *locked:
    locked = list(locked)
    locked_dict = []
    for i in range(len(locked)):
        if locked[i] is None:
            locked[i] = "ZZZ999"  # just unfixable bug =( don't trying to understand why this happened
        locked_dict.append(int("".join([i for i in locked[i] if i.isnumeric()])))
    # check services first:
    for i in range(len(service_dict)):
        tmp_srv = list(service_dict[i].values())  # temp_service, just values without keys
        if tmp_srv.__contains__(day) and tmp_srv.__contains__(time):
            service_dict.remove(service_dict[i])
            return [tmp_srv[0] + str(tmp_srv[1]), tmp_srv[4], day, time]
    # parse in queue:
    for priority in getLeastGrades():
        # if service with priority grade not found try to find course in courses_dict
        for i in range(len(courses_dict)):
            tmp_crs = courses_dict[i]
            lock = False
            for j in range(len(locked_dict)):
                if locked_dict[j] // 100 == tmp_crs["l_code"] // 100 or tmp_crs["l_code"] // 100 != priority:
                    lock = True  # lock is for go next if course is wrong
            if lock:
                continue
            if t_isAvailable(tmp_crs["t_name"], day, time):
                courses_dict.remove(courses_dict[i])
                return [tmp_crs["l_name"] + str(tmp_crs["l_code"]), tmp_crs["t_name"], day, time]
    # if no one finded
    return [None, None, day, time]


def getLessonSmall(day, time, *locked):  # elective
    # parse for *locked:
    locked = list(locked)
    locked_dict = []
    for i in range(len(locked)):
        if locked[i] is None:
            locked[i] = "ZZZ999"  # just unfixable bug =( don't trying to understand why this happened
        locked_dict.append(int("".join([i for i in locked[i] if i.isnumeric()])))
    # check elective from elective_dict for this day and time
    for priority in getLeastGrades():
        for i in range(len(elective_dict)):
            tmp_crs = elective_dict[i]
            lock = False
            for j in range(len(locked_dict)):
                if locked_dict[j] // 100 == tmp_crs["l_code"] // 100 or tmp_crs["l_code"] // 100 != priority:
                    lock = True
            if lock:
                continue
            if t_isAvailable(tmp_crs["t_name"], day, time):
                elective_dict.remove(elective_dict[i])
                return [tmp_crs["l_name"] + str(tmp_crs["l_code"]), tmp_crs["t_name"], day, time]
    return [None, None, day, time]


# ===============
#      main
# ===============

print(
    f"amount of electives: {len(elective_dict)}\namount of courses: {len(courses_dict)}\namount of services: {len(service_dict)}")
schedule = []
for day in day_lst:
    schedule.append({
        "day": day,
        "day_schedule": []
    })
    for time in time_lst:
        schedule[day_lst.index(day)]["day_schedule"].append({
            "time": time,
            "time_schedule": []
        })
        tmp = []
        lock_tmp = []
        # assign courses and services to big rooms
        for i in range(classroom[0][1]):
            tmp.append(getLessonBig(day, time, *lock_tmp))
            lock_tmp.append(tmp[-1][0])
            # PS: it is no really a problem, ignore flashing.
            # noinspection PyTypeChecker
            schedule[day_lst.index(day)]["day_schedule"][time_lst.index(time)]["time_schedule"].append({
                "lesson": tmp[i][0],
                "t_name": tmp[i][1],
                "lesson_type": "course",
                "room_type": "big"
            })
        tmp = []
        # assign electives to small rooms
        for i in range(classroom[1][1]):
            tmp.append(getLessonSmall(day, time, *lock_tmp))
            lock_tmp.append(tmp[-1][0])
            # noinspection PyTypeChecker
            schedule[day_lst.index(day)]["day_schedule"][time_lst.index(time)]["time_schedule"].append({
                "lesson": tmp[i][0],
                "t_name": tmp[i][1],
                "lesson_type": "elective",
                "room_type": "small"
            })
        tmp = []
        # assign electives to big rooms if big room is empty
        # noinspection PyTypeChecker
        for i in range(len(schedule[day_lst.index(day)]["day_schedule"][time_lst.index(time)]["time_schedule"])):
            # noinspection PyTypeChecker
            if schedule[day_lst.index(day)]["day_schedule"][time_lst.index(time)]["time_schedule"][i]["lesson"] is None:
                tmp.append(getLessonSmall(day, time, *lock_tmp))
                lock_tmp.append(tmp[-1][0])
                # noinspection PyTypeChecker
                schedule[day_lst.index(day)]["day_schedule"][
                    time_lst.index(time)]["time_schedule"][i] = {
                    "lesson": tmp[-1][0],
                    "t_name": tmp[-1][1],
                    "lesson_type": "elective",
                    "room_type": "big"
                }

for day_iter in range(5):
    day = day_lst[day_iter]
    print(f"in {day}:")
    for time_iter in range(2):
        time = time_lst[time_iter]
        print(f"\tin {time}:")
        for room_iter in range(3):
            # noinspection PyTypeChecker
            room = schedule[day_iter]["day_schedule"][time_iter]["time_schedule"][room_iter]["room_type"]
            # noinspection PyTypeChecker
            lesson_code = schedule[day_iter]["day_schedule"][time_iter]["time_schedule"][room_iter]["lesson"]
            # noinspection PyTypeChecker
            teacher_name = schedule[day_iter]["day_schedule"][time_iter]["time_schedule"][room_iter]["t_name"]
            # noinspection PyTypeChecker
            lesson_type = schedule[day_iter]["day_schedule"][time_iter]["time_schedule"][room_iter]["lesson_type"]
            print(f"\t\t{lesson_code} {lesson_type} in {room} room with {teacher_name}")
