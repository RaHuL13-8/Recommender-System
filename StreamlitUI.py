import streamlit as st
import pickle
import pandas as pd
import requests
import time

movie_list=pickle.load(open('cbd.pkl','rb'))
cbd=pd.DataFrame(movie_list)

user_info_dict=pickle.load(open('user_info.pkl','rb'))
user_info=pd.DataFrame(user_info_dict)

popular_movies=pickle.load(open('l4.pkl','rb'))
pop_movie_id=pickle.load(open('l3.pkl','rb'))


st.title('Movie Recommender System')

with st.sidebar:
    page = st.selectbox(
        "Navigate",
        ("Home","Registered User", "New User")
    )

if page=="Home":
    st.header('Popular Movies:')
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.subheader(popular_movies[0])
        res3=requests.get('http://localhost:8080/api/poster/'+ str(pop_movie_id[0]))
        with st.spinner('Loading...'):
                time.sleep(1)
        poster_link=res3.json()
        final_link='https://image.tmdb.org/t/p/w500/'+poster_link
        st.image(final_link)

    with col2:
        st.subheader(popular_movies[1])
        res3=requests.get('http://localhost:8080/api/poster/'+ str(pop_movie_id[1]))
        with st.spinner('Loading...'):
                time.sleep(1)
        poster_link=res3.json()
        final_link='https://image.tmdb.org/t/p/w500/'+poster_link
        st.image(final_link)

    with col3:
        st.subheader(popular_movies[2])
        res3=requests.get('http://localhost:8080/api/poster/'+ str(pop_movie_id[2]))
        with st.spinner('Loading...'):
                time.sleep(1)
        poster_link=res3.json()
        final_link='https://image.tmdb.org/t/p/w500/'+poster_link
        st.image(final_link)
    with col4:
        st.subheader(popular_movies[3])
        res3=requests.get('http://localhost:8080/api/poster/'+ str(pop_movie_id[3]))
        with st.spinner('Loading...'):
                time.sleep(1)
        poster_link=res3.json()
        final_link='https://image.tmdb.org/t/p/w500/'+poster_link
        st.image(final_link)

    col5, col6, col7 ,col8 = st.columns(4)

    with col5:
        st.subheader(popular_movies[4])
        res3=requests.get('http://localhost:8080/api/poster/'+ str(pop_movie_id[4]))
        with st.spinner('Loading...'):
                time.sleep(1)
        poster_link=res3.json()
        final_link='https://image.tmdb.org/t/p/w500/'+poster_link
        st.image(final_link)

    with col6:
        st.subheader(popular_movies[5])
        res3=requests.get('http://localhost:8080/api/poster/'+ str(pop_movie_id[5]))
        with st.spinner('Loading...'):
                time.sleep(1)
        poster_link=res3.json()
        final_link='https://image.tmdb.org/t/p/w500/'+poster_link
        st.image(final_link)

    with col7:
        st.subheader(popular_movies[6])
        res3=requests.get('http://localhost:8080/api/poster/'+ str(pop_movie_id[6]))
        with st.spinner('Loading...'):
                time.sleep(1)
        poster_link=res3.json()
        final_link='https://image.tmdb.org/t/p/w500/'+poster_link
        st.image(final_link)
    with col8:
        st.subheader(popular_movies[7])
        res3=requests.get('http://localhost:8080/api/poster/'+ str(pop_movie_id[7]))
        with st.spinner('Loading...'):
                time.sleep(1)
        poster_link=res3.json()
        final_link='https://image.tmdb.org/t/p/w500/'+poster_link
        st.image(final_link)

    col9, col10, col11 ,col12 = st.columns(4)

    with col9:
        st.subheader(popular_movies[8])
        res3=requests.get('http://localhost:8080/api/poster/'+ str(pop_movie_id[8]))
        with st.spinner('Loading...'):
                time.sleep(1)
        poster_link=res3.json()
        final_link='https://image.tmdb.org/t/p/w500/'+poster_link
        st.image(final_link)

    with col10:
        st.subheader(popular_movies[9])
        res3=requests.get('http://localhost:8080/api/poster/'+ str(pop_movie_id[9]))
        with st.spinner('Loading...'):
                time.sleep(1)
        poster_link=res3.json()
        final_link='https://image.tmdb.org/t/p/w500/'+poster_link
        st.image(final_link)

    with col11:
        st.subheader(popular_movies[10])
        res3=requests.get('http://localhost:8080/api/poster/'+ str(pop_movie_id[10]))
        with st.spinner('Loading...'):
                time.sleep(1)
        poster_link=res3.json()
        final_link='https://image.tmdb.org/t/p/w500/'+poster_link
        st.image(final_link)

    with col12:
        st.subheader(popular_movies[11])
        res3=requests.get('http://localhost:8080/api/poster/'+ str(pop_movie_id[11]))
        with st.spinner('Loading...'):
                time.sleep(1)
        poster_link=res3.json()
        final_link='https://image.tmdb.org/t/p/w500/'+poster_link
        st.image(final_link)
    col13, col14, col15 ,col16 = st.columns(4)

    with col13:
        st.subheader(popular_movies[12])
        res3=requests.get('http://localhost:8080/api/poster/'+ str(pop_movie_id[12]))
        with st.spinner('Loading...'):
                time.sleep(1)
        poster_link=res3.json()
        final_link='https://image.tmdb.org/t/p/w500/'+poster_link
        st.image(final_link)

    with col14:
        st.subheader(popular_movies[13])
        res3=requests.get('http://localhost:8080/api/poster/'+ str(pop_movie_id[13]))
        with st.spinner('Loading...'):
                time.sleep(1)
        poster_link=res3.json()
        final_link='https://image.tmdb.org/t/p/w500/'+poster_link
        st.image(final_link)

    with col15:
        st.subheader(popular_movies[14])
        res3=requests.get('http://localhost:8080/api/poster/'+ str(pop_movie_id[14]))
        with st.spinner('Loading...'):
                time.sleep(1)
        poster_link=res3.json()
        final_link='https://image.tmdb.org/t/p/w500/'+poster_link
        st.image(final_link)
    
