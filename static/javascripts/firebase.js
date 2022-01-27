

  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.4/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.6.4/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyBKRcEmfQfEzC4jFZY9UQBO5q5PxqpLiFQ",
    authDomain: "openclasserom-test.firebaseapp.com",
    databaseURL: "https://openclasserom-test.firebaseio.com",
    projectId: "openclasserom-test",
    storageBucket: "openclasserom-test.appspot.com",
    messagingSenderId: "559211486046",
    appId: "1:559211486046:web:1ef78bb5c769a746068dcf",
    measurementId: "G-9NZ12NJVQ6"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);