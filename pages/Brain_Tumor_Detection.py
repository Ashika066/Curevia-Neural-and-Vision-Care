import streamlit as st
import sys
sys.path.append('..')
from utils.brain_predictor import BrainTumorPredictor
from utils.recommendations import get_brain_recommendation
import tempfile
from PIL import Image

st.set_page_config(
    page_title="Brain Tumor Detection - CUREVIA",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .result-box {
        background-color: #f0e8f8;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #7B2CBF;
    }
</style>
""", unsafe_allow_html=True)

# Page header
st.title("🧠 Brain MRI Analysis Platform")
st.markdown("### AI-Powered Brain Tumor Detection System")

# Sidebar navigation
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox(
    "Select Section",
    ["Home", "About", "Tumor Detection"]
)

# Initialize predictor (cached)
@st.cache_resource
def load_brain_model():
    return BrainTumorPredictor("models/brain_tumor/my_model.keras")

# HOME Section
if app_mode == "Home":
    st.markdown("""
    ## **Brain MRI Analysis Platform**

    #### **Welcome to the Brain Tumor Detection Platform**

    **Magnetic Resonance Imaging (MRI)** is the gold standard for brain tumor detection and monitoring. 
    Our AI-powered platform assists healthcare professionals in analyzing brain MRI scans to detect the 
    presence of tumors with high accuracy.

    ##### **Why Brain MRI Analysis Matters**
    Early detection of brain tumors is crucial for successful treatment outcomes. Traditional manual 
    analysis of MRI scans is time-consuming and requires expert radiologists. Our platform uses advanced 
    deep learning algorithms to provide rapid, accurate preliminary screening.

    ---

    #### **Key Features of the Platform**

    - **Automated Tumor Detection**: Advanced AI model trained on thousands of brain MRI scans
    - **High-Resolution Analysis**: Processes detailed MRI images for accurate detection
    - **Instant Results**: Get predictions within seconds
    - **Confidence Scoring**: Each prediction includes a confidence percentage
    - **Expert Recommendations**: Detailed next steps and medical guidance

    ---

    #### **Understanding Brain Tumors**

    **Brain tumors** are abnormal growths of cells in the brain. They can be:

    1. **Benign (Non-cancerous)**
       - Grow slowly
       - Don't spread to other parts of the body
       - Can still cause problems due to location and size

    2. **Malignant (Cancerous)**
       - Grow rapidly
       - May invade nearby tissues
       - Require immediate medical attention

    ---

    #### **Detection Categories**

    Our AI model is trained to classify MRI scans into:
    - **Tumor Detected**: Presence of abnormal growth
    - **No Tumor**: Normal brain tissue

    ---

    #### **Clinical Applications**

    - **Screening Tool**: Rapid preliminary assessment of MRI scans
    - **Second Opinion**: Support for radiological diagnoses
    - **Monitoring**: Track tumor progression over time
    - **Research**: Assist in clinical research and studies

    ---

    #### **Get Started**

    Navigate to the **Tumor Detection** section to upload and analyze brain MRI scans.

    ---

    *This platform is designed to assist medical professionals and should not replace expert clinical judgment.*
    """)

# ABOUT Section
elif app_mode == "About":
    st.header("About")
    st.markdown("""
    #### About Brain Tumor Detection

    - Brain tumors are abnormal growths inside the brain.
    - MRI (Magnetic Resonance Imaging) is the primary tool used for detecting tumors.
    - MRI provides clear cross-sectional images of brain tissues.
    - Tumors often appear as:
        - Irregular mass
        - Swelling (edema)
        - Distorted brain structure
        - Abnormal tissue density

    ---

    #### About the Dataset

    - Contains **thousands of MRI scans**.
    - Two main classes:
        - **Tumor**
        - **No Tumor**
    - Images collected from multiple public datasets.
    - Verified and labeled by trained radiologists.
    - Includes different MRI sequences for better model robustness.
    - Divided into **train, test, and validation** folders.

    ---

    #### Model Architecture

    - Based on a **Convolutional Neural Network (CNN)**.
    - Trained using:
        - Labeled MRI images
        - Data augmentation techniques
    - Validated on a separate dataset.
    - Designed for high accuracy and fast prediction.

    ---

    #### Clinical Validation

    - Tested on diverse patient groups.
    - Cross-checked with expert radiologist diagnoses.
    - Evaluated on multiple tumor types and sizes.
    - Optimized for real-world performance.

    ---

    #### Disclaimer

    - This AI tool is meant as a **support system**, not a replacement.
    - All results should be:
        - Verified by radiologists
        - Supported by clinical tests
        - Reviewed with patient history

    ---

    #### Data Privacy & Security

    - Uploaded images are processed temporarily.
    - No personal data is stored.
    - Secure and confidential workflow.
    """)

# TUMOR DETECTION Section
elif app_mode == "Tumor Detection":
    st.header("🔍 Brain Tumor Detection")
    st.markdown("Upload a brain MRI scan for AI-powered tumor detection")
    
    # File uploader
    test_image = st.file_uploader(
        "Choose an MRI image...", 
        type=["jpg", "jpeg", "png"],
        help="Upload a clear brain MRI scan in JPG or PNG format"
    )
    
    # Display uploaded image
    if test_image is not None:
        image = Image.open(test_image)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📤 Uploaded MRI Scan")
            st.image(image, use_column_width=True, caption="Brain MRI")
        
        with col2:
            st.subheader("🤖 AI Analysis")
            
            # Predict button
            if st.button("🔬 Analyze MRI Scan", type="primary", use_container_width=True):
                with st.spinner("🧠 AI is analyzing your brain MRI scan..."):
                    # Save to temporary file
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
                        tmp_file.write(test_image.getvalue())
                        temp_file_path = tmp_file.name
                    
                    # Load model and predict
                    predictor = load_brain_model()
                    result = predictor.predict(temp_file_path)
                    
                    result_index = result['class_index']
                    class_name = result['class_name']
                    confidence = result['confidence']
                    
                    # Display results
                    st.markdown('<div class="result-box">', unsafe_allow_html=True)
                    st.success(f"✅ Analysis Complete!")
                    
                    # Format class name for display
                    display_name = class_name.title() if class_name != 'notumor' else 'No Tumor'
                    st.metric("Detection Result", display_name, delta=None)
                    st.metric("Confidence Level", f"{confidence:.1%}", delta=None)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Progress bar for confidence
                    st.progress(confidence)
                    
                    # Color-coded alert based on tumor type
                    if class_name == 'notumor':
                        st.success("✅ **NO TUMOR DETECTED** - Normal brain tissue identified")
                    elif class_name == 'glioma':
                        st.error("⚠️ **GLIOMA DETECTED** - Immediate medical consultation required")
                    elif class_name == 'meningioma':
                        st.warning("⚠️ **MENINGIOMA DETECTED** - Prompt medical evaluation recommended")
                    elif class_name == 'pituitary':
                        st.warning("⚠️ **PITUITARY TUMOR DETECTED** - Specialized consultation needed")
                    
                    # Recommendation section
                    st.markdown("---")
                    with st.expander("📋 **Medical Recommendations & Next Steps**", expanded=True):
                        # Get condition-specific description
                        if class_name == 'glioma':
                            st.write("**Analysis Result:** MRI scan shows signs consistent with *Glioma* (brain tumor originating from glial cells).")
                        elif class_name == 'meningioma':
                            st.write("**Analysis Result:** MRI scan shows signs consistent with *Meningioma* (tumor of the meninges).")
                        elif class_name == 'notumor':
                            st.write("**Analysis Result:** MRI scan shows *normal brain tissue without tumor indication*.")
                        elif class_name == 'pituitary':
                            st.write("**Analysis Result:** MRI scan shows signs consistent with *Pituitary Tumor* (tumor of the pituitary gland).")
                        
                        st.image(image, use_column_width=True)
                        
                        # Display recommendations
                        recommendation = get_brain_recommendation(result_index)
                        st.markdown(recommendation)
                        
                        # Critical warning for tumor cases
                        if class_name != 'notumor':
                            st.error("""
                            🚨 **URGENT NOTICE**: 
                            - This is a preliminary AI screening result
                            - **Immediate consultation with a neurologist or neurosurgeon is essential**
                            - Additional diagnostic tests and imaging will be required
                            - Do not delay seeking professional medical evaluation
                            """)
                        else:
                            st.info("""
                            ℹ️ **Notice**: 
                            - While no tumor was detected, this does not guarantee absence of all conditions
                            - Continue regular check-ups as recommended by your healthcare provider
                            - Report any new or worsening symptoms immediately
                            """)
    
    else:
        st.info("👆 Please upload a brain MRI scan image to begin analysis")
        
        # Sample instructions
        st.markdown("""
        ### 📝 Instructions:
        1. Upload a clear brain MRI scan image
        2. Click the "Analyze MRI Scan" button
        3. Review the AI prediction and confidence score
        4. Read the detailed medical recommendations
        5. **Immediately consult with a neurologist if tumor is detected**
        
        ### 🎯 Image Requirements:
        - Clear, high-quality MRI scan
        - Supported formats: JPG, PNG
        - Preferred: T1-weighted or T2-weighted MRI sequences
        - Minimal artifacts or motion blur
        
        ### 🧠 Detectable Conditions:
        - **Glioma**: Tumor from glial cells
        - **Meningioma**: Tumor of the meninges
        - **Pituitary Tumor**: Tumor of pituitary gland
        - **No Tumor**: Normal brain tissue
        """)

# Footer
st.sidebar.markdown("---")
st.sidebar.info("""
**Detection Categories:**
- 🔴 Glioma (Urgent)
- 🟡 Meningioma (Important)
- 🟡 Pituitary Tumor (Important)
- 🟢 No Tumor (Normal)

**Confidence Levels:**
- 90%+ : High confidence
- 70-89%: Moderate confidence
- <70%: Low confidence (review needed)
""")

st.sidebar.warning("""
⚠️ **Important Reminder:**
This tool provides preliminary screening only. 
Always consult qualified medical professionals 
for diagnosis and treatment decisions.
""")

# Footer
st.sidebar.markdown("---")
st.sidebar.info("""
**Detection Categories:**
- 🔴 Tumor Detected
- 🟢 No Tumor (Normal)

**Confidence Levels:**
- 90%+ : High confidence
- 70-89%: Moderate confidence
- <70%: Low confidence (review needed)
""")

st.sidebar.warning("""
⚠️ **Important Reminder:**
This tool provides preliminary screening only. 
Always consult qualified medical professionals 
for diagnosis and treatment decisions.
""")
