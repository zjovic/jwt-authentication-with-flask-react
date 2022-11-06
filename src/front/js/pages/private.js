import React, { useContext, useEffect, useState } from "react";
import { Context } from "../store/appContext";
import { useNavigate } from "react-router-dom";

export const Private = () => {
  const { store, actions } = useContext(Context);
  const navigate = useNavigate();

  useEffect(() => {
    if (store.token === null) {
      navigate("/");
    }
  }, []);

  return (
    <div className="m-auto w-50 my-3">
      <h1>This is private</h1>
    </div>
  );
};
