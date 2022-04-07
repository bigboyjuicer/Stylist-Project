<template>
  <div class="about">
    <navbar page="about"></navbar>
    <my-dialog v-model:show="loginVisible">
      <my-login-form></my-login-form>
    </my-dialog>

    <div class="about_container">
      <img src="http://127.0.0.1:8000/media/images/RFRtZSHRglU.jpg">
      <div class="info">
        <div class="title">
          Зинина Ксения, fashion-стилист
        </div>
        <hr class="rounded">
        <div class="description">
          Занимаюсь стилизацией и разработкой идей для съемок, разбором гардеробов, шоппинг - сопровождениями и
          консультациями по стилю.
        </div>
        <div class="description">
          Опыт работы более 4-х лет. Начинала свой путь в бренде женской одежды SWANK, далее
          окончила курсы стилистов @prostylecommerce, работала с Concept Club, Acoola, Infinity, Lingerie.
        </div>
        <div class="description">
          Есть опыт работы с каталогами, лук буками и кампейнами.
        </div>
        <div class="description">
          Из достижений, публикации в журналах: Sobaka.ru, Shuba Magazine,
          KODD Magazine, Sicky Magazine и обложка в журнале ELEGANT Magazine. Так же работы были представлены на
          фото-выставке в Милане @pa.nova.gallery.
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/MyNavbar";
import MyDialog from "@/components/MyDialog";
import MyLoginForm from "@/components/MyLoginForm";

export default {
  name: "About",
  components: {
    Navbar,
    MyDialog,
    MyLoginForm
  },
  data() {
    return {}
  },
  mounted() {

  },
  methods: {}
}
</script>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@300;400;500;600;700&display=swap');

.about {
  background-color: #EBEBEB;
  height: 100vh;
}

.about_container {
  margin-block: 10vh;
  padding-inline: 10vw;
  display: flex;
  align-items: center;
  gap: 5%;
}

img {
  max-width: 469px;
  width: auto;
  height: auto;
}

.info {
  display: inline-block;
  font-family: 'Cormorant SC', serif;
}

.title {
  font-size: 36px;
}

.description {
  max-width: 67ch;
  margin-top: 25px;
  font-size: 24px;
}

.rounded {
  margin-top: 25px;
  border-top: 1px solid black;
  border-radius: 5px;
}
</style>