npm install -g @vue/cli

if you get an error try this: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

if successful installation: vue create frontend

cd frontend

install axios: npm install axios

npm install vue-router

in a different terminal, Start Flask backend by running the app.js file.
go back to first termianl to Start Vue frontend (npm run serve).
Visit:
http://localhost:8080/: 
Should show a list of movies.
Click on a movie: Should navigate to http://localhost:8080/movie/<movie_id> and show movie details.
