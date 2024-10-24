<template>
    <v-list class="pa-0">
        <v-list-item
            v-if="!rail"
            class="text-caption font-weight-bold text-truncate"
        >
            <v-tooltip>
                <template v-slot:activator="{ props }">
                    <v-icon
                        icon="mdi-information"
                        color="cyan-darken-3"
                        size="12"
                        class="cursor-help"
                        v-bind="props"
                    />
                </template>
                <span class="text-caption ">
                    Информация о странице: <br/>
                    {{router.currentRoute.value.meta.title}} <br/>
                    с {{formatComa(appStore.countvisitor.visitdate)}}
                </span>
            </v-tooltip>
            <p class="cursor-default">Посещений всего: {{ appStore.countvisitor.totalvisit }}</p>
            <v-divider />
            <p class="cursor-default">Посещений сегодня: {{ appStore.countvisitor.visittoday }}</p>
            <v-divider />
            <p class="cursor-default">Из них уникальных: {{ appStore.countvisitor.uniqtoday }}</p>
            <v-divider />
        </v-list-item>
        <v-list-item v-else class="align-center">
            <v-tooltip 
                v-model="showTooltip" 
                location="top"
            >
                <template v-slot:activator="{ props }">
                    <v-icon
                        v-bind="props"
                        color="grey"
                    >
                        mdi-account-eye
                    </v-icon>
                </template>
                <p>Посещений всего: {{ appStore.countvisitor.totalvisit }}</p>
                <v-divider />
                <p>Посещений сегодня: {{ appStore.countvisitor.visittoday }}</p>
                <v-divider />
                <p>Из них уникальных: {{ appStore.countvisitor.uniqtoday }}</p>
            </v-tooltip>
        </v-list-item>
    </v-list>
</template>

<script>
import { formatComa } from '@/utils/universal_functions'
import { useRouter } from 'vue-router'
import { useAppStore } from '@/store/app'
import { ref } from 'vue'

export default {
    name: "PageCounter",
    
    props: {
        rail: {
            type: Boolean,
            default: false
        }
    },

    setup() {
        const router = useRouter()
        const appStore = useAppStore()
        const showTooltip = ref(false)

        return {
            router,
            appStore,
            showTooltip,
            formatComa
        }
    }
}
</script>

<style>

</style>