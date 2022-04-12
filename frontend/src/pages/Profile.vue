<template>
  <div class="profile">
    <div class="profile-content" v-if="$store.state.isAuthenticated">
      <div v-if="!$store.state.loaderVisible">
        <div class="profile-title">Ваш профиль</div>
        <div class="profile-info">
          <div class="profile-name">
            Имя:
            <div class="name" v-if="user.first_name"> {{ user.first_name }}</div>
            <div class="name" v-else> Вы не указали имя</div>
            <img class="edit-icon" src="https://www.svgrepo.com/show/42233/pencil-edit-button.svg" @click="changeName">
          </div>
        </div>

        <div class="order-title">Ваши заказы</div>

        <div class="order-list">
          <div class="order" v-for="order in orders" v-bind:key="order.id">
            <div class="service-title">{{ order.service.title }}</div>
            <div class="arrow-down"></div>
          </div>
        </div>
      </div>
      <!--      <table>
              <thead>
              <tr>
                <th scope="col">Название услуги</th>
                <th scope="col">Принят в обработку</th>
                <th scope="col">Выполенен</th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="order in orders" v-bind:key="order.id">
                <th>{{ order.service.title }}</th>
                <th v-if="order.is_accepted">ABOBA</th>
                <th v-else>dayn</th>
                <th v-if="order.is_completed"></th>
                <th v-else>aboba</th>
              </tr>
              </tbody>
            </table>-->
    </div>
    <div v-else-if="!$store.state.isAuthenticated" class="authentication-error">
      <div class="message">
        Вы не авторизованы
      </div>
      <my-button @click="openLogin" class="btn">Авторизоваться</my-button>
    </div>
    <my-dialog v-model:show="$store.state.changeNameVisible">
      <my-name-form :name="user.first_name"></my-name-form>
    </my-dialog>
  </div>
</template>

<script>
import axios from "axios";
import MyDialog from "@/components/MyDialog";
import MyNameForm from "@/components/MyNameForm";

export default {
  name: "Profile",
  components: {
    MyDialog,
    MyNameForm
  },

  data() {
    return {
      orders: [],
      user: [],
      user_id: '',
    }
  },
  mounted() {
    this.getOrders()
    document.title = 'Профиль | Kseniia Zi'
  },
  methods: {
    openLogin() {
      this.$store.commit('changeLoginVisible')
    },
    changeName() {
      this.$store.commit('changeNameVisible')
    },
    getOrders() {
      this.$store.commit('changeLoaderVisible')

      axios.defaults.headers.common['Authorization'] = 'Token ' + localStorage.getItem('token')

      setTimeout(async () => {
        await axios
            .get(`api/auth/users/me`)
            .then(response => {
              this.user_id = response.data.id
            }).catch(error => {
              console.log(error)
            })

        axios
            .get(`api/users/${this.user_id}`)
            .then(response => {
              this.orders = response.data.orders
              this.user = response.data
            }).catch(error => {
          console.log(error)
        }).finally(onFinally => {
          this.$store.commit('changeLoaderVisible')
        })
      }, 500)
    },
  }
}
</script>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@300;400;500;600;700&display=swap');

.profile {
  background-color: white;
  background-image: url("https://www.transparenttextures.com/patterns/concrete-wall-2.png");
  background-size: auto;
  height: 100vh;
  padding-block: 10vh;
  padding-inline: 10vw;
}

.profile-content {
  display: flex;
  flex-flow: column;
}

.profile-title {
  font-family: 'Cormorant SC', serif;
  font-size: 32px;
}

.profile-info {
  padding: 30px;
}

.profile-name {
  display: flex;
  font-family: 'Cormorant SC', serif;
  font-size: 20px;
}

.name {
  padding-inline: 15px;
}

img {
  margin-top: 3px;
  max-width: 16px;
  max-height: 16px;
  cursor: pointer;
}

.order-title {
  font-family: 'Cormorant SC', serif;
  font-size: 32px;
}

.order-list {
  font-family: 'Cormorant SC', serif;
  margin-top: 2rem;
  display: flex;
  flex-flow: column;
  gap: 2rem;
}

.order {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 3rem;
  color: white;
  background-color: black;
  border-radius: 10px;
  padding-inline: 2rem;
  cursor: pointer;
}

.arrow-down {
  border: solid white;
  border-width: 0 3px 3px 0;
  display: inline-block;
  padding: 3px;
  transform: rotate(45deg);
  -webkit-transform: rotate(45deg);
}

table {
  border: 1px solid gray;
  border-radius: 15px;
  margin-top: 30px;
  table-layout: fixed;
}

th, td {
  font-family: 'Cormorant SC', serif;
  text-align: start;
  padding: 20px;
}

thead th {
  font-size: 20px;
  font-family: 'Cormorant SC', serif;
}

.authentication-error {
  display: inline-block;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.message {
  font-family: 'Cormorant SC', serif;
  font-size: 64px;
}

.btn {
  margin-top: 1rem;
  font-family: 'Cormorant SC', serif;
  background-color: black;
}

.btn:hover {
  color: black;
  background-color: rgb(239, 180, 78);
}
</style>