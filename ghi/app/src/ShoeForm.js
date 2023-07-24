import React, { useState, useEffect } from 'react';

const ShoeForm = () => {
<<<<<<< HEAD
    const [color, setColor] = useState('');
    const [model_name, setModelName] = useState('');
    const [picture, setPicture] = useState('');
    const [manufacturer, setManufacturer] = useState('');
    const [bins, setBins] = useState([]);
    const [selectedBin, setSelectedBin] = useState(''); // new state for selected bin id
=======
    const [model_name, setModelName] = useState('');
    const [picture, setPicture] = useState('');
    const [manufacturer, setManufacturer] = useState('');
    const [bin, setBin] = useState('');
    const [shoe_color, setShoeColor] = useState('');
    const [bins, setBins] = useState([]);
>>>>>>> kacton2


    useEffect(() => {
        fetch('http://localhost:8100/api/bins/')
            .then(response => response.json())
            .then(data => {
                setBins(data.bins);
            })
            .catch(err => console.log(err));
    }, []);

    const handleSubmit = async e => {
        e.preventDefault();
<<<<<<< HEAD
        const shoe = { manufacturer, model_name, color, picture, bin_id: selectedBin }; //bin location
=======
        const shoe = { manufacturer, model_name, shoe_color, picture, bin };
>>>>>>> kacton2

        const response = await fetch('http://localhost:8080/api/shoes/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json' },
            body: JSON.stringify(shoe)
        });

        if (response.ok) {
            setShoeColor('');
            setModelName('');
            setPicture('');
            setManufacturer('');
<<<<<<< HEAD
            setSelectedBin(''); // reset selected bin to empty
=======
            setBin();
>>>>>>> kacton2
        }
    }

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" value={model_name} onChange={e => setModelName(e.target.value)} placeholder="Model Name" required />
            <input type="text" value={manufacturer} onChange={e => setManufacturer(e.target.value)} placeholder="Manufacturer" required />
<<<<<<< HEAD
            <input type="text" value={color} onChange={e => setColor(e.target.value)} placeholder="Color" required />
            <select value={selectedBin} onChange={e => setSelectedBin(e.target.value)} required>
                <option value="">--Select Bin--</option>
                {bins.map((bin, index) => (
                    <option key={index} value={bin.id}>
                        {bin.closet_name} - {bin.bin_number}/{bin.bin_size}
=======
            <input type="text" value={shoe_color} onChange={e => setShoeColor(e.target.value)} placeholder="Shoe Color" required />
            <select value={bin} onChange={e => setBin(parseInt(e.target.value, 10))} required>
                <option value="">--Select Bin--</option>
                {bins.map(bin => (
                    <option key={bin.id} value={bin.id}>
                        {bin.id}
>>>>>>> kacton2
                    </option>
                ))}
            </select>
            <input type="text" value={picture} onChange={e => setPicture(e.target.value)} placeholder="Picture URL" required />
            <button type="submit">Add Shoe</button>
        </form>
    );
};

export default ShoeForm;
