import React, { useState, useEffect } from "react";

const WeatherComponent = () => {
    const [data, setData] = useState({
        airtemperature: null,
        airquality: null
    });
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch("/api/weather")
            .then((res) => {
                if (!res.ok) {
                    throw new Error("Network response was not ok");
                }
                return res.json();
            })
            .then((data) => {
                setData({
                    airtemperature: data.airtemperature,
                    airquality: data.airquality
                });
                setError(null);
            })
            .catch((error) => {
                setError("Error fetching weather data");
                console.error(error);
            });
    }, []);

    return (
        <div>
            {error ? (
                <p>{error}</p>
            ) : (
                <h2>
                    {data.airtemperature} °C {data.airquality} AQI
                </h2>
            )}
        </div>
    );
};

export default WeatherComponent;