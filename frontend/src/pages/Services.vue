<template>
  <div class="services">
    <navbar page="services"></navbar>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";

export default {
  name: "Services",
  components: {
    Navbar
  }
}
</script>

<style scoped>
.services {
  background-color: #EBEBEB;
  height: 100vh;
}
</style>