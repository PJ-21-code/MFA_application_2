const ResendButton = ({onClick, disabled}) => {
  return (
    <div>
        <div className='flex gap-4'>
          <button
          type= 'submit'
          onClick= {onClick}
          disabled= {disabled}
          className="w-full rounded-md text-center bg-blue-200 p-2.5 text-sm font-semibold text-white transition duration-200 hover:bg-blue-200 focus:outline-none focus:ring-2 focus:ring-blue-300 focus:ring-offset-2"
          >Resend OTP</button>
        </div>
    </div>
  )
}

export default ResendButton