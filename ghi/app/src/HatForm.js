import React, { useState, useEffect } from 'react';

const HatForm = () => {
    const [style_name, setStyleName] = useState('');
    const [color, setColor] = useState('');
    const [fabric, setFabric] = useState('');
    const [wardrobe_location, setLocation] = useState('');
    const [picture_url, setPictureUrl] = useState('');
    const [locations, setLocations] = useState([]);

    useEffect(() => {
        fetch('http://localhost:8100/api/locations/')
            .then(response => response.json())
            .then(data => {
                setLocations(data.locations);
            })
            .catch(err => console.log(err));
    }, []);

    const handleSubmit = async e => {
        e.preventDefault();
        const hat = { style_name, color, fabric, picture_url, wardrobe_location };

        const response = await fetch('http://localhost:8090/api/hats/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(hat)
        });

        if (response.ok) {
            setStyleName('');
            setColor('');
            setFabric('');
            setLocation('');
            setPictureUrl('');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" value={style_name} onChange={e => setStyleName(e.target.value)} placeholder="Style Name" required />
            <input type="text" value={color} onChange={e => setColor(e.target.value)} placeholder="Color" required />
            <input type="text" value={fabric} onChange={e => setFabric(e.target.value)} placeholder="Fabric" required />
            <select value={wardrobe_location} onChange={e => setLocation(parseInt(e.target.value, 10))} required>
                <option value="">--Select Location--</option>
                {locations.map((loc, index) => (
                    <option key={index} value={loc.id}>
                        {loc.closet_name} - {loc.section_number}/{loc.shelf_number}
                    </option>
                ))}
            </select>
            <input type="text" value={picture_url} onChange={e => setPictureUrl(e.target.value)} placeholder="Picture URL" required />
            <button type="submit">Add Hat</button>
        </form>
    );
};

export default HatForm;
