import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import components from '@/components/UI'
import loader from "vue-ui-preloader";
import Notifications from '@kyvg/vue3-notification'


axios.defaults.baseURL = 'http://127.0.0.1:8000/'

const app = createApp(App)

components.forEach(component => {
    app.component(component.name, component)
})


app.use(store).use(router, axios).use(loader).use(Notifications).mount('#app')

