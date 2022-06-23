<template>
  <div id="wrapper">
    <my-navbar></my-navbar>
    <router-view/>
    <my-dialog v-model:show="$store.state.loginVisible">
      <my-login-form></my-login-form>
    </my-dialog>
    <my-dialog v-model:show="$store.state.registrationVisible">
      <my-registration-form></my-registration-form>
    </my-dialog>
    <notifications group="app" position="bottom center" width="25%" classes="my-notification"/>
    <loader class="loader" object="black" size="10" speed="1" bg="#ffffff" opacity="0" name="dots"
            v-if="$store.state.loaderVisible"></loader>
  </div>
</template>

<script>
import axios from 'axios'
import store from "@/store";
import MyNavbar from "@/components/MyNavbar";
import MyDialog from "@/components/MyDialog";
import MyLoginForm from "@/components/MyLoginForm";
import MyRegistrationForm from "@/components/MyRegistrationForm";

export default {
  components: {
    MyNavbar,
    MyDialog,
    MyLoginForm,
    MyRegistrationForm,
  },
  data() {
    return {}
  },
  mounted() {
    this.Authorization()
  },
  methods: {
    Authorization() {
      if (localStorage.getItem('token')) {
        let token = localStorage.getItem('token')
        axios.defaults.headers.common['Authorization'] = 'Token ' + token

        axios.get("api/auth/users/me/").then(response => {
          store.commit('setUserId', response.data.id)
          store.commit('setEmail', response.data.email)
          store.commit('setToken', token)
        }).catch(errors => {
          console.log(errors)
        })
      }
    },
  }
}


</script>


<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@300;400;500;600;700&display=swap');

::-webkit-scrollbar {
  width: 16px;
}

::-webkit-scrollbar-track {
  background-color: transparent;
}

::-webkit-scrollbar-thumb {
  border-radius: 100px;
  border: 5px solid transparent;
  background-clip: padding-box;
  background-color: gray;
}

.bottom-info-bar {
  background-color: black;
  height: 7vh;
}

/* Box sizing rules */
*,
*::before,
*::after {
  box-sizing: border-box;
}

/* Remove default margin */
body,
h1,
h2,
h3,
h4,
p,
figure,
blockquote,
dl,
dd {
  margin: 0;
}

/* Set core body defaults */
body {
  min-height: 100vh;
  text-rendering: optimizeSpeed;
}

/* Inherit fonts for inputs and buttons */
input,
button,
textarea,
select {
  font: inherit;
}

.my-notification {
  margin-bottom: 2rem;
  padding: 10px;
  font-size: 12px;
  color: #ffffff;

  .notification-title {
    font-family: 'Cormorant SC', serif;
    font-size: 1.5rem;
    text-align: center;
  }

  .notification-content {
    font-family: 'Cormorant SC', serif;
  }

  &.success {
    background: #68cd86;
    border-left-color: #68cd86;

  }

  &.info {
  }

  &.error {
    background: red;
  }
}
</style>
