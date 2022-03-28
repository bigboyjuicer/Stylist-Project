<template>
  <div class="home">
    <div class="navbar">
    </div>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Portfolio</h2>
      </div>
      <div class="column is-3" v-for="collection in collections" v-bind:key="collection.id">
        <div style="text-align: center">
          <a href="/about">
            <img v-bind:src="collection.cover_picture" style=" max-height: 430px; width: auto; height: auto;">
          </a>
          <h3 class="is-size-5">{{ collection.title }}</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
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

<style scoped>
.home{
  background-image: url(http://127.0.0.1:8000/media/images/pexels-jo%C3%A3o-jesus-925743_1.jpg);
  background-repeat: no-repeat;
  background-size: cover;
  height: 100vh;
  width: 100%;
}

.navbar {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(8px);
  height: 94px;
  filter: drop-shadow(0px 5px 50px rgba(0, 0, 0, 0.25));
}
</style>