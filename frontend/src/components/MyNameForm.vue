<template>
  <form @submit.prevent="saveName">
    <h3>Изменить имя</h3>
    <my-input
        v-model="name"
        type="text"
        placeholder="Имя"
    />
    <my-button class="save-btn">Сохранить</my-button>
  </form>
</template>

<script>
import axios from "axios";
import store from "@/store";

export default {
  name: "MyNameForm",
  props: {
    name: {
      type: String,
    }
  },
  methods: {
    saveName() {
      const formData = {
        email: this.$store.state.email,
        first_name: this.name
      }

      axios.put(`api/users/${this.$store.state.user_id}`, formData).then(response => {
        store.commit('changeNameVisible')

        this.$notify({
          group: "app",
          type: "success",
          duration: 500,
          title: "Имя успешно изменено",
        });
      }).catch(error => {
        store.commit('changeNameVisible')

        this.$notify({
          group: "app",
          type: "error",
          duration: 500,
          title: "Ошибка",
        });
        console.log(error)
      })
      this.$router.go()
    }
  }
}
</script>

<style scoped>
form {
  height: 19rem;
  width: 25rem;
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

button:hover {
  color: black;
  background-color: rgb(239, 180, 78);
}

.save-btn {
  margin-top: 5%;
}
</style>