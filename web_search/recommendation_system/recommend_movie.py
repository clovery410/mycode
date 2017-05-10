import random
import numpy as np
import scipy as sp
from scipy import spatial
from heapq import *
import collections
import matplotlib.pyplot as plt

class MovieRecommend(object):
    def __init__(self, k):
        self.raw_user_movie = np.zeros((201, 1001), dtype = int)
        self.user_movie = np.zeros((201, 1001), dtype = int)
        self.iuf_rating = np.zeros((201, 1001), dtype = int)
        self.movie_movie = np.zeros((1001, 1001), dtype = int)
        self.movie_rating_cnt = np.zeros(1001, dtype = int)
        self.movie_cnt = 0
        self.user_cnt = 0
        self.k = k
        
    def preprocessTrainingData(self):
        f1 = open('train.txt', 'r')
        raw_content = f1.read()
        raw_lines = raw_content.splitlines()

        user_movie_matrix = self.user_movie
        for i, line in enumerate(raw_lines):
            user_movie_matrix[i+1] = [0,] + line.split('\t')

        self.user_cnt = len(user_movie_matrix)
        self.movie_cnt = len(user_movie_matrix[0])

        f1.close()
        self.calMovieCount()

    def calMovieCount(self):
        movie_rating_cnt = self.movie_rating_cnt
        user_movie = self.user_movie
        
        for j in range(self.movie_cnt):
            for i in range(self.user_cnt):
                if user_movie[i][j] > 0:
                    movie_rating_cnt[j] += 1

    def calIUFRating(self):
        for i in range(1, self.user_cnt):
            for j in range(1, self.movie_cnt):
                self.iuf_rating[i][j] = self.user_movie[i][j] * np.log((self.user_cnt-1) / movie_rating_cnt[j])
        
                    
    def recommendEval(self, test_input):
        f1 = open(test_input, 'r')
        content = f1.read()
        lines = content.splitlines()
        
        test_user_seen = collections.defaultdict(list)
        test_user_not_seen = collections.defaultdict(list)
        
        for line in lines:
            user_id, movie_id, rating = line.split()
            if rating != '0':
                test_user_seen[int(user_id)].append((int(movie_id), int(rating)))
            else:
                test_user_not_seen[int(user_id)].append(int(movie_id))

        # self.basicUserBaseCF(test_input, test_user_seen, test_user_not_seen)
        # self.pearsonCorrelationCF(test_input, test_user_seen, test_user_not_seen)

        f1.close()

    def crossValidation(self, n):
        user_movie = self.user_movie
        test_user_seen = collections.defaultdict(list)
        test_user_not_seen = collections.defaultdict(list)

        for i in range(151, self.user_cnt):
            for j in range(self.movie_cnt):
                if user_movie[i][j] == 0:
                    continue
                if len(test_user_seen[i]) < n:
                    test_user_seen[i].append((j, user_movie[i][j]))
                else:
                    test_user_not_seen[i].append(j)

        maes = []
        for k in [5, 10, 15, 20, 30, 150]:
            # maes.append(self.pearsonCorrelation_cross(k, user_movie[:151], test_user_seen, test_user_not_seen))
            # maes.append(self.basicUserBaseCF_cross(k, user_movie[:151], test_user_seen, test_user_not_seen))
            maes.append(self.itemBasedCF_cross(k, user_movie[:151], test_user_seen, test_user_not_seen))
        print maes
        # plt.plot(maes)

    def itemBasedCF_cross(self, k, user_movie, test_user_seen, test_user_not_seen):
        mae = []
        for test_user_id, movie_list in test_user_not_seen.items():
            seen_movie_rating = test_user_seen[test_user_id]
            for not_seen_movie_id in sorted(movie_list):
                k_nearest_movies = self.itemBasedAdjustedCosSim(k, user_movie, seen_movie_rating, not_seen_movie_id)
                score = 3
                if k_nearest_movies:
                    if sum(x[0] for x in k_nearest_movies) != 0:
                        # print test_user_id, test_user_not_seen, test_user_seen, k_nearest_movies
                        score = int(round(sum(x[0] * x[1] for x in k_nearest_movies) / sum(x[0] for x in k_nearest_movies)))
                mae.append(abs(score - self.user_movie[test_user_id][not_seen_movie_id]))
                
        return sum(mae) * 1.0 / len(mae)
                
    def pearsonCorrelation_cross(self, k, user_movie, test_user_seen, test_user_not_seen):
        mae = []
        for test_user_id, movie_list in test_user_not_seen.items():
            seen_movie_rating = test_user_seen[test_user_id]
            test_user_average_rate = sum(x[1] for x in seen_movie_rating) * 1.0 / len(seen_movie_rating)
            for not_seen_movie_id in sorted(movie_list):
                k_nearest_users = self.pearsonSimMethod(k, user_movie, seen_movie_rating, not_seen_movie_id, test_user_average_rate, False, 2.5)
                score = test_user_average_rate
                sum_abs_weight, sum_diff_rate = 0, 0
                
                for abs_w, w, u_id, u_ave_r in k_nearest_users:
                    sum_abs_weight += abs_w
                    sum_diff_rate += w * (user_movie[u_id][not_seen_movie_id] - u_ave_r)
                if sum_abs_weight != 0:
                    score += sum_diff_rate / sum_abs_weight

                score = min(5, max(int(round(score)), 1))
                mae.append(abs(score - self.user_movie[test_user_id][not_seen_movie_id]))

        return sum(mae) * 1.0 / len(mae)        

    def basicUserBaseCF_cross(self, k, user_movie, test_user_seen, test_user_not_seen):
        mae = []
        for test_user_id, movie_list in test_user_not_seen.items():
            seen_movie_rating = test_user_seen[test_user_id]
            for not_seen_movie_id in sorted(movie_list):
                k_nearest_users = self.cosineSimMethod(k, user_movie, seen_movie_rating, not_seen_movie_id)
                score = 0
                if k_nearest_users:
                    score = int(round(sum(x[0] * user_movie[x[1]][not_seen_movie_id] for x in k_nearest_users) / sum(x[0] for x in k_nearest_users)))
                mae.append(abs(score - self.user_movie[test_user_id][not_seen_movie_id]))
                
        return sum(mae) * 1.0 / len(mae)
    
    def getAverageRating(self, movie_list):
        return movie_list.sum() * 1.0 / (movie_list != 0).sum()

    def cosineSimMethod(self, k, user_movie, seen_movie_rating, not_seen_movie_id):
        # user_movie = self.user_movie
        k_nearest_users = []

        for cur_user_id, cur_user_ratings in enumerate(user_movie):
            if cur_user_ratings[not_seen_movie_id] == 0:
                continue
            v1, v2 = [], []
            for j, rate in seen_movie_rating:
                if cur_user_ratings[j] > 0:
                    v1.append(cur_user_ratings[j])
                    v2.append(rate)
            if v1:
                cosine_sim = 1 - spatial.distance.cosine(v1, v2)
                heappush(k_nearest_users, (cosine_sim, cur_user_id))

            if len(k_nearest_users) > k:
                heappop(k_nearest_users)

        return k_nearest_users
    
    def basicUserBaseCF(self, test_input, test_user_seen, test_user_not_seen):
        f = open('basic_out_' + test_input, 'w')
        user_movie = self.user_movie
        
        for test_user_id, movie_list in test_user_not_seen.items():
            seen_movie_rating = test_user_seen[test_user_id]
            for not_seen_movie_id in sorted(movie_list):
                k_nearest_users = self.cosineSimMethod(self.k, user_movie, seen_movie_rating, not_seen_movie_id)
                score = random.randint(1, 5)
                if k_nearest_users:
                    score = int(round(sum(x[0] * user_movie[x[1]][not_seen_movie_id] for x in k_nearest_users) / sum(x[0] for x in k_nearest_users)))
                    
                f.writelines(str(test_user_id) + ' ' + str(not_seen_movie_id) + ' ' + str(score) + '\n')
                
        f.close()

    def pearsonSimMethod(self, k, user_movie, seen_movie_rating, not_seen_movie_id, average_v2, iuf = False, rou = None):
        # user_movie = self.user_movie
        k_nearest_users = []
        movie_rating_cnt = self.movie_rating_cnt
        
        for cur_user_id, cur_user_ratings in enumerate(user_movie):
            if cur_user_ratings[not_seen_movie_id] == 0:
                continue
            v1, v2 = [], []   # v1 is training user, v2 is active user
            average_v1 = self.getAverageRating(cur_user_ratings)
            
            for j, rate in seen_movie_rating:
                if cur_user_ratings[j] > 0:
                    # If iuf is True, then multiply true iuf value
                    iuf_val = np.log((self.user_cnt-1) / movie_rating_cnt[j]) if iuf else 1
                    v1.append((cur_user_ratings[j] - average_v1) * iuf_val)
                    v2.append((rate - average_v2) * iuf_val)
                    
            if len(v1) >= 1:
                if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0 or len(v1) == 1:
                    cosine_sim = 0       # need to think about it
                else:
                    cosine_sim = 1 - spatial.distance.cosine(v1, v2)
                if rou is not None:
                    cosine_sim = cosine_sim * pow(abs(cosine_sim), rou-1)
                heappush(k_nearest_users, (abs(cosine_sim), cosine_sim, cur_user_id, average_v1))

            if len(k_nearest_users) > k:
                heappop(k_nearest_users)

        return k_nearest_users

    def pearsonCorrelationCF(self, test_input, test_user_seen, test_user_not_seen):
        f = open('pearson_iuf_out_' + test_input, 'w')
        user_movie = self.user_movie

        for test_user_id, movie_list in test_user_not_seen.items():
            seen_movie_rating = test_user_seen[test_user_id]
            test_user_average_rate = sum(x[1] for x in seen_movie_rating) * 1.0 / len(seen_movie_rating)
            for not_seen_movie_id in sorted(movie_list):
                k_nearest_users = self.pearsonSimMethod(self.k, user_movie, seen_movie_rating, not_seen_movie_id, test_user_average_rate, True)
                score = test_user_average_rate
                sum_abs_weight, sum_diff_rate = 0, 0
                
                for abs_w, w, u_id, u_ave_r in k_nearest_users:
                    sum_abs_weight += abs_w
                    sum_diff_rate += w * (user_movie[u_id][not_seen_movie_id] - u_ave_r)
                if sum_abs_weight != 0:
                    score += sum_diff_rate / sum_abs_weight
                    
                score = min(5, max(int(round(score)), 1))
                f.writelines(str(test_user_id) + ' ' + str(not_seen_movie_id) + ' ' + str(score) + '\n')
                
        f.close()

    def itemBasedAdjustedCosSim(self, k, user_movie, seen_movie_rating, not_seen_movie_id):
        k_nearest_movies = []

        for j, rate in seen_movie_rating:
            v1, v2 = [], []   # v1 is movie active user rated, v2 is not seen current movie by the active user 
            
            for cur_user_id, cur_user_ratings in enumerate(user_movie):
                if cur_user_ratings[not_seen_movie_id] == 0 or cur_user_ratings[j] == 0:
                    continue
                average_u_rate = self.getAverageRating(cur_user_ratings)
                v1.append(cur_user_ratings[j] - average_u_rate)
                v2.append(cur_user_ratings[not_seen_movie_id] - average_u_rate)

            if len(v1) >= 1:
                if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0 or len(v1) == 1:
                    cosine_sim = 0       # need to think about it
                else:
                    cosine_sim = 1 - spatial.distance.cosine(v1, v2)
                if cosine_sim > 0:
                    heappush(k_nearest_movies, (cosine_sim, rate))
                         
            if len(k_nearest_movies) > k:
                heappop(k_nearest_movies)

        return k_nearest_movies
    
    def itemBasedCF(self, test_input, test_user_seen, test_user_not_seen):
        f = open('item_based_out_' + test_input, 'w')
        user_movie = self.user_movie
        
        for test_user_id, movie_list in test_user_not_seen.items():
            seen_movie_rating = test_user_seen[test_user_id]
            for not_seen_movie_id in sorted(movie_list):
                k_nearest_movies = self.itemBasedAdjustedCosSim(self.k, user_movie, seen_movie_rating, not_seen_movie_id)
                score = 3
                if k_nearest_movies:
                    score = int(round(sum(x[0] * x[1] for x in k_nearest_movies) / sum(x[0] for x in k_nearest_movies)))
                
                f.writelines(str(test_user_id) + ' ' + str(not_seen_movie_id) + ' ' + str(score) + '\n')
                
        f.close()


if __name__ == "__main__":
    mr = MovieRecommend(200)
    mr.preprocessTrainingData()
    # mr.recommendEval('test5.txt')
    mr.crossValidation(20)
        
