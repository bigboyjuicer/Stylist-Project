<template>
  <div class="collection_detail">
    <div class="title">{{ collection.title }}</div>
    <div class="pictures">
      <img :src="picture.image" v-for="picture in collection.pictures" v-bind:key="picture.id">
    </div>
  </div>
</template>

<script>
export default {
  name: "MyCollectionDetail",
  props: {
    collection: {
      type: [],
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@300;400;500;600;700&display=swap');

.collection_detail {
  position: absolute;
  transform: translate(-50%, -50%);
  top: 50%;
  left: 50%;
  height: max-content;
  width: 70vw;
  border-radius: 15px;
  backdrop-filter: blur(15px);
  border: 2px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 0 40px rgba(8, 7, 16, 0.6);
  padding: 50px;
}

.title{
  max-width: max-content;
  margin-inline: auto;
  padding-inline: 25px;
  border-radius: 15px;
  backdrop-filter: blur(10px);
  border: 2px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 0 40px rgba(8, 7, 16, 0.6);
  font-size: 48px;
  font-family: 'Cormorant SC', serif;
  color: white;
}

img {
  max-height: 220px;
  height: auto;
  width: auto;
  border-radius: 10px;
  box-shadow: 0 0 40px rgba(8, 7, 16, 0.6);
}

.pictures {
  margin-top: 25px;
  padding: 25px 50px 50px 50px;
  display: flex;
  justify-content: start;
  gap: 5%;
  overflow-x: auto;
}

::-webkit-scrollbar-thumb{
  background-color: white;
}
</style>