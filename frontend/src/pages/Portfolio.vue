<template>
  <div class="portfolio">
    <my-navbar page="portfolio" @openDialog="loginOpen"></my-navbar>
    <my-dialog v-model:show="loginVisible">
      <my-login-form></my-login-form>
    </my-dialog>
    <my-dialog v-model:show="collectionVisible">
      <my-collection-detail :collection="chosenCollection"></my-collection-detail>
    </my-dialog>
    <div class="reel">
      <div class="collection" @click="collectionOpen(collection)" v-for="collection in collections" v-bind:key="collection.id">
        <img :src="collection.cover_picture">
        <div class="collection_title">{{ collection.title }}</div>
      </div>
      <div class="collection" @click="collectionOpen(collection)" v-for="collection in collections" v-bind:key="collection.id">
        <img :src="collection.cover_picture">
        <div class="collection_title">{{ collection.title }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MyNavbar from "@/components/MyNavbar";
import MyDialog from "@/components/MyDialog";
import MyLoginForm from "@/components/MyLoginForm";
import MyCollectionDetail from "@/components/MyCollectionDetail";


export default {
  name: 'Portfolio',
  data() {
    return {
      collections: [],
      loginVisible: false,
      collectionVisible: false,
      chosenCollection: 0,
    }
  },
  components: {
    MyNavbar,
    MyDialog,
    MyLoginForm,
    MyCollectionDetail,
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
    },
    loginOpen(dialogVisible) {
      this.loginVisible = dialogVisible
    },
    collectionOpen(collection) {
      this.collectionVisible = true;
      this.chosenCollection = collection;
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
  cursor: pointer;
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