<template>
  <div class="navbar">
    <div class="title" @click="$router.push('/')">Kseniia Zi</div>
    <div class="pages">
      <div class="page" :class="{'current-page': page==='portfolio'}" @click="$router.push('/portfolio')">Портфолио</div>
      <div class="page" :class="{'current-page': page==='about'}" @click="$router.push('/about')">О себе</div>
      <div class="page" :class="{'current-page': page==='services'}" @click="$router.push('/services')">Услуги</div>
      <div class="page" :class="{'current-page': page==='reviews'}" @click="$router.push('/reviews')">Отзывы</div>
      <div class="page" :class="{'current-page': page==='auth'}" @click="$router.push('/auth')">Войти</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  props: {
    page: String
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@500;300&display=swap');

.navbar {
  display: flex;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 70px;
  backdrop-filter: blur(5px);
  box-shadow: 0 5px 40px 1px gray;
  padding-left: 108px;
  padding-right: 108px;
}

.title {
  font-family: 'Cormorant SC', serif;
  font-weight: 500;
  font-size: 48px;
  cursor: pointer;
  align-self: center;
}

.pages {
  display: flex;
  font-family: 'Cormorant SC', serif;
  font-weight: 300;
  font-size: 18px;
  align-self: center;
  margin-left: auto;
}

.page {
  margin-inline: 21px;
  padding: 6px 23px 6px 23px;
}

.page:hover {
  cursor: pointer;
  color: gray;
}

.current-page{
  border: 1px solid #000000;
  border-radius: 10px;
}

.current-page:hover{
  border: 1px solid gray;
}
</style>