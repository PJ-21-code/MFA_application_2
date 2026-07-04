import Otp from './Otp'
import ResendButton from './ResendButton'
import SubmitButton from './SubmitButton'
import { authService } from '../../api/authApiService'
import { useLocation, useNavigate } from 'react-router-dom'
import { useState } from 'react'

const OtpPage = () => {

  const [otp, setOtp] = useState('')
  const [message, setMessage] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const navigate= useNavigate()
  const location= useLocation()

  const sessionId = location.state?.session_id || 'mock_session_123'

  const otpHandler = async (event) => {
    event.preventDefault()
    if(!sessionId)
    {
      setMessage('Session is Missing')
      return
    }

    setIsLoading(true)
    setMessage('')

    try {
      const response = await authService.verifyOtp(sessionId, otp)

      const jwtToken = response.access_token;
      console.log("Success! JWT_token:", jwtToken)
      localStorage.setItem('token', jwtToken)
      navigate('/dashboard')
    } catch (error) {
      const errorMsg = error.response?.data?.detail || "Invalid OTP"
      setMessage(errorMsg)
    } finally {
      setIsLoading(false)
    }
  }

  const resendHandler= async () => {

    if(!sessionId){
      return
    }
    setMessage('Resending OTP...')
    setIsLoading(true)

    try {
      await authService.resendOtp(sessionId)
      setMessage("New OTP sent successfully!")
    } catch (error) {
      const errorMsg = error.response?.data?.detail || "Failed to resend OTP"
      setMessage(errorMsg)
    } finally {
      setIsLoading(false)
    }
  }
  return (
    <div className="flex h-screen items-center justify-center bg-gray-300 px-4 font-sans">
      <form onSubmit={otpHandler} className='w-full max-w-sm rounded-lg bg-white p-8 shadow-md'>
        <h2 className='mb-6 text-center text-3xl font-bold text-gray-800'>OTP</h2>
        <p className="mb-6 text-center text-sm text-gray-500">
        Enter the 6-digit code sent to your email.
        </p>

        {message && (
          <p className={`mb-4 text-center text-sm font-semibold ${message.includes('sent') ? 'text-green-600' : 'text-red-500'}`}>
            {message}
          </p>
        )}

        <Otp otpValue={otp} setOtpValue={setOtp} />
        <ResendButton onClick={resendHandler} disabled={isLoading}/>
        <SubmitButton disabled={isLoading || otp.length!==6} />
      </form>
    </div>
  )
}

export default OtpPage