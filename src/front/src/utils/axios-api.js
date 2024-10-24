import {useAccountStore} from '@/store/AccountStore'
import axios from "axios";
const spravURL = 'http://10.252.44.33/accounting6/images/photo/'
const spravURLBase = 'http://10.252.44.33/accounting6/'
const baseURL = process.env.NODE_ENV == 'development'? 'http://127.0.0.1:8000/': `http://${window.location.host}/`;
const baseWS = process.env.NODE_ENV == 'development'? 'ws://127.0.0.1:8000/': `ws://${window.location.host}/`;
// const baseURL = process.env.NODE_ENV == 'development'? 'http://127.0.0.1:8000/': `http://10.252.44.60:9965/`;
// const baseWS = process.env.NODE_ENV == 'development'? 'ws://127.0.0.1:8000/': `ws://10.252.44.60:9966/`;
// для релизного меняем 'http://ukd/'
// const baseURL = 'http://127.0.0.1:8000/';

async function refreshToken() {

    const refresh = localStorage.getItem('refresh');

    try {
        const result = await axios.post('/api/accounts/token/refresh/', {refresh}, {
            baseURL
        })
       
        if (result.config.data) localStorage.setItem('refresh', JSON.parse(result.config.data).refresh);
        localStorage.setItem('access', result.data.access)

        return result.data.access;
    }
        
    catch(e) {  
        const accountStore = useAccountStore()     
        accountStore.logout()
        accountStore.cod2user.value=false
       
        return Promise.reject(e);
    }
}

const axiosApiInstance = axios.create({
    baseURL,
});

const clearAxios = axios.create({
    baseURL,
});

axiosApiInstance.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('access')}`

axiosApiInstance.interceptors.request.use(config => {
    const access = localStorage.getItem('access');
    if (access) {
        config.headers = { 
            'Authorization': `Bearer ${access}`,
        }
    }
    return config;
}, error => {
    return Promise.reject(error);
})

axiosApiInstance.interceptors.response.use(
response => {
    return response;
},
async error => {

    const originalRequest = error.config;
    if ((error.response.status === 401 || error.response.status === 403) && !originalRequest._retry) {
    
        originalRequest._retry = true;
        try {

            const token = await refreshToken();
            
            axiosApiInstance.defaults.headers.common['Authorization'] = `Bearer ${token}`; 
           
            if (originalRequest.data){
            originalRequest.data = JSON.parse(originalRequest.data);  }          
           
            return axiosApiInstance(originalRequest);

        } catch(e) {            
           
            // 
            // if (window.location.pathname!='/auth') window.location.reload()
            // window.location.reload()
            
            return Promise.reject(error);
        }
    }
    return Promise.reject(error);
})


export { axiosApiInstance, clearAxios, baseURL,spravURL, spravURLBase, baseWS }