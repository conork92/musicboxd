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


class App extends React.Component {
    constructor(props) {
        super(props)
    }
    render() {
        const welcome = this.props.name;
        return (
            
            <div>
                <h1>Hello, {this.props.name}</h1>
                <p>Welcome to your first React Class Component!</p>
            </div>
        );
    }
}


ReactDOM.render(app,
    document.getElementById("root"))