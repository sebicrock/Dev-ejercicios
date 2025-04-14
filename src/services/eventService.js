import axios from 'axios';

const API_URL = 'http://localhost:5000/api/events'; // Cambia la URL según tu configuración

export const createEvent = async (eventData) => {
    try {
        const response = await axios.post(API_URL, eventData);
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};

export const getEvents = async () => {
    try {
        const response = await axios.get(API_URL);
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};