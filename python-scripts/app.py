import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load movie data from CSV
movies_df = pd.read_csv('../python-scripts/movies.csv')

@app.route('/api/recommend', methods=['POST'])
def recommend_movies():
    movie_title = request.json.get('movieTitle')
    if movie_title:
        # Implement recommendation logic based on movies_df
        recommendations = list(movies_df['title'].sample(5))  # Example: Random recommendation
        return jsonify(recommendations)
    else:
        return 'Error: Movie title not provided.'

if __name__ == '__main__':
    app.run(debug=True)
