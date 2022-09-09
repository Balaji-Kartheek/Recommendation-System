import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:13]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)


    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Select a movie from the dropdown",
    movie_list
)



if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3  = st.columns(3)
    with col1:
        st.image(recommended_movie_posters[0])
        st.text(recommended_movie_names[0])
    with col2:
        st.image(recommended_movie_posters[1])
        st.text(recommended_movie_names[1])
    with col3:
        st.image(recommended_movie_posters[2])
        st.text(recommended_movie_names[2])
    with col1:
        st.image(recommended_movie_posters[3])
        st.text(recommended_movie_names[3])
    with col2:
        st.image(recommended_movie_posters[4])
        st.text(recommended_movie_names[4])
    with col3:
        st.image(recommended_movie_posters[5])
        st.text(recommended_movie_names[5])
    with col1:
        st.image(recommended_movie_posters[6])
        st.text(recommended_movie_names[6])
    with col2:
        st.image(recommended_movie_posters[7])
        st.text(recommended_movie_names[7])
    with col3:
        st.image(recommended_movie_posters[8])
        st.text(recommended_movie_names[8])
    with col1:
        st.image(recommended_movie_posters[9])
        st.text(recommended_movie_names[9])
    with col2:
        st.image(recommended_movie_posters[10])
        st.text(recommended_movie_names[10])
    with col3:
        st.image(recommended_movie_posters[11])
        st.text(recommended_movie_names[11])

