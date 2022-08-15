import React from "react";
import { StyleSheet, View } from "react-native";
import { WebView } from 'react-native-webview';

// Within your render function, assuming you have a file called
// "background.mp4" in your project. You can include multiple videos
// on a single screen if you like.

function VideoStreamScreen() {
  return(
    <View style={styles.container}>
      <WebView
          style={styles.backgroundVideo}
          automaticallyAdjustContentInsets={true}
          scalesPageToFit={true}
          startInLoadingState={false}
          contentInset={{top: 0, right: 0, left: 0, bottom: 0}}
          scrollEnabled={false}
          // When you run your Flask server you should see an IP URI
          source={{ uri: 'http://YOUR.IP.ADD.HERE:5000' }}/>
    </View>
  );
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

export default VideoStreamScreen;