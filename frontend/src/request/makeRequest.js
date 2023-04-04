import axios from "axios";

export const makeRequest = (url, method, data = {}) => {
    return axios({
        url,
        method,
        baseURL: "http://localhost:8000",
        data,
    })
}