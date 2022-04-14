<template>
  <div class="portfolio">
    <my-dialog v-model:show="collectionVisible">
      <my-collection-detail :collection="chosenCollection"></my-collection-detail>
    </my-dialog>
    <div class="reel">
      <div class="collection" @click="collectionOpen(collection)" v-for="collection in collections"
           v-bind:key="collection.id">
        <div class="frame">
          <img :src="collection.cover_picture">
        </div>
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
    document.title = 'Портфолио | Kseniia Zi'
  },
  methods: {
    getPortfolio() {

      this.$store.commit('changeLoaderVisible')

      axios.defaults.headers.common['Authorization'] = ''

      setTimeout(async () => {
        axios
            .get('/api/portfolio/')
            .then(response => {
              this.collections = response.data
            })
            .catch(error => {
              console.log(error)
            }).finally(onFinally => {
          this.$store.commit('changeLoaderVisible')
        })
      }, 500)
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
  background-color: white;
  height: 100vh;
}

.reel {
  padding: 10vh 10vw;
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

.frame{
  overflow: hidden;
  height: 560px;
  width: 381px;
}

.frame img {
  width: 100%;
  height: 100%;
  transition: transform 1s ease;
}

.frame img:focus,
.frame img:hover{
  transform: scale(1.3);
}

.collection_title {
  font-family: 'Cormorant SC', serif;
  font-weight: 400;
  font-size: 25px;
}

.collection_title:hover {
  cursor: pointer;
  text-decoration: underline;
}
</style>