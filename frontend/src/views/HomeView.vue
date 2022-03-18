<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to Stylist WebSite
        </p>
        <p class="subtitle">
          The best stylist in the world
        </p>
      </div>

    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Portfolio</h2>
      </div>

      <div class="column is-3" v-for="collection in collections" v-bind:key="collection.id">
        <div class="box">
          <figure class="image mb-4">
            <img v-bind:src="collection.get_cover_picture">
          </figure>

          <h3 class="is-size-4">{{ collection.title }}</h3>

          View details
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
  components: {
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

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>