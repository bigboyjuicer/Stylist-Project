<template>
  <div class="home">
    <router-link to="/portfolio">
      <div class="blur">
        <div class="title">
<!--          <div class="stylist">Стилист</div>-->
          <div class="name">Kseniia Zi</div>
<!--          <div class="annotation">Тут говорят о женственности</div>-->
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      picture: ""
    }
  },
  components: {},
  mounted() {
    this.getPortfolio()
    document.title = 'Kseniia Zi'
  },
  methods: {
    getPortfolio() {
      axios
          .get('/api/pictures/7/')
          .then(response => {
            this.picture = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
  },
}
</script>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display+SC:wght@400&display=swap');

.home {
  background-image: url(http://127.0.0.1:8000/media/images/Second_background.jpg);
  background-size: cover;
  background-position: center;
}

.blur {
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(8px);
  height: 100vh;
}

.title {
  display: inline-block;
  font-family: 'Playfair Display SC', serif;
  color: black;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: min-content;
  white-space: nowrap;
  text-align: center;
}

.stylist {
  font-size: 2.25rem;
}

.name {
  font-size: 4.5rem;
}

.annotation {
  font-size: 2.25rem;
}

</style>