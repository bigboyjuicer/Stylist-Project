<template>
  <div class="services">
    <div class="title">Выберите подходящую услугу</div>
    <div class="services-content">
      <div class="service-list">
        <div class="service" v-for="service in services" v-bind:key="service.id">
          <div class="service-title">{{ service.title }}</div>
          <div class="service-description">{{ service.description }}</div>
          <div class="checkout-button" @click="makeOrder(service.id, service.title)">Сделать заказ</div>
        </div>
      </div>
    </div>
  </div>
  <my-dialog v-model:show="$store.state.orderVisible">
    <my-order-form :service="chosen_service" :title="service_title"></my-order-form>
  </my-dialog>
</template>

<script>
import axios from 'axios'
import MyDialog from "@/components/MyDialog";
import MyOrderForm from "@/components/MyOrderForm";

export default {
  name: "Services",
  components: {
    MyDialog,
    MyOrderForm
  },
  data() {
    return {
      services: [],
      chosen_service: null,
      service_title: '',
    }
  },
  mounted() {
    this.getService()
    document.title = 'Услуги | Kseniia Zi'
  },
  methods: {
    makeOrder(service, title) {
      this.chosen_service = service
      this.service_title = title
      this.$store.commit('changeOrderVisible')
    },

    getService() {
      this.$store.commit('changeLoaderVisible')

      axios.defaults.headers.common['Authorization'] = ''

      setTimeout(async () => {
        axios
            .get('/api/service/')
            .then(response => {
              this.services = response.data
            })
            .catch(error => {
              console.log(error)
            }).finally(onFinally => {
          this.$store.commit('changeLoaderVisible')
        })
      }, 500)
    }
  }
}
</script>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@300;400;500;600;700&display=swap');

.services {
  background-color: #EBEBEB;
  height: 250vh;
}

.services-content {
  padding-block: 15vh;
  height: max-content;
}

.title {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  padding-block: 10vh 0;
  font-size: 52px;
  font-family: 'Cormorant SC', serif;
}

.service-list {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 15vh;
  justify-items: center;
  margin-inline: 10vw;
}

.service {
  display: flex;
  flex-flow: column;
  height: max-content;
  width: max-content;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 15px;
  padding: 15px;
  box-shadow: 0 0 10px 10px rgba(0, 0, 0, 0.2);
}

.service-title {
  text-align: center;
  margin-block: 30px 30px;
  margin-inline: 30px;
  font-size: 36px;
  font-family: 'Cormorant SC', serif;
  font-weight: 500;
  white-space: nowrap;
}

.service-description {
  text-align: center;
  font-size: 20px;
  font-family: 'Cormorant SC', serif;
  white-space: pre-line;
}

.checkout-button {
  padding: 5px 10px;
  margin-inline: auto;
  margin-block: 30px 15px;
  border: 0;
  text-align: center;
  background: #707070;
  border-radius: 15px;
  color: white;
  cursor: pointer;
  font-size: 20px;
  font-family: 'Cormorant SC', serif;
}

.checkout-button:hover {
  background-color: black;
}
</style>