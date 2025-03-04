
import pandas as pd
#import statistics
from matplotlib import pyplot as plt

df = pd.read_csv("billboard.csv")
print(df)

# i deleted the unnessisary data from my dataset like the current total number of spotify streams
# as it would not benefit my hypothesis 
# List of genres to track
genres_billboard = ["Pop", "Pop Rock", "R&B", "Soul", "Pop Soul", "Pop Rap", 
                   "Metal", "Rap", "Rock", "Swing"]

# start a list setting counts to 0
genre_count = {genre.lower().replace(" ", "_"): 0 for genre in genres_billboard}

# Count frequency of each genre in the dataset
for genre in df["Genre"].dropna():  # Drop NaN values to avoid errors
    genre_list = genre.lower().replace(" ", "_")  # Convert to dictionary list format
    if genre_list in genre_count:
        genre_count[genre_list] += 1  # Increase count instead of appending 1s

# Unpacking individual counts
pop = genre_count["pop"]
pop_rock = genre_count["pop_rock"]
rnb = genre_count["r&b"]
soul = genre_count["soul"]
pop_soul = genre_count["pop_soul"]
pop_rap = genre_count["pop_rap"]
metal = genre_count["metal"]
rap = genre_count["rap"]
rock = genre_count["rock"]
swing = genre_count["swing"]

# Print the final counts
print(f"Pop: {pop}")
print(f"Pop Rock: {pop_rock}")
print(f"R&B: {rnb}")
print(f"Soul: {soul}")
print(f"Pop Soul: {pop_soul}")
print(f"Pop Rap: {pop_rap}")
print(f"Metal: {metal}")
print(f"Rap: {rap}")
print(f"Rock: {rock}")
print(f"Swing: {swing}")

# attempt 2 

# print(dataIn)
# myList = dataIn.split(",")
# print(myList)
# Rock = 0
# Soul = 0
# Pop = 0
# PopRock = 0
# R&B = 0
# Metal = 0
# Rap = 0
# Swing = 0
# PopRap = 0
# genreList = []
# 
# for i in myList:
#     if i == "Rock":
#         rock += 1
#     if i == "Soul":
#         soul+=1
#     if i == "Pop":
#         pop+=1
#     if i == "Pop Rock":
#         poprock+=1
#     if i == "R&B":
#         r&b+=1
#      if i == "Metal":
#         metal+=1
#      if i == "Rap":
#         rap+=1
#      if i == "Swing":
#         swing+=1
#      if i == "Pop Rap":
#         poprap+=1
#         
# genreList.append(rock)
# genreList.append(soul)
# genreList.append(pop)
# genreList.append(poprock)
# genreList.append(r&b)
# genreList.append(metal)
# genreList.append(rap)
# genreList.append(swing)
# genreList.append(poprap)
# print(genreList)

# creates a bar chart 
xAxis = ["Rock","Soul","Pop","Pop Rock", "R&B", "Pop rap", "Rap", "Metal", "Swing",]  
plt.bar(xAxis,genreList, color="violet")
plt.title('Each Genres Popularity', color="violet")
plt.xlabel('Genres', color="violet")
plt.ylabel('Number Of Times It Appears', color="violet")
plt.show()

myList =(genreList)
median = statistics.median










