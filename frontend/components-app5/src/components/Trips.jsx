import { useEffect, useState } from 'react'
import Card from './Card'
import Dropdown from './Dropdown'

const Trips = () => {
    const [searchTerm, setSearchTerm] = useState('')
    const [previousTrips, setPreviousTrips] = useState('')
    const [tag, setTag] = useState('')
    const [trips, setTrips] = useState([])

    useEffect(()=>{
      console.log("Fetching trips...");

      fetch('http://localhost:8000/api/v1/destinations')
       .then(response => response.json())
       .then(data => {
         setTrips(data);
         console.log("Fetched trips:", data);
       })
      
    }, [])

      const sortTrips = (sortDir) => {
        let sortedTrips = [...trips];

        if(sortDir === 'asc'){
            sortedTrips.sort((a,b) => a.destination.localeCompare(b.destination))
        }
        else if(sortDir === 'desc'){
            sortedTrips.sort((a,b) => b.destination.localeCompare(a.destination))
        }
        setTrips(sortedTrips)
      }

      const searchTrip = (e) => {
        const previousTrips = [...trips]
        setPreviousTrips(previousTrips);
        setTrips(trips.filter(trip => trip.destination.toLowerCase().includes(e.target.value.toLowerCase())))
      }

      const clearFilter = () => {
        setTrips(previousTrips);
        setSearchTerm('')
        setTag('')
      }

      const chooseTrips = (text) => {
        console.log('Tag selected:', text);

        let chosenTrips = [...trips];
        setPreviousTrips(chosenTrips);
        setTag(text)
        setTrips(chosenTrips.filter(trip => trip.description.toLowerCase().includes(text.toLowerCase())))
        
      }

    
      let tripsList = trips.map((trip)=> <Card className="card-display" key={trip.id} trip={trip} ></Card>)
      console.log(tripsList)
      return (
        <>
        <div className="input-group mb-3">
        <span className="input-group-text" id="basic-addon1">Search Trip</span>
        <input type="text" onBlur={searchTrip} value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)} className="form-control" placeholder="Enter a destination.." aria-label="Username" aria-describedby="basic-addon1"/>
        </div>

        {(searchTerm || tag) &&  <div className="input-group mb-3">
            <button onClick={clearFilter} type="button" className='close'>{searchTerm || tag} <span aria-hidden="true">&times;</span></button>
        </div>}

        <div className="input-group mb-3">
            <button onClick={()=>sortTrips('asc')} type="button" className='close'>Sort Asc</button>
            <button onClick={()=>sortTrips('desc')} type="button" className='close'>Sort Desc</button>
        </div>
        <div className="input-group mb-3">
            <Dropdown whenTagSelected={chooseTrips}/>
        </div>
          
         {tripsList}
        </>
         
 
      )
}

export default Trips;