"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#

# dictionaries with distance: speed rate


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    end = brevet_dist_km
    dist = control_dist_km
    otime = arrow.get(brevet_start_time)


    time = 0
    newdist = 0


    if (dist <= 200) and (dist > 0):  # 0-200
        time += dist / 34
    elif ((dist - 200) > 0):  # 200+
        time = 200 / 34
        newdist = dist - 200

    if (dist <= 400) and (dist > 200):  # 201-400
        time += newdist / 32
        print(time)
    if (dist > 400):  # 400+
        time += 200 / 32
        newdist = newdist - 200

    if (dist <= 600) and (dist > 400):  # 401-600
        time += newdist / 30
    if (dist > 600): # 600+
        time += 200 / 30
        newdist = newdist - 200

    if ((dist - 600) > 0) and (dist > 1000): #1000+
        time += 400 / 28  # 600+
        newdist = newdist - 200

    print("600: ", time)

    if (dist <= 1000) and (dist > 600):  # 601-1000
        time += newdist / 28
    elif ((dist - 1000) > 0) and (dist > 1300):
        time += 400 / 28  # 1000+
        newdist = newdist - 400
    print("1000: ", time)


    print(time)
    splittimeformat = math.modf(time)  # splits the rate to integer and decimal
    hour = splittimeformat[1]
    minute = splittimeformat[0]
    minute = minute * 60
    minute = round(minute)


    otime = otime.shift(hours=hour, minutes=minute)
    otime = otime.shift(hours=8)
    print(otime.isoformat())
    return otime.isoformat()
    #return arrow.now() #maybe this is the right one


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    dist = control_dist_km
    ctime = arrow.get(brevet_start_time)



    time = 0
    newdist = 0
    specialtime = 0
    # print(speed[200])
    if dist <= 60:
        specialtime += 1
        specialtime += dist / 20
        print("special time", specialtime)
        ###return early

    if (dist <= 200) and (dist > 0):  # 0-200
        time += dist / 15
    elif ((dist - 200) > 0):  # 200+
        time += 200 / 15
        newdist = dist - 200
    print(newdist)
    # ans = 200/34 + 200/32 + 50/30

    if (dist <= 400) and (dist > 200):  # 201-400
        time += newdist / 15


    if (dist > 400):  # 400+
        time += 200 / 15
        newdist = newdist - 200


    if (dist <= 600) and (dist > 400):  # 401-600
        time += newdist / 15
    if (dist > 600):
        time += 200 / 15
        newdist = newdist - 200

    if ((dist - 600) > 0) and (dist > 1000):
        time += 400 / 11.428  # 600+
        newdist = newdist - 200
    print(newdist)
    print("600: ", time)

    if (dist <= 1000) and (dist > 600):  # 601-1200
        time += newdist / 11.428
    elif ((dist - 1000) > 0) and (dist > 1300):
        time += 400 / 11.428  # 1000+
        newdist = newdist - 400




    t = math.modf(time)
    hour = t[1]
    min = t[0] * 60
    min = round(min)
    ctime = ctime.shift(hours=8)
    if dist == 0:
        ctime = ctime.shift(hours=1)
        return ctime.isoformat()
    ctime = ctime.shift(hours=hour, minutes=min)

    print(ctime.isoformat())
    print(specialtime)

    if (dist <= 60) and (dist != 0):
        split = math.modf(specialtime)
        h = split[1]
        m = split[0]
        print(m)
        m = m*60
        m = round(m)
        stime = arrow.get(brevet_start_time)
        stime = stime.shift(hours=h, minutes=m)
        stime = stime.shift(hours=8)
        return stime.isoformat()

    else:
        return ctime.isoformat()


    #return arrow.now()
