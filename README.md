# Web Streaming a TensorFlow Object Detector to a React Native Mobile App

Note: This project was developed in Windows. The directory organization should stay the same, but Python module imports, virtual environment execution, and terminal commands might differ if implementing on other OS.

There are two components two major components to this:

### Using Transfer Learning with a TensorFlow Hub pre-trained object detection algorithm.
1. Creating a React Native mobile app which can remotely visualize the result.
2. Potential applications for a project like this:
* Smart surveillance camera system with object detection, motion detection, face-recognition, etc.
* You can easily deploy any pre-trained (or trained yourself) TensorFlow model from TensorFlow Hub to deploy to your mobile applications.
* React Native is flexible, the application is transferrable to Android, iOS, and Web Apps. So you can visualize your camera system remotely from many different devices.
* All the processing stays in one device. For example, this project could be deployed into a Raspberry Pi by simply using a TensorFlow Lite version of the model. The Raspberry Pi then would take care entirely of the processing. Meanwhile, the app on your phone merely visualizes the results from your computing device holding the camera. Note: The computing device with the camera doing the object recognition could be a laptop or even a phone. Your choice!


### React Native App
Please note that the code related to the React Native App is not the app itself. Rather it is a sample of what the two essential files in the project should look like.


Project References and Troubleshooting:
1. To create the virtual environment, follow the guide outlined in the official 'venv' site. https://docs.python.org/3/library/venv.html
2. To solve the potential issue of not being able to retrieve Tensorflow model labels/classes. IF using the COCO SSD MOBILENET V2 model, simply use a list of the classes. If you decide to deploy a different model, simply search the model documentation for the list of classes. Otherwise, if training your own model, make sure you can easily retrieve the class labels from the Python script in its Saved Model format. https://stackoverflow.com/questions/59397139/how-can-i-get-the-class-name-of-tensorflow-models-from-zoo
3. The structure of this project and Flask server handling are heavily inspired from this Medium guide: https://medium.datadriveninvestor.com/video-streaming-using-flask-and-opencv-c464bf8473d6. Note: After designing my own web server host to display the camera, and separately creating an object recognition script, I had trouble connecting both scripts, as I couldn't make the HTTP class compatible with OpenCV. I compromised for using Flask which is compatible with OpenCV and this guide helped with that. However, it does not utilize a TensorFlow model, for which I had to change the structure of the directory quite a bit as well as the main function.
4. To learn how to read a TensorFlow model with OpenCV, I followed this useful guide: https://jeanvitor.com/tensorflow-object-detecion-opencv/. Please note though, that it does not retrieve the class labels from the output of the model, nor does the explain how to navigate this output directory.
5. To cross reference the methodology from the previous ref, this guide does something similar. https://automaticaddison.com/how-to-load-a-tensorflow-model-using-opencv/
6. The model I used from TensorFlow Hub: https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2.


# Project Usage
### React Native
I created my React Native App with expo, simply with expo init YourAppName. Which initializes a blank RN project folder.

To run the react native app on a mobile device, you can either use a RN emulator or a physical device (but you will need the Expo Go App). If using Expo, this can be done by running `expo start`.

After running you should be able to visualize the output of your camera with object detection remotely from your phone.

### Object Detection
First create a virtual environment with virtualenv, to ensure that all your project libraries do not affect the rest of your local imports. You can find the guide on this in the link above.

In Windows you activate your virtualenv by going directly into the "your_virtual_env/Scripts" folder and running the `activate.bat` command. To deactivate, simply type `deactivate` in the same directory in the terminal.

Download all files necessary under one main project folder, following a similar structure to mine. Or simply create your own.

To execute the python scripts just run `python main.py` and the Flask server will start running. It will print out your IP at port 5000 in which you can open a localhost in your web browser to test your app.

Note: If making changes to the file while the script is running, it will update automatically without having to run it again. All you need to do is restart the localhost in your web browser.


# Challenges and Current Problems

* As of now this project requires a shared WiFi connection between mobile device and computer running the object detection (whether it's a laptop or a Raspberry Pi). Limiting the capability and range of the project.

* This project does not yet address the Flask settings for allowing multiple devices to access the server port. This is not an issue when setting up a server through the HTTP class, however, the Flask server tends to crash if multiple devices access the port at once.


