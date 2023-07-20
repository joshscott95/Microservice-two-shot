import React, { useEffect, useState } from 'react';

function MainPage() {
  // state to store hats
  const [hats, setHats] = useState([]);

  // function to fetch hats
  const fetchHats = async () => {
    const response = await fetch('http://localhost:8090/api/hats/');
    const data = await response.json();
    setHats(data.hats);
  };

  // fetch hats when component mounts
  useEffect(() => {
    fetchHats();
  }, []);

  return (
    <div className="px-4 py-5 my-5 text-center">
      <h1 className="display-5 fw-bold">WARDROBIFY!</h1>
      <div className="col-lg-6 mx-auto">
        <p className="lead mb-4">
          Need to keep track of your shoes and hats? We have
          the solution for you!
        </p>
        {/* List of Hats */}
        <ul>
          {hats.map((hat, index) => (
            <li key={index}>{hat.style_name}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default MainPage;