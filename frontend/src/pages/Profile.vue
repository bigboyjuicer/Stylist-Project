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

        <div class="tablinks">
          <div id="OrderTab" class="order-title order-title-active" @click="openTab('OrderTab', 'ChatTab','Orders')">
            Ваши заказы
          </div>
          <div v-if="chats.length > 0" id="ChatTab" class="order-title" @click="openTab('ChatTab', 'OrderTab', 'Chat')">
            Чаты
          </div>
          <div v-else class="order-title" id="ChatTab" @click="openTab('ChatTab', 'OrderTab', 'Chat')">
            Чат со стилистом
          </div>
        </div>

        <div id="Chat" class="tabcontent">
          <div v-if="chats.length > 0">
            <div class="chat">
              <div class="chat-groups">
                <div class="chat-groups-body">
                  <div v-for="(chat, index) in chats" v-bind:key="chat.id">
                    <div @click="openChat(chat.messages, chat.id, index)" class="chat-groups-body-chat">
                      {{ chat.user.email }}
                    </div>
                  </div>
                </div>
              </div>
              <div class="chat-box">
                <div class="chat-box-body">
                  <div style="display: flex; flex-direction: column" v-for="message in messages"
                       v-bind:key="message.id">
                    <div class="chat-box-body-message-right" v-if="message.user === this.user_id">
                      {{ message.text }}
                    </div>
                    <div class="chat-box-body-message-left" v-else>
                      {{ message.text }}
                    </div>
                  </div>
                </div>
                <div class="chat-box-bottom">
                  <my-input class="chat-box-bottom-input" v-on:keydown.enter="sendMessage(2)" v-model="text" type="text"
                            placeholder="Введите сообщение"
                            style="background: white"></my-input>
                  <svg @click="sendMessage" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"
                       class="chat-box-bottom-send-btn">
                    <path d="M18.86 57.47l25.26-26.63L18.86 6.58"></path>
                  </svg>
                </div>
              </div>
            </div>
          </div>
          <div v-else>
            <div class="chat">
              <div class="chat-box">
                <div class="chat-box-body">
                  <div style="display: flex; flex-direction: column" v-for="message in messages"
                       v-bind:key="message.id">
                    <div class="chat-box-body-message-right" v-if="message.user === this.user_id">
                      {{ message.text }}
                    </div>
                    <div class="chat-box-body-message-left" v-else>
                      {{ message.text }}
                    </div>
                  </div>
                </div>
                <div class="chat-box-bottom">
                  <my-input class="chat-box-bottom-input" v-on:keydown.enter="sendMessage" v-model="text" type="text"
                            placeholder="Введите сообщение"
                            style="background: white"></my-input>
                  <svg @click="sendMessage" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"
                       class="chat-box-bottom-send-btn">
                    <path d="M18.86 57.47l25.26-26.63L18.86 6.58"></path>
                  </svg>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div id="Orders" class="order-list tabcontent">
          <div class="order" v-for="(order, index) in orders" v-bind:key="order.id">
            <div @click="openCollapsible(index)" class="order-header">
              <div class="service-title">{{ order.service.title }}</div>
              <svg class="collapse-btn" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
                <path d="M6.53 18.86l26.63 25.26 24.26-25.26"></path>
              </svg>
            </div>
            <div class="order-body">
              <div class="order-info">
                <div class="order-status">
                  Состояние заказа:
                  <div style="display: inline-block; margin-left: 8px; font-weight: bold"
                       v-if="!order.is_accepted && !order.is_completed">Не принят
                  </div>
                  <div style="display: inline-block; margin-left: 8px; font-weight: bold" v-else>
                    {{ order.is_completed ? "Выполнен" : order.is_accepted ? "Принят" : "Не принят" }}
                  </div>
                </div>
                <div class="order-comment">
                  Ваш комментарий:
                  <div style="display: inline-block; margin-left: 8px; font-weight: bold"> {{ order.comment }}</div>
                </div>
              </div>
              <div class="decline-btn">
                <my-button @click="openDecline(order.id)" class="delete-btn">Отменить заказ</my-button>
              </div>
            </div>
          </div>
        </div>
        <div v-if="orders.length > 0" class="review">
          <my-button v-if="this.review.id" class="review-btn" @click="makeReview">Изменить отзыв</my-button>
          <my-button v-else class="review-btn" @click="makeReview">Оставить отзыв</my-button>
        </div>
        <div class="delete-profile">
          <my-button class="delete-btn" @click="deleteProfile">Удалить профиль</my-button>
        </div>
      </div>
    </div>
    <div v-else-if="!$store.state.isAuthenticated" class="authentication-error">
      <div class="message">
        Вы не авторизованы
      </div>
      <my-button @click="openLogin" class="btn">Авторизоваться</my-button>
    </div>
    <my-dialog v-model:show="$store.state.changeNameVisible">
      <my-name-form :name="user.first_name" :chat="user.chat"></my-name-form>
    </my-dialog>
    <my-dialog v-model:show="$store.state.makeReviewVisible">
      <my-review-form :user="user" :review="review"></my-review-form>
    </my-dialog>
    <my-dialog v-model:show="$store.state.deleteProfileVisible">
      <my-delete-profile-form></my-delete-profile-form>
    </my-dialog>
    <my-dialog v-model:show="$store.state.declineVisible">
      <my-decline-form v-model:orderId="chosenOrder"></my-decline-form>
    </my-dialog>
  </div>
