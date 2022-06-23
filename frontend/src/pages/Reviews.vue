<template>
  <div class="reviews">
    <div class="title">Отзывы</div>
    <div class="reviews-list">
      <div style="display: flex; flex-direction: column" v-for="(review, index) in reviews" v-bind:key="review.id">
        <div v-if="(index + 1) % 2 !== 0" class="review-left">
          <div v-if="review.user.first_name" class="reviewer-name">{{ review.user.first_name }}</div>
          <div v-else class="reviewer-name">Аноним</div>
          <div class="review-description">{{ review.content }}</div>
          <div class="review-date">{{ getTime(review.created) }}</div>
        </div>
        <div v-else class="review-right">
          <div v-if="review.user.first_name" class="reviewer-name">{{ review.user.first_name }}</div>
          <div v-else class="reviewer-name">Аноним</div>
          <div class="review-description">{{ review.content }}</div>
          <div class="review-date">{{ getTime(review.created) }}</div>
        </div>
      </div>
      <div class="reviews-list-divider"></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import moment from 'moment'

export default {
  name: "Reviews",
  data() {
    return {
      reviews: [],
    }
  },
  mounted() {
    this.getReviews()
    document.title = 'Отзывы | Kseniia Zi'
  },
  methods: {
    getReviews() {
      this.$store.commit('changeLoaderVisible')

      setTimeout(async () => {
        axios.get('api/review/').then(response => {
          this.reviews = response.data
        }).catch(error => {
          console.log(error)
        }).finally(onFinally => {
          this.$store.commit('changeLoaderVisible')
        })
      }, 500)
    },
    getTime(time) {
      moment.locale("ru")

      return moment(time).format('DD MMMM YYYY')
    }
  }

}
</script>

<style scoped>
.reviews {
  background-color: white;
  height: 100vh;
}

.title {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  padding-block: 10vh 0;
  font-size: 52px;
  font-family: 'Cormorant SC', serif;
}

.reviews-list {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 32px;
  margin: 10vh 20vw;
}

.reviews-list-divider {
  position: absolute;
  left: 50%;
  right: 50%;
  height: 100%;
  width: 1px;
  border-left: 1px solid lightgray;
}

.review-left {
  position: relative;
  display: flex;
  flex-flow: column;
  gap: 16px;
  height: max-content;
  width: 400px;
  background: rgba(239, 180, 78, 0.7);
  border-radius: 15px;
  padding: 15px;
  box-shadow: 0px 100px 80px rgba(0, 0, 0, 0.07), 0px 41.7776px 33.4221px rgba(0, 0, 0, 0.0503198), 0px 22.3363px 17.869px rgba(0, 0, 0, 0.0417275), 0px 12.5216px 10.0172px rgba(0, 0, 0, 0.035), 0px 6.6501px 5.32008px rgba(0, 0, 0, 0.0282725), 0px 2.76726px 2.21381px rgba(0, 0, 0, 0.0196802);
}

.review-right {
  align-self: flex-end;
  position: relative;
  display: flex;
  flex-flow: column;
  gap: 16px;
  height: max-content;
  width: 400px;
  background: rgba(239, 180, 78, 0.7);
  border-radius: 15px;
  padding: 15px;
  border: 1px solid rgba(39, 36, 32, 0.1);
  box-shadow: 0px 100px 80px rgba(0, 0, 0, 0.07), 0px 41.7776px 33.4221px rgba(0, 0, 0, 0.0503198), 0px 22.3363px 17.869px rgba(0, 0, 0, 0.0417275), 0px 12.5216px 10.0172px rgba(0, 0, 0, 0.035), 0px 6.6501px 5.32008px rgba(0, 0, 0, 0.0282725), 0px 2.76726px 2.21381px rgba(0, 0, 0, 0.0196802);
}

.reviewer-name {
  font-family: 'Cormorant SC', serif;
  font-size: 24px;
  font-weight: bold;
}

.review-description {
  max-width: 400px;
  font-size: 20px;
  font-family: 'Cormorant SC', serif;
  white-space: pre-line;
}

.review-date {
  position: absolute;
  right: 15px;
  top: 15px;
  font-size: 14px;
  font-family: 'Cormorant SC', serif;
}


</style>