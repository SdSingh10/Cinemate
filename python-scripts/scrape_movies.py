import requests
from bs4 import BeautifulSoup
import csv

def scrape_movies():
    url = 'https://www.imdb.com/chart/top'  # Example URL
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    movies = []
    movie_titles = soup.select('.titleColumn a')
    movie_years = soup.select('.titleColumn span')
    movie_ratings = soup.select('.imdbRating strong')

    for i in range(len(movie_titles)):
        title = movie_titles[i].text.strip()
        year = movie_years[i].text.strip()[1:-1]  # Remove parentheses
        rating = movie_ratings[i].text.strip()
        movies.append({
            'title': title,
            'year': year,
            'rating': rating
        })

    return movies

def save_to_csv(movies):
    headers = ['title', 'year', 'rating']
    with open('../python-scripts/movies.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(movies)

if __name__ == '__main__':
    movie_data = scrape_movies()
    save_to_csv(movie_data)
    print('Scraping and saving to CSV completed.')
