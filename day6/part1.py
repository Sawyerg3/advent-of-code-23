
def main():
    t,d = [34,90,89,86],[204, 1713, 1210, 1780]
    # t,d =  [7, 15, 30], [9, 40,  200]
    td =  list(zip(t,d))

    total = 1
    for time, distance in td:
        raceTotal = 0
        for h in range(time):
            if h * (time - h) > distance:
                raceTotal += 1        
        total *= raceTotal
    print(total)
    return 
main()