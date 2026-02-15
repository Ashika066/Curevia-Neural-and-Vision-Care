import streamlit as st
import sys
sys.path.append('..')
from utils.eye_predictor import EyeDiseasePredictor
from utils.recommendations import get_eye_recommendation
import tempfile
from PIL import Image

st.set_page_config(
    page_title="Eye Disease Detection - CUREVIA",
    page_icon="👁️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .result-box {
        background-color: #e8f4f8;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2E86AB;
    }
</style>
""", unsafe_allow_html=True)

# Page header
st.title("👁️ OCT Retinal Analysis Platform")
st.markdown("### AI-Powered Eye Disease Detection System")

# Sidebar navigation
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox(
    "Select Section",
    ["Home", "About", "Disease Identification"]
)

# Initialize predictor (cached)
@st.cache_resource
def load_eye_model():
    return EyeDiseasePredictor("models/eye_disease/Trained_Model.keras")

# HOME Section
if app_mode == "Home":
    st.markdown("""
    ## **OCT Retinal Analysis Platform**

    #### **Welcome to the Retinal OCT Analysis Platform**

    **Optical Coherence Tomography (OCT)** is a powerful imaging technique that provides high-resolution cross-sectional images of the retina, allowing for early detection and monitoring of various retinal diseases. Each year, over 30 million OCT scans are performed, aiding in the diagnosis and management of eye conditions that can lead to vision loss, such as choroidal neovascularization (CNV), diabetic macular edema (DME), and age-related macular degeneration (AMD).

    ##### **Why OCT Matters**
    OCT is a crucial tool in ophthalmology, offering non-invasive imaging to detect retinal abnormalities. On this platform, we aim to streamline the analysis and interpretation of these scans, reducing the time burden on medical professionals and increasing diagnostic accuracy through advanced automated analysis.

    ---

    #### **Key Features of the Platform**

    - **Automated Image Analysis**: Our platform uses state-of-the-art machine learning models to classify OCT images into distinct categories: **Normal**, **CNV**, **DME**, and **Drusen**.
    - **Cross-Sectional Retinal Imaging**: Examine high-quality images showcasing both normal retinas and various pathologies, helping doctors make informed clinical decisions.
    - **Streamlined Workflow**: Upload, analyze, and review OCT scans in a few easy steps.

    ---

    #### **Understanding Retinal Diseases through OCT**

    1. **Choroidal Neovascularization (CNV)**
       - Neovascular membrane with subretinal fluid
       
    2. **Diabetic Macular Edema (DME)**
       - Retinal thickening with intraretinal fluid
       
    3. **Drusen (Early AMD)**
       - Presence of multiple drusen deposits

    4. **Normal Retina**
       - Preserved foveal contour, absence of fluid or edema

    ---

    #### **About the Dataset**

    Our dataset consists of **84,495 high-resolution OCT images** (JPEG format) organized into **train, test, and validation** sets, split into four primary categories:
    - **Normal**
    - **CNV**
    - **DME**
    - **Drusen**

    Each image has undergone multiple layers of expert verification to ensure accuracy in disease classification. The images were obtained from various renowned medical centers worldwide and span across a diverse patient population, ensuring comprehensive coverage of different retinal conditions.

    ---

    #### **Get Started**

    - **Upload OCT Images**: Begin by uploading your OCT scans for analysis.
    - **Explore Results**: View categorized scans and detailed diagnostic insights.
    - **Learn More**: Dive deeper into the different retinal diseases and how OCT helps diagnose them.

    ---

    #### **Contact Us**

    Have questions or need assistance? Contact our support team for more information on how to use the platform or integrate it into your clinical practice.
    """)

# ABOUT Section
elif app_mode == "About":
    st.header("About")
    st.markdown("""
    #### About Dataset
    Retinal optical coherence tomography (OCT) is an imaging technique used to capture high-resolution cross sections of the retinas of living patients. 
    Approximately 30 million OCT scans are performed each year, and the analysis and interpretation of these images takes up a significant amount of time.
    
    (A) (Far left) choroidal neovascularization (CNV) with neovascular membrane (white arrowheads) and associated subretinal fluid (arrows). 
    (Middle left) Diabetic macular edema (DME) with retinal-thickening-associated intraretinal fluid (arrows). 
    (Middle right) Multiple drusen (arrowheads) present in early AMD. 
    (Far right) Normal retina with preserved foveal contour and absence of any retinal fluid/edema.

    ---

    #### Content
    The dataset is organized into 3 folders (train, test, val) and contains subfolders for each image category (NORMAL, CNV, DME, DRUSEN). 
    There are 84,495 X-Ray images (JPEG) and 4 categories (NORMAL, CNV, DME, DRUSEN).

    Images are labeled as (disease)-(randomized patient ID)-(image number by this patient) and split into 4 directories: CNV, DME, DRUSEN, and NORMAL.

    Optical coherence tomography (OCT) images (Spectralis OCT, Heidelberg Engineering, Germany) were selected from retrospective cohorts of adult patients from the Shiley Eye Institute of the University of California San Diego, the California Retinal Research Foundation, Medical Center Ophthalmology Associates, the Shanghai First People's Hospital, and Beijing Tongren Eye Center between July 1, 2013 and March 1, 2017.

    Before training, each image went through a tiered grading system consisting of multiple layers of trained graders of increasing expertise for verification and correction of image labels. Each image imported into the database started with a label matching the most recent diagnosis of the patient. The first tier of graders consisted of undergraduate and medical students who had taken and passed an OCT interpretation course review. This first tier of graders conducted initial quality control and excluded OCT images containing severe artifacts or significant image resolution reductions. The second tier of graders consisted of four ophthalmologists who independently graded each image that had passed the first tier. The presence or absence of choroidal neovascularization (active or in the form of subretinal fibrosis), macular edema, drusen, and other pathologies visible on the OCT scan were recorded. Finally, a third tier of two senior independent retinal specialists, each with over 20 years of clinical retina experience, verified the true labels for each image. The dataset selection and stratification process is displayed in a CONSORT-style diagram in Figure 2B. To account for human error in grading, a validation subset of 993 scans was graded separately by two ophthalmologist graders, with disagreement in clinical labels arbitrated by a senior retinal specialist.
    """)

# DISEASE IDENTIFICATION Section
elif app_mode == "Disease Identification":
    st.header("🔍 Disease Identification")
    st.markdown("Upload an OCT retinal scan for AI-powered analysis")
    
    # File uploader
    test_image = st.file_uploader(
        "Choose an OCT image...", 
        type=["jpg", "jpeg", "png"],
        help="Upload a clear OCT scan image in JPG or PNG format"
    )
    
    # Display uploaded image
    if test_image is not None:
        image = Image.open(test_image)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📤 Uploaded Image")
            st.image(image, use_column_width=True, caption="OCT Scan")
        
        with col2:
            st.subheader("🤖 AI Analysis")
            
            # Predict button
            if st.button("🔬 Analyze Image", type="primary", use_container_width=True):
                with st.spinner("🧠 AI is analyzing your OCT scan..."):
                    # Save to temporary file
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
                        tmp_file.write(test_image.getvalue())
                        temp_file_path = tmp_file.name
                    
                    # Load model and predict
                    predictor = load_eye_model()
                    result = predictor.predict(temp_file_path)
                    
                    result_index = result['class_index']
                    class_name = result['class_name']
                    confidence = result['confidence']
                    
                    # Display results
                    st.markdown('<div class="result-box">', unsafe_allow_html=True)
                    st.success(f"✅ Analysis Complete!")
                    st.metric("Detected Condition", class_name, delta=None)
                    st.metric("Confidence Level", f"{confidence:.1%}", delta=None)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Progress bar for confidence
                    st.progress(confidence)
                    
                    # Recommendation section
                    st.markdown("---")
                    with st.expander("📋 **Medical Recommendations & Information**", expanded=True):
                        # Get condition-specific description
                        if result_index == 0:  # CNV
                            st.write("**Detected Condition:** OCT scan showing *CNV with subretinal fluid.*")
                        elif result_index == 1:  # DME
                            st.write("**Detected Condition:** OCT scan showing *DME with retinal thickening and intraretinal fluid.*")
                        elif result_index == 2:  # DRUSEN
                            st.write("**Detected Condition:** OCT scan showing *drusen deposits in early AMD.*")
                        elif result_index == 3:  # NORMAL
                            st.write("**Detected Condition:** OCT scan showing a *normal retina with preserved foveal contour.*")
                        
                        st.image(image, use_column_width=True)
                        
                        # Display recommendations
                        recommendation = get_eye_recommendation(result_index)
                        st.markdown(recommendation)
                        
                        # Warning
                        st.warning("⚠️ **Important**: This AI analysis is a screening tool and should not replace professional medical diagnosis. Please consult with a qualified ophthalmologist for proper evaluation and treatment.")
    
    else:
        st.info("👆 Please upload an OCT retinal scan image to begin analysis")
        
        # Sample instructions
        st.markdown("""
        ### 📝 Instructions:
        1. Upload a clear OCT retinal scan image
        2. Click the "Analyze Image" button
        3. Review the AI prediction and confidence score
        4. Read the detailed medical recommendations
        5. Consult with your ophthalmologist for proper diagnosis
        """)

# Footer
st.sidebar.markdown("---")
st.sidebar.info("""
**Eye Disease Categories:**
- CNV (Choroidal Neovascularization)
- DME (Diabetic Macular Edema)
- Drusen (Early AMD)
- Normal Retina
""")
