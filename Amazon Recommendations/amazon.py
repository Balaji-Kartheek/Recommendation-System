import pickle
import numpy as np
import streamlit as st
import pandas as pd




def recommend(productid,df,pt,similarity_scores):
    # index fetch

    index = np.where(pt.index == productid)[0][0]
    similar_products = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

    data = []
    for i in similar_products:
        r_products= []
        temp_df = df[df['productid'] == pt.index[i[0]]]
        # products.extend(list(temp_df.drop_duplicates('productid')['productid'].values))
        r_products.extend(list(temp_df.drop_duplicates('productid')['product_title'].values))

        data.append(r_products)
    return data

# Load the files.

#           Arts Categry
arts_products_dict = pickle.load(open('arts_products_dict.pkl','rb'))
arts_pivot_table = pickle.load(open('arts_pivot_table.pkl','rb'))
arts_similarity_scores = pickle.load(open('arts_similarity_scores.pkl','rb'))
arts_prodcuts = pd.DataFrame(arts_products_dict)
arts_pt = pd.DataFrame(arts_pivot_table)



#           Office Products Categry
off_prod_products_dict = pickle.load(open('off_prod_products_dict.pkl','rb'))
off_prod_pivot_table = pickle.load(open('off_prod_pivot_table.pkl','rb'))
off_prod_similarity_scores = pickle.load(open('off_prod_similarity_scores.pkl','rb'))
off_prod_prodcuts = pd.DataFrame(off_prod_products_dict)
off_prod_pt = pd.DataFrame(off_prod_pivot_table)

#           Phone Accessories Categry
phn_acc_products_dict = pickle.load(open('phn_acc_products_dict.pkl','rb'))
phn_acc_pivot_table = pickle.load(open('phn_acc_pivot_table.pkl','rb'))
phn_acc_similarity_scores = pickle.load(open('phn_acc_similarity_scores.pkl','rb'))
phn_acc_prodcuts = pd.DataFrame(phn_acc_products_dict)
phn_acc_pt = pd.DataFrame(phn_acc_pivot_table)

#           Video Games Categry
video_games_products_dict = pickle.load(open('video_games_products_dict.pkl','rb'))
video_games_pivot_table = pickle.load(open('video_games_pt.pkl','rb'))
video_games_similarity_scores = pickle.load(open('video_games_similarity_scores.pkl','rb'))
video_games_prodcuts = pd.DataFrame(video_games_products_dict)
video_games_pt = pd.DataFrame(video_games_pivot_table)

st.header('Amazon Recommender System')

category = st.radio(
     "select the following category: ",
     ('Arts', 'Electronics','Office Products', 'Phone Accessories','Video Games'))

if category == 'Arts':
    pt = arts_pt
    df = arts_prodcuts
    similarity_scores = arts_similarity_scores
    st.subheader('You have selected Arts Category.')

elif category == 'Office Products':
    pt = off_prod_pt
    df = off_prod_prodcuts
    similarity_scores = off_prod_similarity_scores
    st.subheader("You have selected Office Products Category.")
elif category == 'Phone Accessories':
    pt = phn_acc_pt
    df = phn_acc_prodcuts
    similarity_scores = phn_acc_similarity_scores
    st.subheader("You have selected Phone Accessories Category.")
elif category == 'Video Games':
    pt = video_games_pt
    df = video_games_prodcuts
    similarity_scores = video_games_similarity_scores
    st.subheader("You have selected Video Games Category.")
else:
    st.subheader("You have selected Out of stock Category.")

selected_product_name = st.selectbox(
    'Select the product that you want to recommend->',
    df['product_title'].values
)
select_df = df[df['product_title'] == selected_product_name]
selected_productid = select_df['productid'][1]

st.write(selected_productid)

if st.button('Recommend'):
    recommended_products = recommend(selected_productid,df,pt,similarity_scores)
    product_list = []
    for i in recommended_products:
        product_list.extend(i)

    for i in product_list:
        st.write(i)




