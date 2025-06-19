import './assets/main.css'
// import './assets/style/main.scss'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import Application from './App.vue'
import router from './router'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

const app = createApp(Application)

// app.prototype.$axios = axios
app.use(ElementPlus)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}
app.use(createPinia())
app.use(router)

app.mount('#app')
