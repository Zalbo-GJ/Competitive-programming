def countingValleys(steps, path):
    # Write your code here

    valleys = 0
    altitude = 0
    for i in path:
        if (i == 'U'):
            if altitude+1 == 0:
                valleys += 1
            altitude += 1
        else:
            altitude -= 1

    return valleys
