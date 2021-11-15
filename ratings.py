"""Restaurant rating lister."""
# Reads the ratings in from the file
scores = open("scores.txt")
# Stores them in a dictionary

ratings = {}
for score in scores:
    score = score.rstrip('\n').split(':')

    keys = score[0]
    values = int(score[1])
    ratings[f'{keys}']=f'{values}'
    # print(keys, " is rated at ", values)

# print(ratings.items())
# print(type(ratings))

# And finally, spits out the ratings in alphabetical order by restaurant

# print(ratings)
asc_ratings = {}

for pos in sorted(ratings):
    asc_ratings[pos] = ratings[pos]

for pos in asc_ratings:
    print(pos, " is rated at ", asc_ratings[pos])
    
    




