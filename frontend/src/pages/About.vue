<template>
  <div class="about">
    <navbar page="about"></navbar>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";

export default {
  name: "About",
  components: {
    Navbar
  }
}
</script>

<style scoped>
.about {
  background-color: #EBEBEB;
  height: 100vh;
}
</style>