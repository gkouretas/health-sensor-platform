import os
import json

def checkValidEntries(info):
    msg = ""

    if not info[0].isalpha(): msg = "Invalid entry for first name\n"

    if not info[1].isalpha(): msg += "Invalid entry for last name\n"

    for dir in os.listdir("./users"):
        if(dir == (info[0] + " " + info[1])):
            msg += "User already exists"
            break

    try: int(info[2])
    except ValueError: msg += "Invalid age entry\n"

    if info[3] == '': msg += "No entry selected for your gender\n"

    if info[4] == '': msg += "No entry selected for your ethnicity\n"

    return msg

def saveUser(name, info):
    path = './users/' + name

    os.mkdir(path)

    os.mkdir(path + "/about")

    info = {
        'name': "{}".format(name),
        'age': info[2],
        'gender': info[3],
        'ethnicity': info[4]
    }

    with open("{}/about/info.json".format(path), "w") as out:
        json.dump(info, out)

    os.mkdir(path + "/vitals")
    
