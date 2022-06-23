<template>
  <div class="delete-form">
    <h3>Вы точно хотите отменить заказ?</h3>
    <div class="buttons">
      <my-button class="yes-btn" @click="declineOrder">Отменить</my-button>
      <my-button class="no-btn" @click="$store.commit('changeDeclineVisible')">Не отменять</my-button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import store from "@/store";

export default {
  name: "MyDeclineForm",
  components: {},
  props: {
    orderId: {
      type: Number,
      default: -1,
    }
  },
  methods: {
    declineOrder() {
      axios.delete(`api/order/${this.orderId}`).then(response => {
        this.$store.commit('changeDeclineVisible')
        this.$notify({
          group: "app",
          type: "success",
          duration: 500,
          title: "Заказ был удален",
        });
        this.$router.go()
      }).catch(error => {
        this.$store.commit('changeDeclineVisible')

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
.delete-form {
  height: 18rem;
  width: 30rem;
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

.delete-form * {
  font-family: 'Cormorant SC', serif;
  color: #ffffff;
  letter-spacing: 0.5px;
  outline: none;
  border: none;
}

.delete-form h3 {
  font-size: 32px;
  font-weight: 500;
  line-height: 42px;
  text-align: center;
}

.input-title {
  margin-top: 1rem;
}

.buttons {
  display: flex;
  gap: 2rem;
}

::placeholder {
  color: #e5e5e5;
  vertical-align: center;
}

.yes-btn {
  margin-top: 2rem;
}

.no-btn {
  margin-top: 2rem;
}

.yes-btn:hover {
  color: white;
  background-color: red;
}

.no-btn:hover {
  color: black;
  background-color: rgb(239, 180, 78);
}

</style>