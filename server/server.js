// server.js
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'client/build')));

app.get('/', (req, res) => {
    res.send('Welcome to the Movie Recommendation API');
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

const fs = require('fs');
const csv = require('csv-parser');

let movies = [];

// Load movies from CSV
fs.createReadStream('movies.csv')
    .pipe(csv())
    .on('data', (row) => {
        movies.push(row);
    })
    .on('end', () => {
        console.log('CSV file successfully processed');
    });

// Endpoint to get movies
app.get('/api/movies', (req, res) => {
    res.json(movies);
});