import React from "react";

export default function TrainCard({ train }) {
  return (
    <div style={{ border: "1px solid #ccc", margin: "1rem", padding: "1rem" }}>
      <h3>{train.name} ({train.train_id})</h3>
      <p>From: {train.origin} → To: {train.destination}</p>
      <p>Departure: {train.departure}</p>
      <p>Arrival: {train.arrival}</p>
      <p>Status: {train.status}</p>
    </div>
  );
}
