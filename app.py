import streamlit as st
import pandas as pd
import requests

import pickle


def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2ce1ecd99c298461e0f04744dc79f2f2&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # Fetching the index of the movie
    distance = similarity[movie_index]
    #     print(distance)
    # sort the distance,without changing the index postion
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    # enumerate will create indexes for the distances

    recommended_m=[]
    recommended_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].id
        # fetching poster from the api
        recommended_poster.append(fetch_poster(movie_id))

        recommended_m.append(movies.iloc[i[0]].title)
    return recommended_m,recommended_poster



movie_dict=pickle.load(open('Movies_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)

    ##movie_list=pickle.load(open('Movies.pkl','rb'))
    ##movie_list=movie_list['title'].values

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie=st.selectbox(
'Select the movie for which you need recommendation',
(movies['title'].values)
)
if st.button('Recommend'):
    names,posters=recommend(selected_movie)
    col1,col2,col3,col4,col5=st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
