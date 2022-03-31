<template>
  <div class="portfolio">
    <div class="navbar">
      <div class="title" @click="$router.push('/')">Kseniia Zi</div>
      <div class="pages">
        <div class="page" @click="$router.push('/portfolio')">Портфолио</div>
        <div class="page" @click="$router.push('/about')">О себе</div>
        <div class="page" @click="$router.push('/services')">Услуги</div>
        <div class="page" @click="$router.push('/reviews')">Отзывы</div>
        <div class="page" @click="$router.push('/auth')">Войти</div>
      </div>
    </div>

    <div class="reel">
      <div class="collection" v-for="collection in collections" v-bind:key="collection.id">
        <img v-bind:src="collection.cover_picture" style=" max-height: 430px; width: auto; height: auto;">
        <div class="collection__title">{{ collection.title }}</div>
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
@import url('https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@500; 300&display=swap');

.portfolio {
  background-image: url(http://127.0.0.1:8000/media/images/pexels-jo%C3%A3o-jesus-925743_1.jpg);
  background-repeat: repeat;
  background-size: cover;
  height: 100vh;
  width: 100%;
}

.navbar {
  display: flex;
  position: fixed;
  width: 100%;
  height: 70px;
  backdrop-filter: blur(25px);
  box-shadow: 0 5px 40px 1px gray;
  padding-left: 108px;
  padding-right: 108px;
}

.title {
  font-family: 'Cormorant SC', serif;
  font-weight: 500;
  font-size: 48px;
  cursor: pointer;
  align-self: center;
}

.pages {
  display: flex;
  font-family: 'Cormorant SC', serif;
  font-weight: 300;
  font-size: 18px;
  align-self: center;
  margin-left: auto;
}

.page {
  margin-inline: 21px;
  padding: 6px 23px 6px 23px;
  cursor: pointer;
  /*border: 1px solid #000000;
  border-radius: 10px;*/
}

.reel {
  display: flex;
  overflow-x: scroll;
  white-space: nowrap;
  scroll-behavior: smooth;
}

.collection {
  margin: auto;
  margin-top: 150px;
  text-align: center;
}

.collection__title {
  font-family: 'Cormorant SC', serif;
  font-weight: 300;
  font-size: 25px;
}
</style>