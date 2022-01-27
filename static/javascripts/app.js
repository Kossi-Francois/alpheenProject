console.log("in js");

function sendRequest(inputData, callback) {
  const xhr = new XMLHttpRequest();
  // we defined the xhr

  xhr.onreadystatechange = function () {
    if (this.readyState != 4) return;

    if (this.status == 200) {
      //console.log("on res");
      const data = JSON.parse(this.responseText);
      callback(data);
      //console.log(data);

      // we get the returned data
    }

    // end of state change: it can be after some time (async)
  };

  xhr.open("POST", "/post2RTDB", true);
  //xhr.setRequestHeader( "content-type", "application/x-www-form-urlencoded;charset=UTF-8");
  xhr.setRequestHeader("content-type", "application/json;charset=UTF-8");
  xhr.send(JSON.stringify(inputData));
}





function test() {
  //let inputData = { data: [], methode: "getAll" };

  //let inputData = { data: [{ prenom: "franfran", vitesse: 50 }, { age: 10 }],  methode: "add", };

  //let inputData = { data: { id: ["tXZB3DMPw8l64JvIq8cm"], data: [{ age: 20, telephone: 752 }],}, methode: "update", };

  //{"getAll", "add", "delete"}
  let inputData = {
    data:  { id: "ss,xs,x,", nom: "kossi", prenom: "franfran" } ,
    methode: "getAll",
  };

  let after = (data) => {
    console.log(typeof data);
    console.log(data);
  };

  sendRequest(inputData, after);
}
