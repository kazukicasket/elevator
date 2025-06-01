import random
import time

bold_on, bold_off = "\033[1m", "\033[0m"

while True:
    negativeFloors, positiveFloors = random.randrange(-9, 0), random.randrange(20, 51)
    elevatorOneFloor = random.randrange(negativeFloors, positiveFloors)
    elevatorTwoFloor = random.randrange(negativeFloors, positiveFloors)
    userFloor, oneBreakFloors, twoBreakFloors = 0, 0, 0
    oneMainDirection, oneLastDirection, oneTempDirection = 0, 0, 0
    twoMainDirection, twoLastDirection, twoTempDirection = 0, 0, 0
    requestedFloors = []
    elevatorOne, sortedElevatorOne, oneFinalFloors = [], [], []
    elevatorTwo, sortedElevatorTwo, twoFinalFloors = [], [], []
    oneFloors, twoFloors = {}, {}
    holdElevatorOne, openElevatorOne, holdElevatorTwo, openElevatorTwo = False, False, False, False
    stopFloor, stopExecution, skipToNextFloor = False, False, False

    while True:
        print(f"\n{bold_on}-------| FAST ELEVATOR |-------{bold_off}")

        elevatorOneString, elevatorTwoString = " Elevator-One ", " Elevator-Two "
        floorSize = len("◀ 00 ▶")
        extraSpace = " " * int((len(elevatorOneString) - floorSize) / 2)

        print(f"\n{bold_on}|{elevatorOneString}|{elevatorTwoString}|{bold_off}")

        if len(sortedElevatorOne) > 0 or holdElevatorOne:
            if elevatorOneFloor == sortedElevatorOne[0] or holdElevatorOne:
                print(f"{bold_on}|{bold_off}{extraSpace}"
                      f"◀ {'0' if 10 > elevatorOneFloor >= 0 else ''}{elevatorOneFloor} ▶"
                      f"{extraSpace}{bold_on}|{bold_off}", end="")

            else:
                if oneMainDirection == 1 or oneTempDirection == 1:
                    print(f"{bold_on}|{bold_off}{extraSpace}"
                          f"▲ {'0' if 10 > elevatorOneFloor >= 0 else ''}{elevatorOneFloor} ▲"
                          f"{extraSpace}{bold_on}|{bold_off}", end="")

                elif oneMainDirection == -1 or oneTempDirection == -1:
                    print(f"{bold_on}|{bold_off}{extraSpace}"
                          f"▼ {'0' if 10 > elevatorOneFloor >= 0 else ''}{elevatorOneFloor} ▼"
                          f"{extraSpace}{bold_on}|{bold_off}", end="")

        else:
            print(f"{bold_on}|{bold_off}{extraSpace}"
                  f"▶ {'0' if 10 > elevatorOneFloor >= 0 else ''}{elevatorOneFloor} ◀"
                  f"{extraSpace}{bold_on}|{bold_off}", end="")

        if len(sortedElevatorTwo) > 0 or holdElevatorTwo:
            if elevatorTwoFloor == sortedElevatorTwo[0] or holdElevatorTwo:
                print(f"{extraSpace}◀ {'0' if 10 > elevatorTwoFloor >= 0 else ''}{elevatorTwoFloor} ▶"
                      f"{extraSpace}{bold_on}|{bold_off}")

            else:
                if twoMainDirection == 1 or twoTempDirection == 1:
                    print(f"{extraSpace}▲ {'0' if 10 > elevatorTwoFloor >= 0 else ''}{elevatorTwoFloor} ▲"
                          f"{extraSpace}{bold_on}|{bold_off}")

                elif twoMainDirection == -1 or twoTempDirection == -1:
                    print(f"{extraSpace}▼ {'0' if 10 > elevatorTwoFloor >= 0 else ''}{elevatorTwoFloor} ▼"
                          f"{extraSpace}{bold_on}|{bold_off}")

        else:
            print(f"{extraSpace}▶ {'0' if 10 > elevatorTwoFloor >= 0 else ''}{elevatorTwoFloor} ◀"
                  f"{extraSpace}{bold_on}|{bold_off}")

        print(f"\n{bold_on}Elevator-One Queue:{bold_off} {'——' if len(sortedElevatorOne) == 0 else ''}", end="")

        for i in range(len(sortedElevatorOne)):
            if i < (len(sortedElevatorOne) - 1):
                print(f"{f'{bold_on}' if elevatorOneFloor == sortedElevatorOne[i] else ''}"
                      f"{'0' if 10 > sortedElevatorOne[i] >= 0 else ''}{sortedElevatorOne[i]}"
                      f"{f'{bold_off}' if elevatorOneFloor == sortedElevatorOne[i] else ''} {bold_on}|{bold_off} ",
                      end="")

            else:
                print(f"{f'{bold_on}' if elevatorOneFloor == sortedElevatorOne[i] else ''}"
                      f"{'0' if 10 > sortedElevatorOne[i] >= 0 else ''}{sortedElevatorOne[i]}"
                      f"{f'{bold_off}' if elevatorOneFloor == sortedElevatorOne[i] else ''}", end="")

        print(f"\n{bold_on}Elevator-Two Queue:{bold_off} {'——' if len(sortedElevatorTwo) == 0 else ''}", end="")

        for i in range(len(sortedElevatorTwo)):
            if i < (len(sortedElevatorTwo) - 1):
                print(f"{f'{bold_on}' if elevatorTwoFloor == sortedElevatorTwo[i] else ''}"
                      f"{'0' if 10 > sortedElevatorTwo[i] >= 0 else ''}{sortedElevatorTwo[i]}"
                      f"{f'{bold_off}' if elevatorTwoFloor == sortedElevatorTwo[i] else ''} {bold_on}|{bold_off} ",
                      end="")

            else:
                print(f"{f'{bold_on}' if elevatorTwoFloor == sortedElevatorTwo[i] else ''}"
                      f"{'0' if 10 > sortedElevatorTwo[i] >= 0 else ''}{sortedElevatorTwo[i]}"
                      f"{f'{bold_off}' if elevatorTwoFloor == sortedElevatorTwo[i] else ''}")

        if len(sortedElevatorTwo) == 0:
            print()

        if len(requestedFloors) > len(elevatorOne) + len(elevatorTwo):
            print(f"\n▶ Standby Requests: ", end="")

            standby_queue = []

            for i in range(len(requestedFloors)):
                if requestedFloors[i] not in elevatorOne and requestedFloors[i] not in elevatorTwo:
                    standby_queue.append(requestedFloors[i])

            for i in range(len(standby_queue)):
                print(f"{'0' if 10 > standby_queue[i] >= 0 else ''}{standby_queue[i]}", end="")

                if i < len(standby_queue) - 1:
                    print(f" {bold_on}|{bold_off} ", end="")

                else:
                    print()

        inputFloor = ""
        intFloor, skipFloor, invalidFloor = False, False, False

        if not stopFloor and not skipToNextFloor:
            while True:
                inputFloor = input(f"\n{bold_on}Request{bold_off} ({negativeFloors} to {positiveFloors}): ").upper()

                if inputFloor == "":
                    skipFloor = True

                    break

                elif inputFloor == "H1":
                    holdElevatorOne = (True if not holdElevatorOne else False)
                    openElevatorOne = (True if holdElevatorOne else openElevatorOne)

                    break

                elif inputFloor == "H2":
                    holdElevatorTwo = (True if not holdElevatorTwo else False)
                    openElevatorTwo = (True if holdElevatorTwo else openElevatorTwo)

                    break

                elif inputFloor == "S" and len(requestedFloors) > 0:
                    skipToNextFloor = True

                    if len(sortedElevatorOne) > 0 < len(sortedElevatorTwo):
                        if abs(elevatorOneFloor - sortedElevatorOne[0]) < abs(elevatorTwoFloor - sortedElevatorTwo[0]):
                            holdElevatorOne, openElevatorOne = False, False

                        else:
                            holdElevatorTwo, openElevatorTwo = False, False

                    else:
                        if len(sortedElevatorOne) > 0:
                            holdElevatorOne, openElevatorOne = False, False

                        else:
                            holdElevatorTwo, openElevatorTwo = False, False

                    break

                else:
                    try:
                        userFloor = int(inputFloor)
                        intFloor = True

                        break

                    except ValueError:
                        input(f"\n{bold_on}- Integers Only -{bold_off}")

        if intFloor or stopFloor:
            if negativeFloors <= userFloor <= positiveFloors and userFloor not in requestedFloors:
                requestedFloors.append(userFloor)

                if userFloor not in oneFloors:
                    oneFloors[userFloor] = [(-1 if userFloor != elevatorOneFloor else 0), 0,
                                            (False if len(oneFinalFloors) > 0 else True)]

                if userFloor not in twoFloors:
                    twoFloors[userFloor] = [(-1 if userFloor != elevatorTwoFloor else 0), 0,
                                            (False if len(twoFinalFloors) > 0 else True)]

                if oneFloors[userFloor][0] == -1:
                    oneBreakFloors = 0
                    oneFloors[userFloor][0] = abs(elevatorOneFloor - userFloor)

                    for i in range(len(oneFinalFloors)):
                        if i == 0:
                            if oneMainDirection == 1:
                                if userFloor > elevatorOneFloor:
                                    if userFloor < oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                        oneFloors[userFloor][2] = (False if userFloor < oneFinalFloors[i] else True)

                                        break

                                    else:
                                        oneFloors[userFloor][0] = abs(oneFinalFloors[i] - elevatorOneFloor)

                                else:
                                    if len(oneFinalFloors) == (i + 1):
                                        oneFloors[userFloor][0] = (abs(oneFinalFloors[i] - elevatorOneFloor) +
                                                                   abs(oneFinalFloors[i] - userFloor))
                                        oneFloors[userFloor][1] = i + 1
                                        oneFloors[userFloor][2] = True

                                    else:
                                        oneFloors[userFloor][0] = abs(oneFinalFloors[i] - elevatorOneFloor)

                            elif oneMainDirection == -1:
                                if userFloor < elevatorOneFloor:
                                    if userFloor > oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                        oneFloors[userFloor][2] = (False if userFloor > oneFinalFloors[i] else True)

                                        break

                                    else:
                                        oneFloors[userFloor][0] = abs(oneFinalFloors[i] - elevatorOneFloor)

                                else:
                                    if len(oneFinalFloors) == (i + 1):
                                        oneFloors[userFloor][0] = (abs(oneFinalFloors[i] - elevatorOneFloor) +
                                                                   abs(oneFinalFloors[i] - userFloor))
                                        oneFloors[userFloor][1] = i + 1
                                        oneFloors[userFloor][2] = True

                                    else:
                                        oneFloors[userFloor][0] = abs(oneFinalFloors[i] - elevatorOneFloor)

                            elif oneMainDirection == 0:
                                if oneLastDirection == 1:
                                    if userFloor > elevatorOneFloor:
                                        if userFloor < oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                            oneFloors[userFloor][2] = (False if userFloor < oneFinalFloors[i] else True)

                                            break

                                        else:
                                            oneFloors[userFloor][0] = abs(oneFinalFloors[i] - elevatorOneFloor)

                                    else:
                                        if len(oneFinalFloors) == (i + 1):
                                            oneFloors[userFloor][0] = (abs(oneFinalFloors[i] - elevatorOneFloor) +
                                                                       abs(oneFinalFloors[i] - userFloor))
                                            oneFloors[userFloor][1] = i + 1
                                            oneFloors[userFloor][2] = True

                                        else:
                                            oneFloors[userFloor][0] = abs(oneFinalFloors[i] - elevatorOneFloor)

                                elif oneLastDirection == -1:
                                    if userFloor < elevatorOneFloor:
                                        if userFloor > oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                            oneFloors[userFloor][2] = (False if userFloor > oneFinalFloors[i] else True)

                                            break

                                        else:
                                            oneFloors[userFloor][0] = abs(oneFinalFloors[i] - elevatorOneFloor)

                                    else:
                                        if len(oneFinalFloors) == (i + 1):
                                            oneFloors[userFloor][0] = (abs(oneFinalFloors[i] - elevatorOneFloor) +
                                                                       abs(oneFinalFloors[i] - userFloor))
                                            oneFloors[userFloor][1] = i + 1
                                            oneFloors[userFloor][2] = True

                                        else:
                                            oneFloors[userFloor][0] = abs(oneFinalFloors[i] - elevatorOneFloor)

                        else:
                            if oneMainDirection == 1:
                                if i % 2 == 0:
                                    if userFloor > elevatorOneFloor:
                                        if userFloor < oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                            oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] - userFloor)
                                            oneFloors[userFloor][1] = i
                                            oneFloors[userFloor][2] = (False if userFloor < oneFinalFloors[i] else True)

                                            break

                                        else:
                                            oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] - oneFinalFloors[i])

                                    else:
                                        if len(oneFinalFloors) == (i + 1):
                                            oneFloors[userFloor][0] += (abs(oneFinalFloors[i - 1] - oneFinalFloors[i]) +
                                                                        abs(oneFinalFloors[i] - userFloor))
                                            oneFloors[userFloor][1] = i + 1
                                            oneFloors[userFloor][2] = True

                                        else:
                                            oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] - oneFinalFloors[i])

                                else:
                                    if userFloor > elevatorOneFloor:
                                        if len(oneFinalFloors) == (i + 1):
                                            oneFloors[userFloor][0] += (abs(oneFinalFloors[i - 1] - oneFinalFloors[i]) +
                                                                        abs(oneFinalFloors[i] - userFloor))
                                            oneFloors[userFloor][1] = i + 1
                                            oneFloors[userFloor][2] = True

                                        else:
                                            oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] - oneFinalFloors[i])

                                    else:
                                        if userFloor > oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                            oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] - userFloor)
                                            oneFloors[userFloor][1] = i
                                            oneFloors[userFloor][2] = (False if userFloor > oneFinalFloors[i] else True)

                                            break

                                        else:
                                            oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] - oneFinalFloors[i])

                            elif oneMainDirection == -1:
                                if i % 2 == 0:
                                    if userFloor < elevatorOneFloor:
                                        if userFloor > oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                            oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] - userFloor)
                                            oneFloors[userFloor][1] = i
                                            oneFloors[userFloor][2] = (False if userFloor > oneFinalFloors[i] else True)

                                            break

                                        else:
                                            oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] - oneFinalFloors[i])

                                    else:
                                        if len(oneFinalFloors) == (i + 1):
                                            oneFloors[userFloor][0] += (abs(oneFinalFloors[i - 1] - oneFinalFloors[i]) +
                                                                        abs(oneFinalFloors[i] - userFloor))
                                            oneFloors[userFloor][1] = i + 1
                                            oneFloors[userFloor][2] = True

                                        else:
                                            oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] - oneFinalFloors[i])

                                else:
                                    if userFloor < elevatorOneFloor:
                                        if len(oneFinalFloors) == (i + 1):
                                            oneFloors[userFloor][0] += (abs(oneFinalFloors[i - 1] - oneFinalFloors[i]) +
                                                                        abs(oneFinalFloors[i] - userFloor))
                                            oneFloors[userFloor][1] = i + 1
                                            oneFloors[userFloor][2] = True

                                        else:
                                            oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] - oneFinalFloors[i])

                                    else:
                                        if userFloor < oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                            oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] - userFloor)
                                            oneFloors[userFloor][1] = i
                                            oneFloors[userFloor][2] = (False if userFloor < oneFinalFloors[i] else True)

                                            break

                                        else:
                                            oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] - oneFinalFloors[i])

                            elif oneMainDirection == 0:
                                if oneLastDirection == 1:
                                    if i % 2 == 0:
                                        if userFloor > elevatorOneFloor:
                                            if userFloor < oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                                oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] - userFloor)
                                                oneFloors[userFloor][1] = i
                                                oneFloors[userFloor][2] = (
                                                    False if userFloor < oneFinalFloors[i] else True)

                                                break

                                            else:
                                                oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] -
                                                                               oneFinalFloors[i])

                                        else:
                                            if len(oneFinalFloors) == (i + 1):
                                                oneFloors[userFloor][0] += (abs(oneFinalFloors[i - 1] -
                                                                                oneFinalFloors[i]) +
                                                                            abs(oneFinalFloors[i] - userFloor))
                                                oneFloors[userFloor][1] = i + 1
                                                oneFloors[userFloor][2] = True

                                            else:
                                                oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] -
                                                                               oneFinalFloors[i])

                                    else:
                                        if userFloor > elevatorOneFloor:
                                            if len(oneFinalFloors) == (i + 1):
                                                oneFloors[userFloor][0] += (abs(oneFinalFloors[i - 1] -
                                                                                oneFinalFloors[i]) +
                                                                            abs(oneFinalFloors[i] - userFloor))
                                                oneFloors[userFloor][1] = i + 1
                                                oneFloors[userFloor][2] = True

                                            else:
                                                oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] -
                                                                               oneFinalFloors[i])

                                        else:
                                            if userFloor > oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                                oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] - userFloor)
                                                oneFloors[userFloor][1] = i
                                                oneFloors[userFloor][2] = (
                                                    False if userFloor > oneFinalFloors[i] else True)

                                                break

                                            else:
                                                oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] -
                                                                               oneFinalFloors[i])

                                elif oneLastDirection == -1:
                                    if i % 2 == 0:
                                        if userFloor < elevatorOneFloor:
                                            if userFloor > oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                                oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] - userFloor)
                                                oneFloors[userFloor][1] = i
                                                oneFloors[userFloor][2] = (
                                                    False if userFloor > oneFinalFloors[i] else True)

                                                break

                                            else:
                                                oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] -
                                                                               oneFinalFloors[i])

                                        else:
                                            if len(oneFinalFloors) == (i + 1):
                                                oneFloors[userFloor][0] += (abs(oneFinalFloors[i - 1] -
                                                                                oneFinalFloors[i]) +
                                                                            abs(oneFinalFloors[i] - userFloor))
                                                oneFloors[userFloor][1] = i + 1
                                                oneFloors[userFloor][2] = True

                                            else:
                                                oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] -
                                                                               oneFinalFloors[i])

                                    else:
                                        if userFloor < elevatorOneFloor:
                                            if len(oneFinalFloors) == (i + 1):
                                                oneFloors[userFloor][0] += (abs(oneFinalFloors[i - 1] -
                                                                                oneFinalFloors[i]) +
                                                                            abs(oneFinalFloors[i] - userFloor))
                                                oneFloors[userFloor][1] = i + 1
                                                oneFloors[userFloor][2] = True

                                            else:
                                                oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] -
                                                                               oneFinalFloors[i])

                                        else:
                                            if userFloor < oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                                oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] - userFloor)
                                                oneFloors[userFloor][1] = i
                                                oneFloors[userFloor][2] = (
                                                    False if userFloor < oneFinalFloors[i] else True)

                                                break

                                            else:
                                                oneFloors[userFloor][0] += abs(oneFinalFloors[i - 1] -
                                                                               oneFinalFloors[i])

                    if oneFloors[userFloor][0] > 1:
                        for one_floor in oneFloors:
                            if twoFloors[one_floor][1] == -2:
                                if oneFloors[userFloor][1] > oneFloors[one_floor][1]:
                                    oneBreakFloors += 1

                                elif oneFloors[userFloor][1] == oneFloors[one_floor][1]:
                                    if oneFloors[one_floor][1] % 2 == 0:
                                        if oneMainDirection == 1 and userFloor > one_floor:
                                            oneBreakFloors += 1

                                        elif oneMainDirection == -1 and userFloor < one_floor:
                                            oneBreakFloors += 1

                                        elif oneMainDirection == 0:
                                            if oneLastDirection == 1 and userFloor > one_floor:
                                                oneBreakFloors += 1

                                            elif oneLastDirection == -1 and userFloor < one_floor:
                                                oneBreakFloors += 1

                                    else:
                                        if oneMainDirection == 1 and userFloor < one_floor:
                                            oneBreakFloors += 1

                                        elif oneMainDirection == -1 and userFloor > one_floor:
                                            oneBreakFloors += 1

                                        elif oneMainDirection == 0:
                                            if oneLastDirection == 1 and userFloor < one_floor:
                                                oneBreakFloors += 1

                                            elif oneLastDirection == -1 and userFloor > one_floor:
                                                oneBreakFloors += 1

                    if len(sortedElevatorOne) > 0 and elevatorOneFloor == sortedElevatorOne[0]:
                        oneBreakFloors += 1

                if twoFloors[userFloor][0] == -1:
                    twoBreakFloors = 0
                    twoFloors[userFloor][0] = abs(elevatorTwoFloor - userFloor)

                    for i in range(len(twoFinalFloors)):
                        if i == 0:
                            if twoMainDirection == 1:
                                if userFloor > elevatorTwoFloor:
                                    if userFloor < twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                        twoFloors[userFloor][2] = (False if userFloor < twoFinalFloors[i] else True)

                                        break

                                    else:
                                        twoFloors[userFloor][0] = abs(twoFinalFloors[i] - elevatorTwoFloor)

                                else:
                                    if len(twoFinalFloors) == (i + 1):
                                        twoFloors[userFloor][0] = (abs(twoFinalFloors[i] - elevatorTwoFloor) +
                                                                   abs(twoFinalFloors[i] - userFloor))
                                        twoFloors[userFloor][1] = i + 1
                                        twoFloors[userFloor][2] = True

                                    else:
                                        twoFloors[userFloor][0] = abs(twoFinalFloors[i] - elevatorTwoFloor)

                            elif twoMainDirection == -1:
                                if userFloor < elevatorTwoFloor:
                                    if userFloor > twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                        twoFloors[userFloor][2] = (False if userFloor > twoFinalFloors[i] else True)

                                        break

                                    else:
                                        twoFloors[userFloor][0] = abs(twoFinalFloors[i] - elevatorTwoFloor)

                                else:
                                    if len(twoFinalFloors) == (i + 1):
                                        twoFloors[userFloor][0] = (abs(twoFinalFloors[i] - elevatorTwoFloor) +
                                                                   abs(twoFinalFloors[i] - userFloor))
                                        twoFloors[userFloor][1] = i + 1
                                        twoFloors[userFloor][2] = True

                                    else:
                                        twoFloors[userFloor][0] = abs(twoFinalFloors[i] - elevatorTwoFloor)

                            elif twoMainDirection == 0:
                                if twoLastDirection == 1:
                                    if userFloor > elevatorTwoFloor:
                                        if userFloor < twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                            twoFloors[userFloor][2] = (False if userFloor < twoFinalFloors[i] else True)

                                            break

                                        else:
                                            twoFloors[userFloor][0] = abs(twoFinalFloors[i] - elevatorTwoFloor)

                                    else:
                                        if len(twoFinalFloors) == (i + 1):
                                            twoFloors[userFloor][0] = (abs(twoFinalFloors[i] - elevatorTwoFloor) +
                                                                       abs(twoFinalFloors[i] - userFloor))
                                            twoFloors[userFloor][1] = i + 1
                                            twoFloors[userFloor][2] = True

                                        else:
                                            twoFloors[userFloor][0] = abs(twoFinalFloors[i] - elevatorTwoFloor)

                                elif twoLastDirection == -1:
                                    if userFloor < elevatorTwoFloor:
                                        if userFloor > twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                            twoFloors[userFloor][2] = (False if userFloor > twoFinalFloors[i] else True)

                                            break

                                        else:
                                            twoFloors[userFloor][0] = abs(twoFinalFloors[i] - elevatorTwoFloor)

                                    else:
                                        if len(twoFinalFloors) == (i + 1):
                                            twoFloors[userFloor][0] = (abs(twoFinalFloors[i] - elevatorTwoFloor) +
                                                                       abs(twoFinalFloors[i] - userFloor))
                                            twoFloors[userFloor][1] = i + 1
                                            twoFloors[userFloor][2] = True

                                        else:
                                            twoFloors[userFloor][0] = abs(twoFinalFloors[i] - elevatorTwoFloor)

                        else:
                            if twoMainDirection == 1:
                                if i % 2 == 0:
                                    if userFloor > elevatorTwoFloor:
                                        if userFloor < twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                            twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] - userFloor)
                                            twoFloors[userFloor][1] = i
                                            twoFloors[userFloor][2] = (False if userFloor < twoFinalFloors[i] else True)

                                            break

                                        else:
                                            twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] - twoFinalFloors[i])

                                    else:
                                        if len(twoFinalFloors) == (i + 1):
                                            twoFloors[userFloor][0] += (abs(twoFinalFloors[i - 1] - twoFinalFloors[i]) +
                                                                        abs(twoFinalFloors[i] - userFloor))
                                            twoFloors[userFloor][1] = i + 1
                                            twoFloors[userFloor][2] = True

                                        else:
                                            twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] - twoFinalFloors[i])

                                else:
                                    if userFloor > elevatorTwoFloor:
                                        if len(twoFinalFloors) == (i + 1):
                                            twoFloors[userFloor][0] += (abs(twoFinalFloors[i - 1] - twoFinalFloors[i]) +
                                                                        abs(twoFinalFloors[i] - userFloor))
                                            twoFloors[userFloor][1] = i + 1
                                            twoFloors[userFloor][2] = True

                                        else:
                                            twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] - twoFinalFloors[i])

                                    else:
                                        if userFloor > twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                            twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] - userFloor)
                                            twoFloors[userFloor][1] = i
                                            twoFloors[userFloor][2] = (False if userFloor > twoFinalFloors[i] else True)

                                            break

                                        else:
                                            twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] - twoFinalFloors[i])

                            elif twoMainDirection == -1:
                                if i % 2 == 0:
                                    if userFloor < elevatorTwoFloor:
                                        if userFloor > twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                            twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] - userFloor)
                                            twoFloors[userFloor][1] = i
                                            twoFloors[userFloor][2] = (False if userFloor > twoFinalFloors[i] else True)

                                            break

                                        else:
                                            twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] - twoFinalFloors[i])

                                    else:
                                        if len(twoFinalFloors) == (i + 1):
                                            twoFloors[userFloor][0] += (abs(twoFinalFloors[i - 1] - twoFinalFloors[i]) +
                                                                        abs(twoFinalFloors[i] - userFloor))
                                            twoFloors[userFloor][1] = i + 1
                                            twoFloors[userFloor][2] = True

                                        else:
                                            twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] - twoFinalFloors[i])

                                else:
                                    if userFloor < elevatorTwoFloor:
                                        if len(twoFinalFloors) == (i + 1):
                                            twoFloors[userFloor][0] += (abs(twoFinalFloors[i - 1] - twoFinalFloors[i]) +
                                                                        abs(twoFinalFloors[i] - userFloor))
                                            twoFloors[userFloor][1] = i + 1
                                            twoFloors[userFloor][2] = True

                                        else:
                                            twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] - twoFinalFloors[i])

                                    else:
                                        if userFloor < twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                            twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] - userFloor)
                                            twoFloors[userFloor][1] = i
                                            twoFloors[userFloor][2] = (False if userFloor < twoFinalFloors[i] else True)

                                            break

                                        else:
                                            twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] - twoFinalFloors[i])

                            elif twoMainDirection == 0:
                                if twoLastDirection == 1:
                                    if i % 2 == 0:
                                        if userFloor > elevatorTwoFloor:
                                            if userFloor < twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                                twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] - userFloor)
                                                twoFloors[userFloor][1] = i
                                                twoFloors[userFloor][2] = (
                                                    False if userFloor < twoFinalFloors[i] else True)

                                                break

                                            else:
                                                twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] -
                                                                               twoFinalFloors[i])

                                        else:
                                            if len(twoFinalFloors) == (i + 1):
                                                twoFloors[userFloor][0] += (abs(twoFinalFloors[i - 1] -
                                                                                twoFinalFloors[i]) +
                                                                            abs(twoFinalFloors[i] - userFloor))
                                                twoFloors[userFloor][1] = i + 1
                                                twoFloors[userFloor][2] = True

                                            else:
                                                twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] -
                                                                               twoFinalFloors[i])

                                    else:
                                        if userFloor > elevatorTwoFloor:
                                            if len(twoFinalFloors) == (i + 1):
                                                twoFloors[userFloor][0] += (abs(twoFinalFloors[i - 1] -
                                                                                twoFinalFloors[i]) +
                                                                            abs(twoFinalFloors[i] - userFloor))
                                                twoFloors[userFloor][1] = i + 1
                                                twoFloors[userFloor][2] = True

                                            else:
                                                twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] -
                                                                               twoFinalFloors[i])

                                        else:
                                            if userFloor > twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                                twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] - userFloor)
                                                twoFloors[userFloor][1] = i
                                                twoFloors[userFloor][2] = (
                                                    False if userFloor > twoFinalFloors[i] else True)

                                                break

                                            else:
                                                twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] -
                                                                               twoFinalFloors[i])

                                elif twoLastDirection == -1:
                                    if i % 2 == 0:
                                        if userFloor < elevatorTwoFloor:
                                            if userFloor > twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                                twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] - userFloor)
                                                twoFloors[userFloor][1] = i
                                                twoFloors[userFloor][2] = (
                                                    False if userFloor > twoFinalFloors[i] else True)

                                                break

                                            else:
                                                twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] -
                                                                               twoFinalFloors[i])

                                        else:
                                            if len(twoFinalFloors) == (i + 1):
                                                twoFloors[userFloor][0] += (abs(twoFinalFloors[i - 1] -
                                                                                twoFinalFloors[i]) +
                                                                            abs(twoFinalFloors[i] - userFloor))
                                                twoFloors[userFloor][1] = i + 1
                                                twoFloors[userFloor][2] = True

                                            else:
                                                twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] -
                                                                               twoFinalFloors[i])

                                    else:
                                        if userFloor < elevatorTwoFloor:
                                            if len(twoFinalFloors) == (i + 1):
                                                twoFloors[userFloor][0] += (abs(twoFinalFloors[i - 1] -
                                                                                twoFinalFloors[i]) +
                                                                            abs(twoFinalFloors[i] - userFloor))
                                                twoFloors[userFloor][1] = i + 1
                                                twoFloors[userFloor][2] = True

                                            else:
                                                twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] -
                                                                               twoFinalFloors[i])

                                        else:
                                            if userFloor < twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                                twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] - userFloor)
                                                twoFloors[userFloor][1] = i
                                                twoFloors[userFloor][2] = (
                                                    False if userFloor < twoFinalFloors[i] else True)

                                                break

                                            else:
                                                twoFloors[userFloor][0] += abs(twoFinalFloors[i - 1] -
                                                                               twoFinalFloors[i])

                    if twoFloors[userFloor][0] > 1:
                        for two_floor in twoFloors:
                            if oneFloors[two_floor][1] == -2:
                                if twoFloors[userFloor][1] > twoFloors[two_floor][1]:
                                    twoBreakFloors += 1

                                elif twoFloors[userFloor][1] == twoFloors[two_floor][1]:
                                    if twoFloors[two_floor][1] % 2 == 0:
                                        if twoMainDirection == 1 and userFloor > two_floor:
                                            twoBreakFloors += 1

                                        elif twoMainDirection == -1 and userFloor < two_floor:
                                            twoBreakFloors += 1

                                        elif twoMainDirection == 0:
                                            if twoLastDirection == 1 and userFloor > two_floor:
                                                twoBreakFloors += 1

                                            elif twoLastDirection == -1 and userFloor < two_floor:
                                                twoBreakFloors += 1

                                    else:
                                        if twoMainDirection == 1 and userFloor < two_floor:
                                            twoBreakFloors += 1

                                        elif twoMainDirection == -1 and userFloor > two_floor:
                                            twoBreakFloors += 1

                                        elif twoMainDirection == 0:
                                            if twoLastDirection == 1 and userFloor < two_floor:
                                                twoBreakFloors += 1

                                            elif twoLastDirection == -1 and userFloor > two_floor:
                                                twoBreakFloors += 1

                    if len(sortedElevatorTwo) > 0 and elevatorTwoFloor == sortedElevatorTwo[0]:
                        twoBreakFloors += 1

                if (oneFloors[userFloor][0] + oneBreakFloors) < (twoFloors[userFloor][0] + twoBreakFloors):
                    if len(elevatorOne) == 0:
                        oneMainDirection, oneTempDirection = 0, 0

                    if oneFloors[userFloor][1] == 0:
                        elevatorOne.append(userFloor)

                    if oneFloors[userFloor][2]:
                        if len(oneFinalFloors) > oneFloors[userFloor][1]:
                            oneFinalFloors[oneFloors[userFloor][1]] = userFloor

                        else:
                            oneFinalFloors.insert(oneFloors[userFloor][1], userFloor)

                    twoFloors[userFloor][1], twoFloors[userFloor][2] = -2, False

                else:
                    if len(elevatorTwo) == 0:
                        twoMainDirection, twoTempDirection = 0, 0

                    if twoFloors[userFloor][1] == 0:
                        elevatorTwo.append(userFloor)

                    if twoFloors[userFloor][2]:
                        if len(twoFinalFloors) > twoFloors[userFloor][1]:
                            twoFinalFloors[twoFloors[userFloor][1]] = userFloor

                        else:
                            twoFinalFloors.insert(twoFloors[userFloor][1], userFloor)

                    oneFloors[userFloor][1], oneFloors[userFloor][2] = -2, False

            elif userFloor in requestedFloors:
                input(f"\n{bold_on}- Floor Already Requested -{bold_off}")

            elif userFloor <= negativeFloors - 1:
                stopFloor = True
                holdElevatorOne, openElevatorOne, holdElevatorTwo, openElevatorTwo = False, False, False, False

                if len(requestedFloors) == 0:
                    stopExecution = True

                    break

                if userFloor < negativeFloors - 1:
                    time.sleep(1.0)

                userFloor -= 1

            else:
                invalidFloor = True

                input(f"\n{bold_on}- Invalid Floor -{bold_off}")

        if not invalidFloor:
            if len(oneFinalFloors) > 0 and len(twoFinalFloors) > 0:
                print(f"\nOne Final Floors: {oneFinalFloors} / Two Final Floors: {twoFinalFloors}\n")

                for user_floor in requestedFloors:
                    oneBreakFloors, twoBreakFloors = 0, 0
                    one_user_queue, one_user_final, two_user_queue, two_user_final = 0, False, 0, False

                    if oneFloors[user_floor][1] == -2:
                        oneFloors[userFloor][0] = abs(elevatorOneFloor - user_floor)

                        for i in range(len(oneFinalFloors)):
                            if i == 0:
                                if oneMainDirection == 1:
                                    if user_floor > elevatorOneFloor:
                                        if user_floor < oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                            one_user_final = (False if user_floor < oneFinalFloors[i] else True)

                                            break

                                        else:
                                            oneFloors[user_floor][0] = abs(oneFinalFloors[i] - elevatorOneFloor)

                                    else:
                                        if len(oneFinalFloors) == (i + 1):
                                            oneFloors[user_floor][0] = (abs(oneFinalFloors[i] - elevatorOneFloor) +
                                                                        abs(oneFinalFloors[i] - user_floor))
                                            one_user_queue = i + 1
                                            one_user_final = True

                                        else:
                                            oneFloors[user_floor][0] = abs(oneFinalFloors[i] - elevatorOneFloor)

                                elif oneMainDirection == -1:
                                    if user_floor < elevatorOneFloor:
                                        if user_floor > oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                            one_user_final = (False if user_floor > oneFinalFloors[i] else True)

                                            break

                                        else:
                                            oneFloors[user_floor][0] = abs(oneFinalFloors[i] - elevatorOneFloor)

                                    else:
                                        if len(oneFinalFloors) == (i + 1):
                                            oneFloors[user_floor][0] = (abs(oneFinalFloors[i] - elevatorOneFloor) +
                                                                        abs(oneFinalFloors[i] - user_floor))
                                            one_user_queue = i + 1
                                            one_user_final = True

                                        else:
                                            oneFloors[user_floor][0] = abs(oneFinalFloors[i] - elevatorOneFloor)

                                elif oneMainDirection == 0:
                                    if oneLastDirection == 1:
                                        if user_floor > elevatorOneFloor:
                                            if user_floor < oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                                one_user_final = (False if user_floor < oneFinalFloors[i] else True)

                                                break

                                            else:
                                                oneFloors[user_floor][0] = abs(oneFinalFloors[i] - elevatorOneFloor)

                                        else:
                                            if len(oneFinalFloors) == (i + 1):
                                                oneFloors[user_floor][0] = (abs(oneFinalFloors[i] - elevatorOneFloor) +
                                                                            abs(oneFinalFloors[i] - user_floor))
                                                one_user_queue = i + 1
                                                one_user_final = True

                                            else:
                                                oneFloors[user_floor][0] = abs(oneFinalFloors[i] - elevatorOneFloor)

                                    elif oneLastDirection == -1:
                                        if user_floor < elevatorOneFloor:
                                            if user_floor > oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                                one_user_final = (False if user_floor > oneFinalFloors[i] else True)

                                                break

                                            else:
                                                oneFloors[user_floor][0] = abs(oneFinalFloors[i] - elevatorOneFloor)

                                        else:
                                            if len(oneFinalFloors) == (i + 1):
                                                oneFloors[user_floor][0] = (abs(oneFinalFloors[i] - elevatorOneFloor) +
                                                                            abs(oneFinalFloors[i] - user_floor))
                                                one_user_queue = i + 1
                                                one_user_final = True

                                            else:
                                                oneFloors[user_floor][0] = abs(oneFinalFloors[i] - elevatorOneFloor)

                            else:
                                if oneMainDirection == 1:
                                    if i % 2 == 0:
                                        if user_floor > elevatorOneFloor:
                                            if user_floor < oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                                oneFloors[user_floor][0] += abs(oneFinalFloors[i - 1] - user_floor)
                                                one_user_queue = i
                                                one_user_final = (False if user_floor < oneFinalFloors[i] else True)

                                                break

                                            else:
                                                oneFloors[user_floor][0] += abs(
                                                    oneFinalFloors[i - 1] - oneFinalFloors[i])

                                        else:
                                            if len(oneFinalFloors) == (i + 1):
                                                oneFloors[user_floor][0] += (
                                                            abs(oneFinalFloors[i - 1] - oneFinalFloors[i]) +
                                                            abs(oneFinalFloors[i] - user_floor))
                                                one_user_queue = i + 1
                                                one_user_final = True

                                            else:
                                                oneFloors[user_floor][0] += abs(
                                                    oneFinalFloors[i - 1] - oneFinalFloors[i])

                                    else:
                                        if user_floor > elevatorOneFloor:
                                            if len(oneFinalFloors) == (i + 1):
                                                oneFloors[user_floor][0] += (
                                                            abs(oneFinalFloors[i - 1] - oneFinalFloors[i]) +
                                                            abs(oneFinalFloors[i] - user_floor))
                                                one_user_queue = i + 1
                                                one_user_final = True

                                            else:
                                                oneFloors[user_floor][0] += abs(
                                                    oneFinalFloors[i - 1] - oneFinalFloors[i])

                                        else:
                                            if user_floor > oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                                oneFloors[user_floor][0] += abs(oneFinalFloors[i - 1] - user_floor)
                                                one_user_queue = i
                                                one_user_final = (False if user_floor > oneFinalFloors[i] else True)

                                                break

                                            else:
                                                oneFloors[user_floor][0] += abs(
                                                    oneFinalFloors[i - 1] - oneFinalFloors[i])

                                elif oneMainDirection == -1:
                                    if i % 2 == 0:
                                        if user_floor < elevatorOneFloor:
                                            if user_floor > oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                                oneFloors[user_floor][0] += abs(oneFinalFloors[i - 1] - user_floor)
                                                one_user_queue = i
                                                one_user_final = (False if user_floor > oneFinalFloors[i] else True)

                                                break

                                            else:
                                                oneFloors[user_floor][0] += abs(
                                                    oneFinalFloors[i - 1] - oneFinalFloors[i])

                                        else:
                                            if len(oneFinalFloors) == (i + 1):
                                                oneFloors[user_floor][0] += (
                                                            abs(oneFinalFloors[i - 1] - oneFinalFloors[i]) +
                                                            abs(oneFinalFloors[i] - user_floor))
                                                one_user_queue = i + 1
                                                one_user_final = True

                                            else:
                                                oneFloors[user_floor][0] += abs(
                                                    oneFinalFloors[i - 1] - oneFinalFloors[i])

                                    else:
                                        if user_floor < elevatorOneFloor:
                                            if len(oneFinalFloors) == (i + 1):
                                                oneFloors[user_floor][0] += (
                                                            abs(oneFinalFloors[i - 1] - oneFinalFloors[i]) +
                                                            abs(oneFinalFloors[i] - user_floor))
                                                one_user_queue = i + 1
                                                one_user_final = True

                                            else:
                                                oneFloors[user_floor][0] += abs(
                                                    oneFinalFloors[i - 1] - oneFinalFloors[i])

                                        else:
                                            if user_floor < oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                                oneFloors[user_floor][0] += abs(oneFinalFloors[i - 1] - user_floor)
                                                one_user_queue = i
                                                one_user_final = (False if user_floor < oneFinalFloors[i] else True)

                                                break

                                            else:
                                                oneFloors[user_floor][0] += abs(
                                                    oneFinalFloors[i - 1] - oneFinalFloors[i])

                                elif oneMainDirection == 0:
                                    if oneLastDirection == 1:
                                        if i % 2 == 0:
                                            if user_floor > elevatorOneFloor:
                                                if user_floor < oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                                    oneFloors[user_floor][0] += abs(oneFinalFloors[i - 1] - user_floor)
                                                    one_user_queue = i
                                                    one_user_final = (False if user_floor < oneFinalFloors[i] else True)

                                                    break

                                                else:
                                                    oneFloors[user_floor][0] += abs(oneFinalFloors[i - 1] -
                                                                                    oneFinalFloors[i])

                                            else:
                                                if len(oneFinalFloors) == (i + 1):
                                                    oneFloors[user_floor][0] += (abs(oneFinalFloors[i - 1] -
                                                                                     oneFinalFloors[i]) +
                                                                                 abs(oneFinalFloors[i] - user_floor))
                                                    one_user_queue = i + 1
                                                    one_user_final = True

                                                else:
                                                    oneFloors[user_floor][0] += abs(oneFinalFloors[i - 1] -
                                                                                    oneFinalFloors[i])

                                        else:
                                            if user_floor > elevatorOneFloor:
                                                if len(oneFinalFloors) == (i + 1):
                                                    oneFloors[user_floor][0] += (abs(oneFinalFloors[i - 1] -
                                                                                     oneFinalFloors[i]) +
                                                                                 abs(oneFinalFloors[i] - user_floor))
                                                    one_user_queue = i + 1
                                                    one_user_final = True

                                                else:
                                                    oneFloors[user_floor][0] += abs(oneFinalFloors[i - 1] -
                                                                                    oneFinalFloors[i])

                                            else:
                                                if user_floor > oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                                    oneFloors[user_floor][0] += abs(oneFinalFloors[i - 1] - user_floor)
                                                    one_user_queue = i
                                                    one_user_final = (False if user_floor > oneFinalFloors[i] else True)

                                                    break

                                                else:
                                                    oneFloors[user_floor][0] += abs(oneFinalFloors[i - 1] -
                                                                                    oneFinalFloors[i])

                                    elif oneLastDirection == -1:
                                        if i % 2 == 0:
                                            if user_floor < elevatorOneFloor:
                                                if user_floor > oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                                    oneFloors[user_floor][0] += abs(oneFinalFloors[i - 1] - user_floor)
                                                    one_user_queue = i
                                                    one_user_final = (False if user_floor > oneFinalFloors[i] else True)

                                                    break

                                                else:
                                                    oneFloors[user_floor][0] += abs(oneFinalFloors[i - 1] -
                                                                                    oneFinalFloors[i])

                                            else:
                                                if len(oneFinalFloors) == (i + 1):
                                                    oneFloors[user_floor][0] += (abs(oneFinalFloors[i - 1] -
                                                                                     oneFinalFloors[i]) +
                                                                                 abs(oneFinalFloors[i] - user_floor))
                                                    one_user_queue = i + 1
                                                    one_user_final = True

                                                else:
                                                    oneFloors[user_floor][0] += abs(oneFinalFloors[i - 1] -
                                                                                    oneFinalFloors[i])

                                        else:
                                            if user_floor < elevatorOneFloor:
                                                if len(oneFinalFloors) == (i + 1):
                                                    oneFloors[user_floor][0] += (abs(oneFinalFloors[i - 1] -
                                                                                     oneFinalFloors[i]) +
                                                                                 abs(oneFinalFloors[i] - user_floor))
                                                    one_user_queue = i + 1
                                                    one_user_final = True

                                                else:
                                                    oneFloors[user_floor][0] += abs(oneFinalFloors[i - 1] -
                                                                                    oneFinalFloors[i])

                                            else:
                                                if user_floor < oneFinalFloors[i] or len(oneFinalFloors) == (i + 1):
                                                    oneFloors[user_floor][0] += abs(oneFinalFloors[i - 1] - user_floor)
                                                    one_user_queue = i
                                                    one_user_final = (False if user_floor < oneFinalFloors[i] else True)

                                                    break

                                                else:
                                                    oneFloors[user_floor][0] += abs(oneFinalFloors[i - 1] -
                                                                                    oneFinalFloors[i])

                    for one_floor in oneFloors:
                        if oneFloors[one_floor][1] != -2 and user_floor != one_floor:
                            if ((one_user_queue if oneFloors[user_floor][1] == -2 else oneFloors[user_floor][1]) >
                                    oneFloors[one_floor][1]):
                                oneBreakFloors += 1

                            elif ((one_user_queue if oneFloors[user_floor][1] == -2 else oneFloors[user_floor][1]) ==
                                    oneFloors[one_floor][1]):
                                if oneFloors[one_floor][1] % 2 == 0:
                                    if oneMainDirection == 1 and user_floor > one_floor:
                                        oneBreakFloors += 1

                                    elif oneMainDirection == -1 and user_floor < one_floor:
                                        oneBreakFloors += 1

                                    elif oneMainDirection == 0:
                                        if oneLastDirection == 1 and user_floor > one_floor:
                                            oneBreakFloors += 1

                                        elif oneLastDirection == -1 and user_floor < one_floor:
                                            oneBreakFloors += 1

                                else:
                                    if oneMainDirection == 1 and user_floor < one_floor:
                                        oneBreakFloors += 1

                                    elif oneMainDirection == -1 and user_floor > one_floor:
                                        oneBreakFloors += 1

                                    elif oneMainDirection == 0:
                                        if oneLastDirection == 1 and user_floor < one_floor:
                                            oneBreakFloors += 1

                                        elif oneLastDirection == -1 and user_floor > one_floor:
                                            oneBreakFloors += 1

                    if twoFloors[user_floor][1] == -2:
                        twoFloors[userFloor][0] = abs(elevatorTwoFloor - user_floor)

                        for i in range(len(twoFinalFloors)):
                            if i == 0:
                                if twoMainDirection == 1:
                                    if user_floor > elevatorTwoFloor:
                                        if user_floor < twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                            two_user_final = (False if user_floor < twoFinalFloors[i] else True)

                                            break

                                        else:
                                            twoFloors[user_floor][0] = abs(twoFinalFloors[i] - elevatorTwoFloor)

                                    else:
                                        if len(twoFinalFloors) == (i + 1):
                                            twoFloors[user_floor][0] = (abs(twoFinalFloors[i] - elevatorTwoFloor) +
                                                                        abs(twoFinalFloors[i] - user_floor))
                                            two_user_queue = i + 1
                                            two_user_final = True

                                        else:
                                            twoFloors[user_floor][0] = abs(twoFinalFloors[i] - elevatorTwoFloor)

                                elif twoMainDirection == -1:
                                    if user_floor < elevatorTwoFloor:
                                        if user_floor > twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                            two_user_final = (False if user_floor > twoFinalFloors[i] else True)

                                            break

                                        else:
                                            twoFloors[user_floor][0] = abs(twoFinalFloors[i] - elevatorTwoFloor)

                                    else:
                                        if len(twoFinalFloors) == (i + 1):
                                            twoFloors[user_floor][0] = (abs(twoFinalFloors[i] - elevatorTwoFloor) +
                                                                        abs(twoFinalFloors[i] - user_floor))
                                            two_user_queue = i + 1
                                            two_user_final = True

                                        else:
                                            twoFloors[user_floor][0] = abs(twoFinalFloors[i] - elevatorTwoFloor)

                                elif twoMainDirection == 0:
                                    if twoLastDirection == 1:
                                        if user_floor > elevatorTwoFloor:
                                            if user_floor < twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                                two_user_final = (False if user_floor < twoFinalFloors[i] else True)

                                                break

                                            else:
                                                twoFloors[user_floor][0] = abs(twoFinalFloors[i] - elevatorTwoFloor)

                                        else:
                                            if len(twoFinalFloors) == (i + 1):
                                                twoFloors[user_floor][0] = (abs(twoFinalFloors[i] - elevatorTwoFloor) +
                                                                            abs(twoFinalFloors[i] - user_floor))
                                                two_user_queue = i + 1
                                                two_user_final = True

                                            else:
                                                twoFloors[user_floor][0] = abs(twoFinalFloors[i] - elevatorTwoFloor)

                                    elif twoLastDirection == -1:
                                        if user_floor < elevatorTwoFloor:
                                            if user_floor > twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                                two_user_final = (False if user_floor > twoFinalFloors[i] else True)

                                                break

                                            else:
                                                twoFloors[user_floor][0] = abs(twoFinalFloors[i] - elevatorTwoFloor)

                                        else:
                                            if len(twoFinalFloors) == (i + 1):
                                                twoFloors[user_floor][0] = (abs(twoFinalFloors[i] - elevatorTwoFloor) +
                                                                            abs(twoFinalFloors[i] - user_floor))
                                                two_user_queue = i + 1
                                                two_user_final = True

                                            else:
                                                twoFloors[user_floor][0] = abs(twoFinalFloors[i] - elevatorTwoFloor)

                            else:
                                if twoMainDirection == 1:
                                    if i % 2 == 0:
                                        if user_floor > elevatorTwoFloor:
                                            if user_floor < twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                                twoFloors[user_floor][0] += abs(twoFinalFloors[i - 1] - user_floor)
                                                two_user_queue = i
                                                two_user_final = (False if user_floor < twoFinalFloors[i] else True)

                                                break

                                            else:
                                                twoFloors[user_floor][0] += abs(
                                                    twoFinalFloors[i - 1] - twoFinalFloors[i])

                                        else:
                                            if len(twoFinalFloors) == (i + 1):
                                                twoFloors[user_floor][0] += (
                                                            abs(twoFinalFloors[i - 1] - twoFinalFloors[i]) +
                                                            abs(twoFinalFloors[i] - user_floor))
                                                two_user_queue = i + 1
                                                two_user_final = True

                                            else:
                                                twoFloors[user_floor][0] += abs(
                                                    twoFinalFloors[i - 1] - twoFinalFloors[i])

                                    else:
                                        if user_floor > elevatorTwoFloor:
                                            if len(twoFinalFloors) == (i + 1):
                                                twoFloors[user_floor][0] += (
                                                            abs(twoFinalFloors[i - 1] - twoFinalFloors[i]) +
                                                            abs(twoFinalFloors[i] - user_floor))
                                                two_user_queue = i + 1
                                                two_user_final = True

                                            else:
                                                twoFloors[user_floor][0] += abs(
                                                    twoFinalFloors[i - 1] - twoFinalFloors[i])

                                        else:
                                            if user_floor > twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                                twoFloors[user_floor][0] += abs(twoFinalFloors[i - 1] - user_floor)
                                                two_user_queue = i
                                                two_user_final = (False if user_floor > twoFinalFloors[i] else True)

                                                break

                                            else:
                                                twoFloors[user_floor][0] += abs(
                                                    twoFinalFloors[i - 1] - twoFinalFloors[i])

                                elif twoMainDirection == -1:
                                    if i % 2 == 0:
                                        if user_floor < elevatorTwoFloor:
                                            if user_floor > twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                                twoFloors[user_floor][0] += abs(twoFinalFloors[i - 1] - user_floor)
                                                two_user_queue = i
                                                two_user_final = (False if user_floor > twoFinalFloors[i] else True)

                                                break

                                            else:
                                                twoFloors[user_floor][0] += abs(
                                                    twoFinalFloors[i - 1] - twoFinalFloors[i])

                                        else:
                                            if len(twoFinalFloors) == (i + 1):
                                                twoFloors[user_floor][0] += (
                                                            abs(twoFinalFloors[i - 1] - twoFinalFloors[i]) +
                                                            abs(twoFinalFloors[i] - user_floor))
                                                two_user_queue = i + 1
                                                two_user_final = True

                                            else:
                                                twoFloors[user_floor][0] += abs(
                                                    twoFinalFloors[i - 1] - twoFinalFloors[i])

                                    else:
                                        if user_floor < elevatorTwoFloor:
                                            if len(twoFinalFloors) == (i + 1):
                                                twoFloors[user_floor][0] += (
                                                            abs(twoFinalFloors[i - 1] - twoFinalFloors[i]) +
                                                            abs(twoFinalFloors[i] - user_floor))
                                                two_user_queue = i + 1
                                                two_user_final = True

                                            else:
                                                twoFloors[user_floor][0] += abs(
                                                    twoFinalFloors[i - 1] - twoFinalFloors[i])

                                        else:
                                            if user_floor < twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                                twoFloors[user_floor][0] += abs(twoFinalFloors[i - 1] - user_floor)
                                                two_user_queue = i
                                                two_user_final = (False if user_floor < twoFinalFloors[i] else True)

                                                break

                                            else:
                                                twoFloors[user_floor][0] += abs(
                                                    twoFinalFloors[i - 1] - twoFinalFloors[i])

                                elif twoMainDirection == 0:
                                    if twoLastDirection == 1:
                                        if i % 2 == 0:
                                            if user_floor > elevatorTwoFloor:
                                                if user_floor < twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                                    twoFloors[user_floor][0] += abs(twoFinalFloors[i - 1] - user_floor)
                                                    two_user_queue = i
                                                    two_user_final = (False if user_floor < twoFinalFloors[i] else True)

                                                    break

                                                else:
                                                    twoFloors[user_floor][0] += abs(twoFinalFloors[i - 1] -
                                                                                    twoFinalFloors[i])

                                            else:
                                                if len(twoFinalFloors) == (i + 1):
                                                    twoFloors[user_floor][0] += (abs(twoFinalFloors[i - 1] -
                                                                                     twoFinalFloors[i]) +
                                                                                 abs(twoFinalFloors[i] - user_floor))
                                                    two_user_queue = i + 1
                                                    two_user_final = True

                                                else:
                                                    twoFloors[user_floor][0] += abs(twoFinalFloors[i - 1] -
                                                                                    twoFinalFloors[i])

                                        else:
                                            if user_floor > elevatorTwoFloor:
                                                if len(twoFinalFloors) == (i + 1):
                                                    twoFloors[user_floor][0] += (abs(twoFinalFloors[i - 1] -
                                                                                     twoFinalFloors[i]) +
                                                                                 abs(twoFinalFloors[i] - user_floor))
                                                    two_user_queue = i + 1
                                                    two_user_final = True

                                                else:
                                                    twoFloors[user_floor][0] += abs(twoFinalFloors[i - 1] -
                                                                                    twoFinalFloors[i])

                                            else:
                                                if user_floor > twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                                    twoFloors[user_floor][0] += abs(twoFinalFloors[i - 1] - user_floor)
                                                    two_user_queue = i
                                                    two_user_final = (False if user_floor > twoFinalFloors[i] else True)

                                                    break

                                                else:
                                                    twoFloors[user_floor][0] += abs(twoFinalFloors[i - 1] -
                                                                                    twoFinalFloors[i])

                                    elif twoLastDirection == -1:
                                        if i % 2 == 0:
                                            if user_floor < elevatorTwoFloor:
                                                if user_floor > twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                                    twoFloors[user_floor][0] += abs(twoFinalFloors[i - 1] - user_floor)
                                                    two_user_queue = i
                                                    two_user_final = (False if user_floor > twoFinalFloors[i] else True)

                                                    break

                                                else:
                                                    twoFloors[user_floor][0] += abs(twoFinalFloors[i - 1] -
                                                                                    twoFinalFloors[i])

                                            else:
                                                if len(twoFinalFloors) == (i + 1):
                                                    twoFloors[user_floor][0] += (abs(twoFinalFloors[i - 1] -
                                                                                     twoFinalFloors[i]) +
                                                                                 abs(twoFinalFloors[i] - user_floor))
                                                    two_user_queue = i + 1
                                                    two_user_final = True

                                                else:
                                                    twoFloors[user_floor][0] += abs(twoFinalFloors[i - 1] -
                                                                                    twoFinalFloors[i])

                                        else:
                                            if user_floor < elevatorTwoFloor:
                                                if len(twoFinalFloors) == (i + 1):
                                                    twoFloors[user_floor][0] += (abs(twoFinalFloors[i - 1] -
                                                                                     twoFinalFloors[i]) +
                                                                                 abs(twoFinalFloors[i] - user_floor))
                                                    two_user_queue = i + 1
                                                    two_user_final = True

                                                else:
                                                    twoFloors[user_floor][0] += abs(twoFinalFloors[i - 1] -
                                                                                    twoFinalFloors[i])

                                            else:
                                                if user_floor < twoFinalFloors[i] or len(twoFinalFloors) == (i + 1):
                                                    twoFloors[user_floor][0] += abs(twoFinalFloors[i - 1] - user_floor)
                                                    two_user_queue = i
                                                    two_user_final = (False if user_floor < twoFinalFloors[i] else True)

                                                    break

                                                else:
                                                    twoFloors[user_floor][0] += abs(twoFinalFloors[i - 1] -
                                                                                    twoFinalFloors[i])

                    for two_floor in twoFloors:
                        if twoFloors[two_floor][1] != -2 and user_floor != two_floor:
                            if ((two_user_queue if twoFloors[user_floor][1] == -2 else twoFloors[user_floor][1]) >
                                    twoFloors[two_floor][1]):
                                twoBreakFloors += 1

                            elif ((two_user_queue if twoFloors[user_floor][1] == -2 else twoFloors[user_floor][1]) ==
                                    twoFloors[two_floor][1]):
                                if twoFloors[two_floor][1] % 2 == 0:
                                    if twoMainDirection == 1 and user_floor > two_floor:
                                        twoBreakFloors += 1

                                    elif twoMainDirection == -1 and user_floor < two_floor:
                                        twoBreakFloors += 1

                                    elif twoMainDirection == 0:
                                        if twoLastDirection == 1 and user_floor > two_floor:
                                            twoBreakFloors += 1

                                        elif twoLastDirection == -1 and user_floor < two_floor:
                                            twoBreakFloors += 1

                                else:
                                    if twoMainDirection == 1 and user_floor < two_floor:
                                        twoBreakFloors += 1

                                    elif twoMainDirection == -1 and user_floor > two_floor:
                                        twoBreakFloors += 1

                                    elif twoMainDirection == 0:
                                        if twoLastDirection == 1 and user_floor < two_floor:
                                            twoBreakFloors += 1

                                        elif twoLastDirection == -1 and user_floor > two_floor:
                                            twoBreakFloors += 1

                    print(f"'{'0' if -1 < user_floor < 10 else ''}{user_floor}': "
                          f"({'0' if -1 < oneFloors[user_floor][0] < 10 else ''}{oneFloors[user_floor][0]}, "
                          f"{'0' if -1 < oneFloors[user_floor][1] < 10 else ''}{oneFloors[user_floor][1]}, "
                          f"{' ' if oneFloors[user_floor][2] else ''}{oneFloors[user_floor][2]}) / "
                          f"({'0' if -1 < twoFloors[user_floor][0] < 10 else ''}{twoFloors[user_floor][0]}, "
                          f"{'0' if -1 < twoFloors[user_floor][1] < 10 else ''}{twoFloors[user_floor][1]}, "
                          f"{' ' if twoFloors[user_floor][2] else ''}{twoFloors[user_floor][2]}) {bold_on}|{bold_off} "
                          f"Break Floors: {'0' if -1 < oneBreakFloors < 10 else ''}{oneBreakFloors} / "
                          f"{'0' if -1 < twoBreakFloors < 10 else ''}{twoBreakFloors}")

                    if elevatorOneFloor != user_floor != elevatorTwoFloor:
                        if (oneFloors[user_floor][0] + oneBreakFloors) < (twoFloors[user_floor][0] + twoBreakFloors):
                            if oneFloors[user_floor][1] == -2:
                                print(f"{bold_on}- DEVE SER REMANEJADO PARA O ELEVATOR-ONE{bold_off}")

                                queue_floors = []

                                for two_floor in twoFloors:
                                    if user_floor != two_floor and twoFloors[two_floor][1] == twoFloors[user_floor][1]:
                                        queue_floors.append(two_floor)

                                if len(queue_floors) > 0:
                                    if twoFloors[user_floor][1] % 2 == 0:
                                        twoFinalFloors[twoFloors[user_floor][1]] = (
                                            max(queue_floors) if twoMainDirection == 1 else min(queue_floors))

                                    else:
                                        twoFinalFloors[twoFloors[user_floor][1]] = (
                                            min(queue_floors) if twoMainDirection == 1 else max(queue_floors))

                                else:
                                    twoFinalFloors.pop(twoFloors[user_floor][1])

                                if user_floor in elevatorTwo:
                                    for i in range(len(elevatorTwo)):
                                        if user_floor == elevatorTwo[i]:
                                            elevatorTwo.pop(i)

                                            break

                                    for i in range(len(sortedElevatorTwo)):
                                        if user_floor == sortedElevatorTwo[i]:
                                            sortedElevatorTwo.pop(i)

                                            break

                                twoTempDirection, twoFloors[user_floor][1], twoFloors[user_floor][2] = 0, -2, False
                                oneFloors[user_floor][1], oneFloors[user_floor][2] = one_user_queue, one_user_final

                                if oneFloors[user_floor][1] == 0:
                                    elevatorOne.append(user_floor)

                                if oneFloors[user_floor][2]:
                                    if len(oneFinalFloors) > oneFloors[user_floor][1]:
                                        oneFinalFloors[oneFloors[user_floor][1]] = user_floor

                                    else:
                                        oneFinalFloors.insert(oneFloors[user_floor][1], user_floor)

                        elif (oneFloors[user_floor][0] + oneBreakFloors) > (twoFloors[user_floor][0] + twoBreakFloors):
                            if twoFloors[user_floor][1] == -2:
                                print(f"{bold_on}- DEVE SER REMANEJADO PARA O ELEVATOR-TWO{bold_off}")

                                queue_floors = []

                                for one_floor in oneFloors:
                                    if user_floor != one_floor and oneFloors[one_floor][1] == oneFloors[user_floor][1]:
                                        queue_floors.append(one_floor)

                                if len(queue_floors) > 0:
                                    if oneFloors[user_floor][1] % 2 == 0:
                                        oneFinalFloors[oneFloors[user_floor][1]] = (
                                            max(queue_floors) if oneMainDirection == 1 else min(queue_floors))

                                    else:
                                        oneFinalFloors[oneFloors[user_floor][1]] = (
                                            min(queue_floors) if oneMainDirection == 1 else max(queue_floors))

                                else:
                                    oneFinalFloors.pop(oneFloors[user_floor][1])

                                if user_floor in elevatorOne:
                                    for i in range(len(elevatorOne)):
                                        if user_floor == elevatorOne[i]:
                                            elevatorOne.pop(i)

                                            break

                                    for i in range(len(sortedElevatorOne)):
                                        if user_floor == sortedElevatorOne[i]:
                                            sortedElevatorOne.pop(i)

                                            break

                                oneTempDirection, oneFloors[user_floor][1], oneFloors[user_floor][2] = 0, -2, False
                                twoFloors[user_floor][1], twoFloors[user_floor][2] = two_user_queue, two_user_final

                                if twoFloors[user_floor][1] == 0:
                                    elevatorTwo.append(user_floor)

                                if twoFloors[user_floor][2]:
                                    if len(twoFinalFloors) > twoFloors[user_floor][1]:
                                        twoFinalFloors[twoFloors[user_floor][1]] = user_floor

                                    else:
                                        twoFinalFloors.insert(twoFloors[user_floor][1], user_floor)

            if not holdElevatorOne:
                if len(elevatorOne) > 0:
                    for i in range(len(elevatorOne)):
                        if elevatorOneFloor == elevatorOne[i] != (userFloor if inputFloor != "" else ""):
                            elevatorOne.pop(i), sortedElevatorOne.pop(0)
                            oneFloors.pop(elevatorOneFloor), twoFloors.pop(elevatorOneFloor)

                            break

                    for i in range(len(requestedFloors)):
                        if elevatorOneFloor == requestedFloors[i] != (userFloor if inputFloor != "" else ""):
                            requestedFloors.pop(i)

                            break

                if len(elevatorOne) > 0:
                    if not openElevatorOne and ((elevatorOneFloor == userFloor not in elevatorOne) or
                                                elevatorOneFloor != userFloor):
                        if oneFinalFloors[0] > elevatorOneFloor:
                            elevatorOneFloor += 1

                            if oneMainDirection == 0:
                                oneMainDirection = 1

                            for one_floor in oneFloors:
                                if oneFloors[one_floor][1] != -2:
                                    oneFloors[one_floor][0] -= 1

                        elif oneFinalFloors[0] < elevatorOneFloor:
                            elevatorOneFloor -= 1

                            if oneMainDirection == 0:
                                oneMainDirection = -1

                            for one_floor in oneFloors:
                                if oneFloors[one_floor][1] != -2:
                                    oneFloors[one_floor][0] -= 1

                    if oneFinalFloors[0] == elevatorOneFloor:
                        oneLastDirection = oneMainDirection
                        oneMainDirection = 0

                else:
                    if len(oneFinalFloors) > 0:
                        if elevatorOneFloor == oneFinalFloors[0]:
                            for one_floor in oneFloors:
                                if oneFloors[one_floor][1] > 0:
                                    oneFloors[one_floor][1] -= 1

                                if len(oneFinalFloors) > 1 and one_floor != oneFinalFloors[1]:
                                    oneFloors[one_floor][2] = False

                            for one_floor in oneFloors:
                                if oneFloors[one_floor][1] == 0:
                                    elevatorOne.append(one_floor)

                            if len(elevatorOne) > 0:
                                oneMainDirection = (1 if oneLastDirection == -1 else -1)

                            oneFinalFloors.pop(0)

                    if len(oneFinalFloors) == 0 < len(sortedElevatorTwo) and holdElevatorTwo:
                        if (abs(elevatorOneFloor - sortedElevatorTwo[0]) <=
                                abs(elevatorOneFloor - sortedElevatorTwo[-1])):
                            elevator_size = (True if len(sortedElevatorTwo) > 1 else False)
                            near_floor = (sortedElevatorTwo[0] if elevatorTwoFloor != sortedElevatorTwo[0] else
                                          (sortedElevatorTwo[1] if elevator_size else elevatorOneFloor))
                            if elevatorOneFloor > near_floor:
                                oneTempDirection = -1
                                elevatorOneFloor -= 1

                            elif elevatorOneFloor < near_floor:
                                oneTempDirection = 1
                                elevatorOneFloor += 1

                            if elevatorOneFloor != near_floor:
                                if len(sortedElevatorOne) > 0:
                                    sortedElevatorOne[0] = near_floor

                                else:
                                    sortedElevatorOne.append(near_floor)

                            if abs(elevatorOneFloor - sortedElevatorTwo[0]) < abs(
                                    elevatorTwoFloor - sortedElevatorTwo[0]):
                                elevatorOne, oneFinalFloors = elevatorTwo.copy(), twoFinalFloors.copy()
                                oneFloors, oneMainDirection = twoFloors.copy(), twoMainDirection
                                elevatorTwo.clear(), sortedElevatorTwo.clear(), twoFinalFloors.clear()
                                twoMainDirection, oneTempDirection = 0, 0

                                for two_floor in twoFloors:
                                    twoFloors[two_floor][1], twoFloors[two_floor][2] = -2, False

                        else:
                            if elevatorOneFloor > sortedElevatorTwo[-1]:
                                oneTempDirection = -1
                                elevatorOneFloor -= 1

                            elif elevatorOneFloor < sortedElevatorTwo[-1]:
                                oneTempDirection = 1
                                elevatorOneFloor += 1

                            if len(sortedElevatorOne) > 0:
                                sortedElevatorOne[0] = sortedElevatorTwo[-1]

                            else:
                                sortedElevatorOne.append(sortedElevatorTwo[-1])

                            if (abs(elevatorOneFloor - sortedElevatorTwo[-1]) <
                                    abs(elevatorTwoFloor - sortedElevatorTwo[-1])):
                                elevatorOne.append(sortedElevatorTwo[-1]), oneFinalFloors.append(sortedElevatorTwo[-1])
                                oneFloors[sortedElevatorTwo[-1]][0] = abs(elevatorOneFloor - sortedElevatorTwo[-1])
                                oneFloors[sortedElevatorTwo[-1]][1], oneFloors[sortedElevatorTwo[-1]][2] = 0, True
                                oneMainDirection = oneTempDirection
                                oneTempDirection = 0

                                for i in range(len(elevatorTwo)):
                                    if elevatorTwo[i] == sortedElevatorTwo[-1]:
                                        elevatorTwo.pop(i)

                                        break

                                for two_floor in twoFloors:
                                    if two_floor == sortedElevatorTwo[-1]:
                                        twoFloors[two_floor][1], twoFloors[two_floor][2] = -2, False

                                sortedElevatorTwo.pop(-1)
                                twoFinalFloors[0] = sortedElevatorTwo[-1]

            if not holdElevatorTwo:
                if len(elevatorTwo) > 0:
                    for i in range(len(elevatorTwo)):
                        if elevatorTwoFloor == elevatorTwo[i] != (userFloor if inputFloor != "" else ""):
                            elevatorTwo.pop(i), sortedElevatorTwo.pop(0)
                            oneFloors.pop(elevatorTwoFloor), twoFloors.pop(elevatorTwoFloor)

                            break

                    for i in range(len(requestedFloors)):
                        if elevatorTwoFloor == requestedFloors[i] != (userFloor if inputFloor != "" else ""):
                            requestedFloors.pop(i)

                            break

                if len(elevatorTwo) > 0:
                    if not openElevatorTwo and ((elevatorTwoFloor == userFloor not in elevatorTwo) or
                                                elevatorTwoFloor != userFloor):
                        if twoFinalFloors[0] > elevatorTwoFloor:
                            elevatorTwoFloor += 1

                            if twoMainDirection == 0:
                                twoMainDirection = 1

                            for two_floor in twoFloors:
                                if twoFloors[two_floor][1] != -2:
                                    twoFloors[two_floor][0] -= 1

                        elif twoFinalFloors[0] < elevatorTwoFloor:
                            elevatorTwoFloor -= 1

                            if twoMainDirection == 0:
                                twoMainDirection = -1

                            for two_floor in twoFloors:
                                if twoFloors[two_floor][1] != -2:
                                    twoFloors[two_floor][0] -= 1

                    if twoFinalFloors[0] == elevatorTwoFloor:
                        twoLastDirection = twoMainDirection
                        twoMainDirection = 0

                else:
                    if len(twoFinalFloors) > 0:
                        if elevatorTwoFloor == twoFinalFloors[0]:
                            for two_floor in twoFloors:
                                if twoFloors[two_floor][1] > 0:
                                    twoFloors[two_floor][1] -= 1

                                if len(twoFinalFloors) > 1 and two_floor != twoFinalFloors[1]:
                                    twoFloors[two_floor][2] = False

                            for two_floor in twoFloors:
                                if twoFloors[two_floor][1] == 0:
                                    elevatorTwo.append(two_floor)

                            if len(elevatorTwo) > 0:
                                twoMainDirection = (1 if twoLastDirection == -1 else -1)

                            twoFinalFloors.pop(0)

                    if len(twoFinalFloors) == 0 < len(sortedElevatorOne) and holdElevatorOne:
                        if (abs(elevatorTwoFloor - sortedElevatorOne[0]) <=
                                abs(elevatorTwoFloor - sortedElevatorOne[-1])):
                            elevator_size = (True if len(sortedElevatorOne) > 1 else False)
                            near_floor = (sortedElevatorOne[0] if elevatorOneFloor != sortedElevatorOne[0] else
                                          (sortedElevatorOne[1] if elevator_size else elevatorTwoFloor))
                            if elevatorTwoFloor > near_floor:
                                twoTempDirection = -1
                                elevatorTwoFloor -= 1

                            elif elevatorTwoFloor < near_floor:
                                twoTempDirection = 1
                                elevatorTwoFloor += 1

                            if elevatorTwoFloor != near_floor:
                                if len(sortedElevatorTwo) > 0:
                                    sortedElevatorTwo[0] = near_floor

                                else:
                                    sortedElevatorTwo.append(near_floor)

                            if abs(elevatorTwoFloor - sortedElevatorOne[0]) < abs(
                                    elevatorOneFloor - sortedElevatorOne[0]):
                                elevatorTwo, twoFinalFloors = elevatorOne.copy(), oneFinalFloors.copy()
                                twoFloors, twoMainDirection = oneFloors.copy(), oneMainDirection
                                elevatorOne.clear(), sortedElevatorOne.clear(), oneFinalFloors.clear()
                                oneMainDirection, twoTempDirection = 0, 0

                                for one_floor in oneFloors:
                                    oneFloors[one_floor][1], oneFloors[one_floor][2] = -2, False

                        else:
                            if elevatorTwoFloor > sortedElevatorOne[-1]:
                                twoTempDirection = -1
                                elevatorTwoFloor -= 1

                            elif elevatorTwoFloor < sortedElevatorOne[-1]:
                                twoTempDirection = 1
                                elevatorTwoFloor += 1

                            if len(sortedElevatorTwo) > 0:
                                sortedElevatorTwo[0] = sortedElevatorOne[-1]

                            else:
                                sortedElevatorTwo.append(sortedElevatorOne[-1])

                            if (abs(elevatorTwoFloor - sortedElevatorOne[-1]) <
                                    abs(elevatorOneFloor - sortedElevatorOne[-1])):
                                elevatorTwo.append(sortedElevatorOne[-1]), twoFinalFloors.append(sortedElevatorOne[-1])
                                twoFloors[sortedElevatorOne[-1]][0] = abs(elevatorTwoFloor - sortedElevatorOne[-1])
                                twoFloors[sortedElevatorOne[-1]][1], twoFloors[sortedElevatorOne[-1]][2] = 0, True
                                twoMainDirection = twoTempDirection
                                twoTempDirection = 0

                                for i in range(len(elevatorOne)):
                                    if elevatorOne[i] == sortedElevatorOne[-1]:
                                        elevatorOne.pop(i)

                                        break

                                for one_floor in oneFloors:
                                    if one_floor == sortedElevatorOne[-1]:
                                        oneFloors[one_floor][1], oneFloors[one_floor][2] = -2, False

                                sortedElevatorOne.pop(-1)
                                oneFinalFloors[0] = sortedElevatorOne[-1]

            if len(elevatorOne) > 0:
                elevatorOne.sort()
                sortedElevatorOne = (elevatorOne[::-1] if oneMainDirection == -1 else elevatorOne.copy())

            if len(elevatorTwo) > 0:
                elevatorTwo.sort()
                sortedElevatorTwo = (elevatorTwo[::-1] if twoMainDirection == -1 else elevatorTwo.copy())

            openElevatorOne, openElevatorTwo = False, False

            if len(sortedElevatorOne) > 0:
                if elevatorOneFloor == sortedElevatorOne[0]:
                    openElevatorOne = True
                    skipToNextFloor = False

            if len(sortedElevatorTwo) > 0:
                if elevatorTwoFloor == sortedElevatorTwo[0]:
                    openElevatorTwo = True
                    skipToNextFloor = False

            if skipToNextFloor and inputFloor != "S":
                time.sleep(1.0)

    if stopExecution:
        print(f"\n{bold_on}Restart Execution?{bold_off}\n"
              "0 - No\n"
              "1 - Yes")
        restartExecution = input(f"{bold_on}Option:{bold_off} ")

        if restartExecution == "0":
            print(f"\n{bold_on}----------| THE END |----------{bold_off}")

            break
