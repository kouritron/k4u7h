
import * as React from 'react'
import { createRoot } from 'react-dom/client';


function my_start() {
    
    // make an element
    const elem1 = <h1>Hello from my app.jsx</h1>;

    // function component
    var Home = () => {
        return <div>k4u7h homepage</div>;
    }


    const app_container = document.getElementById('k4u7h_app');
    const react_root = createRoot(app_container);
    react_root.render(<Home />);
}

// invoke start options
// onLoad="my_start();      // add to body tag
// my_start();              // call about here
// set timeout to call my_start soon.

// setTimeout(function, milliseconds, param1, param2, ...)
setTimeout(my_start, 700);
console.log("hello from app.jsx")



