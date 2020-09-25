import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("api/post/")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }


  render() {
    const final = [];
    for (let  post of this.state.data) 
    {
      if(post.image) {
        final.push(<img style={{maxWidth: 500, borderRadius: 8, alignSelf: 'center'}} src={post.image}></img>)
      }
      final.push(<li key={post.title}>{post.text}</li>);  
    }

      return (
        <div className="App">
          <ul>{final}</ul>    </div>
      );
    // return (
    //   <ul>
    //     {this.state.data.map(post => {
    //       return (
    //         <li key={post.id}>
    //           {post.title} - {post.text}
    //         </li>
    //       );
    //     })}
    //   </ul>
    // );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);