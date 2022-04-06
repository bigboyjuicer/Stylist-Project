<template>
  <div class="portfolio">
    <navbar page="portfolio"></navbar>
    <div class="reel">
      <div class="collection" v-for="collection in collections" v-bind:key="collection.id">
        <img v-bind:src="collection.cover_picture">
        <div class="collection_title">{{ collection.title }}</div>
      </div>
      <div class="collection" v-for="collection in collections" v-bind:key="collection.id">
        <img v-bind:src="collection.cover_picture">
        <div class="collection_title">{{ collection.title }}</div>
      </div>
    </div>
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
@import url('https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@300;400;500;600;700&display=swap');

.portfolio {
  background-color: #EBEBEB;
  background-size: cover;
  height: 200vh;
}

.reel {
  margin-block: 10vh;
  padding-inline: 10vw;
  display: flex;
  overflow-x: auto;
  align-items: start;
  gap: 16vw;
}

.reel::-webkit-scrollbar {
  width: 1px;
}

.reel::-webkit-scrollbar-thumb {
  border-radius: 100px;
  border: 5px solid transparent;
  background-clip: padding-box;
  background-color: lightgray;
}

.collection {
  padding-bottom: 3vh;
  text-align: center;
}

img {
  max-height: 430px;
  width: auto;
  height: auto;
}

.collection_title {
  font-family: 'Cormorant SC', serif;
  font-weight: 300;
  font-size: 25px;
}

.collection_title:hover {
  cursor: pointer;
  text-decoration: underline;
}

.bottom {
  border-radius: 10px 10px 0 0;
  margin-top: 500px;
  width: 100%;
  height: 150px;
  box-shadow: 0 -5px 40px 1px gray;
}
</style>