const SubmitButton = ({disabled}) => {
  return (
    <div>
        <div className= 'flex gap-4'>
          <button
          type= 'submit'
          disabled={disabled}
          className="w-full rounded-md text-center bg-blue-600 p-2.5 text-sm font-semibold text-white transition duration-200 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
          >Verify and Login</button>
        </div>
    </div>
  )
}

export default SubmitButton