const DropdownItem = ({text, whenItemClicked}) => {

    const handleItemClick = () => {
        // Add logic to handle item click
        console.log('Item clicked: ', text);
        whenItemClicked(text);
    }

    return(
        <li><a onClick={handleItemClick} className="dropdown-item" href="#">{text}</a></li>
    )
}

export default DropdownItem;