<script>
      // variables
      let name1 = "Clement"; // String
      const age1 = 25; // Number
      let isStudent = true; // Boolean
      let empty = null; // Null
      let notDefined; // Undefined

      //   operators

      let a = 5 + 2; // Arithmetic
      let isEqual = 5 === 5; // Comparison (strict equality)
      let result = a > 3 && a < 10; // Logical

      // conditionals
      var ag1e = 20;
      ((ag1e) => 18) ? "Adult" : "Minor";
      if (ag1e >= 18) {
        console.log("Adult");
      } else {
        console.log("Minor");
      }
      //  loops
      for (let j = 0; j < 3; j++) {
        console.log(j);
      }

      //while loop
      let i = 0;

      while (i < 3) {
        console.log(i);
        i++;
      }

      // Arrays
      let fruits = ["Apple", "Banana"];
      console.log(fruits[0]); // Access element
      fruits.push("Mango"); // Add element

      //   objects
      let user = {
        name: "clement",
        agee: 25,

        greet() {
          return `Hi, I'm ${this.name}`;
        },
      };

      // traditional function
      function greet(name) {
        return `Hello, ${name}`;
        console.log(greet);
      }

      const mname = "clement";
      console.log(name);
      // arrow function
      const greetArrow = (name) => `Hi, ${name}`;

      // function
      function sayHi() {
        alert("Hello");
      }
      // async wait
      async function fetchData() {
        let res = await fetch("https://api.example.com");
        let data = await res.json();

        console.log(data);
      }

      // fetch API

      fetch("https://api.example.com")
        .then((res) => res.json())
        .then((data) => console.log(data))
        .catch((err) => console.error(err));

      // error handling

      try {
        let result = riskyFunction();
      } catch (error) {
        console.log("Error occurred :", error.message);
      }

      // class

      class Person {
        constructor(name) {
          this.name = name;
        }
        greet() {
          return `Hi, I'm ${this.name}`;
        }
      }

      // Es6+ features

      const person = {
        name: "Clem",
        age: 25,
      };

      const { name, age } = person; //destructuring

      const nums = [1, 2, 3];

      const more = [...nums, 4];

      // module
      // slipt codes into reusable files

      // greet.js
    //   export function greet(name) {
    //     return `Hello, ${name}`;
    //   }

    //   // main.js

    //   import { greet } from "./greet.js";

      // store data in browser
      localStorage.setItem("uname", "Clement");
      let uname = localStorage.getItem("uname");
      
 </script>