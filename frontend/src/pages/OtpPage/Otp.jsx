const Otp = ({otpValue, setOtpValue}) => {

  return (
    <div>
        <div className='mb-4 flex flex-col'>
          <label htmlFor='email' className='mb-1 text-sm font-medium text-gray-600'>
            Type code here
          </label>
          <input
          type='text'
          id= 'otp'
          value={otpValue}
          maxLength={6}
          onChange={(e) => {setOtpValue(e.target.value)}}
          required
          placeholder= '000000'
          className='rounded-md border border-gray-300 p-2.5 text-sm outline-none transition duration-200 focus:border-blue-500 focus:ring-2 focus:ring-blue-200' />
        </div>
    </div>
  )
}

export default Otp