<template>
  <center>
    <h1>Страница не найдена!</h1>
    <p>
      <a href="/">Вернуться на домашнюю страницу</a>
      <div class="arrow">&#8593;</div>
      Нажми сюда
    </p>
  </center>
</template>

<script>
export default {
  name: "PageNotFound",
  mounted() {
    document.title = 'Страница не найдена | Kseniia Zi'
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@300;400;500;600;700&display=swap');

center {
  font-family: 'Cormorant SC', serif;
  height: 50vh;
  margin: 15vw;
}

h1 {
  font-size: 4em;
}

a{
  font-size: 1.5rem;
  color: black;
  text-decoration: none;
}

a:hover {
  font-weight: bold;
}

.arrow {
  font-size: 1.5rem;
}
</style>