import React from 'react';

var data = {
  "sanctuaries": [
    {
      "animals": [
        {
          "animalId": 1,
          "events": [
            {
              "due": "1/1/17",
              "eventId": 1,
              "task": "teeth cleaning"
            },
            {
              "due": "5/23/17",
              "eventId": 2,
              "task": "hoof trim"
            }
          ],
          "name": "Persephone"
        },
        {
          "animalId": 2,
          "events": [
            {
              "due": "1/15/17",
              "eventId": 1,
              "task": "teeth floating"
            },
            {
              "due": "4/23/17",
              "eventId": 2,
              "task": "deworm"
            }
          ],
          "name": "Carl"
        }
      ],
      "name": "Hope Haven",
      "uri": "http://localhost:5000/sanctuary/api/sanctuaries/1"
    },
    {
      "animals": [
        {
          "animalId": 1,
          "events": [
            {
              "due": "5/1/17",
              "eventId": 1,
              "task": "teeth cleaning"
            },
            {
              "due": "4/23/17",
              "eventId": 2,
              "task": "deworming"
            }
          ],
          "name": "Louis"
        },
        {
          "animalId": 2,
          "events": [
            {
              "due": "1/15/17",
              "eventId": 1,
              "task": "hoof maintenance"
            },
            {
              "due": "4/15/17",
              "eventId": 2,
              "task": "antibiotics"
            }
          ],
          "name": "Isaac"
        }
      ],
      "name": "Farm Friends",
      "uri": "http://localhost:5000/sanctuary/api/sanctuaries/2"
    }
  ]
};

class Main extends React.Component {
  render() {
    var mainStyle = {
      color: "black",
      display: "block",
      width: "300",
      // fontFamily: "monospace",
      fontSize: "20",
      textAlign: "center"
    };

    return (
      <div style={mainStyle}>
        This will describe what the page is used for and the intended audience.
        <p>{ data["sanctuaries"][0]["animals"][0]["events"][0]["task"] }</p>
      </div>
    );
  }
};

export default Main;
