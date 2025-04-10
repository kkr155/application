import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import Live2D from './App.vue'
import router from './router'

const app = createApp(Live2D)

app.use(createPinia())
app.use(router)

app.mount('#app')
