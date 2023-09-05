// Import statements
import React from "react";
import { Link } from "react-router-dom";

// CSS module import statement
import styles from "../css/index.module.css";

const Garibaldi = () => {
  // Renders Index.jsx component
  return (
    <div
      className={`row justify-content-center align-items-center h-100 ${styles.indexBody}`}
    >
      <div className="col-md-8">
        <div className={`card-body ${styles.indexCard}`}>
          <div className="text-center">
            <h1 className={styles.indexTitle}>
              Camp<span className={styles.titleStyle}>Pass</span>
            </h1>
            <h4 className={styles.indexDescription}>
              CampPass is an app designed to simplify the process of
              securing day passes to B user-friendly app ensures
              outdoor enthusiasts never miss out on their favorite outdoor
              adventures by providing timely updates on park availability,
              making planning your next outdoor getaway a breeze.
            </h4>
            <div className={`button-group`}>
              <Link to="/garibaldi">
                <button className={`btn btn-primary btn-lg ${styles.indexBtn}`}>
                  Garibaldi Provincial Park
                </button>
              </Link>
              <Link to="/golden_ears">
                <button className={`btn btn-primary btn-lg ${styles.indexBtn}`}>
                  Golden Ears Provincial Park
                </button>
              </Link>
              <Link to="/joffre">
                <button className={`btn btn-primary btn-lg ${styles.indexBtn}`}>
                  Joffre Lakes Provincial Park
                </button>
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
  // End of Index.jsx component
};

export default Garibaldi;
