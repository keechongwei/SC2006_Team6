<template>
  <div class="app-container">
    <header class="header">
      <h1 class="logo">LearnLeap</h1>
      <nav class="navbar">
        <router-link to="/" class="nav-link">Home</router-link>
        <router-link to="/login" class="nav-link">Login</router-link>
        <router-link to="/register" class="nav-link">Register</router-link>
        <router-link to="/Institution" class="nav-link">Institution</router-link>
      </nav>
    </header>

    <main class="main-content">
      <router-view />
    </main>

    <footer class="footer">
      <p>&copy; 2025 LearnLeap. Empowering your academic journey.</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style scoped>
.app-container {
  font-family: 'Segoe UI', Roboto, sans-serif;
  background: linear-gradient(to right, #f4f6f9, #e1ecf4);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.header {
  background: #1e3a8a;
  padding: 1.2rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: white;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.logo {
  font-size: 1.8rem;
  font-weight: bold;
  letter-spacing: 1px;
}

.navbar {
  display: flex;
  gap: 1.5rem;
}

.nav-link {
  color: #e0f2fe;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: #93c5fd;
}

.main-content {
  flex: 1;
  padding: 2rem;
  color: #1e293b;
  font-size: 1.1rem;
}

.footer {
  background: #1e3a8a;
  color: #cbd5e1;
  text-align: center;
  padding: 1rem;
  font-size: 0.9rem;
}
</style>
