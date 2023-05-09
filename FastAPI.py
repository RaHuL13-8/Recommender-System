import logging
import joblib
import sys
import requests
import pandas as pd
import pickle
from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from datetime import datetime
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors

# Initialize FastAPI app
app = FastAPI()

df_dict=pickle.load(open('df.pkl','rb'))
df=pd.DataFrame(df_dict)
df2_dict=pickle.load(open('df2.pkl','rb'))
df2=pd.DataFrame(df2_dict)
user_info_dict=pickle.load(open('user_info.pkl','rb'))
user_info=pd.DataFrame(user_info_dict)
poster_dict=pickle.load(open('poster.pkl','rb'))
poster=pd.DataFrame(poster_dict)
cbd = pickle.load(open('cbd.pkl','rb'))
cbd=pd.DataFrame(cbd)
similarity= pickle.load(open('simi.pkl','rb'))


# To check if the server is up
@app.get('/status')
def health_check():
    return "Success!"

def load_model_files():
    """
    Loads the model and the label encoding dictionary
    """
    cbd = pickle.load(open('cbd.pkl','rb'))
    simi= joblib.load('simi.pkl','rb')
    return cbd,simi

def fetch_tmdb_id(movieId):

    return float(str(poster[poster['movieId']==movieId].tmdbId).split(" ")[4].split("\n")[0])

def recommend_cf(movie):
    
    
    lis=[]
    
    movie_index=cbd[cbd['title'] == movie].index[0]
#     key_list=list(movie_index_dict['movieId'].keys())
#     movie_index=key_list[0]
    
    
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:17]
    
    recommended_list=[]
    recommended_movieIds=[]
#     recommended_list.append(movie_index)
    
    for i in movies_list:
        recommended_list.append(cbd.iloc[i[0]].title)
        recommended_movieIds.append(str(cbd.iloc[i[0]].movieId))
    return recommended_list,recommended_movieIds


df1 = df.copy()

def recommend_movies(user, num_recommended_movies):

#     print('The list of the Movies {} Has Watched \n'.format(user))

    for m in df[df[user] > 0][user].index.tolist():
#         print(m)
        recommended_movies = []

    for m in df[df[user] == 0].index.tolist():

        index_df = df.index.tolist().index(m)
        predicted_rating = df1.iloc[index_df, df1.columns.tolist().index(user)]
        recommended_movies.append((m, predicted_rating))

        sorted_rm = sorted(recommended_movies, key=lambda x:x[1], reverse=True)

    print('The list of the Recommended Movies \n')
#     rank = 1
    recommended_movie_list=[]
    recommended_movie_ids=[]
    for recommended_movie in sorted_rm[:num_recommended_movies]:
        recommended_movie_list.append(recommended_movie[0])
        recommended_movie_ids.append((str(cbd[cbd['title']==recommended_movie[0]].movieId).split(" ")[4]).split("\n")[0])
#         print('{}: {} - predicted rating:{}'.format(rank, recommended_movie[0], recommended_movie[1]))
#         rank = rank + 1
    return recommended_movie_list,recommended_movie_ids

def movie_recommender(user, num_neighbors, num_recommendation):
    rml=[]
    number_neighbors = num_neighbors
    knn = NearestNeighbors(metric='cosine', algorithm='brute')
    knn.fit(df2.values)
    distances, indices = knn.kneighbors(df2.values, n_neighbors=number_neighbors)

    user_index = df.columns.tolist().index(user)

    for m,t in list(enumerate(df.index)):
        if df.iloc[m, user_index] == 0:
            sim_movies = indices[m].tolist()
            movie_distances = distances[m].tolist()

            if m in sim_movies:
                id_movie = sim_movies.index(m)
                sim_movies.remove(m)                                                                
                movie_distances.pop(id_movie) 

            else:
                sim_movies = sim_movies[:num_neighbors-1]
                movie_distances = movie_distances[:num_neighbors-1]

            movie_similarity = [1-x for x in movie_distances]
            movie_similarity_copy = movie_similarity.copy()
            nominator = 0

            for s in range(0, len(movie_similarity)):
                if df.iloc[sim_movies[s], user_index] == 0:
                    if len(movie_similarity_copy) == (number_neighbors - 1):
                        movie_similarity_copy.pop(s)

                    else:
                        movie_similarity_copy.pop(s-(len(movie_similarity)-len(movie_similarity_copy)))

                else:
                    nominator = nominator + movie_similarity[s]*df.iloc[sim_movies[s],user_index]

            if len(movie_similarity_copy) > 0:
                if sum(movie_similarity_copy) > 0:
                    predicted_r = nominator/sum(movie_similarity_copy)

                else:
                    predicted_r = 0

            else:
                predicted_r = 0

            df1.iloc[m,user_index] = predicted_r
    rml,rmi=recommend_movies(user,num_recommendation)
    return rml,rmi

@app.get('/api/rec_movies_to_new_user/{movie}')
def predict(movie: str):
    response_data={}
    response_data2={}
    
    tick = datetime.now()
    logging.info('Preprocessing request data...')
    
    
    tock = datetime.now()
    diff = str(int((tock - tick).total_seconds() * 1000))
    logging.info('Preprocessed request data in ' + diff + ' ms!')
    pred=[]

    tick = datetime.now()
    logging.info('Predicting credit worthiness...')
    pred,movie_id_list = recommend_cf(movie)
    response_data['Recommended_Movies'] = pred
    response_data2['MovieId_List']=movie_id_list
    tock = datetime.now()
    diff = str(int((tock - tick).total_seconds() * 1000))
    logging.info('Predicted credit worthiness in ' + diff + ' ms!')
        
    
    return response_data,response_data2

@app.get('/api/rec_movies_to_registered_user/{user_id}')
def predict(user_id: int):
    response_data={}
    response_data2={}
    
    tick = datetime.now()
    logging.info('Preprocessing request data...')
    
    tock = datetime.now()
    diff = str(int((tock - tick).total_seconds() * 1000))
    logging.info('Preprocessed request data in ' + diff + ' ms!')
    pred=[]
    
    tick = datetime.now()
    logging.info('Predicting credit worthiness...')
    pred , rmi= movie_recommender(user_id,15,15)
    response_data['Recommended_Movies'] = pred
    response_data2['MovieId_List'] = rmi
    tock = datetime.now()
    diff = str(int((tock - tick).total_seconds() * 1000))
    logging.info('Predicted credit worthiness in ' + diff + ' ms!')
    
    return response_data,response_data2
        
@app.get('/api/poster/{movie_id}')
def fetch_poster(movie_id: int):
    
    tmdb_id=fetch_tmdb_id(movie_id)
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=34aee5900d537f23e55aab8aeba48d73&language=en-US'.format(tmdb_id))
    data=response.json()
    return data['poster_path']
    
    
    