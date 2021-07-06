from tabulate import tabulate
import random

fileCourses = open("Courses.csv", "r")
fileClass = open("classroom.csv")
fileServices = open("service.csv", "r")
fileBusy = open("busy.csv", "r")
courses = []
classrooms = []
services = []
busy = []
ders = []


while True:
    line = fileCourses.readline()
    if not line:
        break
    courses.append(line.split(";"))
while True:
    line = fileServices.readline()
    if not line:
        break
    services.append(line.split(";"))

while True:
    line = fileBusy.readline()
    if not line:
        break
    busy.append(line.split(";"))
#print(courses)
# bcn = Big class number
# scn = Small class number
bcn = int(fileClass.readline().split(";")[1])
scn = int(fileClass.readline().split(";")[1])

Compulsory = []
Elective = []
Final = []
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
more = ["Morning", "Afternoon"]
classes = []
for i in range(bcn):
    classes.append("Bigclass" + str(i + 1))
for i in range(scn):
    classes.append("SmallClass" + str(i + 1))

courses.reverse()


def isava2(sira, lesson):
    day = days[sira // ((bcn + scn) * 2)]
    mr = more[(sira // (bcn + scn)) % 2]
    mod = sira % (bcn + scn)
    for z in services:
        if z[1] == day and z[2] == mr + '\n':
            Final.append(z)
            services.remove(z)
            return True
    for i in busy:
        if i[0] + '\n' == lesson[6] and i[1] == day and i[2] == mr + '\n':
            return False

    if mod == 2:
        if Final[sira - 1] is None and Final[sira - 2] is None:
            return True
        elif Final[sira - 1] is None:
            if Final[sira - 2][2] == lesson[2]:
                return False
        elif Final[sira - 2] is None:
            if Final[sira - 1][2] == lesson[2]:
                return False
        elif Final[sira - 1][2] == lesson[2]:
            return False
        elif Final[sira - 2][2] == lesson[2]:
            return False

    elif mod == 1:
        if Final[sira - 1] is None:
            return True
        elif Final[sira - 1][2] == lesson[2]:
            return False

    return True


def rec2(k, lesson, l):
    if l >= len(lesson):
        Final.append(None)
        return
    if isava2(k, lesson[l]):
        Final.append(lesson[l])
        lesson.remove(lesson[l])
        return

    l += 1
    return rec2(k, lesson, l)


def rep(i):
    mod = i % (bcn + scn)
    if not mod == 2:
        if 0 <= len(Compulsory):
            rec2(i, Elective, 0)
        else:
            rec2(i, Compulsory, 0)
    else:
        rec2(i, Elective, 0)


def make():
    i = 0
    for day in days:
        for me in more:
            for clas in classes:
                if i < len(Final):
                    if Final[i] is None:
                        if isava2(i, Elective[0]):
                            Final[i] = (Elective[0])
                            Elective.remove(Elective[0])
                        if Final[i] is None:
                            print(day, me, clas, "------")
                        else:
                            print(day, me, clas, Final[i][0])
                    else:
                        print(day, me, clas, Final[i][0])
                    i += 1
                else:
                    print(day, me, clas, "------")
                    i += 1

    print(len(Elective))
    print(tabulate(Elective))
    exit()


def isava(sira, lesson):
    if sira == 29:
        make()
    day = days[sira // ((bcn + scn) * 2)]
    mr = more[(sira // (bcn + scn)) % 2]
    mod = sira % (bcn + scn)
    for z in services:
        if z[1] == day and z[2] == mr + '\n':
            Final.append(z)
            services.remove(z)
            return True
    for i in busy:
        if i[0] + '\n' == lesson[6] and i[1] == day and i[2] == mr + '\n':
            return False

    if mod == 2:
        if Final[sira - 1] is None and Final[sira - 2] is None:
            return True
        elif Final[sira - 1] is None:
            if Final[sira - 2][2] == lesson[2]:
                return False
        elif Final[sira - 2] is None:
            if Final[sira - 1][2] == lesson[2]:
                return False
        elif Final[sira - 1][2] == lesson[2]:
            return False
        elif Final[sira - 2][2] == lesson[2]:
            return False

    elif mod == 1:
        if Final[sira - 1] is None:
            return True
        elif Final[sira - 1][2] == lesson[2]:
            return False

    return True


def rec(k, lesson, l):
    if l >= len(lesson):
        Final.append(None)
        return
    if isava(k, lesson[l]):
        if len(Final) <= k:
            Final.append(lesson[l])
            lesson.remove(lesson[l])
        return
    l += 1
    return rec(k, lesson, l)


for s in services:
    for c in courses:
        if c[0] == s[0]:
            courses.remove(c)

for a in courses:
    if a[4] == "C":
        Compulsory.append(a)
    else:
        Elective.append(a)
k = 0
l = 0
m = 0
for a in days:
    for b in more:
        for j in range(bcn):
            if l < len(Compulsory):
                rec(k, Compulsory, 0)
                k += 1
            elif m < len(Elective):
                rec(k, Elective, 0)
                k += 1
        for n in range(scn):
            if m < len(Elective):
                rec(k, Elective, 0)
                k += 1