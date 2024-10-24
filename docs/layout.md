### Шаблон страницы

Пример использования верстки

```
    <v-row no-gutters class="gap flex-column">
        <v-col lg=2 class='bg-red w100'>
            1
        </v-col>
        <v-col class="d-flex flex-column">
            <v-row no-gutters class="gap">
                <v-col lg=9 class="d-flex flex-column">
                    <v-row no-gutters class="gap flex-column">
                        <v-col class=" d-flex flex-column">
                            <v-row no-gutters class="gap">
                                <v-col class="bg-green">1</v-col>
                                <v-col class="bg-orange">2</v-col>
                            </v-row>
                        </v-col>
                        <v-col class=" d-flex flex-column">
                            <v-row no-gutters class="gap">
                                <v-col class="bg-purple">1</v-col>
                                <v-col class="bg-green">2</v-col>
                            </v-row>
                        </v-col>
                    </v-row>
                </v-col>
                <v-col  class="bg-yellow">2</v-col>
            </v-row>
        </v-col>
        <v-col lg=2 class="bg-grey w100">
            3
        </v-col>
    </v-row>
```