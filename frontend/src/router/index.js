import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../components/HomePage.vue";
import LoginPage from "../components/LoginPage.vue";
import MoviePage from "../components/MoviePage.vue";
import UserProfile from "../components/UserProfile.vue"; 
import CreateProfile from "@/components/CreateProfile.vue";
import UserSettings from "../components/UserSettings.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomePage,
  },
  {
    path: "/login",
    name: "Login",
    component: LoginPage,
  },
  {
    path: "/movie/:mid",
    name: "Movie",
    component: MoviePage,
  },
  {
    path: "/profile/:uid",
    name: "UserProfile",
    component: UserProfile,
  },
  {
    path: "/create-profile",
    name: "CreateProfile",
    component: CreateProfile,
  },
  {
    path: "/settings",
    name: "UserSettings",
    component: UserSettings,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
