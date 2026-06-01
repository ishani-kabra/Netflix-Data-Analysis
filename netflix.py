import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
netflix=pd.read_csv('project/netflix_titles.csv')
print(netflix)
print(netflix.isnull().sum())
netflix.fillna("NA",inplace=True)
print(netflix)

print("the total number of movies present are",netflix.shape[0])

# # MOVIE OR TV SHOW
watch=netflix.groupby('type')

print("the total movies on netflix  are",watch.get_group('Movie').shape[0])
print("the total tv shows on netflix are",watch.get_group('TV Show').shape[0])
x=input("enter movie to see movie and tv for tv shows")
if x.lower()=="movie":
    print("movies are", watch.get_group('Movie'))
else:
    print("tv show are ",watch.get_group('TV Show'))
# release year
release_year= netflix.groupby('release_year')
year=int(input("enter the year you want to search movie of "))
print("the movies of the year is ",release_year.get_group(year))
print(release_year.get_group(year).shape[0])
# year with highest release is 
no_of_movies=netflix['release_year'].value_counts().head(10)
print("highest release of movies is ",no_of_movies)

# according to ratings
print("according to rating movies are ",netflix['rating'].value_counts())
# genre of the movie 
print("genre of the movies are ",netflix['listed_in'].value_counts())


movie_year=netflix["release_year"].value_counts().head(10)
plt.bar( movie_year.index,movie_year.values,color="green")
plt.title("top releases")
plt.ylabel("movie and tv show")
plt.xlabel("year")
plt.show()


sns.countplot(x="type",data=netflix,color="red")
plt.title("types")
plt.show()

rating=netflix['rating'].value_counts().head(10)
sns.barplot(x=rating.values,y=rating.index,color="green")
plt.title("rating")
plt.ylabel("Ratings")
plt.xlabel("count")
plt.show()


plt.pie(rating.values,labels=rating.index,autopct= "%0.1f%%")
plt.show()

# top genres
genre=netflix['listed_in'].value_counts().head(10)
sns.barplot(x=genre.values,y=genre.index,color="pink")
plt.title("Top Netflix Genres")
plt.show()