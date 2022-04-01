<template>
  <div class="portfolio">
    <navbar page="portfolio"></navbar>
    <div class="reel">
      <div class="collection" v-for="collection in collections" v-bind:key="collection.id">
        <img v-bind:src="collection.cover_picture" style=" max-height: 430px; width: auto; height: auto;">
        <div class="collection__title">{{ collection.title }}</div>
      </div>
    </div>
    <div class="bottom"></div>
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
import Navbar from "@/components/Navbar";


export default {
  name: 'Portfolio',
  data() {
    return {
      collections: []
    }
  },
  components: {
    Navbar
  },
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
@import url('https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@500;300&display=swap');

.portfolio {
  background-color: #EBEBEB;
  //background-image: url(http://127.0.0.1:8000/media/images/pexels-jo%C3%A3o-jesus-925743_1.jpg);
  overflow: auto;
}

.reel {
  margin-top: 70px;
  display: flex;
}

.collection {
  margin: auto;
  margin-top: 70px;
  text-align: center;
}

.collection__title {
  font-family: 'Cormorant SC', serif;
  font-weight: 300;
  font-size: 25px;
}

.bottom {
  border-radius: 10px 10px 0 0;
  margin-top: 500px;
  width: 100%;
  height: 150px;
  box-shadow: 0 -5px 40px 1px gray;
}
</style>