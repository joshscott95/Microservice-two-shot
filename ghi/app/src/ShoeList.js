import React, { useEffect, useState } from 'react';

function ShoeList () {
    const [shoes, setShoes] = useState([]);

    const fetchShoes = async () => {
        const response = await fetch('http://localhost:8080/api/shoes/');
        const data = await response.json();
        setShoes(data.shoes);
    };

    const deleteShoe = async (id) => {
        const response = await fetch(`http://localhost:8080/api/shoes/${id}`, {
            method: 'DELETE'
        });

        if (response.ok) {
            const remainingShoes = shoes.filter(shoe => shoe.id !== id);
            setShoes(remainingShoes);
        } else {
            console.error(`Failed to delete shoe at id: ${id}`)
        }
    }


    useEffect(() => {
        fetchShoes();
    }, []);

    return (
        <div className="px-4 py-5 my-5 text-center">
            <h1 className="display-5 fw-bold">WARDROBIFY!</h1>
            <div className="col-lg-6 mx-auto">
                <p className="lead mb-4">
                    Need to keep track of your shoes and hats? We have
                    the solution for you!
                </p>
                <ul>
                    {shoes.map((shoe, index) => (
                        <li key={index}>
                            <h2>{shoe.manufacturer}</h2>
                            <p>Fabric: {shoe.model_name}</p>
                            <p>Color: {shoe.color}</p>
                            <img src={shoe.picture} alt={shoe.manufacturer} style={{ width: "200px" }} />
                            <button onClick={() => deleteShoe(shoe.id)}>Delete</button>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default ShoeList;