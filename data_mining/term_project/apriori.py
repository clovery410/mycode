from __future__ import division, print_function
import numpy as np
import itertools
import collections
from DBSCAN import Dbscan
from reconstuct import reconstruct_trjs

class Apriori():
    def __init__(self, min_sup = 0.3, min_conf = 0.81):
        # The minimum fraction of trajectoriess a pattern needs to
        # occur in to be deemed frequent
        self.min_sup = min_sup
        # The minimum fraction of times the antecedent needs to imply
        # the concequent to justify rule
        self.min_conf = min_conf
        self.freq_patterns = None      # List of freqeuent patterns
        self.trajectories = None       # List of trajectories
        self.data_from_dbscan = False
        
    def _calculate_support(self, pattern):
        count = 0
        for trajectory in self.trajectories:
            if self._trajectory_contains_regions(trajectory, pattern):
                count += 1
            
        support = count / len(self.trajectories)

        return support

    # Prunes the candidates that are not frequent
    # => returns list with only frequent patterns
    # Candidates is a list
    def _get_frequent_patterns(self, candidates):
        frequent = []
        k = len(self.freq_patterns)
        subsets = list(itertools.permutations(candidates, k+1))

        for t in subsets:
            pattern = list(t)
            support = self._calculate_support(pattern)

            # record global frequent patterns - including non-consecutive trajectories
            if support >= self.min_sup:
                frequent.append([pattern, support])

        return frequent

    # Refined Candidate Generate Algorithm - monotonicity
    # To generate kth candidate, count the number of each individual item
    # select the item whose count >= k - 1 and prunes others
    def _generate_candidates(self, freq_pattern):
        candidates = []
        k = len(self.freq_patterns)
        region_count = collections.defaultdict(int)

        if self.data_from_dbscan:
            single_item = isinstance(freq_pattern[0][0], np.int64)
        else:
            single_item = isinstance(freq_pattern[0][0], int)

        for pattern in freq_pattern:
            if single_item:
                region_count[pattern[0]] += 1
            else:
                for region in pattern[0]:
                    region_count[region] += 1

        # choose region whose cnt >= k as candidates
        for region, cnt in region_count.items():
            if cnt >= k:
                candidates.append(region)

        return candidates

    # True or false depending on each region in the pattern is
    # in the trajectory in order
    def _trajectory_contains_regions(self, trajectory, regions):
        i = 0
        for region in regions:
            while i < len(trajectory) and region != trajectory[i]:
                i += 1
            if i >= len(trajectory):
                return False
            if region == trajectory[i]:
                i += 1
        return True

    # Returns 1. the set of frequent patterns in the list of trajectories
    #		  2. consecituve frequent trajectory
    #		  3. consecutive non-frequent trajectory
    def find_frequent_patterns(self, trajectories):
        self.trajectories = trajectories
        # Get all unique regions in the trajectories
        unique_regions = set(region for trajectory in self.trajectories for region in trajectory)
        # Get the frequent regions which forms 1-Pattern
        one_patterns = []
        for cur_region in unique_regions:
        	cur_support = self._calculate_support([cur_region])
        	if cur_support >= self.min_sup:
        		one_patterns.append([cur_region, cur_support])
        self.freq_patterns = [one_patterns]
        # self.freq_patterns = [list(unique_regions)]

        while(True):
            # Generate new candidates from last added frequent patterns
            candidates = self._generate_candidates(self.freq_patterns[-1])

            # Get the frequent patterns among those candidates
            frequent_patterns = self._get_frequent_patterns(candidates)

            # If there are no frequent patterns we're done
            if not frequent_patterns:
                break

            # Add them to the list of frequent patterns and start over
            self.freq_patterns.append(frequent_patterns)

        # Flatten the array and return every frequent regionset
        frequent_patterns = [
            pattern for patterns in self.freq_patterns for pattern in patterns]

        return frequent_patterns

    # Iterate through all trajectories, count and record every consecutive traj and its subsets
    # then split them into frequent and non-frequent and return
    # This function is used for reconstruct.py 
    def get_consecutive_trajectories(self, trajectories):
    	all_traj = collections.defaultdict(int)
    	consec_freq_traj = {}
    	consec_non_freq_traj = {}

    	for trajectory in trajectories:
    		for start_idx in range(len(trajectory)):
    			for end_idx in range(start_idx+1, len(trajectory)):
    				if start_idx < end_idx:
    					t = tuple(trajectory[start_idx:end_idx+1])
    					all_traj[t] += 1
    	
    	for t, cnt in all_traj.items():
    		if cnt >= self.min_sup * len(trajectories):
    			consec_freq_traj[t] = cnt
    		else:
    			consec_non_freq_traj[t] = cnt

    	return consec_freq_traj, consec_non_freq_traj

def main():
    # db = Dbscan()
    # db.run()
    # trajectories = db.DT
    # trajectories = np.array([[0, 5], [1], [1, 0], [1, 2, 0], [2, 3, 0, 1], [1, 3, 0]])
    trajectories = np.array([[0, 1, 3], [0, 1, 3], [0, 3], [0, 2], [0, 4], [0, 2, 4], [0, 2, 4, 5], [0, 1]])
    
    print ("- Apriori -")
    min_sup = 0.3  # This parameter should be tuned.
    min_conf = 0.8
    print ("Minimum - support: %.2f, confidence: %s" % (min_sup, min_conf))
    print ("Trajectories:")
    for trajectory in trajectories:
        print ("\t%s" % trajectory)

    apriori = Apriori(min_sup=min_sup, min_conf=min_conf)
    # apriori.data_from_dbscan = True  # uncomment it if trajectories from Dbscan

    # Get and print the frequent itemsets, the result we need to show
    frequent_patterns_before = apriori.find_frequent_patterns(trajectories)
    # Following function get all consecutive freq and non-freq traj, used for reconstruct.py
    consec_freq_traj, consec_non_freq_traj = apriori.get_consecutive_trajectories(trajectories)

    print ("\nOriginal Frequent Patterns:")
    for pattern_name, pattern_support in frequent_patterns_before:
    	print ("\tPattern: %s, Support: %s" % (pattern_name, pattern_support * len(trajectories)))
    # print ("Frequent Consecutive Trajectories:\n\t%s\nNon-frequent Consecutive Trajectories:\n\t%s\n" %
    #  (consec_freq_traj, consec_non_freq_traj))

    rt = reconstruct_trjs()
    # print (consec_freq_traj, consec_non_freq_traj)
    reconstructed_trajectories = rt.get_reconstruct_data(trajectories, consec_freq_traj, consec_non_freq_traj)
    frequent_patterns_after = apriori.find_frequent_patterns(reconstructed_trajectories)
    print("\n- After Reconstructed -")
    print ("New Trajectories:")
    for trajectory in reconstructed_trajectories:
        print ("\t%s" % trajectory)

    print ("\nNew Frequent Patterns:")
    for pattern_name, pattern_support in frequent_patterns_after:
    	print ("\tPattern: %s, Support: %s" % (pattern_name, pattern_support * len(reconstructed_trajectories)))
    
if __name__ == "__main__":
    main()

