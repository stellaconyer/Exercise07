# from sys import argv

# filename = argv[1]

# call in the file
# enter the data into a dictionary
# pull out the data and sort it alphabetically
# print out names and ratings

ratings = open("scores.txt")
ratings_info = ratings.readlines()
ratings.close()

ratings_dict={}

for line in ratings_info:
    line = line.strip("\n")
    ratings_info = line.split(":")
    ratings_dict [ratings_info[0]] = ratings_info[1]

keys = ratings_dict.keys()
for key in sorted(keys):
    print "Restaurant %s is rated at %s." % (key, ratings_dict[key])