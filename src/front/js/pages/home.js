import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";

export const Home = () => {
  const { store, actions } = useContext(Context);

  return (
    <div className="text-center mt-5">
      <h1>This is home</h1>
      <Link to="/login" className="me-5">
        Login
      </Link>
      <Link to="/signup">Signup</Link>
    </div>
  );
};
