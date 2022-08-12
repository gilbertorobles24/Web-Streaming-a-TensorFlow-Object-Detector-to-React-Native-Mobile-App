# Web Streaming a TensorFlow Object Detector to a React Native Mobile App
There are two components two major components to this:

Using Transfer Learning with a TensorFlow Hub pre-trained object detection algorithm.
1. Creating a React Native mobile app which can remotely visualize the result.
2. Potential applications for a project like this:
* Smart surveillance camera system with object detection, motion detection, face-recognition, etc.
* You can easily deploy any pre-trained (or trained yourself) TensorFlow model from TensorFlow Hub to deploy to your mobile applications.
* React Native is flexible, the application is transferrable to Android, iOS, and Web Apps. So you can visualize your camera system remotely from many different devices.
* All the processing stays in one device. For example, this project could be deployed into a Raspberry Pi by simply using a TensorFlow Lite version of the model. The Raspberry Pi then would take care entirely of the processing. Meanwhile, the app on your phone merely visualizes the results from your computing device holding the camera. Note: The computing device with the camera doing the object recognition could be a laptop or even a phone. Your choice!
