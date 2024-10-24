const str = "hello";
import { useAccountStore } from "@/store/AccountStore";
import { useAppStore } from "@/store/app";
import { baseURL } from "@/utils/axios-api";
import { axiosApiInstance, clearAxios } from "@/utils/axios-api";
import { useRouter } from "vue-router";
import moment from "moment";
import { ref, onMounted } from "vue";


export function get_name(namestr) {
  let arr = namestr.split("/");
  return arr[arr.length - 1];
};

export function formatComa(date) {
  return moment(date).format("DD.MM.YYYY");
}

export function formatDash(date) {
  return moment(date).format("YYYY-MM-DD");
}

export function formaComaTime(date) {
  return moment(date).format("DD.MM.YYYY H:mm");
}

export function formaDashTime(date) {
  return moment(date).format("YYYY-MM-DD H:mm");
}

export function checking_for_entry(where, what) {
  if (!where.includes(what)) {
    where.push(what);
  }
} 

export function getfromserver(path, reactive) {
  try {
    axiosApiInstance.get(path).then((result) => {
      reactive.value = result.data;
    });
  } catch (e) {
    console.log(e);
  }
}

export function getfromserverfree(path, reactive) {
  try {
    clearAxios.get(path).then((result) => {
      reactive.value = result.data;
    });
  } catch (e) {
    console.log(e);
  }
}

export function checkremote(filecheck) {
  return process.env.NODE_ENV == "development"
    ? "https://pixelbox.ru/wp-content/uploads/2021/11/avatar-whatsapp-pixelbox.ru-36.jpg"
    : filecheck;
}

export default str;

export function splitname(name) {
  return name.familyname + " " + name.name[0] + "." + name.parentname[0] + ".";
}

export function pagecounter() {
  const router = useRouter();
  const accountStore = useAccountStore();
  const appStore = useAppStore();

  let postdata = {
    user__id:
      "user" in accountStore && "id" in accountStore.user
        ? accountStore.user.id
        : null,
    page: router.currentRoute.value.meta.title,
    fullPath: router.currentRoute.value.fullPath,
    ico: router.currentRoute.value.meta.ico,
  };

  clearAxios.post(`${baseURL}api/watcher/counter/`, postdata).then((result) => {
    appStore.countvisitor = result.data;
  });
}

export function getDevelopment() {
  return process.env.NODE_ENV == "development" ? true : false;
}

export function useICalReader(url) {
  ///
  const events = ref([]);
 
  const loadICalFile = async () => {
    try {
      const response = await fetch(url);
      const data = await response.text();
      const jcalData = ical.parse(data);
      const icalComponent = new ical.Component(jcalData);
      const name = icalComponent.getFirstPropertyValue("x-wr-calname");

      const events = icalComponent
        .getAllSubcomponents("vevent")
        .map((vevent) => new ical.Event(vevent));

      const calendarEvents = events.map((event) => {
        return {
          summary: event.summary,
          description: event.description,
          organizer: event.organizer,
          attendee_count: event.attendees.length,
          duration_seconds: event.duration.toSeconds(),
          start: event.startDate.toJSDate().getTime() / 1000,
          end: event.endDate.toJSDate().getTime() / 1000,
          location: event.location,
        }
      })
     
      return {
        type: "calendar",
        title: name,
        calendar: calendarEvents,
      }
    
      // const vevents = comp.getAllSubcomponents('vevent')
      // const eventsData = vevents.map(vevent => ({
      //   vevent: vevent,

      // summary: vevent.getFirstPropertyValue('summary'),
      // start: vevent.getFirstPropertyValue('dtstart'),
      // end: vevent.getFirstPropertyValue('dtend')
      // }))
      // events.value = eventsData
    } catch (error) {
      console.error(error);
    }
  };

  onMounted(() => {
    loadICalFile();
  });

  return {
    events,
  };
}

// export function useICalReader(filePath) {
//   const icsContent = ref('')

//   const fetchICalFile = async () => {
//     try {
//       const response = await fetch(filePath)
//       if (!response.ok) {
//         throw new Error('Ошибка при загрузке файла')
//       }
//       const data = await response.text()
//       icsContent.value = data
//     } catch (error) {
//       console.error('Ошибка при чтении файла:', error)
//     }
//   }

//   return { icsContent, fetchICalFile }
// }