</template>

<script>
import axios from "axios";
import MyDialog from "@/components/MyDialog";
import MyNameForm from "@/components/MyNameForm";
import MyDeleteProfileForm from "@/components/MyDeleteProfileForm";
import MyDeclineForm from "@/components/MyDeclineForm";
import Pusher from 'pusher-js';
import MyReviewForm from "@/components/MyReviewForm";

export default {
  name: "Profile",
  components: {
    MyReviewForm,
    MyDialog,
    MyNameForm,
    MyDeleteProfileForm,
    MyDeclineForm,
  },
  data() {
    return {
      orders: [],
      user: [],
      user_id: '',
      chosenOrder: -1,
      chatId: 0,
      messages: [],
      text: '',
      chats: [],
      review: [],
    }
  },
  async mounted() {

    await this.getOrders()

    document.title = 'Профиль | Kseniia Zi'

    Pusher.logToConsole = true;

    const pusher = new Pusher('228b0dbd0877933623f4', {
      cluster: 'eu'
    });

    const channel = pusher.subscribe('chat');
    channel.bind('message', data => {
      this.messages.push(data);
    });

    document.querySelector('.chat-box-body')?.scrollTo(0, document.querySelector('.chat-box-body').scrollHeight)
  },
  methods: {
    openChat(messages, chatId, elId) {

      const chatGroups = document.getElementsByClassName("chat-groups-body-chat")

      for (let i = 0; i < chatGroups.length; i++) {
        if (document.getElementsByClassName("chat-groups-body-chat")[i].classList.contains("chat-groups-body-chat-active")) {
          document.getElementsByClassName("chat-groups-body-chat")[i].classList.toggle("chat-groups-body-chat-active")
        }
      }

      document.getElementsByClassName("chat-groups-body-chat")[elId].classList.toggle("chat-groups-body-chat-active")
      this.messages = messages
      this.chatId = chatId

      document.querySelector('.chat-box-body')?.scrollTo(0, document.querySelector('.chat-box-body').scrollHeight)
    },
    sendMessage() {
      axios.defaults.headers.common['Authorization'] = 'Token ' + localStorage.getItem('token')

      if (this.text !== '') {
        const formData = {
          text: this.text,
          user: this.user_id,
          chat: this.chatId
        }

        axios
            .post(`api/message/`, formData)
            .then(response => {
              this.text = ''
            }).catch(error => {
          console.log(error)
        })
      }

    },
    openCollapsible(id) {
      document.getElementsByClassName("collapse-btn")[id].classList.toggle("collapse-btn-active");
      if (document.getElementsByClassName("order-body")[id].style.maxHeight) {
        document.getElementsByClassName("order-body")[id].style.maxHeight = null;
      } else {
        document.getElementsByClassName("order-body")[id].style.maxHeight = document.getElementsByClassName("order-body")[id].scrollHeight + "px";
      }
    },
    openTab(tabClass, otherTabClass, tabName) {

      let tabcontent = document.getElementsByClassName("tabcontent")
      for (let i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none"
      }

      document.getElementById(tabClass).classList.toggle("order-title-active")
      document.getElementById(otherTabClass).classList.toggle("order-title-active")


      document.getElementById(tabName).style.display = "flex"
      document.querySelector('.chat-box-body')?.scrollTo(0, document.querySelector('.chat-box-body').scrollHeight)
    },
    openDecline(id) {
      this.chosenOrder = id
      this.$store.commit("changeDeclineVisible")
    },
    openLogin() {
      this.$store.commit('changeLoginVisible')
    },
    changeName() {
      this.$store.commit('changeNameVisible')
    },
    deleteProfile() {
      this.$store.commit('changeDeleteProfileVisible')
    },
    makeReview() {
      this.$store.commit('changeMakeReviewVisible')
    },
    async getOrders() {
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

        await axios
            .get(`api/users/${this.user_id}`)
            .then(response => {
              this.orders = response.data.orders
              this.user = response.data
              this.chatId = response.data.chat
            }).catch(error => {
              console.log(error)
            })

        await axios.get('api/make-review/').then(response => {
          for(let i = 0; i < response.data.length; i++) {
            if(response.data[i].user === this.user_id){
              this.review = response.data[i]
            }
          }
        })

        await axios
            .get(`api/chat/`)
            .then(response => {
              this.chats = response.data
            }).catch(error => {
          axios
              .get(`api/chat/${this.chatId}`)
              .then(response => {
                this.messages = response.data.messages
              }).catch(error => {

            console.log(error)
          })
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

.tablinks {
  display: flex;
  gap: 32px;
}

.order-title {
  cursor: pointer;
  font-family: 'Cormorant SC', serif;
  font-size: 32px;
}

.order-title-active {
  text-decoration: underline;
}

.tabcontent {
  margin-top: 32px;
  display: none;
  animation: fadeEffect 1s; /* Fading effect takes 1 second */
}

/* Go from zero to full opacity */
@keyframes fadeEffect {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.order-list {
  font-family: 'Cormorant SC', serif;
  margin-top: 2rem;
  display: flex;
  flex-flow: column;
  gap: 2rem;
}

.order {
  padding: 16px 32px;
  display: flex;
  flex-direction: column;
  color: white;
  background-color: black;
  border-radius: 10px;
}

.order-header {
  font-size: 20px;
  font-weight: bold;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.collapse-btn {
  width: 24px;
  height: 24px;
  stroke: white;
  stroke-width: 4;
  transition: transform 300ms;
}

.collapse-btn-active {
  transform: rotate(90deg);
}

.order-body {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  overflow: hidden;
  max-height: 0;
  transition: max-height 300ms;
}

.order-info {
  display: flex;
  gap: 32px;
}

.order-status {
  margin-top: 32px;
  margin-bottom: 16px;
}

.order-comment {
  margin-top: 32px;
  margin-bottom: 16px;
}

.decline-btn {
  margin-top: 16px;
}

.arrow-down {
  border: solid white;
  border-width: 0 3px 3px 0;
  display: inline-block;
  padding: 3px;
  transform: rotate(45deg);
  -webkit-transform: rotate(45deg);
}

.review {
  margin-top: 4rem;
  margin-bottom: 4rem;
  max-width: max-content;
}

.review-btn {
  display: inline-block;
  padding: 0.5rem;
  font-family: 'Cormorant SC', serif;
  font-size: 16px;
  margin-top: 0;
  color: black;
  background-color: rgb(239, 180, 78);
  box-shadow: 0px 5px 10px 2px rgba(0, 0, 0, 0.3);
}

.delete-profile {
  margin-top: 4rem;
  margin-bottom: 4rem;
  max-width: max-content;
}

.delete-btn {
  display: inline-block;
  padding: 0.5rem;
  font-family: 'Cormorant SC', serif;
  font-size: 16px;
  margin-top: 0;
  background-color: red;
  box-shadow: 0px 5px 10px 2px rgba(0, 0, 0, 0.3);
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

.chat {
  font-family: 'Cormorant SC', serif;
  display: flex;
  justify-content: center;
}

.chat-box {
  width: 384px;
  height: 640px;
  background-color: black;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
}

.chat-box-body {
  overflow: auto;
  border-radius: 6px;
  margin: 8px;
  padding: 16px;
  flex: 14;
  background-color: white;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.chat-box-body-message-left {
  white-space: pre-line;
  max-width: 70%;
  word-wrap: break-word;
  color: white;
  background: black;
  display: inline-block;
  padding: 8px 16px;
  border-radius: 12px 16px 16px 12px;
  align-self: start;
}

.chat-box-body-message-right {
  white-space: pre-line;
  max-width: 70%;
  word-wrap: break-word;
  color: black;
  background: rgb(239, 180, 78);
  display: inline-block;
  padding: 8px 16px;
  border-radius: 16px 12px 12px 16px;
  align-self: end;
}

.chat-box-bottom {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 8px;
  padding-inline: 8px;
  padding-bottom: 8px;
}

.chat-box-bottom-input {
  margin: 0;
  color: black;
  padding: 8px;
  font-size: 16px;
  font-weight: bold;
  background: lightgray;
  border-radius: 6px;
  border: none;
  width: 100%;
}

.chat-box-bottom-send-btn {
  width: 32px;
  height: 32px;
  stroke: lightgray;
  stroke-width: 2.5;
  transition: stroke-width 50ms;
}

.chat-box-bottom-send-btn:hover {
  stroke: rgb(239, 180, 78);
  stroke-width: 5;
}

.chat-box-bottom-input:focus {
  outline: none;
  box-shadow: 0 0 0 2px rgb(239, 180, 78);
}

.chat-groups {
  border-radius: 12px;
  width: 200px;
  background: black;
  margin-right: -20px;
  display: flex;
}

.chat-groups-body {
  overflow: auto;
  display: flex;
  flex-direction: column;
  gap: 8px;
  width: 100%;
  margin: 8px 20px 8px 8px;
  padding: 8px 4px;
  border-radius: 12px;
}

.chat-groups-body-chat {
  cursor: pointer;
  font-size: 14px;
  border-radius: 12px;
  width: 100%;
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  background: #181818FF;
}

.chat-groups-body-chat:hover {
  background: #262626FF;
}

.chat-groups-body-chat-active {
  color: black;
  background: rgb(239, 180, 78);
}

.chat-groups-body-chat-active:hover {
  background: #8F6E2EFF;
}
</style>