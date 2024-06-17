import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, RTCConfiguration
import cv2

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

class VideoTransformer(VideoTransformerBase):
    frame_lock: st.session_state  # Use Streamlit session_state to store the frame

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        if self.frame_lock.save_frame:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
            st.session_state['captured_image'] = img  # Save the frame to session_state
            self.frame_lock.save_frame = False

        return img

def show_buttons():
    st.title('Voter Roadmap')
    col1, col2 = st.columns(2)
    with col1:
        if st.button('#DressTheVote'):
            st.session_state.current_page = 'webcam1'
        if st.button('#FoodForVote'):
            st.session_state.current_page = 'webcam2'
    with col2:
        if st.button('#MeetUrSenator'):
            st.session_state.current_page = 'webcam3'
        if st.button('#GoVote'):
            st.session_state.current_page = 'webcam4'
    # Display the captured image if it exists
    if 'captured_image' in st.session_state:
        st.image(st.session_state['captured_image'], caption='Captured Image', width=300)

def show_webcam(key):
    if st.button("Go Back"):
        st.session_state.current_page = 'buttons'
    
    st.write("Click 'Capture' to take a photo.")
    if st.button("Capture"):
        st.session_state.save_frame = True

    webrtc_streamer(key=key, video_processor_factory=VideoTransformer, rtc_configuration=RTC_CONFIGURATION)

if 'current_page' not in st.session_state:
    st.session_state.current_page = 'buttons'
    st.session_state.save_frame = False

if st.session_state.current_page == 'buttons':
    show_buttons()
    if 'captured_image' in st.session_state:
        st.image(st.session_state['captured_image'], caption='Captured Image', width=300)
elif st.session_state.current_page.startswith('webcam'):
    show_webcam(st.session_state.current_page)

