import React, { useEffect, useState } from "react";
import { fetchTrains } from "../services/api";

const TrainTable = () => {
  const [trains, setTrains] = useState([]);

  useEffect(() => {
    const interval = setInterval(async () => {
      const data = await fetchTrains();
      setTrains(data.trains);
    }, 5000); // fetch every 5 seconds

    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h2>Train Status</h2>
      <table border="1">
        <thead>
          <tr>
            <th>No</th>
            <th>Name</th>
            <th>Current Station</th>
            <th>Next Station</th>
            <th>Status</th>
            <th>Delay (min)</th>
          </tr>
        </thead>
        <tbody>
          {trains.map((train) => (
            <tr key={train.train_no}>
              <td>{train.train_no}</td>
              <td>{train.train_name}</td>
              <td>{train.current_station}</td>
              <td>{train.next_station || "-"}</td>
              <td>{train.status}</td>
              <td>{train.delay_minutes}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TrainTable;
