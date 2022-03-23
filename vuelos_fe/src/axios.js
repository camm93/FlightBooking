import axios from "axios"

window.axios = axios
axios.defaults.baseURL = process.env.VUE_APP_API_BASE