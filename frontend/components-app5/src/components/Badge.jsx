import {useEffect, useState} from "react";

const Badge = (props) => {

    const [count, setCount] = useState(10);

    useEffect(()=>{
        setCount(props.votes)
    }, [])

    const incrementCount = () => {
        setCount(count + 1);
    }

    return (
        <button onClick={incrementCount} type="button" className="btn btn-primary">
        {props.caption} <span className="badge text-bg-secondary">{count}</span>
        </button>
    )
}

export default Badge;