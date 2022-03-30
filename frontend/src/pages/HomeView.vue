<template>
  <div class="home">
    <router-link to="/portfolio">
      <div class="blur">
        <div class="title">
          <div class="stylist">Стилист</div>
          <div class="name">Kseniia Zi</div>
          <div class="annotation">Тут говорят о женственности</div>
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'HomeView',
  data() {
    return {
      picture: ""
    }
  },
  components: {},
  mounted() {
    this.getPortfolio()
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
    }
  }
}
</script>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@600;700&display=swap');

.home {
  background-image: url(http://127.0.0.1:8000/media/images/Second_background.jpg);
  background-repeat: no-repeat;
  background-size: cover;
  height: 100vh;
  width: 100%;
}

.blur {
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(8px);
  width: 100%;
  height: 100%;
}

.title {
  font-family: 'Cormorant SC', serif;
  width: 55%;
  color: black;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.stylist {
  margin-left: 20%;
  font-weight: 600;
  font-size: 36px;
}

.name {
  font-weight: 700;
  font-size: 72px;
  text-align: center;
}

.annotation {
  font-weight: 600;
  font-size: 36px;
  padding-left: 52%;
}


</style>