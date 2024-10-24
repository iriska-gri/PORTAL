/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

// Plugins
import { registerPlugins } from '@/plugins'
import components from '@/components/UI/index'


import Vue3Autocounter from 'vue3-autocounter'


const app = createApp(App)

components.forEach((component) => {

    app.component(component.name, component);
  })

app.component('vue3-autocounter', Vue3Autocounter)



// Vue.use(VueScrollTo)

registerPlugins(app)

app.mount('#app')


