## 🎬 Movie Recommendation System  

### 📌 Overview  
This project is a **Movie Recommendation System** built using **Streamlit**, **pandas**, and **scikit-learn**. It suggests similar movies based on a given input, using a **cosine similarity** metric computed from movie metadata. The system also fetches movie posters from **The Movie Database (TMDB) API** to enhance the user experience.  

### 🚀 Features  
✅ Recommend **top 10 similar movies** based on user selection  
✅ **Movie poster display** fetched from TMDB API  
✅ **Interactive UI** with Streamlit  
✅ Uses **cosine similarity** for recommendations  

### 🛠️ Tech Stack  
- **Python**  
- **Streamlit** (for UI)  
- **pandas** (for data processing)  
- **scikit-learn** (for similarity calculations)  
- **TMDB API** (for movie posters)  

### 📂 Project Structure  
```
📦 Movie Recommendation System
│-- 📜 app.py                     # Streamlit app  
│-- 📜 Movie_Recommendation_System.ipynb  # Jupyter notebook for data processing  
│-- 📜 movie_data.pkl              # Preprocessed movie data and similarity matrix  
│-- 📜 README.md                   # Project documentation  
```

### ▶️ How to Run  
1️⃣ Clone the repository  
```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```
2️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```
3️⃣ Run the Streamlit app  
```bash
streamlit run app.py
```
4️⃣ Select a movie and get recommendations! 🎥  

### 🔑 API Key  
To fetch posters from **TMDB**, replace the API key in `app.py`:  
```python
api_key = 'your_tmdb_api_key'
```
Get your API key from [TMDB](https://www.themoviedb.org/) and update it in the code.  

### 📌 Future Enhancements  
✅ Add **genre-based filtering**  
✅ Implement **collaborative filtering**  
✅ Improve **UI/UX** with enhanced visuals  
