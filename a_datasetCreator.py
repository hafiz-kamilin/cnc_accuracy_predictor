from random import uniform, seed, randint
import matplotlib.pyplot as plt
import csv

def saveToCsv(dataset):

    file = open("./data/dataset.csv", "w", newline="")
    writer = csv.writer(file)
    writer.writerow(
        [
            "ondo",
            "komando_no_nagasa",
            "tsukawareta_kaisuu",
            "gosa",
            "yesNo"
        ]
    )

    for i in range(len(dataset)):

        writer.writerow(
            [
                dataset[i][0],
                dataset[i][1],
                dataset[i][2],
                dataset[i][3],
                dataset[i][4]
            ]
        )

def plotGraph(
    plotError,
    tempLow,
    tempHigh,
    shortestCode,
    longestCode,
    minimumUsedTime,
    maximumUsedTime
):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    plt.xlim(tempLow, tempHigh)
    plt.ylim(shortestCode, longestCode)
    ax.set_zlim(minimumUsedTime, maximumUsedTime)

    ax.set_xlabel("Temperature [°C]")
    ax.set_ylabel("Command Length")
    ax.set_zlabel("Number of times used")

    fig.patch.set_linewidth(1)
    fig.patch.set_edgecolor("grey")

    ax.scatter(plotError[0], plotError[1], plotError[2], c = "r", marker= "o")
    ax.view_init(26, 46)
    plt.savefig("./data/output.png")
    plt.show()

def controlledDatasetRandomization(
    tempLow,
    tempHigh,
    shortestCode,
    longestCode,
    minimumUsedTime,
    maximumUsedTime,
    tempLow_error,
    tempHigh_error,
    shortestCode_error,
    longestCode_error,
    minimumUsedTime_error,
    maximumUsedTime_error,
    acceptableRange
):

    seed(2021)

    counter = 0
    dataset = {}
    plotError = [[], [], []]

    for number in range(10000):

        if (randint(1, 100) >= 90):

            if ((tempLow_error is not None) and (shortestCode_error is not None) and (minimumUsedTime_error is not None)):

                temperature = round(uniform(tempLow_error, tempHigh_error), 2)
                codeLength = randint(shortestCode_error, longestCode_error)
                timeUsed = randint(minimumUsedTime_error, maximumUsedTime_error)
                error = round(uniform(acceptableRange, acceptableRange * 2), 2)
                yesNo = 1
                counter += 1

                plotError[0].append(temperature)
                plotError[1].append(codeLength)
                plotError[2].append(timeUsed)

            elif ((tempLow_error is None) and (shortestCode_error is not None) and (minimumUsedTime_error is not None)):

                temperature = round(uniform(tempLow, tempHigh), 2)
                codeLength = randint(shortestCode_error, longestCode_error)
                timeUsed = randint(minimumUsedTime_error, maximumUsedTime_error)
                error = round(uniform(acceptableRange, acceptableRange * 2), 2)
                yesNo = 1
                counter += 1
                
                plotError[0].append(temperature)
                plotError[1].append(codeLength)
                plotError[2].append(timeUsed)

            elif ((tempLow_error is None) and (shortestCode_error is None) and (minimumUsedTime_error is not None)):

                temperature = round(uniform(tempLow, tempHigh), 2)
                codeLength = randint(shortestCode, longestCode)
                timeUsed = randint(minimumUsedTime_error, maximumUsedTime_error)
                error = round(uniform(acceptableRange, acceptableRange * 2), 2)
                yesNo = 1
                counter += 1

                plotError[0].append(temperature)
                plotError[1].append(codeLength)
                plotError[2].append(timeUsed)

            elif ((tempLow_error is None) and (shortestCode_error is None) and (minimumUsedTime_error is None)):

                temperature = round(uniform(tempLow, tempHigh), 2)
                codeLength = randint(shortestCode, longestCode)
                timeUsed = randint(minimumUsedTime, maximumUsedTime)
                error = round(uniform(0, acceptableRange), 2)
                yesNo = 0

            elif ((tempLow_error is not None) and (shortestCode_error is None) and (minimumUsedTime_error is not None)):


                temperature = round(uniform(tempLow_error, tempHigh_error), 2)
                codeLength = randint(shortestCode, longestCode)
                timeUsed = randint(minimumUsedTime_error, maximumUsedTime_error)
                error = round(uniform(acceptableRange, acceptableRange * 2), 2)
                yesNo = 1
                counter += 1

                plotError[0].append(temperature)
                plotError[1].append(codeLength)
                plotError[2].append(timeUsed)
                
            elif ((tempLow_error is not None) and (shortestCode_error is None) and (minimumUsedTime_error is None)):

                temperature = round(uniform(tempLow_error, tempHigh_error), 2)
                codeLength = randint(shortestCode, longestCode)
                timeUsed = randint(minimumUsedTime, maximumUsedTime)
                error = round(uniform(acceptableRange, acceptableRange * 2), 2)
                yesNo = 1
                counter += 1

                plotError[0].append(temperature)
                plotError[1].append(codeLength)
                plotError[2].append(timeUsed)

            elif ((tempLow_error is not None) and (shortestCode_error is None) and (minimumUsedTime_error is not None)):

                temperature = round(uniform(tempLow_error, tempHigh_error), 2)
                codeLength = randint(shortestCode, longestCode)
                timeUsed = randint(minimumUsedTime_error, maximumUsedTime_error)
                error = round(uniform(acceptableRange, acceptableRange * 2), 2)
                yesNo = 1
                counter += 1

                plotError[0].append(temperature)
                plotError[1].append(codeLength)
                plotError[2].append(timeUsed)

        else:

            if (randint(1, 1000) >= 999):

                if ((tempLow_error is not None) and (shortestCode_error is not None) and (minimumUsedTime_error is not None)):

                    temperature = round(uniform(tempLow, tempHigh), 2)
                    codeLength = randint(shortestCode, longestCode)
                    timeUsed = randint(minimumUsedTime, maximumUsedTime)
                    error = round(uniform(0, acceptableRange), 2)
                    yesNo = 1

                    plotError[0].append(temperature)
                    plotError[1].append(codeLength)
                    plotError[2].append(timeUsed)

            else:

                temperature = round(uniform(tempLow, tempHigh), 2)
                codeLength = randint(shortestCode, longestCode)
                timeUsed = randint(minimumUsedTime, maximumUsedTime)
                error = round(uniform(0, acceptableRange), 2)
                yesNo = 0
    
        dataset[number] = [temperature, codeLength, timeUsed, error, yesNo]

    print("\nデータセットを作成しました")
    print("許容範囲以外の誤差を発生するパーセント：" + str(counter / 10000 * 100) + "%")
    plotGraph(plotError, tempLow, tempHigh, shortestCode, longestCode, minimumUsedTime, maximumUsedTime)
    saveToCsv(dataset)

if __name__ == "__main__":

    tempLow = -20
    tempHigh = 40
    shortestCode = 10
    longestCode = 1000
    minimumUsedTime = 0
    maximumUsedTime = 100
    tempLow_error = 35.00
    tempHigh_error = 40.00
    shortestCode_error = 900
    longestCode_error = 1000
    minimumUsedTime_error = 75
    maximumUsedTime_error = 100
    acceptableRange = 5

    controlledDatasetRandomization(
        tempLow,
        tempHigh,
        shortestCode,
        longestCode,
        minimumUsedTime,
        maximumUsedTime,
        tempLow_error,
        tempHigh_error,
        shortestCode_error,
        longestCode_error,
        minimumUsedTime_error,
        maximumUsedTime_error,
        acceptableRange
    )