import { useState } from "react";

const AddTrip = () => {

    const [destination, setDestination] = useState('');
    const [description, setDescription] = useState('');
    const [votes, setVotes] = useState('');
    const [imageUrl, setImageUrl] = useState('');

    const addTrip = () => {
        fetch('http://localhost:8000/trips', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                destination: destination,
                description: description,
                votes: parseInt(votes),
                imageUrl: imageUrl
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Added trip:", data);
            // Reset form inputs
        })
    }

    return (
        <>
            <div className="input-group mb-3">
                <span className="input-group-text" id="basic-addon1">Destination</span>
                <input type="text" value={destination} onChange={(e) => setDestination(e.target.value)} className="form-control" placeholder="Enter a destination.." aria-label="Username" aria-describedby="basic-addon1" />
            </div>
            <div className="input-group mb-3">
                <span className="input-group-text" id="basic-addon1">Description</span>
                <input type="text" value={description} onChange={(e) => setDescription(e.target.value)} className="form-control" placeholder="Enter a description.." aria-label="Username" aria-describedby="basic-addon1" />
            </div>
            <div className="input-group mb-3">
                <span className="input-group-text" id="basic-addon1">Initial Vote Count</span>
                <input type="text" value={votes} onChange={(e) => setVotes(e.target.value)} className="form-control" placeholder="Enter vote count.." aria-label="Username" aria-describedby="basic-addon1" />
            </div>
            <div className="input-group mb-3">
                <span className="input-group-text" id="basic-addon1">Image Url</span>
                <input type="text" value={imageUrl} onChange={(e) => setImageUrl(e.target.value)} className="form-control" placeholder="Enter an imageUrl.." aria-label="Username" aria-describedby="basic-addon1" />
            </div>
            <div className="input-group mb-3">
                <button type="button" className="btn btn-primary" onClick={addTrip}>Add Trip</button>
            </div>
        </>
    )
}

export default AddTrip;