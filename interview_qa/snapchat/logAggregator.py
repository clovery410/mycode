"""
Question:
node1.log:
...
2014-10-19 13:37:48.717 Snapchat[12345:1234567] Something something Foo.
2014-10-19 13:38:50.200 Snapchat[12345:1234567] Something something Bar.
2014-10-19 13:38:51.392 Snapchat[12345:1234567] Something something Baz.
...

node2.log:
...
2014-10-19 13:38:01.454 Snapchat[12345:7654321] Something something Foo2.
2014-10-19 13:38:02.600 Snapchat[12345:7654321] Something something Bar2.
2014-10-19 13:38:50.201 Snapchat[12345:7654321] Something something Baz2.
...

Output File (From aggregating the input files above):
...
node1.log 2014-10-19 13:37:48.717 Snapchat[12345:1234567] Something something Foo.
node2.log 2014-10-19 13:38:01.454 Snapchat[12345:7654321] Something something Foo2.
node2.log 2014-10-19 13:38:02.600 Snapchat[12345:7654321] Something something Bar2.
node1.log 2014-10-19 13:38:50.200 Snapchat[12345:1234567] Something something Bar.
node2.log 2014-10-19 13:38:50.201 Snapchat[12345:7654321] Something something Baz2.
node1.log 2014-10-19 13:38:51.392 Snapchat[12345:1234567] Something something Baz.
...
"""
from heapq import *
def logAggregator(file_names):
    files = []

    # append handler into list
    for file_name in file_names:
        files.append(open(file_name))

    heap = []
    for i, f in enumerate(files):
        heappush(heap, (f.readline(), i))

    merge_file = open("output", "w")
    while heap:
        line, file_idx = heappop(heap)
        merge_file.writeline(file_names[file_idx] + ' ' + line)

        next_line = files[file_idx].readline()
        if next_line != EOF:
            heappush(heap, (next_line, file_idx))

            
    for f in files:
        f.close()
    merge_file.close()
        
