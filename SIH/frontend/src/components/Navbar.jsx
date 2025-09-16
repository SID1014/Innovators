import React from "react";
import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav style={{ padding: "1rem", background: "#222", color: "white" }}>
      <Link to="/" style={{ marginRight: "1rem", color: "white" }}>Home</Link>
      <Link to="/stations" style={{ marginRight: "1rem", color: "white" }}>Stations</Link>
      <Link to="/trains" style={{ color: "white" }}>Trains</Link>
    </nav>
  );
}
