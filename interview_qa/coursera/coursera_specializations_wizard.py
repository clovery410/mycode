import datetime
def specializations_wizard(courses, enroll_date):
    if len(courses) == 0: return []
    res = []
    cur_enroll = datetime.datetime.utcfromtimestamp(enroll_date / 1000.0)
    for i in range(len(courses)):
        launchDate = datetime.datetime.utcfromtimestamp(courses[i][0] / 1000.0)
        weekDate = launchDate.weekday()
        timeDelta = datetime.timedelta(days = (7 - weekDate) % 7)
        cur_session = launchDate + timeDelta

        while cur_session < cur_enroll:
            cur_session += datetime.timedelta(weeks = courses[i][1])
        end_session = cur_session + datetime.timedelta(weeks = courses[i][2])
        start_ts = (cur_session - datetime.datetime(1970, 1, 1)).total_seconds()
        end_ts = (end_session - datetime.datetime(1970, 1, 1)).total_seconds()
        res.append([int(start_ts*1000), int(end_ts*1000)])
        cur_enroll = end_session
    return res

#follow-up, assume courses are grouped by priorities, the course with high priority should be finished first, however this time, same priority courses can be taken at the same time.
def specializations_with_priority(course_groups, enroll_date):
    if len(course_groups) == 0: return []
    res = []
    cur_enroll = datetime.datetime.utcfromtimestamp(enroll_date / 1000.0)
    next_enroll = cur_enroll
    for group in course_groups:
        cur_enroll = next_enroll
        for i in range(len(group)):
            launchDate = datetime.datetime.utcfromtimestamp(group[i][0] / 1000.0)
            weekDate = launchDate.weekday()
            timeDelta = datetime.timedelta(days = (7 - weekDate) % 7)
            cur_session = launchDate + timeDelta

            if cur_session < cur_enroll:
                freq = group[i][1]
                day_counts = (freq * 7) - (cur_enroll - cur_session).day % (freq * 7)
                cur_session = cur_enroll + datetime.timedelta(days = day_counts)
            end_session = cur_session + datetime.timedelta(weeks = group[i][2])
            start_ts = (cur_session - datetime.datetime(1970,1,1)).total_seconds()
            end_ts = (end_session - datetime.datetime(1970,1,1)).total_seconds()
            res.append([int(start_ts * 1000), int(end_ts * 1000)])
            if end_session > next_enroll:
                next_enroll = end_session
    return res
                

if __name__ == "__main__":
    print specializations_wizard([[1469923200000, 2, 4], [1469923200000, 2, 4]], 1470268800000)
        
