class Paging(object):
    def __init__(self):
        self.num = 1000
        self.maxCounter = 0xffffffff
        self.tick = 10

    def shift_counter(self, counter, highest_bit):
        if highest_bit:
            return (counter >> 1) | 0x80000000
        else:
            return counter >> 1

    def reference(self, n, vp_num, counter, page_table, remain_frames, curr_tick_refer):
        """
        input n: number of page frames
        input vp_num: virtual page number
        input curr_tick_refer: current tick reference condition
        return Boolean, Boolean # is_caused_page_falut, is_caused_allocating_frame
        """
        curr_tick_refer[vp_num] = True
        if page_table[vp_num]:
            return (False, False)

        # page fault
        else:
            if remain_frames > 0:
                page_table[vp_num] = True
                return (True, True)

            #else, need to replece
            else:
                nfu_vp_num = self.num
                nfu_counter = self.maxCounter
                for i in xrange(self.num):
                    if page_table[i]:
                        if counter[i] < nfu_counter:
                            nfu_counter = counter[i]
                            nfu_vp_num = i
                page_table[nfu_vp_num] = False
                page_table[vp_num] = True
                return (True, False)

    def simulation(self, n, tick, references):
        counter = [0 for x in xrange(self.num)]
        page_table = [False for x in xrange(self.num)]
        remain_frames = n
        page_fault = 0
        curr_refer = 0
        curr_tick_refer = [False for x in xrange(self.num)]

        while curr_refer < len(references):
            is_page_fault, is_allocated_more = self.reference(n, references[curr_refer] - 1, counter, page_table, remain_frames, curr_tick_refer)
            if is_page_fault:
                page_fault += 1
            if is_allocated_more:
                remain_frames -= 1
            if curr_refer % tick == 0:
                for i in xrange(self.num):
                    counter[i] = self.shift_counter(counter[i], curr_tick_refer[i])
                curr_tick_refer = [False for x in xrange(self.num)]
            curr_refer += 1
        return page_fault

    def printRes(self):
        f = open('test.txt', 'r')
        references = [int(x) for x in f.readlines()]
        i = 100
        while i <= 1000:
            page_fault = self.simulation(i, self.tick, references)
            print i, page_fault, page_fault / (float(len(references)) / 1000)
            i += 100

if __name__ == '__main__':
    p = Paging()
    p.printRes()








