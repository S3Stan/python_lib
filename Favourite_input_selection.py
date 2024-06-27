# collect most from list

from collections import Counter
       # Reading input from STDIN
song_count = int(input().strip())
singers = list(map(int, input().strip().split()))
singer_count = Counter(singers)

max_count = max(singer_count.values())

print(max_count) # Writing output to STDOUT
