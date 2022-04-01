<template>
  <div class="reviews">
    <navbar page="reviews"></navbar>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";

export default {
  name: "Reviews",
  components: {
    Navbar
  }
}
</script>

<style scoped>
.reviews {
  background-color: #EBEBEB;
  //background-image: url(http://127.0.0.1:8000/media/images/pexels-jo%C3%A3o-jesus-925743_1.jpg);
  overflow: auto;
}
</style>