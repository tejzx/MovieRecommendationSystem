import streamlit as st
import pandas as pd
import requests
import pickle

# MUST be the first Streamlit command
st.set_page_config(page_title="Movie Recommender", layout="wide")

# Load data
@st.cache_resource
def load_data():
    with open('movie_data.pkl', 'rb') as file:
        movies, cosine_sim = pickle.load(file)
    return movies, cosine_sim

movies, cosine_sim = load_data()

# Recommendation function
def get_recommendations(title):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    return movies.iloc[[i[0] for i in sim_scores[1:11]]]

# Fetch poster with error handling
def fetch_poster(movie_id):
    try:
        response = requests.get(
            f"https://api.themoviedb.org/3/movie/{movie_id}",
            params={"api_key": "7b995d3c6fd91a2284b4ad8cb390c7b8"}
        )
        return f"https://image.tmdb.org/t/p/w500{response.json()['poster_path']}"
    except:
        return "https://via.placeholder.com/300x450?text=Poster+Not+Available"

# Set background image and styles
def set_bg_hack():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("https://image.tmdb.org/t/p/original/9yBVqNruk6Ykrwc32qrK2TIE5xw.jpg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }}
        .main {{
            background-color: rgba(0, 0, 0, 0.8);
            padding: 3rem;
            border-radius: 15px;
            margin-top: 2rem;
        }}
        /* Dark theme for selectbox */
        .stSelectbox > div > div {{
            background-color: rgba(30, 30, 30, 0.9) !important;
            color: white !important;
            border: 1px solid #444 !important;
        }}
        .stSelectbox svg {{
            color: white !important;
        }}
        /* Button styling */
        .stButton > button {{
            background-color: #f5c518 !important;
            color: #000 !important;
            font-weight: bold;
            border: none;
            height: 48px;  /* Match selectbox height */
            margin-top: 2px;  /* Align with selectbox */
        }}
        .stButton > button:hover {{
            background-color: #ffd700 !important;
        }}
        /* Search row alignment */
        .search-row {{
            display: flex;
            gap: 1rem;
            align-items: flex-end;
        }}
        .search-select {{
            flex-grow: 1;
        }}
        .search-button {{
            width: auto;
        }}
        /* Other styles */
        .stImage {{
            border: 2px solid #f5c518;
            border-radius: 8px;
            transition: transform 0.3s;
            margin-bottom: 1rem;
        }}
        .stImage:hover {{
            transform: scale(1.05);
        }}
        h1, h2, h3, p, .stMarkdown {{
            color: white !important;
        }}
        .recommendation-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }}
        .movie-card {{
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        .movie-title {{
            text-align: center;
            margin-top: 0.5rem;
            font-weight: bold;
            color: white !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_hack()

# Main app
def main():
    st.title("🎬 Movie Recommendation System")
    st.markdown("Discover movies similar to your favorites!")

    # Search box with aligned dropdown and button
    st.markdown('<div class="search-row">', unsafe_allow_html=True)
    
    # Dropdown selectbox
    st.markdown('<div class="search-select">', unsafe_allow_html=True)
    selected_movie = st.selectbox(
        "Select a movie:", 
        movies['title'].unique(),
        label_visibility="collapsed",
        placeholder="Choose a movie..."
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Recommendation button
    st.markdown('<div class="search-button">', unsafe_allow_html=True)
    recommend_clicked = st.button("Get Recommendations")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close search-row

    # Display recommendations
    if recommend_clicked or "recommendations" in st.session_state:
        with st.spinner('Finding similar movies...'):
            if recommend_clicked:
                recommendations = get_recommendations(selected_movie)
                st.session_state.recommendations = recommendations
            
            st.subheader(f"Movies similar to: {selected_movie}")
            
            # Create a grid layout
            st.markdown('<div class="recommendation-grid">', unsafe_allow_html=True)
            
            cols = st.columns(5)
            for i, (_, row) in enumerate(st.session_state.recommendations.iterrows()):
                with cols[i % 5]:
                    st.markdown('<div class="movie-card">', unsafe_allow_html=True)
                    st.image(
                        fetch_poster(row['movie_id']),
                        use_container_width=True
                    )
                    st.markdown(f'<p class="movie-title">{row["title"]}</p>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()