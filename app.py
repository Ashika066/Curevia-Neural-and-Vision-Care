import streamlit as st

st.set_page_config(
    page_title="CUREVIA - Medical AI Platform",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 5rem;
        font-weight: bold;
        text-align: center;
        color: #56719A;
    }
    .sub-header {
        font-size: 1.4rem;
        text-align: center;
        color: #c8cdd6;
        margin-bottom: 1rem;
    }
    .feature-box {
        color: #404040;
        background-color: #c8cdd6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .feature-box h3 {
        color: #2A3E57 !important;
            font-weight: 900 !important;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<p class="main-header">🏥 CUREVIA</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-Powered Medical Disease Detection Platform</p>', unsafe_allow_html=True)

# Introduction
st.markdown("""
Welcome to **CUREVIA**, a comprehensive AI-powered medical diagnosis platform that leverages advanced 
deep learning models to assist healthcare professionals in detecting and analyzing various medical conditions.

---
""")

# Two columns for the detection systems
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-box">
    
    ### 👁️ Eye Disease Detection
    
    Analyze Optical Coherence Tomography (OCT) images to detect:
    - **CNV** (Choroidal Neovascularization)
    - **DME** (Diabetic Macular Edema)
    - **Drusen** (Early AMD)
    - **Normal** Retina
    
    Uses state-of-the-art MobileNetV3 architecture trained on 84,495 high-resolution OCT images.
    
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
    
    ### 🧠 Brain Tumor Detection
    
    Analyze MRI scans to detect:             
    - **Glioma**
    - **Meningioma**
    - **Pituitary**
    - **NoTumor** (Normal Brain)
    
    Advanced deep learning model trained on thousands of brain MRI scans for accurate detection.
    
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# How to Use section
st.markdown("""
## 🚀 How to Use CUREVIA

1. **Select a Detection System** from the sidebar
   - Choose between Eye Disease Detection or Brain Tumor Detection
   
2. **Upload Medical Image**
   - Upload OCT scans for eye disease analysis
   - Upload MRI scans for brain tumor analysis
   
3. **Get Instant AI Analysis**
   - Receive predictions with confidence scores
   - View detailed medical recommendations
   - Learn more about detected conditions

---

## 📊 Platform Statistics

""")

# Statistics
stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

with stat_col1:
    st.metric("Detection Systems", "2", delta="Growing")

with stat_col2:
    st.metric("Disease Categories", "8+", delta="Expanding")

with stat_col3:
    st.metric("Training Images", "92K+", delta="Increasing")

with stat_col4:
    st.metric("Accuracy", "94%+", delta="Improving")

st.markdown("---")

# Key Features
st.markdown("""
## ✨ Key Features

- **Multi-Disease Detection**: Comprehensive platform for various medical imaging analyses
- **High Accuracy**: State-of-the-art deep learning models with 95%+ accuracy
- **Instant Results**: Real-time predictions with detailed confidence scores
- **Medical Recommendations**: Expert-backed treatment and monitoring guidelines
- **User-Friendly Interface**: Simple upload and analysis workflow
- **Detailed Insights**: Comprehensive information about detected conditions

---

## 🎯 Getting Started

**Select a detection system from the sidebar to begin your analysis** ➡️

Choose from:
- 👁️ **Eye Disease Detection** - For OCT retinal scans
- 🧠 **Brain Tumor Detection** - For MRI brain scans

---

## 📞 Support & Contact

Have questions or need assistance? Our platform is designed for healthcare professionals and researchers. 
For technical support or integration inquiries, please contact our support team.

---

*CUREVIA - Empowering Healthcare with Artificial Intelligence*
""")

# Sidebar
st.sidebar.success("👆 Select a detection system above to get started")
st.sidebar.markdown("---")
st.sidebar.info("""
**Quick Navigation:**
- 🏠 Home (Current Page)
- 👁️ Eye Disease Detection
- 🧠 Brain Tumor Detection
""")