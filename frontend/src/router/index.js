import { createRouter, createWebHistory } from "vue-router";
import MovieList from "../components/MovieList.vue"; // Replace with your component paths
import MovieDetails from "../components/MovieDetails.vue";

const routes = [
  { path: "/", name: "Home", component: MovieList },
  { path: "/movie/:id", name: "MovieDetails", component: MovieDetails },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
