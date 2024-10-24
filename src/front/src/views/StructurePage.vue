<template>
    <v-row>
        <v-col 
            class="text-h6 text-grey text-center align-self-center text--lighten-1 font-weight-light"
        >
            Структура
        </v-col>
        
    </v-row>
    <!-- <div>
        <a href="#" v-scroll-to="'#element'">Scroll to #element</a>

<div ref="element">
  Hi. I'm #element.
</div>
    </div> -->

</template>

<script>
import {pagecounter} from '@/utils/universal_functions'
export default {
setup(){
    pagecounter()
}
}

</script>

<style>

</style>