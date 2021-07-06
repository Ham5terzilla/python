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
print(f"stats after parsing:")
for i in range(len(courses)):  # Parsing Courses to 2 dict arrays, courses_dict and elective_dict
    if courses[i][5] == 'S':
        continue
    if courses[i][4] == 'C':  # if this is a Course:
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
for i in range(len(service)):
    service_dict.append(
        {
            "l_name": "".join([i for i in service[i][0] if not i.isnumeric()]),
            "l_code": int("".join([i for i in service[i][0] if i.isnumeric()])),
            "day": service[i][1],
            "time": service[i][2]
        }
    )
# sort
courses_dict.sort(key=lambda x: x['l_code'])
elective_dict.sort(key=lambda x: x['l_code'])


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


# ===================
# lesson availability
# ===================
def getLessonBig(day, time, *locked):
    # parse for *locked:
    locked = list(locked)
    locked_dict = []
    for i in range(len(locked)):
        if locked[i] is None:
            locked[i] = "a1"  # just unfixable bug =( don't trying to understand why this happened
        locked_dict.append(
            {
                "l_name": "".join([i for i in locked[i] if not i.isnumeric()]),
                "l_code": int("".join([i for i in locked[i] if i.isnumeric()]))
            }
        )
    # check is this day for service:
    for i in range(len(service_dict)):
        tmp_srv = list(service_dict[i].values())  # temp_service, just values in every index of service_dict
        if tmp_srv.__contains__(day) and tmp_srv.__contains__(time):
            service_dict.remove(service_dict[i])
            return [tmp_srv[0] + str(tmp_srv[1]), "external", day, time]
    # if service not founded / not exist for this day check courses_dict
    for i in range(len(courses_dict)):
        tmp_crs = courses_dict[i]
        lock = False
        for j in range(len(locked_dict)):
            if locked_dict[j]["l_code"] // 100 == tmp_crs["l_code"] // 100:
                lock = True
        if lock:
            continue
        if t_isAvailable(tmp_crs["t_name"], day, time):
            courses_dict.remove(courses_dict[i])
            return [tmp_crs["l_name"] + str(tmp_crs["l_code"]), tmp_crs["t_name"], day, time]
    return [None, None, day, time]


def getLessonSmall(day, time, *locked):  # elective
    # parse for *locked:
    locked = list(locked)
    locked_dict = []
    for i in range(len(locked)):
        if locked[i] is None:
            locked[i] = "a1"  # just unfixable bug =( don't trying to understand why this happened
        locked_dict.append(
            {
                "l_name": "".join([i for i in locked[i] if not i.isnumeric()]),
                "l_code": int("".join([i for i in locked[i] if i.isnumeric()]))
            }
        )
    # check ellective_dict is avaible
    for i in range(len(elective_dict)):
        tmp_crs = elective_dict[i]
        lock = False
        for j in range(len(locked_dict)):
            if locked_dict[j]["l_code"] // 100 == tmp_crs["l_code"] // 100:
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

print(f"amount of electives: {len(elective_dict)}\namount of courses: {len(courses_dict)}\namount of services: {len(service_dict)}")
schedule = []
for week in range(1, 3):  # from 1 to 2
    schedule.append({
        "week": week,
        "week_schedule": []
    })
    for day in day_lst:
        schedule[week - 1]["week_schedule"].append({
            "day": day,
            "day_schedule": []
        })
        for time in time_lst:
            schedule[week - 1]["week_schedule"][day_lst.index(day)]["day_schedule"].append({
                "time": time,
                "time_schedule": []
            })
            tmp = []
            lock_tmp = []
            # assign courses and services to big rooms
            for i in range(classroom[0][1]):
                tmp.append(getLessonBig(day, time, *lock_tmp))
                lock_tmp.append(tmp[-1][0])
                schedule[week - 1]["week_schedule"][day_lst.index(day)]["day_schedule"][
                    time_lst.index(time)]["time_schedule"].append({
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
                schedule[week - 1]["week_schedule"][day_lst.index(day)]["day_schedule"][
                    time_lst.index(time)]["time_schedule"].append({
                    "lesson": tmp[i][0],
                    "t_name": tmp[i][1],
                    "lesson_type": "elective",
                    "room_type": "small"
                })
            tmp = []
            # assign electives to big rooms if big room is empty
            for i in range(len(schedule[week - 1]["week_schedule"][day_lst.index(day)]["day_schedule"][
                                   time_lst.index(time)]["time_schedule"])):
                if schedule[week - 1]["week_schedule"][day_lst.index(day)]["day_schedule"][
                time_lst.index(time)]["time_schedule"][i]["lesson"] is None:
                    tmp.append(getLessonSmall(day, time, *lock_tmp))
                    lock_tmp.append(tmp[-1][0])
                    schedule[week - 1]["week_schedule"][day_lst.index(day)]["day_schedule"][
                        time_lst.index(time)]["time_schedule"][i] = {
                        "lesson": tmp[-1][0],
                        "t_name": tmp[-1][1],
                        "lesson_type": "elective",
                        "room_type": "big"
                    }


for week_iter in range(2):
    week = week_iter + 1
    if week_iter == 0:
        print(f"in {week} week:")
    else:
        print(f"in {week} week (debug):")
    for day_iter in range(5):
        day = day_lst[day_iter]
        print(f"\tin {day}:")
        for time_iter in range(2):
            time = time_lst[time_iter]
            print(f"\t\tin {time}:")
            for room_iter in range(3):
                room = schedule[week_iter]["week_schedule"][day_iter][
                    "day_schedule"][time_iter]["time_schedule"][room_iter]["room_type"]
                lesson_code = schedule[week_iter]["week_schedule"][day_iter][
                    "day_schedule"][time_iter]["time_schedule"][room_iter]["lesson"]
                teacher_name = schedule[week_iter]["week_schedule"][day_iter][
                    "day_schedule"][time_iter]["time_schedule"][room_iter]["t_name"]
                lesson_type = schedule[week_iter]["week_schedule"][day_iter][
                    "day_schedule"][time_iter]["time_schedule"][room_iter]["lesson_type"]
                print(f"\t\t\t{lesson_code} {lesson_type} in {room} room with {teacher_name}")