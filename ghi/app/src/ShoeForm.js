import React, { useState, useEffect } from 'react';

const ShoeForm = () => {
    const [color, setColor] = useState
    const [model_name, setModelName] = useState
    const [picture, setPicture] = useState
    const [manufacturer, setManufacturer] = useState
    // const [bins, setBins] =useState


    // useEffect(() => {
    //     fetch('http://localhost:8100/api/bins/')
    //         .then(response => response.json())
    //         .then(data => {
    //             setBins(data.bins);
    //         })
    //         .catch(err => console.log(err));
    // }, []);

    const handleSubmit = async e => {
        e.preventDefault();
        const shoe = { manufacturer, model_name, color, picture }; //bin location

        const response = await fetch('http://localhost:8080/api/shoes/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json' },
            body: JSON.stringify(shoe)
        });

        if (response.ok) {
            setColor('');
            setModelName('');
            setPicture('');
            setManufacturer('');
            // setBin('');
        }
    }

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" value={model_name} onChange={e => setModelName(e.target.value)} placeholder="Model Name" required />
            <input type="text" value={manufacturer} onChange={e => setManufacturer(e.target.value)} placeholder="Manufacturer" required />
            <input type="text" value={color} onChange={e => setColor(e.target.value)} placeholder="Color" required />
            {/* <select value={bin} onChange={e => setBin(parseInt(e.target.value, 10))} required>
                <option value="">--Select Bin--</option>
                {bins.map((loc, index) => (
                    <option key={index} value={bin.id}>
                        {bin.closet_name} - {bin.bin_number}/{bin.bin_size}
                    </option>
                ))}
            </select> */}
            <input type="text" value={picture} onChange={e => setPicture(e.target.value)} placeholder="Picture URL" required />
            <button type="submit">Add Shoe</button>
        </form>
    );
};

export default ShoeForm;