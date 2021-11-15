"""Restaurant rating lister."""
# Reads the ratings in from the file
scores = open("scores.txt")

# Stores them in a dictionary

ratings = {}
for score in scores:
    score = score.rstrip('\n').split(':')
    ratings[score[0]] = int(score[1])


# # print(ratings.items())
# # print(type(ratings))

## And finally, spits out the ratings in alphabetical order by restaurant

print(ratings)


for pos in sorted(ratings):
    print(pos, " is rated at ", ratings[pos])

## Prompt the user for a restaurant name

new_rating = input("Add a new restaurant name: ")

## Prompt the user for a restaurant score

new_score = int(input("Add a new restaurant score: "))

## Store the new restaurant/rating in the dictionary

ratings[new_rating] = new_score
## Print all of the ratings in alphabetical order (including the new one, of course)

for pos in sorted(ratings):
    print(pos, " is rated at ", ratings[pos])
    



