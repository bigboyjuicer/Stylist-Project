<template>
  <div class="navbar" v-if="$route.path !== '/'">
    <router-link to="/" class="title">Kseniia Zi</router-link>
    <div class="pages">
      <router-link to="/portfolio" class="page" :class="{'current-page': $route.path==='/portfolio'}">
        Портфолио
      </router-link>
      <router-link to="/about" class="page" :class="{'current-page': $route.path==='/about'}">О себе</router-link>
      <router-link to="/services" class="page" :class="{'current-page': $route.path==='/services'}">Услуги</router-link>
      <router-link to="/reviews" class="page" :class="{'current-page': $route.path==='/reviews'}">Отзывы</router-link>
      <div v-if="!$store.state.isAuthenticated" class="page" @click="this.$store.commit('changeLoginVisible')">Войти</div>
      <div v-else class="profile-dropdown">
        Личный аккаунт
        <div class="dropdown-content">
          <router-link to="/profile" class="dropdown-text">Профиль</router-link>
          <div class="dropdown-text" @click="logOut">Выйти</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Dialog from "@/components/MyDialog";
import axios from "axios";
import store from "@/store";

export default {
  name: "Navbar",
  components: {
    Dialog
  },
  data() {
    return {
      dialogVisible: false,
    }
  },
  methods: {
    logOut() {
      axios.defaults.headers.common['Authorization'] = ""
      localStorage.removeItem('token')
      store.commit('removeToken')
      store.commit('removeEmail')
      this.$router.push('/')
    }
  }
}
</script>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display+SC:wght@400&display=swap');

.navbar {
  display: flex;
  width: 100%;
  height: 70px;
  justify-content: space-between;
  background-color: black;
  color: whitesmoke;
  box-shadow: 0 5px 40px 1px gray;
  padding-inline: 5vw;
}

.title {
  text-decoration: none;
  color: inherit;
  font-family: 'Playfair Display SC', serif;
  font-weight: 500;
  font-size: 48px;
  white-space: nowrap;
  cursor: pointer;
}

.pages {
  display: flex;
  gap: 4vw;
  align-items: center;
  flex-wrap: wrap;
  font-family: 'Cormorant SC', serif;
  font-weight: 300;
  font-size: 18px;
}

.page {
  text-decoration: none;
  color: inherit;
  cursor: pointer;
  padding: 0.25vh 1vw;
  white-space: nowrap;
}

.profile-dropdown {
  text-decoration: none;
  color: inherit;
  cursor: pointer;
  padding: 0.25vh 1vw;
  white-space: nowrap;
}

.dropdown-content {
  display: none;
  flex-flow: column;
  align-items: flex-end;
  width: 155px;
  padding-inline: 15px;
  padding-bottom: 15px;
  position: absolute;
  background-color: black;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
}

.profile-dropdown:hover .dropdown-content {
  display: flex;
}

.dropdown-text {
  margin-top: 15px;
  text-decoration: none;
  color: inherit;
  cursor: pointer;
  white-space: nowrap;
}

.dropdown-text:not(.current-page):hover {
  text-decoration: underline;
}

.page:not(.current-page):hover {
  text-decoration: underline;
}

.current-page {
  border: 1px solid #ffffff;
  border-radius: 8px;
}

</style>