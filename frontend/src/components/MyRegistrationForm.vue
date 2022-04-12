<template>
  <form @submit.prevent="submitForm">
    <h3>Регистрация</h3>

    <my-input
        v-model="email"
        type="text"
        placeholder="Почта"
    />

    <my-input
        v-model="password1"
        type="password"
        placeholder="Пароль"
    />

    <my-input
        v-model="password2"
        type="password"
        placeholder="Пароль"
    />


    <my-button>Зарегистрироваться</my-button>
  </form>
</template>

<script>
import axios from 'axios'
import store from "@/store";

export default {
  name: "MyForm",
  data() {
    return {
      email: '',
      password1: '',
      password2: '',
      errors: []
    }
  },
  mounted() {

  },
  methods: {
    async submitForm() {
      axios.defaults.headers.common['Authorization'] = ""

      localStorage.removeItem('token')

      if (this.password1 === this.password2) {
        const formData = {
          email: this.email,
          password: this.password1
        }

        this.email = ''
        this.password1 = ''
        this.password2 = ''

        await axios
            .post("api/auth/users/", formData)
            .then(response => {
              axios
                  .post("api/auth/token/login", formData)
                  .then(response => {
                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)

                    axios.defaults.headers.common['Authorization'] = 'Token ' + token

                    localStorage.setItem('token', token)

                    axios.get("api/auth/users/me/").then(response => {
                      store.commit('setUserId', response.data.id)
                      store.commit('setEmail', response.data.email)
                    })

                    store.commit('changeRegistrationVisible')

                    this.$notify({
                      group: "app",
                      type: "success",
                      duration: 500,
                      title: "Вы успешно зарегистрировались",
                    });
                  })
                  .catch(error => {
                    if (error.response) {
                      for (const property in error.response.data) {
                        this.errors.push(`${property}: ${error.response.data[property]}`)
                      }
                    } else {
                      this.errors.push('Something went wrong. Please try again')

                      console.log(JSON.stringify(error))
                    }
                  })
            })
            .catch(error => {
              if (error.response) {
                for (const property in error.response.data) {
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }
              } else {
                this.errors.push('Something went wrong. Please try again')

                console.log(JSON.stringify(error))
              }
            })
      }
    }
  }
}
</script>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@300;400;500;600;700&display=swap');


form {
  height: 28rem;
  width: 25rem;
  position: absolute;
  transform: translate(-50%, -50%);
  top: 50%;
  left: 50%;
  border-radius: 15px;
  backdrop-filter: blur(10px);
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

input {
  display: block;
  height: 50px;
  width: 100%;
  background-color: rgba(255, 255, 255, 0.15);
  border-radius: 5px;
  padding: 0 10px;
  margin-top: 15px;
  font-size: 14px;
  font-weight: 300;
}

::placeholder {
  color: #e5e5e5;
}

button {
  margin-top: 15%;
  width: 100%;
  background-color: transparent;
  border: 2px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 0 40px rgba(8, 7, 16, 0.6);
  color: white;
  padding: 15px 0;
  font-size: 18px;
  font-weight: 600;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  color: black;
  background-color: rgb(239, 180, 78);
}

.registration-btn {
  margin-top: 5%;
}
</style>