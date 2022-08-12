import cv2

# define face detector
detector = cv2.dnn.readNetFromTensorflow(
    'frozen_inference_graph.pb', 'graph.pbtxt')
ds_factor = 0.6

# list of classes from COCO Dataset
classes_90 = ["background", "person", "bicycle", "car", "motorcycle",
              "airplane", "bus", "train", "truck", "boat", "traffic light", "fire hydrant",
              "unknown", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse",
              "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "unknown", "backpack",
              "umbrella", "unknown", "unknown", "handbag", "tie", "suitcase", "frisbee", "skis",
              "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard",
              "surfboard", "tennis racket", "bottle", "unknown", "wine glass", "cup", "fork", "knife",
              "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog",
              "pizza", "donut", "cake", "chair", "couch", "potted plant", "bed", "unknown", "dining table",
              "unknown", "unknown", "toilet", "unknown", "tv", "laptop", "mouse", "remote", "keyboard",
              "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "unknown",
              "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]


class VideoCamera(object):
    def __init__(self):
        # capture video
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        # releasing cam
        self.video.release()

    def get_frame(self):
        # extract frames
        # Input image
        ret, img = self.video.read()
        rows = img.shape[0]
        cols = img.shape[1]

        # Use the given image as input, which needs to be blob(s).
        detector.setInput(cv2.dnn.blobFromImage(
            img, size=(300, 300), swapRB=True, crop=False))

        # Runs a forward pass to compute the net output
        networkOutput = detector.forward()

        # Loop on the outputs
        for detection in networkOutput[0, 0]:

            score = float(detection[2])
            if score > 0.2:

                prediction_class_index = int(detection[1])
                label = "{}: {:.2f}%".format(
                    classes_90[prediction_class_index], score * 100)

                left = detection[3] * cols
                top = detection[4] * rows
                right = detection[5] * cols
                bottom = detection[6] * rows

                # draw a red rectangle around detected objects
                cv2.rectangle(img, (int(left), int(top)), (int(
                    right), int(bottom)), (0, 0, 255), thickness=2)
                cv2.putText(img, label, (int(left), int(top)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

        # Show the image with a rectagle surrounding the detected objects
        ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes()
