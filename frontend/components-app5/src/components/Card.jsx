import Badge from "./Badge";


const Card = (props) => {

    const deleteTrip = (id) => {
        fetch('http://localhost:8000/trips/' + id, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            console.log("Deleted trip:", data);
            // Update the list of trips
        })  
    }

    return (
        <div className="card" style={{width: '24rem'}}>
        <img src={ props.trip.imageUrl} className="card-img-top" alt="..."/>
        <div className="card-body">
            <h5 className="card-title">{props.trip.destination}</h5>
            <p className="card-text">{props.trip.description}</p>
            <Badge caption="Votes" votes={props.trip.votes}/>
            <button className= "btn btn-danger" onClick={()=> deleteTrip(props.trip.id)}> X </button>
        </div>
        </div>
    )
}
export default Card;