def timeConversion(s):
    #
    # Write your code here.
    #
    if len(s) < 10:
        old_time = ((10-len(s))*'0') + s
    else:
        old_time = s

    if old_time[8:10] == 'PM' and int(old_time[0:2]) < 12:
        new_time = str(12 + int(old_time[0:2])) + old_time[2:8]

    elif old_time[8:10] == 'AM' and int(old_time[0:2]) == 12:
            new_time = '00' + old_time[2:8]

    else:
        new_time = old_time[0:8]

    return (new_time)


print(timeConversion('12:40:22AM'))