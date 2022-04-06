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
  height: 100vh;
}
</style>