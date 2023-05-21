import React, { useState, useEffect } from "react";

const WeatherComponent = () => {
    const [data, setData] = useState({
        airtemperature: null,
        airquality: null
    });
    useEffect(() => {
        const apiUrl = process.env.REACT_APP_API_URL || "http://localhost:5000";
        fetch(`${apiUrl}/api/weather`).then((res) =>
            res.json().then((data) => {
                setData({
                    airtemperature: data.airtemperature,
                    airquality: data.airquality
                })
            })
        );
    }, []);
    return (
        <div>
            <h2>{data.airtemperature} °C {data.airquality} AQI</h2>
        </div>
    );
};

export default WeatherComponent;