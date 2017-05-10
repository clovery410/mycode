import math

# trjs = [['a','b','c'],['b','c'],['a','e'],['a','e'],['a','b','e']]

# f_trjs = {
#      ('a','b','c','d','e') : 10,
#      ('a','b','c','e') : 7,
#      ('a','c') : 7,
#      ('a','b') : 7
# }

# uf_trjs = {
#     ('a','e') : 3,
#     ('a','c','e') : 4,
#     ('a','d','e') : 3,
#     ('b','c') : 1
# }

class reconstruct_trjs():
    def __init__(self):
        self.uf_trjs_2p = {}
        self.reconstructed_trjs = []

    def get_reconstruct_data(self, trjs, f_trjs, uf_trjs):
        '''
        --------------
        Input Format
        --------------
        trjs = [['a','b','c'],['b','c'],['a','e'],['a','e'],['a','b','e']]

        f_trjs = {
             ('a','b','c','d','e') : 10,
             ('a','b','c','e') : 7,
             ('a','c') : 7,
             ('a','b') : 7
        }

        uf_trjs = {
            ('a','e') : 3,
            ('a','c','e') : 4,
            ('a','d','e') : 3,
            ('b','c') : 1
        }

        ---------------
        Output example
        ---------------
        Case 1:
        [['a', 'b', 'c'], ['b', 'c'], ['a', 'b', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'e']]

        Case 2:
        [['a', 'b', 'c'], ['b', 'c'], ['a', 'b', 'e'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'e'], ['a', 'c', 'e']]

        '''
        trjs = [tuple(trj) for trj in trjs]
        for trj in trjs:
            # only care about 2p
            if len(trj) == 2 and trj not in f_trjs:

                # Case 1: only reconstruct to the frequent trajectories
                # -------------------------------------------
                # self._build_index(trj, f_trjs)
                # -------------------------------------------


                # Case 2: reconstruct to the trajectories which support is bigger
                # -------------------------------------------
                self._build_index_new(trj, f_trjs, uf_trjs)
                # -------------------------------------------

            else:
                self.reconstructed_trjs.append(trj)

        self._arrange_uf_trjs_2p()
        reconstructed_trjs = [list(trj) for trj in self.reconstructed_trjs]
        return reconstructed_trjs

    def _build_index_new(self, uf_trj_2p, f_trjs, uf_trjs):
        trjs_info_filtered = {}
        trjs_info = {}
        trjs_info.update(uf_trjs)
        trjs_info.update(f_trjs)
        for (trj, support) in trjs_info.items():
            if support > trjs_info[uf_trj_2p]:
                trjs_info_filtered[trj] = support
        self._build_index(uf_trj_2p, trjs_info_filtered)

    def _build_index(self, uf_trj_2p, f_trjs):
        has_no_possible_trj = True
        # this boolean can let uf_trj_2p only be count once every time we get it from uf_trj_2p input
        count_this_trj_already = False
        # this boolean can let all of the support of the possible_trjs only be added once for each uf_trj_2p
        support_has_been_added = False

        if uf_trj_2p in self.uf_trjs_2p:
            support_has_been_added = True

        for (f_trj, support) in f_trjs.items():
            if len(f_trj) >= 3 and f_trj[0] == uf_trj_2p[0] and f_trj[-1] == uf_trj_2p[-1]:
                if uf_trj_2p in self.uf_trjs_2p:
                    if not count_this_trj_already:
                        self.uf_trjs_2p[uf_trj_2p]['count'] += 1
                    if support_has_been_added is False:
                        self.uf_trjs_2p[uf_trj_2p]['support_sum'] += support
                        self.uf_trjs_2p[uf_trj_2p]['possible_trjs'].append((f_trj, support))
                else:
                    self.uf_trjs_2p[uf_trj_2p] = { 'count' : 1, 'support_sum' : support, 'possible_trjs' : [(f_trj, support)]}
                count_this_trj_already = True
                has_no_possible_trj = False

        support_has_been_added = True

        if has_no_possible_trj:
            self.reconstructed_trjs.append(uf_trj_2p)

    def _arrange_uf_trjs_2p(self):
        for uf_trj_2p in self.uf_trjs_2p.values():
            uf_trj_2p_count = uf_trj_2p['count']
            for (possible_trj, support) in uf_trj_2p['possible_trjs']:
                # print (possible_trj, uf_trj_2p_count*support/uf_trj_2p['support_sum'])
                for i in range(int(math.ceil(uf_trj_2p_count * support / uf_trj_2p['support_sum']))):
                    self.reconstructed_trjs.append(possible_trj)


if __name__ == "__main__":
    # if you want you use this example code: please unmark the trjs, f_trjs, uf_trjs data on the top of this file
    rt = reconstruct_trjs()
    print (trjs)
    reconstructed_trjs = rt.get_reconstruct_data(trjs, f_trjs, uf_trjs)
    print (reconstructed_trjs)