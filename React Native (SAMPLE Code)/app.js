/* NOTE: THIS IS SAMPLE CODE ONLY. It is a sample of what your app.js should look like in yout React Project.
   The React Native App should be created in a separate folder. Preferrably with Expo.
    */


import VideoStreamScreen from './app/screens/VideoStreamScreen';

import React from "react";
import { StyleSheet } from "react-native";

export default function App() {
    return <VideoStreamScreen/>;
}


var styles = StyleSheet.create({
  container: {
    backgroundColor: 'black',
    flex: 1,
  },
  backgroundVideo: {
    position: 'absolute',
    top: 0,
    left: 0,
    bottom: 0,
    right: 0,
  },
});