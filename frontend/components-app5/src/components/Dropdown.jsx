import { useState } from "react";
import DropdownItem from "./DropdownItem";

const Dropdown = (props) => {

    const [show, setShow] = useState(false);
    const [tags, setTags] = useState(['Beaches', 'Mountains', 'Cities', 'Nature', 'Culture', 'History', 'Waters', 'Nightlife']);
    const [caption, setCaption] = useState('Looking for?');

    const handleItemClick = (item) => {
        console.log('In parent, Clicked on:', item);
        setCaption(item);
        setShow(false);
        props.whenTagSelected(item)
    }

    let listTags = tags.map((tag, index) =>  <DropdownItem key={index} text={tag} whenItemClicked={handleItemClick} /> );

    return (
        <div className="dropdown">
        <button onClick={()=>setShow(!show)} className="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            {caption}
        </button>
        <ul className={show?"dropdown-menu show":"dropdown-menu"}>
        {listTags}
        </ul>
        </div>
    )
}

export default Dropdown;