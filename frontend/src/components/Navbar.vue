<template>
  <div class="navbar">
    <div class="title" @click="$router.push('/')">Kseniia Zi</div>
    <div class="pages">
      <div class="page" :class="{'current-page': page==='portfolio'}" @click="$router.push('/portfolio')">Портфолио
      </div>
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

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display+SC:wght@400&display=swap');

.navbar {
  display: flex;
  width: 100%;
  height: 70px;
  justify-content: space-between;
  background-color: black;
  color: whitesmoke;
  box-shadow: 0 5px 40px 1px gray;
  padding-inline: 5vw;
}

.title {
  font-family: 'Playfair Display SC', serif;
  font-weight: 500;
  font-size: 48px;
  white-space: nowrap;
  cursor: pointer;
}

.pages {
  display: flex;
  gap: 4vw;
  align-items: center;
  flex-wrap: wrap;
  font-family: 'Cormorant SC', serif;
  font-weight: 300;
  font-size: 18px;
}

.page {
  cursor: pointer;
  padding: 0.25vh 1vw;
  white-space: nowrap;
}

.page:not(.current-page):hover{
  text-decoration: underline;
}

.current-page{
  border: 1px solid #ffffff;
  border-radius: 8px;
}

</style>