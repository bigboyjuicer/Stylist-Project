import { createStore } from 'vuex'

export default createStore({
  state: {
    isAuthenticated: false,
    token: '',
    user_id: '',
    email: '',
    loginVisible: false,
    registrationVisible: false,
    changeNameVisible: false,
    loaderVisible: false,
    orderVisible: false,
  },
  getters: {
  },
  mutations: {
    setToken(state, token){
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state){
      state.token = ''
      state.isAuthenticated = false
    },
    setUserId(state, user_id){
      state.user_id = user_id
    },
    removeUserId(state){
      state.user_id = null
    },
    setEmail(state, email){
      state.email = email
    },
    removeEmail(state){
      state.email = ''
    },
    changeLoginVisible(state){
      state.loginVisible = !state.loginVisible
    },
    changeRegistrationVisible(state){
      state.registrationVisible = !state.registrationVisible
    },
    changeNameVisible(state){
      state.changeNameVisible = !state.changeNameVisible
    },
    changeLoaderVisible(state){
      state.loaderVisible = !state.loaderVisible
    },
    changeOrderVisible(state){
      state.orderVisible = !state.orderVisible
    }
  },
  actions: {
  },
  modules: {
  }
})
