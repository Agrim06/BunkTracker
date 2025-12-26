import api from "./axios";

//POST /auth/login
export const loginUser = async (credentials) =>{
    const response = await api.post("/auth/login" , credentials);
    return response.data
};

//POST /auth/register
export const registerUser = async(data) =>{
    const response = await api.post("/auth/register" , data);
    return response.data;
};

