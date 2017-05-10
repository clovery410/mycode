import json
import os
import numpy
from datetime import datetime
from sklearn.cluster import DBSCAN
from collections import OrderedDict
from pprint import pprint

def error(message):
    print(message)

class Tweet(object):
    def __init__(self, time, coordinate):
        self.time = time
        self.coordinate = coordinate
        self.region_id = None

class Dbscan(object):
    file_path = "geo_data_67.json"
    eps = 0.00018
    minPts = 4
    threshold = 10

    user_name = None
    user_id = None
    n_tweets = 0
    n_qualified_tweets = 0
    n_regions = None
    threshold_ratio = None
    n_three_patterns = 0
    TS = list()    # TS:tweet_set = [Tweet{time_object, coordinate, region_id}]
    FRS = dict()   # FRS:frequent_region_set = {key:region_id, value:region_coordinate}
    DTS = dict()   # DTS:daily_trajectory_set = {key:date, value:[Tweet]}
    DT = list()    # DT:daily_trajectory = [[region_id]]

    # def __init__(self):
    #     try:
    #         self.run()
    #     except Exception as e:
    #         print(e)

    def run(self):
        if os.stat(self.file_path).st_size == 0:
            error("ERROR: Empty file.")
            return
        self.TS = self.init_data()
        if not self.TS:
            error("ERROR: TS is empty.")
            return
        self.n_qualified_tweets = len(self.TS)
        self.threshold_ratio = 0.1 * self.threshold / self.n_qualified_tweets
        self.n_regions = self.cluster()
        if self.n_regions == 0:
            error("ERROR: n_regions is 0.")
            return
        self.FRS = self.get_FRS()
        if not self.FRS:
            error("ERROR: FRS is empty.")
            return
        self.DTS = self.get_DTS()
        if not self.DTS:
            error("ERROR: DTS is empty.")
            return
        self.DT = self.get_DT()
        self.show_result()

    def init_data(self):
        TS = list()
        with open(self.file_path) as data_file:
            data = json.load(data_file)
        if "user_screen_name" not in data:
            error("ERROR: No key word \'user_screen_name\' in json file.")
        else:
            self.user_name = data["user_screen_name"]
        if "user_id" not in data:
            error("ERROR: No key word \'user_id\' in json file.")
        else:
            self.user_id = data["user_id"]
        if "features" not in data:
            error("ERROR: No key word \'features\' in json file.")
            return
        if len(data["features"]) == 0:
            error("ERROR: No tweets in json file.")
            return
        for tweet in data["features"]:
            self.n_tweets += 1
            if "geometry" not in tweet or "properties" not in tweet:
                error("ERROR: No key words \'geometry\' or \'properties\' in json file.")
                continue
            if "coordinates" not in tweet["geometry"] or "created_at" not in tweet["properties"]:
                error("ERROR: No key words \'coordinates\' or \'created_at\' in json file.")
                continue
            time = tweet["properties"]["created_at"]
            time_object = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
            if time_object.weekday() >= 5:
                continue    # remove data of weekend
            coordinate = tweet["geometry"]["coordinates"]
            TS.append(Tweet(time_object, coordinate))
        return TS

    def cluster(self):
        data_set = list()
        for tweet in self.TS:
            data_set.append(numpy.array(tweet.coordinate))
        data_set = numpy.array(data_set)
        db = DBSCAN(eps=self.eps, min_samples=self.minPts).fit(data_set)
        for i in range(len(self.TS)):
            self.TS[i].region_id = db.labels_[i]
        n_regions = len(set(db.labels_)) - (1 if -1 in db.labels_ else 0)
        return n_regions

    def get_FRS(self):
        FRS = dict() # {key:region_id, value:region_coordinate}
        RS = dict()  # {key:region_id, value:[coordinate]}
        for tweet in self.TS:
            if tweet.region_id == -1:   # skip noise
                continue
            if tweet.region_id not in RS:
                RS[tweet.region_id] = [tweet.coordinate]
            else:
                RS[tweet.region_id].append(tweet.coordinate)
        for region_id, coordinates in RS.items():
            if len(coordinates) < self.threshold:
                continue
            x = 0.0
            y = 0.0
            for coordinate in coordinates:
                x += coordinate[0]
                y += coordinate[1]
            FRS[region_id] = [x / len(coordinates), y / len(coordinates)]
        return FRS

    def get_DTS(self):
        DTS = dict()  # DTS:daily_trajectory_set(dict) = {key:date, value:[Tweet]}
        for tweet in self.TS:
            if tweet.time.date() not in DTS:
                DTS[tweet.time.date()] = [tweet]
            else:
                DTS[tweet.time.date()].append(tweet)
        DTS = OrderedDict(sorted(DTS.items(), key=lambda t: t[0]))
        return DTS

    def get_DT(self):
        DT = list()    # DT:daily_trajectory = [[region_id]]
        for date, tweets in self.DTS.items():
            dt = list()
            if len(tweets) < 1:
                continue    # skip daily trajectory only with one tweet
            tweets.sort(key=lambda x: x.time)    # sort daily tweets by time
            for tweet in tweets:
                if tweet.region_id not in self.FRS:  # skip infrequent region
                    continue
                if tweet.region_id not in dt:    # only record the first one in the daily trajectory
                    dt.append(tweet.region_id)
                # print("regiond_id: %s ==> time: %s" %(tweet.region_id, tweet.time))
            if len(dt) > 1: # DT only records daily trajectory with tweets more than one
                if len(dt) >= 3:
                    self.n_three_patterns += 1
                DT.append(dt)
        return DT

    def show_result(self):
        print("====================================DBSCAN====================================")
        print("Input:\n\tfile_path = %s\n\teps = %s\n\tminPts = %s\n\tthreshold = %s\n" \
            %(self.file_path, self.eps, self.minPts, self.threshold))
        print("Basic information:")
        print("\tUser name: %s" %self.user_name)
        print("\tUser id: %s" %self.user_id)
        print("\tNumber of tweets: %s" %self.n_tweets)
        print("\tNumber of qualified tweets: %s" %self.n_qualified_tweets)
        print("\tThreshold_ratio: %s" %self.threshold_ratio)
        print("\tNumber of regions: %s" %self.n_regions)
        print()
        # print("DTS: date  ==> number of tweets")
        # for date, dts in self.DTS.items():
        #     print("%s ==> %s" %(date, len(dts)))
            # if date == datetime.strptime("2010-10-21", "%Y-%m-%d").date():
            #     for dt in dts:
            #         print(dt.time, dt.region_id, dt.coordinate)
        print("Number of FRS: %s\n\t%s\n\tFRS: %s\n" %(len(self.FRS), self.FRS.keys(), self.FRS))
        print("Number of DT: %s\nNumber of pattern, which its length is three or more: %s\n\tDT: %s" \
            %(len(self.DT), self.n_three_patterns, self.DT))
        print("==============================================================================")

main = Dbscan

if __name__ == "__main__":
    main().run()
