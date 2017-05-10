#!/opt/python-3.4/linux/bin/python3
import numpy as np
import sys
import collections

class MovieRecommendation(object):
    def __init__(self):
        self.movies = collections.defaultdict(list)
        self.users = collections.defaultdict(list)
        self.movie_cnt = 0
        self.user_cnt = 0
        self.user_index = {}
        self.movie_index = {}
        self.user_lst = []
        self.movie_lst = []
        self.user_movie_matrix = None
        self.movie_movie_matrix = None
        self.user_user_matrix = None
        
    def checkInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def checkFloat(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def preprocessInput(self):
        movies, users = self.movies, self.users
        
        for line in sys.stdin:
            cur_line_s = line.partition('#')[0].strip()
            if cur_line_s == '':
                continue

            cur_array = cur_line_s.split(",")
            if len(cur_array) != 3:
                print ("Invalid Input: not correct parameter numbers")
                return
            
            u_id, m_id, rating = cur_array
            u_id = u_id.strip()
            m_id = m_id.strip()
            rating = rating.strip()
            if not self.checkInt(u_id) or int(u_id) < 0 or int(u_id) > sys.maxsize:
                print ('Invalid Input: user id {0} is not a valid integer'.format(u_id))
                return

            if not self.checkInt(m_id) or int(m_id) < 0 or int(m_id) > sys.maxsize:
                print ('Invalid Input: movie id {0} is not a valid integer'.format(m_id))
                return
                
            if not self.checkFloat(rating) or float(rating) < 0.0 or float(rating) > 5.0:
                print ('Invalid Input: rating score {0} is not a valid float number'.format(rating))
                return

            movies[int(m_id)].append([int(u_id), float(rating)])
            users[int(u_id)].append([int(m_id), float(rating)])
            
        self.movie_cnt = len(movies)
        self.user_cnt = len(users)
        self.buildReverseIndex()
        self.user_movie_matrix, self.movie_movie_matrix, self.user_user_matrix = self.constructMatrix()
        self.coOccurrence()
        self.userBased()

    def buildReverseIndex(self):
        users, movies = self.users, self.movies
        user_index, movie_index = self.user_index, self.movie_index
        user_lst, movie_lst = self.user_lst, self.movie_lst

        # build reverse index for user list
        for key in sorted(users.keys()):
            user_index[key] = len(user_lst)
            user_lst.append(key)

        # build reverse index for movie list
        for key in sorted(movies.keys()):
            movie_index[key] = len(movie_lst)
            movie_lst.append(key)
            
    def constructMatrix(self):
        # construct user-movie matrix, which is used to store users' rating information
        user_movie_matrix = np.zeros((self.user_cnt, self.movie_cnt))
        for u_idx, u_id in enumerate(self.user_lst):
            for m_id, rating in self.users[u_id]:
                user_movie_matrix[u_idx][self.movie_index[m_id]] = rating

        # construct movie-movie matrix, which is used for co-occurrence algorithm
        movie_movie_matrix = np.zeros((self.movie_cnt, self.movie_cnt))
        for u_id, pair in self.users.items():
            for i in range(len(pair)):
                idx1 = self.movie_index[pair[i][0]]
                movie_movie_matrix[idx1][idx1] += 1
                for j in range(i+1, len(pair)):
                    idx2 = self.movie_index[pair[j][0]]
                    movie_movie_matrix[idx1][idx2] += 1
                    movie_movie_matrix[idx2][idx1] += 1

        # construct user-user matrix, which is used to store similarity between each two users
        user_user_matrix = np.ones((self.user_cnt, self.user_cnt))
        for i in range(self.user_cnt):
            for j in range(i+1, self.user_cnt):
                v1, v2 = user_movie_matrix[i], user_movie_matrix[j]
                s = v1.dot(v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
                user_user_matrix[i][j] = user_user_matrix[j][i] = s
                
        return (user_movie_matrix, movie_movie_matrix, user_user_matrix)
                
    def coOccurrence(self):
        movies, users = self.movies, self.users
        movie_movie_matrix, user_movie_matrix = self.movie_movie_matrix, self.user_movie_matrix

        print ("Co-occurence recommendation algorithm result:")
        for u_idx, u_id in enumerate(self.user_lst):
            if len(users[u_id]) == self.movie_cnt:
                print ('user {0}: This user has seen all the movies, nothing to recommend'.format(u_id))
                continue
            
            cur_usr_recommend = [0] * self.movie_cnt
            max_rating, candidate_movie = -1.0, []
            for m_idx, m_id in enumerate(self.movie_lst):
                cur_usr_recommend[m_idx] = movie_movie_matrix[m_idx].dot(user_movie_matrix[u_idx])
                if user_movie_matrix[u_idx][m_idx] == 0:
                    if cur_usr_recommend[m_idx] > max_rating:
                        max_rating = cur_usr_recommend[m_idx]
                        candidate_movie = [m_id]
                    elif cur_usr_recommend[m_idx] == max_rating:
                        candidate_movie.append(m_id)
                        
            print ('user {0}: {1} => recommend movie {2}'.format(u_id, cur_usr_recommend, candidate_movie))
            
    def userBased(self):
        movies, users = self.movies, self.users
        user_user_matrix, user_movie_matrix = self.user_user_matrix, self.user_movie_matrix

        print ("\nUser-based recommendation algorithm result:")
        for u_idx, u_id in enumerate(self.user_lst):
            if len(users[u_id]) == self.movie_cnt:
                print ('user {0}: This user has seen all the movies, nothing to recommend'.format(u_id))
                continue
            
            max_rating, candidate_movie = -1.0, []
            for m_idx, m_id in enumerate(self.movie_lst):
                if user_movie_matrix[u_idx][m_idx] != 0.0:
                    continue

                running_weight = 0.0  # initialize running weight
                for other_user, rating in movies[m_id]:
                    other_user_idx = self.user_index[other_user]
                    running_weight += user_user_matrix[u_idx][other_user_idx] * user_movie_matrix[other_user_idx][m_idx]
                running_weight /= len(movies[m_id])  # this is average running weight
                
                if running_weight > max_rating:
                    max_rating = running_weight
                    candidate_movie = [m_id]
                elif running_weight == max_rating:
                    candidate_movie.append(m_id)
                        
            print ('user {0}: => recommend movie {1}'.format(u_id, candidate_movie))
        
if __name__ == "__main__":
    mr = MovieRecommendation()
    mr.preprocessInput()
    
