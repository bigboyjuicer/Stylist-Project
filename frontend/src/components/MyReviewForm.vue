<template>
  <div class="review-form">
    <h3>Оставьте свой отзыв</h3>
    <my-input v-model="user.first_name" type="text" placeholder="Имя"></my-input>
    <textarea v-model="this.review.content" rows="5" placeholder="Отзыв"></textarea>
    <div class="buttons">
      <my-button class="yes-btn" @click="makeReview">Отправить</my-button>
      <my-button class="no-btn" @click="$store.commit('changeMakeReviewVisible')">Отменить</my-button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import store from "@/store";

export default {
  name: "MyReviewForm",
  components: {},
  props: {
    user: {
      type: [],
    },
    review: {
      type: [],
    }
  },
  data() {
    return {}
  },
  methods: {
    makeReview() {

      axios.defaults.headers.common['Authorization'] = 'Token ' + this.$store.state.token

      if (this.user.first_name) {
        const nameData = {
          email: this.$store.state.email,
          first_name: this.user.first_name,
          chat: this.user.chat
        }

        axios.put(`api/users/${this.$store.state.user_id}`, nameData).catch(error => {
          console.log(error)
        })
      }

      const reviewData = {
        content: this.review.content,
        user: this.user.id
      }

      axios.put(`api/make-review/${this.review.id}/`, reviewData).then(response => {
        this.$store.commit('changeMakeReviewVisible')

        this.$notify({
          group: "app",
          type: "success",
          duration: 500,
          title: "Отзыв успешно изменен",
        });

        this.$router.go()
      }).catch(error => {
        axios.post(`api/make-review/`, reviewData).then(response => {
          this.$store.commit('changeMakeReviewVisible')

          this.$notify({
            group: "app",
            type: "success",
            duration: 500,
            title: "Отзыв успешно отправлен",
          });

          this.$router.go()
        }).catch(error => {

          this.$notify({
            group: "app",
            type: "error",
            duration: 500,
            title: "Ошибка",
          });
          console.log(error)
        })
      })
    }
  }
}
</script>

<style scoped>
.review-form {
  height: 25rem;
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

.review-form * {
  font-family: 'Cormorant SC', serif;
  color: #ffffff;
  letter-spacing: 0.5px;
  outline: none;
  border: none;
}

.review-form h3 {
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
  color: black;
  background-color: rgb(239, 180, 78);
}

.no-btn:hover {
  color: white;
  background-color: red;
}

</style>