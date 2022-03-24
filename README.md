# Movie Recommendation System
Demo link-[Click here](https://movierecommendationadi.herokuapp.com/)

![Car Price Prediction](https://github.com/Aditya-171/Photos/blob/master/Screenshot%20(44).png)
---

## Overview
Content Based Recommender System recommends movies similar to the movie user likes .
The details of the movies(title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, https://www.themoviedb.org/documentation/api.
---
## How to get an API ?
Create an account in https://www.themoviedb.org/, click on the API link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will be able to 
the API key in your API sidebar once your request is approved.

---
## How to run the project?
1.Clone or download this repository to your local machine.
2. Install all the libraries mentioned in the requirements.txt file with the command pip install -r requirements.txt
3. Get your API key from https://www.themoviedb.org/. (Refer the above section on how to get the API key)
4. Replace YOUR_API_KEY in both the places (line no. 15 and 29) of static/recommend.js file and hit save.
5.Open your terminal/command prompt from your project directory and run the file main.py by executing the command python main.py.
6. Go to your browser and type http://127.0.0.1:5000/ in the address bar.
7. That's it, you are good to go.
