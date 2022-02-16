import h11
import React from "react"
import ReactDOM from "react-dom"


var header = (
    <h1> Dear John</h1>
);

var subheader = (
    <h2> The Movie</h2>
);

var app = (
    <div> 
        {header}
        {subheader}
         </div>
)



ReactDOM.render(app,
    document.getElementById("root"))