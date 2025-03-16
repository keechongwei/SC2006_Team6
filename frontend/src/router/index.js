import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '../views/LoginPage.vue';
import HomePage from '../views/HomePage.vue';
import RegisterPage from '../views/RegisterPage.vue';
import InstitutionPage from '../views/InstitutionPage.vue'
import HawkerPage from '../views/HawkerPage.vue';

const routes = [
  { path: '/login', component: LoginPage },
  { path: '/', component: HomePage },
  { path: '/register', component: RegisterPage},
  { path: '/Institution', component: InstitutionPage},
  { path: '/Hawker', component:HawkerPage}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
