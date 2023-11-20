import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import App from './App.vue'
import router from './router'
// import 'bootstrap'
// import 'bootstrap/dist/css/bootstrap.min.css'
 
// createApp(App).mount('#app')







const app = createApp(App)
const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)


// app.use(createPinia())

app.use(router)
app.use(pinia)

app.mount('#app')
