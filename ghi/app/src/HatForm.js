import React, { useState } from 'react';

const HatForm = () => {
    const [style_name, setStyleName] = useState('');
    const [color, setColor] = useState('');
    const [fabric, setFabric] = useState('');
    // const [location, setLocation] = useState('');
    const [picture_url, setPictureUrl] = useState('');

    const handleSubmit = async e => {
        e.preventDefault();
        const hat = { style_name, color, fabric, picture_url };
        // location

        // submit the request
        const response = await fetch('http://localhost:8090/api/hats/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(hat)
        });

        // clear form fields
        if (response.ok) {
            setStyleName('');
            setColor('');
            setFabric('');
            // setLocation('');
            setPictureUrl('');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" value={style_name} onChange={e => setStyleName(e.target.value)} placeholder="Style Name" required />
            <input type="text" value={color} onChange={e => setColor(e.target.value)} placeholder="Color" required />
            <input type="text" value={fabric} onChange={e => setFabric(e.target.value)} placeholder="Fabric" required />
            {/* <input type="text" value={location} onChange={e => setLocation(e.target.value)} placeholder="Location" required /> */}
            <input type="text" value={picture_url} onChange={e => setPictureUrl(e.target.value)} placeholder="Picture URL" required />
            <button type="submit">Add Hat</button>
        </form>
    );
};

export default HatForm;