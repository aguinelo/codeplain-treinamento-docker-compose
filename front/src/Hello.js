import {React, Component} from 'react';

class Hello extends Component{    
    constructor(props) {
        super(props);
        this.state = {
            text: "Initial"
        }
    }

    componentDidMount() {
        this.setState({ text: "" });
        // const apiUrl = "http://localhost:8000";
        const apiUrl = "http://api.treinamentodocker.codeplain.com.br";
        
        fetch(apiUrl, {
            "method": "GET"
        })
        .then(response => response.json())
        .then(response => {
            this.setState({
                text: response.message
            });
        })
        .catch(err => {console.log(err)})
        
    }

    render(){
        return(
            <div>
                <h3>Says: {this.state.text}</h3>
            </div>
        )
    }
}

export default Hello;