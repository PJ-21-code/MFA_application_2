import apiClient from "./axiosConfig";

export const authService = {

    verifyUser: async(email,password) => {
        const response= await apiClient.post('/verify-user', {
            email: email,
            password: password
        });
        return response.data;
    },

    sendOtp: async(sessionID) => {
        const response= await apiClient.post('/send-otp', {
            session_id: sessionID
        });
        return response.data;
    },

    resendOtp: async(sessionID) => {
        const response= await apiClient.post('/resend-otp',{
            session_id: sessionID
        });
        return response.data;
    },

    verifyOtp: async(sessionID, otpCode) => {
        const response= await apiClient.post('/verify-otp', {
            session_id: sessionID,
            otp: otpCode
        });
        return response.data;
    }
};