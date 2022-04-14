<template>
  <form @submit.prevent="makeOrder">
    <h3>{{ title }}</h3>

    <my-input
        v-model="phonenumber"
        type="tel"
        placeholder="Номер телефона"
        pattern="[0-9]{1}[0-9]{3}[0-9]{3}[0-9]{4}"
    />

    <textarea v-model="comment" rows="5" placeholder="Комментарий к заказу"></textarea>
    <my-button class="submit-btn">Подтвердить</my-button>
  </form>
</template>

<script>
import axios from "axios";
import store from "@/store";

export default {
  name: "MyOrderForm",
  components: {},

  props: {
    service: {
      type: Number,
      default: null
    },
    title: {
      type: String,
      default: '',
    }
  },
  data() {
    return {
      phonenumber: '',
      comment: '',
    }
  },
  methods: {
    makeOrder(){
      const formData = {
        user: this.$store.state.user_id,
        service: this.service,
        user_phonenumber: this.phonenumber,
        comment: this.comment,
      }

      axios.defaults.headers.common['Authorization'] = 'Token ' + this.$store.state.token

      axios.post('api/order/', formData).then(response => {
        store.commit('changeOrderVisible')

        this.$notify({
          group: "app",
          type: "success",
          duration: 500,
          title: "Услуга успешно оформлена",
        });
      }).catch(error => {
        store.commit('changeOrderVisible')

        this.$notify({
          group: "app",
          type: "error",
          duration: 500,
          title: "Ошибка",
        });
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>
form {
  height: 26rem;
  width: 40rem;
  position: absolute;
  transform: translate(-50%, -50%);
  top: 50%;
  left: 50%;
  backdrop-filter: blur(15px);
  border-radius: 15px;
  border: 2px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 0 40px rgba(8, 7, 16, 0.6);
  padding: 50px 35px;
}

form * {
  font-family: 'Cormorant SC', serif;
  color: #ffffff;
  letter-spacing: 0.5px;
  outline: none;
  border: none;
}

form h3 {
  font-size: 32px;
  font-weight: 500;
  line-height: 42px;
  text-align: center;
}

::placeholder {
  color: #e5e5e5;
  vertical-align: center;
}

textarea {
  display: block;
  width: 100%;
  background-color: rgba(255, 255, 255, 0.15);
  border-radius: 5px;
  padding: 10px 10px;
  margin-top: 15px;
  font-size: 14px;
  font-weight: 300;
  resize: none;
}

button:hover {
  color: black;
  background-color: rgb(239, 180, 78);
}

.submit-btn{
  margin-top: 5%;
}
</style>