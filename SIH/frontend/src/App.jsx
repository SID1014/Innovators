import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import StationView from "./pages/StationView";
import TrainView from "./pages/TrainView";

function App() {
  return (
    <Router>
      <Navbar />
      <div style={{ padding: "1rem" }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/stations" element={<StationView />} />
          <Route path="/trains" element={<TrainView />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