if page== "Registered_User":
    st.header('Item Based Recommender System')
    
    selected_user_id = st.selectbox(
     'Select your User Id',
     user_info['userId'].values)
    
    user_id_in=selected_user_id.tolist()
    
    res = requests.get('http://localhost:8080/api/rec_movies_to_registered_user/'+str(user_id_in))
    data=res.json()
    
    if st.button('Recommend_IB'):
        st.write('Recommendations:')
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.subheader(data[0]['Recommended_Movies'][0])
            res3=requests.get('http://localhost:8080/api/poster/'+data[1]['MovieId_List'][0])
            with st.spinner('Loading...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)

        with col2:
            st.subheader(data[0]['Recommended_Movies'][1])
            res3=requests.get('http://localhost:8080/api/poster/'+data[1]['MovieId_List'][1])
            with st.spinner('Loading...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)

        with col3:
            st.subheader(data[0]['Recommended_Movies'][2])
            res3=requests.get('http://localhost:8080/api/poster/'+data[1]['MovieId_List'][2])
            with st.spinner('Loading...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)
        with col4:
            st.subheader(data[0]['Recommended_Movies'][3])
            res3=requests.get('http://localhost:8080/api/poster/'+data[1]['MovieId_List'][3])
            with st.spinner('Loading...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)
            
        col5, col6, col7 ,col8 = st.columns(4)

        with col5:
            st.subheader(data[0]['Recommended_Movies'][4])
            res3=requests.get('http://localhost:8080/api/poster/'+data[1]['MovieId_List'][4])
            with st.spinner('Loading...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)

        with col6:
            st.subheader(data[0]['Recommended_Movies'][5])
            res3=requests.get('http://localhost:8080/api/poster/'+data[1]['MovieId_List'][5])
            with st.spinner('Loading...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)

        with col7:
            st.subheader(data[0]['Recommended_Movies'][6])
            res3=requests.get('http://localhost:8080/api/poster/'+data[1]['MovieId_List'][6])
            with st.spinner('Loading...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)
        with col8:
            st.subheader(data[0]['Recommended_Movies'][7])
            res3=requests.get('http://localhost:8080/api/poster/'+data[1]['MovieId_List'][7])
            with st.spinner('Loading...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)
            
        col9, col10, col11 ,col12 = st.columns(4)

        with col9:
            st.subheader(data[0]['Recommended_Movies'][8])
            res3=requests.get('http://localhost:8080/api/poster/'+data[1]['MovieId_List'][8])
            with st.spinner('Loading...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)

        with col10:
            st.subheader(data[0]['Recommended_Movies'][9])
            res3=requests.get('http://localhost:8080/api/poster/'+data[1]['MovieId_List'][9])
            with st.spinner('Loading...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)

        with col11:
            st.subheader(data[0]['Recommended_Movies'][10])
            res3=requests.get('http://localhost:8080/api/poster/'+data[1]['MovieId_List'][10])
            with st.spinner('Loading...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)
            
        with col12:
            st.subheader(data[0]['Recommended_Movies'][11])
            res3=requests.get('http://localhost:8080/api/poster/'+data[1]['MovieId_List'][11])
            with st.spinner('Loading...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)
        col13, col14, col15 ,col16 = st.columns(4)

        with col13:
            st.subheader(data[0]['Recommended_Movies'][12])
            res3=requests.get('http://localhost:8080/api/poster/'+data[1]['MovieId_List'][12])
            with st.spinner('Loading...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)

        with col14:
            st.subheader(data[0]['Recommended_Movies'][13])
            res3=requests.get('http://localhost:8080/api/poster/'+data[1]['MovieId_List'][13])
            with st.spinner('Loading...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)

        with col15:
            st.subheader(data[0]['Recommended_Movies'][14])
            res3=requests.get('http://localhost:8080/api/poster/'+data[1]['MovieId_List'][14])
            with st.spinner('Loading...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)
            
#         with col16:
#             st.subheader(data[0]['Recommended_Movies'][15])
#             res3=requests.get('http://localhost:8080/api/poster/'+data[1]['MovieId_List'][15])
#             with st.spinner('Loading...'):
#                 time.sleep(1)
#             poster_link=res3.json()
#             final_link='https://image.tmdb.org/t/p/w500/'+poster_link
#             st.image(final_link)   
        
if page == "New User":
    st.header('Content Based Recommender System')
    
    selected_movie_name = st.selectbox(
     'Select a movie',
     cbd['title'].values)
    
    selected_movie_name=selected_movie_name.replace(" ", "%20")
    selected_movie_name=selected_movie_name.replace("(", "%28")
    selected_movie_name=selected_movie_name.replace(")", "%29")
    
    res2=requests.get('http://localhost:8080/api/rec_movies_to_new_user/'+selected_movie_name)
    data2=res2.json()
    
    if st.button('Recommend_CB'):
        st.write('Recommendations:')
        
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.subheader(data2[0]['Recommended_Movies'][0])
            res3=requests.get('http://localhost:8080/api/poster/'+data2[1]['MovieId_List'][0])
            with st.spinner('Wait for it...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)

        with col2:
            st.subheader(data2[0]['Recommended_Movies'][1])
            res3=requests.get('http://localhost:8080/api/poster/'+data2[1]['MovieId_List'][1])
            with st.spinner('Wait for it...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)

        with col3:
            st.subheader(data2[0]['Recommended_Movies'][2])
            res3=requests.get('http://localhost:8080/api/poster/'+data2[1]['MovieId_List'][2])
            with st.spinner('Wait for it...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)
        with col4:
            st.subheader(data2[0]['Recommended_Movies'][3])
            res3=requests.get('http://localhost:8080/api/poster/'+data2[1]['MovieId_List'][3])
            with st.spinner('Wait for it...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)
            
        col5, col6, col7 ,col8 = st.columns(4)

        with col5:
            st.subheader(data2[0]['Recommended_Movies'][4])
            res3=requests.get('http://localhost:8080/api/poster/'+data2[1]['MovieId_List'][4])
            with st.spinner('Wait for it...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)

        with col6:
            st.subheader(data2[0]['Recommended_Movies'][5])
            res3=requests.get('http://localhost:8080/api/poster/'+data2[1]['MovieId_List'][5])
            with st.spinner('Wait for it...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)

        with col7:
            st.subheader(data2[0]['Recommended_Movies'][6])
            res3=requests.get('http://localhost:8080/api/poster/'+data2[1]['MovieId_List'][6])
            with st.spinner('Wait for it...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)
        with col8:
            st.subheader(data2[0]['Recommended_Movies'][7])
            res3=requests.get('http://localhost:8080/api/poster/'+data2[1]['MovieId_List'][7])
            with st.spinner('Wait for it...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)
            
        col9, col10, col11 ,col12 = st.columns(4)

        with col9:
            st.subheader(data2[0]['Recommended_Movies'][8])
            res3=requests.get('http://localhost:8080/api/poster/'+data2[1]['MovieId_List'][8])
            with st.spinner('Wait for it...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)

        with col10:
            st.subheader(data2[0]['Recommended_Movies'][9])
            res3=requests.get('http://localhost:8080/api/poster/'+data2[1]['MovieId_List'][9])
            with st.spinner('Wait for it...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)

        with col11:
            st.subheader(data2[0]['Recommended_Movies'][10])
            res3=requests.get('http://localhost:8080/api/poster/'+data2[1]['MovieId_List'][10])
            with st.spinner('Wait for it...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)
            
        with col12:
            st.subheader(data2[0]['Recommended_Movies'][11])
            res3=requests.get('http://localhost:8080/api/poster/'+data2[1]['MovieId_List'][11])
            with st.spinner('Wait for it...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)
        col13, col14, col15 ,col16 = st.columns(4)

        with col13:
            st.subheader(data2[0]['Recommended_Movies'][12])
            res3=requests.get('http://localhost:8080/api/poster/'+data2[1]['MovieId_List'][12])
            with st.spinner('Wait for it...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)

        with col14:
            st.subheader(data2[0]['Recommended_Movies'][13])
            res3=requests.get('http://localhost:8080/api/poster/'+data2[1]['MovieId_List'][13])
            with st.spinner('Wait for it...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)

        with col15:
            st.subheader(data2[0]['Recommended_Movies'][14])
            res3=requests.get('http://localhost:8080/api/poster/'+data2[1]['MovieId_List'][14])
            with st.spinner('Wait for it...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)
            
        with col16:
            st.subheader(data2[0]['Recommended_Movies'][15])
            res3=requests.get('http://localhost:8080/api/poster/'+data2[1]['MovieId_List'][15])
            with st.spinner('Wait for it...'):
                time.sleep(1)
            poster_link=res3.json()
            final_link='https://image.tmdb.org/t/p/w500/'+poster_link
            st.image(final_link)
            