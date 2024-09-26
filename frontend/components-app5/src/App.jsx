
import 'bootstrap/dist/css/bootstrap.min.css'
import Trips from './components/Trips'
import AddTrip from './components/AddTrip'

function App() {

  return (
    <div className="container">
      <div className='row'>
        <AddTrip></AddTrip>
        <hr/>
        <Trips></Trips>
      </div>
    </div>
  )
}

export default App
