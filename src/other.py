def checkValidEntries(info):
    msg = ""

    if not info[0].isalpha(): msg = "Invalid entry for first name"

    if not info[1].isalpha(): msg += "\nInvalid entry for last name"

    try: int(info[2])
    except ValueError: msg += "\nInvalid age entry"

    if info[3] == '': msg += "\nNo entry selected for your gender"

    if info[4] == '': msg += "\nNo entry selected for your ethnicity"

    return msg