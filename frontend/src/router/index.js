import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '../views/LoginPage.vue';
import HomePage from '../views/HomePage.vue';
import RegisterPage from '../views/RegisterPage.vue';
import InstitutionPage from '../views/InstitutionPage.vue'
import SchoolsPage from '../views/SchoolsPage.vue'
import PostSecondaryPage from '../views/PostSecondaryPage.vue'
import SpecialisedPage from '../views/SpecialisedPage.vue'
import UniversitiesPage from '../views/UniversitiesPage.vue'
import AutonomousUniversities from '../views/AutonomousUniversities.vue'

const routes = [
  { path: '/universities/autonomous', component: AutonomousUniversities },
  { path: '/schools', component: SchoolsPage },
  { path: '/post-secondary', component: PostSecondaryPage },
  { path: '/specialised', component: SpecialisedPage },
  { path: '/universities', component: UniversitiesPage },
  { path: '/login', component: LoginPage },
  { path: '/', component: HomePage },
  { path: '/register', component: RegisterPage},
  { path: '/Institution', component: InstitutionPage}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
