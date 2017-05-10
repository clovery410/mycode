import time
import random
import math
import numpy as np
import scipy as sp
from scipy import spatial
from heapq import *
import collections

class MovieRecommend(object):
    def __init__(self, k):
        self.raw_user_movie = np.zeros((201, 1001), dtype = int)   # This is used for cross validation
        self.user_movie = np.zeros((201, 1001), dtype = int)
        self.iuf_matrix = np.zeros((201, 1001), dtype = float)
        self.movie_movie = np.zeros((1001, 1001), dtype = int)
        
        self.movie_rating_cnt = np.zeros(1001, dtype = int)
        self.iuf_rating = np.zeros(1001, dtype = float)
        self.user_ave_rating = np.zeros(1001, dtype = float)
        self.user_iuf_ave_rating = np.zeros(1001, dtype = float)
        self.user_pop_rating = np.zeros(201, dtype = int)

        self.movie_dev = collections.defaultdict(dict)
        
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
            self.user_pop_rating[i+1] = self.getUserPopRating(i+1)
            
        # Should comment following self.user_cnt when doing cross validation, uncomment it when doing real prediction
        self.user_cnt = len(user_movie_matrix)
        self.movie_cnt = len(user_movie_matrix[0])

        f1.close()

    def calMovieCount(self):
        self.movie_rating_cnt = np.zeros(1001, dtype = int)
        user_movie = self.user_movie
        
        for j in range(self.movie_cnt):
            for i in range(self.user_cnt):
                if user_movie[i][j] > 0:
                    self.movie_rating_cnt[j] += 1

    def calIUFRating(self):
        for j in range(1, len(self.iuf_rating)):
            if self.movie_rating_cnt[j] != 0:
                self.iuf_rating[j] = np.log((self.user_cnt-1) * 1.0 / self.movie_rating_cnt[j])

    def calIUFMatrix(self):
        for i in range(self.user_cnt):
            for j in range(self.movie_cnt):
                self.iuf_matrix[i][j] = self.user_movie[i][j] * self.iuf_rating[j]
                
    def calUserAveRating(self):
        for u_id in range(self.user_cnt):
            self.user_ave_rating[u_id] = self.getAverageRating(self.user_movie[u_id])

    def calUserIUFAveRating(self):
        for u_id in range(self.user_cnt):
            self.user_iuf_ave_rating[u_id] = self.getIUFAverageRating(u_id)

    def calItemToItemAdjSim(self):
        user_movie, movie_movie = self.user_movie, self.movie_movie
        user_pop_rating, user_ave_rating = self.user_pop_rating, self.user_ave_rating
        
        for i in range(self.movie_cnt):
            movie_movie[i][i]= 1.0
            for j in range(i+1, self.movie_cnt):
                v1, v2 = [], []
                for u_id in range(self.user_cnt):
                    rate1, rate2 = user_movie[u_id][i], user_movie[u_id][j]
                    if rate1 == 0 or rate2 == 0:
                        continue
                    v1.append(rate1 - user_ave_rating[u_id])
                    v2.append(rate2 - user_ave_rating[u_id])
                    
                if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:
                    cosine_sim = 0
                else:
                    cosine_sim = 1 - spatial.distance.cosine(v1, v2)
                movie_movie[i][j] = movie_movie[j][i] = cosine_sim

    def calDeviation(self):
        user_movie = self.user_movie
        movie_dev = self.movie_dev
        
        for j in range(1, self.movie_cnt):
            for i in range(1, self.movie_cnt):
                dev_val, count = 0, 0
                for u_id in range(1, self.user_cnt):
                    if i != j and user_movie[u_id][j] != 0 and user_movie[u_id][i] != 0:
                        dev_val += user_movie[u_id][j] - user_movie[u_id][i]
                        count += 1
                if count > 0:
                    movie_dev[j][i] = (dev_val * 1.0 / count, count)
                    
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
                
        self.calMovieCount()
        self.calIUFRating()
        self.calIUFMatrix()
        self.calUserAveRating()
        self.calUserIUFAveRating()
        self.calDeviation()

        # self.basicUserBaseCF(test_input, test_user_seen, test_user_not_seen)
        # self.pearsonCorrelationCF(test_input, test_user_seen, test_user_not_seen)
        # self.itemBasedCF(test_input, test_user_seen, test_user_not_seen)
        # self.slopeOneCF(test_input, test_user_seen, test_user_not_seen)
        self.ensemble(test_input, test_user_seen, test_user_not_seen, 0.71)
        
        f1.close()

    def shuffle(self, nums):
        n = len(nums)
        for i in range(n):
            j = random.randint(i, n-1)
            nums[i], nums[j] = nums[j], nums[i]
        return nums

    def crossLoop(self, n):
        """
        This fucntion is only used for cross validation
        Inner loop of cross validation
        Does work of spliting training data into training and testing randomly
        and the preparation work before algorithm
        """
        indices = range(1, 201)
        indices = self.shuffle(indices)
        test_user_seen = collections.defaultdict(list)
        test_user_not_seen = collections.defaultdict(list)
        
        for i in range(180):
            self.user_movie[i+1] = self.raw_user_movie[indices[i]]
            self.user_pop_rating[i+1] = self.getUserPopRating(i+1)
            
        self.user_cnt = len(self.user_movie)
        self.calMovieCount()
        self.calIUFRating()
        self.calIUFMatrix()
        self.calUserAveRating()
        self.calUserIUFAveRating()
        # self.calItemToItemAdjSim()
        self.calDeviation()
        
        for i in range(180, 200):
            user_idx = indices[i]
            movie_indices = self.shuffle(range(1, 1001))
            for j in movie_indices:
                if self.raw_user_movie[user_idx][j] == 0:
                    continue
                if len(test_user_seen[user_idx]) < n:
                    test_user_seen[user_idx].append((j, self.raw_user_movie[user_idx][j]))
                else:
                    test_user_not_seen[user_idx].append(j)
        maes = []
        # for k in [20]:
        for weight in [0.7, 0.8, 0.9]:
            # maes.append(self.itemBasedCF_cross(k, self.user_movie, test_user_seen, test_user_not_seen))
            # maes.append(self.slopeOneCF_cross(k, self.user_movie, test_user_seen, test_user_not_seen))
            # maes.append(self.pearsonCorrelation_cross(k, self.user_movie, test_user_seen, test_user_not_seen))
            # maes.append(self.basicUserBaseCF_cross(k, self.user_movie, test_user_seen, test_user_not_seen))
            maes.append(self.ensemble_cross(180, self.user_movie, test_user_seen, test_user_not_seen, weight))

        return maes
        
    def crossValidation(self, n):
        """
        This function is only used for cross validation
        Outer loop of cross validation
        """
        ave_maes = [0] * 3
        for i in range(10):
            maes = self.crossLoop(n)
            for j in range(len(maes)):
                ave_maes[j] += maes[j]
        for j in range(len(ave_maes)):
            ave_maes[j] /= 10
            
        print ave_maes

    def ensemble_cross(self, k, user_movie, test_user_seen, test_user_not_seen, weight):
        """
        This function is only used for cross validation
        Main function of ensemble method
        """
        movie_dev = self.movie_dev
        mae = []
        for test_user_id, movie_list in test_user_not_seen.items():
            seen_movie_rating = test_user_seen[test_user_id]
            test_user_pop_rate = collections.Counter([x[1] for x in seen_movie_rating]).most_common(1)[0][0]
            test_user_average_rate = sum(x[1] for x in seen_movie_rating) * 1.0 / len(seen_movie_rating)
            test_user_average_iuf_rate = sum(x[1] * self.iuf_rating[x[0]] for x in seen_movie_rating) * 1.0 / sum(self.iuf_rating[x[0]] for x in seen_movie_rating)
            for not_seen_movie_id in sorted(movie_list):
                k_nearest_users_basic = self.cosineSimMethod(k, user_movie, seen_movie_rating, not_seen_movie_id, True)
                k_nearest_users_pearson = self.pearsonSimMethod(k, user_movie, seen_movie_rating, not_seen_movie_id, test_user_average_iuf_rate, True)

                #### This is cosine iuf prediction
                score_basic = test_user_pop_rate
                if k_nearest_users_basic:
                    score_basic = sum(x[0] * user_movie[x[1]][not_seen_movie_id] for x in k_nearest_users_basic) / sum(x[0] for x in k_nearest_users_basic)

                # #### This is pearson iuf prediction
                # score_pearson = test_user_average_rate
                # sum_abs_weight, sum_diff_rate = 0, 0
                
                # for abs_w, w, u_id, u_ave_r in k_nearest_users_pearson:
                #     sum_abs_weight += abs_w
                #     sum_diff_rate += w * (user_movie[u_id][not_seen_movie_id] - u_ave_r)
                # if sum_abs_weight != 0:
                #     score_pearson += sum_diff_rate / sum_abs_weight

                #### This is weighted slope one prediction
                slope_score, slope_count = 0, 0
                for seen_movie_id, seen_rate in seen_movie_rating:
                    if seen_movie_id in movie_dev[not_seen_movie_id]:
                        d, c = movie_dev[not_seen_movie_id][seen_movie_id]
                        slope_score += (d + seen_rate) * c
                        slope_count += c
                slope_score = slope_score * 1.0 / slope_count if slope_count else test_user_pop_rate

                score = min(5, max(int(round(weight * slope_score + (1 - weight) * score_basic)), 1))
                mae.append(abs(score - self.raw_user_movie[test_user_id][not_seen_movie_id]))

        return sum(mae) * 1.0 / len(mae)
        
    def slopeOneCF_cross(self, k, user_movie, test_user_seen, test_user_not_seen):
        """
        This function is only used for cross validation
        Main function of Weighted Slope One algorithm
        """
        movie_dev = self.movie_dev
        mae = []
        for test_user_id, movie_list in test_user_not_seen.items():
            seen_movie_rating = test_user_seen[test_user_id]
            cur_user_pop_rate = collections.Counter([x[1] for x in seen_movie_rating]).most_common(1)[0][0]
            for not_seen_movie_id in sorted(movie_list):
                cur_score, cur_count = 0, 0
                for seen_movie_id, seen_rate in seen_movie_rating:
                    if seen_movie_id in movie_dev[not_seen_movie_id]:
                        d, c = movie_dev[not_seen_movie_id][seen_movie_id]
                        cur_score += (d + seen_rate) * c
                        cur_count += c
                score = cur_score * 1.0 / cur_count if cur_count else cur_user_pop_rate
                score = max(1, min(5, int(round(score))))
                mae.append(abs(score - self.raw_user_movie[test_user_id][not_seen_movie_id]))

        return sum(mae) * 1.0 / len(mae)
                
    def itemBasedCF_cross(self, k, user_movie, test_user_seen, test_user_not_seen):
        """
        This function is only used for cross validation
        Main function of item-based CF algorithm
        """
        mae = []
        for test_user_id, movie_list in test_user_not_seen.items():
            seen_movie_rating = test_user_seen[test_user_id]
            test_user_average_rate = sum(x[1] for x in seen_movie_rating) * 1.0 / len(seen_movie_rating)
            for not_seen_movie_id in sorted(movie_list):
                k_nearest_movies = self.itemBasedAdjustedCosSim(k, user_movie, seen_movie_rating, not_seen_movie_id)
                score = test_user_average_rate
                sum_abs_weight, sum_diff_rate = 0, 0
                
                for w, rate in k_nearest_movies:
                    sum_abs_weight += abs(w)
                    sum_diff_rate += w * (rate - test_user_average_rate)
                if sum_abs_weight != 0:
                    score += sum_diff_rate / sum_abs_weight

                score = min(5, max(int(round(score)), 1))
                mae.append(abs(score - self.raw_user_movie[test_user_id][not_seen_movie_id]))

        return sum(mae) * 1.0 / len(mae)
        
    def pearsonCorrelation_cross(self, k, user_movie, test_user_seen, test_user_not_seen):
        """
        This function is only used for cross validation
        Main function of user-based CF with Pearson Correlation
        """
        mae = []
        for test_user_id, movie_list in test_user_not_seen.items():
            seen_movie_rating = test_user_seen[test_user_id]
            test_user_average_rate = sum(x[1] for x in seen_movie_rating) * 1.0 / len(seen_movie_rating)
            test_user_average_iuf_rate = sum(x[1] * self.iuf_rating[x[0]] for x in seen_movie_rating) * 1.0 / sum(self.iuf_rating[x[0]] for x in seen_movie_rating)
            for not_seen_movie_id in sorted(movie_list):
                k_nearest_users = self.pearsonSimMethod(k, user_movie, seen_movie_rating, not_seen_movie_id, test_user_average_iuf_rate, True)
                import pdb
                pdb.set_trace()
                score = test_user_average_rate
                sum_abs_weight, sum_diff_rate = 0, 0
                
                for abs_w, w, u_id, u_ave_r in k_nearest_users:
                    sum_abs_weight += abs_w
                    sum_diff_rate += w * (user_movie[u_id][not_seen_movie_id] - u_ave_r)
                if sum_abs_weight != 0:
                    score += sum_diff_rate / sum_abs_weight

                score = min(5, max(int(round(score)), 1))
                mae.append(abs(score - self.raw_user_movie[test_user_id][not_seen_movie_id]))

        return sum(mae) * 1.0 / len(mae)

    def basicUserBaseCF_cross(self, k, user_movie, test_user_seen, test_user_not_seen):
        """
        This function is only used for cross validaton
        Main function of user-based CF with cosine similarity
        """
        mae = []
        for test_user_id, movie_list in test_user_not_seen.items():
            seen_movie_rating = test_user_seen[test_user_id]
            for not_seen_movie_id in sorted(movie_list):
                k_nearest_users = self.cosineSimMethod(k, user_movie, seen_movie_rating, not_seen_movie_id)
                score = collections.Counter([x[1] for x in seen_movie_rating]).most_common(1)[0][0]
                if k_nearest_users:
                    score = int(round(sum(x[0] * user_movie[x[1]][not_seen_movie_id] for x in k_nearest_users) / sum(x[0] for x in k_nearest_users)))
                mae.append(abs(score - self.raw_user_movie[test_user_id][not_seen_movie_id]))
                
        return sum(mae) * 1.0 / len(mae)
    
    def getAverageRating(self, movie_list):
        return 0.0 if not movie_list.sum() else movie_list.sum() * 1.0 / (movie_list != 0).sum()
    
    def getIUFAverageRating(self, u_id):
        numerator = self.iuf_matrix[u_id].sum()
        denominator = sum(self.iuf_rating[j] for j in range(self.movie_cnt) if self.iuf_matrix[u_id][j] > 0)
        return numerator / denominator if denominator else 0

    def getUserPopRating(self, u_id):
        counter = collections.defaultdict(int)
        for rate in self.user_movie[u_id]:
            if rate > 0:
                counter[rate] += 1
        return max(counter, key = counter.get)
    
    def cosineSimMethod(self, k, user_movie, seen_movie_rating, not_seen_movie_id, iuf_flag = False):
        """
        This is a helper function for calculating cosine similarity
        """
        user_movie = self.user_movie
        k_nearest_users = []
        iuf_rating, iuf_matrix = self.iuf_rating, self.iuf_matrix
        user_pop_rating = self.user_pop_rating

        for cur_user_id, cur_user_ratings in enumerate(user_movie):
            if cur_user_ratings[not_seen_movie_id] == 0:
                continue
            v1, v2 = [], []  # v1 stores common rated movie for current user, v2 stores common rated movie for active user
            for j, rate2 in seen_movie_rating:
                if cur_user_ratings[j] >= 0:  # here modified > to >= will have effect of default voting strategy
                    rate1 = cur_user_ratings[j] or user_pop_rating[cur_user_id]
                    # If iuf is True, then multiply true iuf value
                    if iuf_flag:
                        v1.append(rate1 * iuf_rating[j])
                        v2.append(rate2 * iuf_rating[j])
                    else:
                        v1.append(rate1)
                        v2.append(rate2)
            if v1:
                cosine_sim = 1 - spatial.distance.cosine(v1, v2)
                heappush(k_nearest_users, (cosine_sim, cur_user_id))

            if len(k_nearest_users) > k:
                heappop(k_nearest_users)

        return k_nearest_users
    
    def basicUserBaseCF(self, test_input, test_user_seen, test_user_not_seen):
        """
        This is main entrance for user-based CF with cosine similarity
        """
        f = open('basic_out_' + test_input, 'w')
        user_movie = self.user_movie
        
        for test_user_id, movie_list in test_user_not_seen.items():
            seen_movie_rating = test_user_seen[test_user_id]
            for not_seen_movie_id in sorted(movie_list):
                k_nearest_users = self.cosineSimMethod(self.k, user_movie, seen_movie_rating, not_seen_movie_id)
                score = collections.Counter([x[1] for x in seen_movie_rating]).most_common(1)[0][0]
                if k_nearest_users:
                    score = int(round(sum(x[0] * user_movie[x[1]][not_seen_movie_id] for x in k_nearest_users) / sum(x[0] for x in k_nearest_users)))
                    
                f.writelines(str(test_user_id) + ' ' + str(not_seen_movie_id) + ' ' + str(score) + '\n')
                
        f.close()

    def pearsonSimMethod(self, k, user_movie, seen_movie_rating, not_seen_movie_id, average_v2, iuf_flag = False, rou = None):
        """
        This is a helper function for calculating pearson correlation similarity
        It also has two flags which is used for turning on IUF and Case modification
        """
        k_nearest_users = []
        iuf_rating, user_pop_rating = self.iuf_rating, self.user_pop_rating
        user_ave_rating, user_iuf_ave_rating = self.user_ave_rating, self.user_iuf_ave_rating
        
        for cur_user_id, cur_user_ratings in enumerate(user_movie):
            if cur_user_ratings[not_seen_movie_id] == 0:
                continue
            v1, v2 = [], []   # v1 is training user, v2 is active user
            average_v1 = user_ave_rating[cur_user_id]
            average_iuf_v1 = user_iuf_ave_rating[cur_user_id]
            
            for j, rate2 in seen_movie_rating:
                if cur_user_ratings[j] > 0: # here if modify > to >= will have effect of default voting strategy
                    rate1 = cur_user_ratings[j] or user_pop_rating[cur_user_id]
                    # If iuf is True, then multiply true iuf value
                    if iuf_flag:
                        v1.append(rate1 * iuf_rating[j] - average_iuf_v1)
                        v2.append(rate2 * iuf_rating[j] - average_v2)
                    else:
                        v1.append(rate1 - average_v1)
                        v2.append(rate2 - average_v2)
            if len(v1) > 0:
                if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:
                    cosine_sim = 0       # need to think about it
                else:
                    cosine_sim = 1 - spatial.distance.cosine(v1, v2)
                if rou is not None:
                    cosine_sim = cosine_sim * pow(abs(cosine_sim), rou - 1)
                heappush(k_nearest_users, (abs(cosine_sim), cosine_sim, cur_user_id, average_v1))
                
            if len(k_nearest_users) > k:
                heappop(k_nearest_users)

        return k_nearest_users

    def pearsonCorrelationCF(self, test_input, test_user_seen, test_user_not_seen):
        """
        This is main entrance for user-based pearson correlation algorithm
        """
        f = open('pearson_out_' + test_input, 'w')
        user_movie = self.user_movie

        for test_user_id, movie_list in test_user_not_seen.items():
            seen_movie_rating = test_user_seen[test_user_id]
            test_user_average_rate = sum(x[1] for x in seen_movie_rating) * 1.0 / len(seen_movie_rating)
            test_user_average_iuf_rate = sum(x[1] * self.iuf_rating[x[0]] for x in seen_movie_rating) * 1.0 / sum(self.iuf_rating[x[0]] for x in seen_movie_rating)
            for not_seen_movie_id in sorted(movie_list):
                k_nearest_users = self.pearsonSimMethod(self.k, user_movie, seen_movie_rating, not_seen_movie_id, test_user_average_iuf_rate)
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
        """
        This is a helper function for calculating adjusted cosine similarity
        """
        k_nearest_movies = []
        movie_movie = self.movie_movie

        for j, rate in seen_movie_rating:
            cosine_sim = movie_movie[j][not_seen_movie_id]
            heappush(k_nearest_movies, (cosine_sim, rate))

            if len(k_nearest_movies) > k:
                heappop(k_nearest_movies)

        return k_nearest_movies

    def itemBasedCF(self, test_input, test_user_seen, test_user_not_seen):
        """
        This is main entrance for item-based CF algorithm
        """
        f = open('item_based_out_' + test_input, 'w')
        self.calItemToItemAdjSim()
        user_movie = self.user_movie

        for test_user_id, movie_list in test_user_not_seen.items():
            seen_movie_rating = test_user_seen[test_user_id]
            test_user_average_rate = sum(x[1] for x in seen_movie_rating) * 1.0 / len(seen_movie_rating)
            for not_seen_movie_id in sorted(movie_list):
                k_nearest_movies = self.itemBasedAdjustedCosSim(self.k, user_movie, seen_movie_rating, not_seen_movie_id)
                score = test_user_average_rate
                sum_abs_weight, sum_diff_rate = 0, 0
                
                for w, rate in k_nearest_movies:
                    sum_abs_weight += abs(w)
                    sum_diff_rate += w * (rate - test_user_average_rate)
                if sum_abs_weight != 0:
                    score += sum_diff_rate / sum_abs_weight
                    
                score = min(5, max(int(round(score)), 1))
                f.writelines(str(test_user_id) + ' ' + str(not_seen_movie_id) + ' ' + str(score) + '\n')

        f.close()

    def slopeOneCF(self, test_input, test_user_seen, test_user_not_seen):
        """
        This is main entrance for weighted slope one algorithm
        """
        f = open('slope_one_out_' + test_input, 'w')
        user_movie = self.user_movie
        movie_dev = self.movie_dev

        for test_user_id, movie_list in test_user_not_seen.items():
            seen_movie_rating = test_user_seen[test_user_id]
            cur_user_pop_rate = collections.Counter([x[1] for x in seen_movie_rating]).most_common(1)[0][0]
            for not_seen_movie_id in sorted(movie_list):
                cur_score, cur_count = 0, 0
                for seen_movie_id, seen_rate in seen_movie_rating:
                    if seen_movie_id in movie_dev[not_seen_movie_id]:
                        d, c = movie_dev[not_seen_movie_id][seen_movie_id]
                        cur_score += (d + seen_rate) * c
                        cur_count += c
                score = cur_score * 1.0 / cur_count if cur_count else cur_user_pop_rate
                score = max(1, min(5, int(round(score))))
                
                f.writelines(str(test_user_id) + ' ' + str(not_seen_movie_id) + ' ' + str(score) + '\n')
        f.close()
                
    def ensemble(self, test_input, test_user_seen, test_user_not_seen, weight):
        """
        This is main entrance for ensemble method
        Following listed three candidates which could be combined
        user-based cosine, user-based pearson and weighted slope one
        """
        f = open('ensemble_slope_cosine_out_' + test_input, 'w')
        user_movie, movie_dev = self.user_movie, self.movie_dev
        
        for test_user_id, movie_list in test_user_not_seen.items():
            seen_movie_rating = test_user_seen[test_user_id]
            test_user_pop_rate = collections.Counter([x[1] for x in seen_movie_rating]).most_common(1)[0][0]
            test_user_average_rate = sum(x[1] for x in seen_movie_rating) * 1.0 / len(seen_movie_rating)
            test_user_average_iuf_rate = sum(x[1] * self.iuf_rating[x[0]] for x in seen_movie_rating) * 1.0 / sum(self.iuf_rating[x[0]] for x in seen_movie_rating)
            for not_seen_movie_id in sorted(movie_list):
                k_nearest_users_basic = self.cosineSimMethod(self.k, user_movie, seen_movie_rating, not_seen_movie_id, True)
                # k_nearest_users_pearson = self.pearsonSimMethod(self.k, user_movie, seen_movie_rating, not_seen_movie_id, test_user_average_iuf_rate, True)
                ##### This is user-based cosine similarity prediction
                score_basic = test_user_pop_rate
                if k_nearest_users_basic:
                    score_basic = sum(x[0] * user_movie[x[1]][not_seen_movie_id] for x in k_nearest_users_basic) / sum(x[0] for x in k_nearest_users_basic)
                # #### This is user-based pearson correlation prediction    
                # score_pearson = test_user_average_rate
                # sum_abs_weight, sum_diff_rate = 0, 0

                # for abs_w, w, u_id, u_ave_r in k_nearest_users_pearson:
                #     sum_abs_weight += abs_w
                #     sum_diff_rate += w * (user_movie[u_id][not_seen_movie_id] - u_ave_r)
                # if sum_abs_weight != 0:
                #     score_pearson += sum_diff_rate / sum_abs_weight

                #### This is weighted slope one prediction
                slope_score, slope_count = 0, 0
                for seen_movie_id, seen_rate in seen_movie_rating:
                    if seen_movie_id in movie_dev[not_seen_movie_id]:
                        d, c = movie_dev[not_seen_movie_id][seen_movie_id]
                        slope_score += (d + seen_rate) * c
                        slope_count += c
                slope_score = slope_score * 1.0 / slope_count if slope_count else test_user_pop_rate

                score = min(5, max(int(round(weight * slope_score + (1 - weight) * score_basic)), 1))
                f.writelines(str(test_user_id) + ' ' + str(not_seen_movie_id) + ' ' + str(score) + '\n')

        f.close()

if __name__ == "__main__":
    start_time = time.time()
    mr = MovieRecommend(200)
    mr.preprocessTrainingData()
    mr.recommendEval('test10.txt')
    # mr.crossValidation(5)
    print "Time used is: " + str(time.time() - start_time)
