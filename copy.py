import streamlit as st
import cv2
import uuid

def show_cover_song_analyzer_page():
    st.title("Real-time Video Recorder")

    # Initialize OpenCV VideoCapture object
    video_capture = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not video_capture.isOpened():
        st.error("Error: Unable to open webcam.")
        return

    # Create a placeholder for the video player
    video_placeholder = st.empty()

    # Create a boolean variable to toggle recording state
    is_recording = False

    # Define a unique key for the button
    button_label = "Start/Stop Recording"
    button_key = f"{button_label}-{uuid.uuid4()}"

    # Create the recording button outside of the loop
    record_button = st.button(button_label, key=button_key)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = None

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Check if frame is captured successfully
        if not ret:
            st.error("Error: Unable to capture frame.")
            break

        # Display the frame
        video_placeholder.image(frame, channels="BGR")

        # Check if the recording button is clicked
        if record_button:
            if is_recording:
                # Stop recording
                st.success("Recording stopped.")
                is_recording = False
                # Release the video writer
                out.release()
            else:
                # Start recording
                st.success("Recording started.")
                is_recording = True
                # Create VideoWriter object if not already created
                if out is None:
                    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame.shape[1], frame.shape[0]))

        # Record video if the recording button is pressed
        if is_recording:
            # Write the frame to video file
            out.write(frame)

    # Release the VideoCapture object
    video_capture.release()

    # Release the VideoWriter object
    if out is not None:
        out.release()


