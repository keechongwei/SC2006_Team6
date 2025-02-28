import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '../views/LoginPage.vue';
import HomePage from '../views/HomePage.vue';
import RegisterPage from '../views/RegisterPage.vue';

const routes = [
  { path: '/login', component: LoginPage },
  { path: '/', component: HomePage },
  { path: '/register', component: RegisterPage},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
