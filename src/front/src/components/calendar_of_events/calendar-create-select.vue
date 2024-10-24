<template>
  <!--  -->
  <v-autocomplete
    v-model="selectedStaff"
    :items="staffed"
    label="Выберите из списка или найдите по ФИО"
    item-title="title"
    item-value="id"
    :custom-filter="onFilter"
    @update:search="(val) => (filtered = val)"
    multiple
    hide-details
    variant="outlined"
    density="compact"
    class="max-height-select py-3"
    return-object
  >
    <template v-slot:selection="{ item }">
      <v-chip
      class="me-2"
          color="teal-darken-3"
          size="small"
          label>
        <span> {{ item.title }}</span>
        <v-icon
          v-if="item.value != accountStore.user.is_idEmployee"
          icon="mdi-close-circle"
          size="x-small"
          class="ml-3"
          @click.stop="selectedStaff = item.raw"
        />
      </v-chip>
    </template>
    <template v-slot:prepend-item>
      <v-list-item
        @click.stop="allUser()"
        :disabled="staffed.length == 1 && staffed[0].employees.length == 1"
        class="text-body-2"
      >
        <span class="text-body-2"> ВСЕ СОТРУДНИКИ </span>

        <template v-slot:prepend>
          <v-checkbox-btn
            :model-value="staffed.every((e) => e[okey] == true)"
            :disabled="staffed.length == 1 && staffed[0].employees.length == 1"
          ></v-checkbox-btn>
        </template>
      </v-list-item>

      <v-divider class="mt-2"></v-divider>
    </template>

    <template v-slot:item="{ props, item }">
      <v-list-group v-bind="props" :value="item.raw.title">
        <template v-slot:activator="{ props }">
          <v-list-item
            v-bind="props"
            @click.stop=""
            density="compact"
            class="text-body-2"
          >
            <template v-slot:prepend>
              <v-checkbox-btn
                @click.stop="selectedStaff = item.raw"
                :color="'indigo-darken-4'"
                :true-value="true"
                :false-value="false"
                :disabled="disable(item.raw)"
                :indeterminate="
                  item.raw.employees.some((e) => e[okey] == true) &&
                  !item.raw.employees.every((e) => e[okey] == true)
                "
                :model-value="item.raw[okey]"
              ></v-checkbox-btn>
            </template>
          </v-list-item>
        </template>

        <v-list-item
          v-for="x in item.raw.employees.filter((e) =>
            e.title.toLowerCase().includes(filtered.toLowerCase())
          )"
          :key="x.id"
          :value="x.title"
          :disabled="x.id == accountStore.user.is_idEmployee"
          @click.stop="selectedStaff = x"
          density="compact"
        >
          <template v-slot:prepend>
            <v-checkbox-btn
              :disabled="x.id == accountStore.user.is_idEmployee"
              color="indigo-darken-4"
              :model-value="x[okey]"
            ></v-checkbox-btn>
          </template>
          <span class="text-body-2"> {{ x.title }} </span>
        </v-list-item>
      </v-list-group>
    </template>
  </v-autocomplete>
</template>

<script>
import { ref, computed } from "vue";
import { splitname } from "@/utils/universal_functions";
import { useAccountStore } from "@/store/AccountStore";

export default {
  props: {
    staff: {
      type: Array,
      default: () => [],
    },
    okey: {
      type: String,
      default: "selected",
    },
  },

  setup(props, { emit }) {
    const filtered = ref("");
    const accountStore = useAccountStore();
    const back = ref([]);

    const staffed = computed({
      get() {
        if (props.okey == "editor") {
          let ns = [];
          props.staff.forEach((e) => {
            let emp = { ...e };
            emp.employees = e.employees.filter((n) => n.selected == true);
            if (emp.employees.length > 0) ns.push(emp);
          });

          ns.forEach((e) => {
            if (e.employees.every((w) => w.editor == true)) {
              e.editor = true;
            }
          });
          return ns;
        }
        return props.staff;
      },
    });

    const selectedStaff = computed({
      get() {
        let selected = [];
        props.staff.forEach((e) => {
          if (
            e.employees.length != 1 &&
            e.employees.every((n) => n[props.okey] == true)
          ) {
            e[props.okey] = true;
            selected.push(e);
          } else if (e.employees.length == 1) {
            e[props.okey] = true;
            selected.push(...e.employees.filter((n) => n[props.okey] == true));
          } else {
            e[props.okey] = false;
            selected.push(...e.employees.filter((n) => n[props.okey] == true));
          }
        });
        return selected;
      },

      set(item) {
        // Если нажимать на пользователя с disable, то срабатывает
        // set и отправляет данные которые не нужны, но выдает только в виде массива.
        // Остальные данные передаются объектом, кроме выбора ВСЕХ ПОЛЬЗОВАТЕЛЕЙ, для него написан отдельный клик на обработку
        // Таким образом предотсвращаем клик на автокомплид (хз понятно или нет)
        if (!Array.isArray(item)) {
          emitUp(item);
        }
      },
    });

    const emitUp = (part) => {
      if ("employees" in part) {
        part.employees.forEach((e) => {
          if (e.id != accountStore.user.is_idEmployee) {
            e[props.okey] = !part[props.okey];
          }
        });
        emit("returnIdParticant", {
          okey: props.okey,
          staff: part.employees,
          select: [],
        });
      } else if (part.length) {
        if (part[0].id != accountStore.user.is_idEmployee) {
          let val = part.every((e) => e[props.okey] == true) ? false : true;
          cbstaff(part, val);
          emit("returnIdParticant", {
            okey: props.okey,
            staff: back.value,
            select: [],
          });
          back.value = [];
        }
      } else {
        part[props.okey] = !part[props.okey];
        emit("returnIdParticant", {
          okey: props.okey,
          staff: [part],
          select: [],
        });
      }
    };

    const cbstaff = (item, value) => {
      item.forEach((e) => {
        if (e.id != accountStore.user.is_idEmployee) {
          e[props.okey] = value;
        }
        if (!("employees" in e)) {
          back.value.push(e);
        }
        if ("employees" in e) {
          cbstaff(e.employees, value);
        }
      });
    };

    function onFilter(item, itemText) {
      return (
        item.includes(filtered.value) ||
        itemText.raw.employees.some((e) =>
          e.title.toLowerCase().includes(filtered.value.toLowerCase())
        )
      );
    }

    const disable = (department) => {
      return department.id == accountStore.user.id_dict_department &&
        department.employees.length == 1
        ? true
        : false;
    };

    const allUser = () => {
      emitUp(staffed.value);
    };

    return {
      staffed,
      filtered,
      accountStore,
      selectedStaff,
      splitname,
      onFilter,
      disable,
      allUser,
    };
  },
};
</script>

<style>
.max-height-select .v-field__input {
  max-height: 300px; /* Установите желаемую максимальную высоту */
  overflow-y: auto; /* Добавьте прокрутку, если список превышает максимальную высоту */
  overflow-x: hidden;
  margin: 5px;
}
</style>
