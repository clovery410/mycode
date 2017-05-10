import datetime, time
def courseSession(launch_date, repeat_freq, enroll_date):
    s1 = launch_date / 1000.0
    # launch = datetime.datetime.utcfromtimestamp(s1).strftime('%Y-%m-%d-%A %H:%M:%S.%f')
    s2 = enroll_date / 1000.0
    # enroll = datetime.datetime.utcfromtimestamp(s2).strftime('%Y-%m-%d-%A %H:%M:%S.%f')
    # print launch, enroll

    launchDate = datetime.datetime.utcfromtimestamp(s1)
    enrollDate = datetime.datetime.utcfromtimestamp(s2)
    weekDate = launchDate.weekday()
    timeDelta = datetime.timedelta(days = (7 - weekDate) % 7)
    first_session = launchDate + timeDelta

    res = []
    cur_session = first_session
    while cur_session < enrollDate:
        cur_session += datetime.timedelta(weeks = repeat_freq)
    for i in range(3):
        ts = (cur_session - datetime.datetime(1970, 1, 1)).total_seconds()
        res.append(int(ts*1000))
        cur_session += datetime.timedelta(weeks = repeat_freq)
    return res
    
    # s3 = 1236472051807 / 1000.0
    # print datetime.datetime.utcfromtimestamp(s3).strftime('%Y-%m-%d-%A %H:%M:%S.%f')
    # print datetime.datetime.utcnow()

#solution2, O(1) solution
def getUpcomingSessions(launch_date, repeat_frequency, enrollment_date):
    launchDate = datetime.datetime.utcfromtimestamp(launch_date / 1000.0)
    enrollDate = datetime.datetime.utcfromtimestamp(enrollment_date / 1000.0)
    weekDate = launchDate.weekday()
    timeDelta = datetime.timedelta(days = (7 - weekDate) % 7)
    cur_session = launchDate + timeDelta

    res = []
    if cur_session < enrollDate:
        days_delta = enrollDate - cur_session
        diff_days = (repeat_frequency * 7) - days_delta.days % (repeat_frequency * 7)
        cur_session = enrollDate + datetime.timedelta(days = diff_days)
    for i in range(3):
        ts = (cur_session - datetime.datetime(1970, 1, 1)).total_seconds()
        res.append(int(ts * 1000))
        cur_session += datetime.timedelta(weeks = repeat_frequency)
    return res
        
        
if __name__ == "__main__":
    print courseSession(1470096000000, 2, 1470787200000)
    print getUpcomingSessions(1470096000000, 2, 1470787200000)
