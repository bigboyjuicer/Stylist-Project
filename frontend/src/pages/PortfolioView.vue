<template>
  <div class="home">
    <div class="navbar">
      <router-link to="/">
        <div class="title">Kseniia Zi</div>
      </router-link>
      <div class="pages">
        Портфолио

      </div>
    </div>

    <!--    <div class="columns is-multiline">-->
    <!--      <div class="column is-12">-->
    <!--        <h2 class="is-size-2 has-text-centered">Portfolio</h2>-->
    <!--      </div>-->
    <!--      <div class="column is-3" v-for="collection in collections" v-bind:key="collection.id">-->
    <!--        <div style="text-align: center">-->
    <!--          <a href="/about">-->
    <!--            <img v-bind:src="collection.cover_picture" style=" max-height: 430px; width: auto; height: auto;">-->
    <!--          </a>-->
    <!--          <h3 class="is-size-5">{{ collection.title }}</h3>-->
    <!--        </div>-->
    <!--      </div>-->
    <!--    </div>-->
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'HomeView',
  data() {
    return {
      collections: []
    }
  },
  components: {},
  mounted() {
    this.getPortfolio()
  },
  methods: {
    getPortfolio() {
      axios
          .get('/api/portfolio/')
          .then(response => {
            this.collections = response.data
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
}
</script>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@500&display=swap');

.home {
  background-image: url(http://127.0.0.1:8000/media/images/pexels-jo%C3%A3o-jesus-925743_1.jpg);
  background-repeat: no-repeat;
  background-size: cover;
  height: 100vh;
  width: 100%;
}

.navbar {
  display: flex;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 9999;
  width: 100%;
  height: 70px;
  background-color: transparent;
  backdrop-filter: blur(25px);
  box-shadow: 0px 5px 40px 1px gray;
  padding-inline: 108px;
}

.title {
  font-family: 'Cormorant SC', serif;
  font-weight: 500;
  font-size: 48px;
  text-align: center;
}
</style>