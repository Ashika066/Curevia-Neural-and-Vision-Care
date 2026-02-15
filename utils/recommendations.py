"""
Medical recommendations for detected conditions.
"""

# Eye Disease Recommendations (keep your existing ones)
EYE_RECOMMENDATIONS = {
    0: """**For CNV (Choroidal Neovascularization)**:
- **Recommendation**: 
    - **Immediate Referral**: Seek prompt evaluation by a retinal specialist. CNV is often associated with conditions like age-related macular degeneration (AMD) and can lead to significant vision loss if left untreated.
    - **Treatment Options**: 
      - **Anti-VEGF Therapy**: Anti-vascular endothelial growth factor (anti-VEGF) injections such as Ranibizumab or Aflibercept are commonly used to halt or slow the progression of CNV.
      - **Photodynamic Therapy (PDT)**: In some cases, photodynamic therapy may be used alongside anti-VEGF injections.
      - **Laser Treatment**: Though less commonly used now, laser therapy may be recommended in certain situations.
    - **Lifestyle and Monitoring**: 
      - **Diet**: A diet rich in leafy greens, omega-3 fatty acids, and antioxidants (e.g., lutein, zeaxanthin) can help support retinal health.
      - **Supplements**: Consider supplements such as AREDS2 formulation for patients with AMD.
      - **Regular Monitoring**: Repeat OCT scans every 1 to 3 months to assess response to treatment and progression of disease.
    - **Next Steps**: 
      - Schedule immediate follow-up with a retina specialist.
      - If receiving anti-VEGF injections, expect regular treatments initially, with the frequency tapering as the condition stabilizes.
""",
    
    1: """**For DME (Diabetic Macular Edema)**:
- **Recommendation**:
    - **Endocrinology Consultation**: In addition to ophthalmic care, close coordination with an endocrinologist is essential to manage systemic diabetes, which directly impacts the progression of DME.
    - **Treatment Options**: 
      - **Anti-VEGF Injections**: Similar to CNV, anti-VEGF therapy is the first-line treatment to reduce retinal swelling and improve vision.
      - **Corticosteroid Implants**: In cases where anti-VEGF is less effective, intravitreal steroid injections or implants may be considered.
      - **Laser Photocoagulation**: Focal or grid laser therapy may be used to treat areas of leakage, especially in non-central-involved DME.
    - **Blood Sugar and Blood Pressure Control**: 
      - **Strict Glycemic Control**: Keeping HbA1c levels below 7% is crucial to slowing the progression of diabetic retinopathy and macular edema.
      - **Blood Pressure Management**: Hypertension worsens DME; aim to maintain a blood pressure below 140/80 mmHg.
    - **Monitoring**:
      - **Frequent Eye Exams**: Patients with DME require regular OCT scans (every 3 to 6 months) to monitor fluid accumulation and treatment response.
      - **Diabetes Management**: Tight control of blood sugar and blood pressure levels will help prevent future episodes of macular edema.
    - **Next Steps**: 
      - Schedule a visit with both your retina specialist and endocrinologist.
      - Begin or continue anti-VEGF treatment as needed, and ensure systemic conditions are tightly managed.
""",
    
    2: """**For Drusen (Early AMD)**:
- **Recommendation**:
    - **Dietary Changes**: 
      - **High in Antioxidants**: Incorporate foods rich in vitamins C, E, zinc, copper, and beta-carotene, which can help slow the progression of AMD. Spinach, kale, and fish rich in omega-3s are beneficial.
      - **Supplements**: The **AREDS2** (Age-Related Eye Disease Study 2) formulation is recommended for patients at moderate to high risk of progression to advanced AMD.
    - **Lifestyle Modifications**: 
      - **Quit Smoking**: Smoking greatly increases the risk of AMD progression and should be avoided.
      - **UV Protection**: Wear sunglasses with UV protection to reduce retinal damage from harmful sunlight exposure.
    - **Monitoring**:
      - **Regular OCT Scans**: For early AMD or drusen, repeat OCT imaging every 6 to 12 months to track changes in retinal structure.
      - **Amsler Grid Monitoring**: Use an Amsler grid at home to self-monitor for sudden vision changes, such as wavy lines or blank spots, which could indicate progression to wet AMD.
    - **Next Steps**:
      - Discuss AREDS2 supplements and lifestyle changes with your healthcare provider.
      - Schedule routine OCT scans to monitor drusen size and any potential advancement of AMD.
""",
    
    3: """**For Normal Retina**:
- **Recommendation**: 
    - **Routine Eye Care**: While your OCT scan shows a normal retina, it's essential to maintain regular eye exams, particularly if you have risk factors like a family history of retinal diseases.
    - **Eye Health Maintenance**:
      - **Balanced Diet**: Continue a diet rich in nutrients that support eye health, such as dark leafy greens, fish high in omega-3 fatty acids, and foods rich in antioxidants.
      - **Sun Protection**: Wear sunglasses with UV protection to minimize the risk of retinal damage from sunlight.
    - **Next Steps**:
      - If you have no symptoms or vision problems, follow up with routine eye exams as recommended by your ophthalmologist (typically every 1 to 2 years).
      - Maintain general health practices, including managing conditions like diabetes or hypertension that could affect retinal health.
"""
}

# Brain Tumor Recommendations (updated with 4 classes)
BRAIN_RECOMMENDATIONS = {
    0: """**For Glioma Detected**:
- **🚨 URGENT RECOMMENDATION**:
    - **Immediate Medical Consultation**: Schedule an urgent appointment with a neurologist or neurosurgeon within 24-48 hours.
    - **Do Not Delay**: Gliomas are brain tumors that require prompt evaluation and treatment planning.
    
- **About Gliomas**:
    - Gliomas are tumors that arise from glial cells in the brain
    - They can range from low-grade (slow-growing) to high-grade (aggressive)
    - Treatment depends on grade, location, and patient factors
    
- **Diagnostic Next Steps**:
    - **Comprehensive MRI**: Additional MRI sequences with contrast for detailed characterization
    - **Biopsy/Surgery**: Tissue sample needed to determine exact type and grade
    - **Neurological Examination**: Complete assessment by a specialist
    - **Molecular Testing**: Genetic markers to guide treatment decisions
    
- **Treatment Options** (Specialist will determine):
    - **Surgery**: Maximal safe resection of the tumor
    - **Radiation Therapy**: External beam radiation or specialized techniques
    - **Chemotherapy**: Temozolomide or other agents based on tumor type
    - **Targeted Therapy**: Based on molecular profile
    - **Clinical Trials**: Access to newest treatment approaches
    
- **Specialist Referrals Required**:
    - **Neurosurgeon**: For surgical evaluation
    - **Neuro-oncologist**: Specialized cancer treatment
    - **Radiation Oncologist**: For radiation planning
    - **Neuropsychologist**: Cognitive support
    
- **Next Steps**:
    - Contact neurologist/neurosurgeon immediately
    - Gather all previous imaging and medical records
    - Prepare list of symptoms and their timeline
    - Consider second opinion at specialized center

⚠️ **CRITICAL**: This AI detection requires immediate medical confirmation. Gliomas need expert evaluation and individualized treatment planning.
""",
    
    1: """**For Meningioma Detected**:
- **⚠️ IMPORTANT RECOMMENDATION**:
    - **Prompt Medical Consultation**: Schedule appointment with neurologist or neurosurgeon within 1-2 weeks
    - **Not Always Urgent**: Many meningiomas are slow-growing, but evaluation is still essential
    
- **About Meningiomas**:
    - Tumors that arise from meninges (protective membranes covering brain)
    - Usually benign (non-cancerous) - about 90% of cases
    - Slow-growing in most cases
    - Treatment depends on size, location, and symptoms
    
- **Diagnostic Next Steps**:
    - **Enhanced MRI**: Contrast-enhanced imaging for detailed assessment
    - **CT Scan**: May be needed to assess bone involvement
    - **Neurological Examination**: Evaluate for any neurological deficits
    - **Serial Imaging**: Sometimes watchful waiting with regular monitoring
    
- **Treatment Options** (Based on specific case):
    - **Observation**: "Watch and wait" for small, asymptomatic meningiomas
    - **Surgery**: Complete removal if accessible and symptomatic
    - **Radiation Therapy**: 
      - Stereotactic radiosurgery for small tumors
      - Conventional radiation for larger or incompletely resected tumors
    - **Medications**: Rarely used, under investigation
    
- **Factors Affecting Treatment Decision**:
    - Size and location of tumor
    - Presence and severity of symptoms
    - Growth rate (if previous imaging available)
    - Patient age and overall health
    - Risk-benefit analysis of intervention
    
- **Monitoring Protocol**:
    - Regular MRI scans (frequency determined by specialist)
    - Neurological check-ups
    - Report new symptoms immediately
    
- **Prognosis**:
    - Generally excellent for benign meningiomas
    - Complete surgical removal often curative
    - Even with observation, many remain stable for years
    
- **Next Steps**:
    - Schedule consultation with neurosurgeon
    - Bring all imaging and medical history
    - Document any symptoms (headaches, vision changes, seizures)
    - Discuss treatment options vs. observation

ℹ️ **Note**: While meningiomas are usually benign, professional evaluation is essential to determine the best management approach.
""",
    
    2: """**For No Tumor Detected (Normal Brain Tissue)**:
- **✅ GOOD NEWS**:
    - No tumor detected in the MRI scan
    - Brain tissue appears normal
    
- **Recommendation**:
    - **Continue Routine Monitoring**: Follow regular health check-ups as recommended by your healthcare provider
    - **If You Had Symptoms**: If this MRI was done due to symptoms, discuss them with your neurologist to rule out other conditions
    
- **Symptom Awareness**:
    Be aware of any new neurological symptoms and report them promptly:
    - Persistent or severe headaches (especially morning headaches)
    - Vision changes or double vision
    - Balance or coordination problems
    - Memory or cognitive changes
    - Seizures
    - Weakness or numbness
    - Personality or behavior changes
    
- **Preventive Brain Health**:
    - **Healthy Lifestyle**: 
      - Regular exercise (150 minutes moderate activity per week)
      - Balanced diet rich in fruits, vegetables, omega-3s
      - Adequate sleep (7-9 hours nightly)
      - Stay mentally active
    - **Avoid Risk Factors**:
      - Limit alcohol consumption
      - Don't smoke
      - Manage chronic conditions (diabetes, hypertension)
      - Minimize head injury risks (wear helmets, seatbelts)
    - **Stress Management**: Practice meditation, yoga, or relaxation techniques
    
- **Follow-Up Schedule**:
    - If you had symptoms: Continue follow-up with your neurologist as scheduled
    - For routine screening: Follow your doctor's advice on future imaging needs
    - Document any new symptoms with dates and characteristics
    
- **When to Seek Immediate Care**:
    - Sudden, severe "thunderclap" headache
    - Sudden vision loss or severe vision changes
    - Sudden weakness, numbness, or paralysis
    - Difficulty speaking or understanding speech
    - Sudden confusion or altered consciousness
    - New onset seizures
    - Severe dizziness with inability to walk
    
- **Next Steps**:
    - Discuss this result with your healthcare provider
    - Continue any existing treatment plans for other conditions
    - Maintain healthy lifestyle habits
    - Keep scheduled follow-up appointments

ℹ️ **Important**: While no tumor was detected, continue to monitor your health and report any new or concerning symptoms to your healthcare provider.
""",
    
    3: """**For Pituitary Tumor Detected**:
- **⚠️ IMPORTANT RECOMMENDATION**:
    - **Prompt Specialized Consultation**: Schedule appointment with endocrinologist and neurosurgeon within 1-2 weeks
    - **Specialized Care Needed**: Pituitary tumors require coordinated care from multiple specialists
    
- **About Pituitary Tumors**:
    - Tumors of the pituitary gland (master endocrine gland)
    - Usually benign (adenomas) - about 99% of cases
    - Can be functioning (hormone-producing) or non-functioning
    - May cause hormonal imbalances or mass effect symptoms
    
- **Diagnostic Next Steps**:
    - **Hormonal Testing**: Comprehensive blood tests for pituitary hormones
      - Prolactin, growth hormone, ACTH, TSH, LH, FSH
      - Cortisol levels (morning and evening)
      - IGF-1, free T4, testosterone/estrogen
    - **Enhanced MRI**: Dedicated pituitary protocol imaging
    - **Visual Field Testing**: Check for optic nerve compression
    - **Endocrine Evaluation**: Complete hormonal assessment
    
- **Types of Pituitary Tumors**:
    - **Prolactinoma**: Most common, excess prolactin
    - **Growth Hormone**: Causes acromegaly/gigantism
    - **ACTH-secreting**: Causes Cushing's disease
    - **Non-functioning**: No hormone excess, but mass effect
    - **TSH, LH, FSH-secreting**: Rare types
    
- **Treatment Options** (Based on type and size):
    - **Medications**:
      - Dopamine agonists for prolactinomas (often first-line)
      - Somatostatin analogs for GH-secreting tumors
      - Medical management may avoid surgery in some cases
    - **Surgery**:
      - Transsphenoidal surgery (through nose) - most common
      - Indicated for non-prolactinomas, large tumors, or failed medical therapy
      - High success rate with experienced surgeon
    - **Radiation Therapy**:
      - Stereotactic radiosurgery for residual or recurrent tumors
      - Conventional radiation in selected cases
    - **Hormone Replacement**:
      - May be needed if pituitary function is impaired
    
- **Symptoms to Monitor**:
    - **Hormonal**: Menstrual irregularities, sexual dysfunction, fatigue, weight changes
    - **Mass Effect**: Headaches, vision changes, double vision
    - **Specific**: Depends on hormone type (enlarged hands/feet, moon face, etc.)
    
- **Specialist Team**:
    - **Endocrinologist**: Primary hormone management
    - **Neurosurgeon**: Surgical expertise (pituitary specialist preferred)
    - **Ophthalmologist**: Visual assessment
    - **Radiation Oncologist**: If radiation needed
    
- **Prognosis**:
    - Generally excellent for most pituitary adenomas
    - High cure rates with appropriate treatment
    - Prolactinomas often well-controlled with medication alone
    - Regular monitoring needed long-term
    
- **Next Steps**:
    - Schedule endocrinology appointment urgently
    - Get comprehensive hormone panel done
    - Visual field testing if not done
    - Consult with pituitary neurosurgeon
    - Consider evaluation at pituitary center of excellence

ℹ️ **Note**: Pituitary tumors, while usually benign, require specialized evaluation and treatment. Early diagnosis and proper management lead to excellent outcomes in most cases.
"""
}


def get_eye_recommendation(class_index):
    """
    Get eye disease recommendation based on prediction class.
    
    Args:
        class_index: Index of predicted class (0-3)
        
    Returns:
        str: Formatted recommendation text
    """
    return EYE_RECOMMENDATIONS.get(class_index, "No recommendation available.")


def get_brain_recommendation(class_index):
    """
    Get brain tumor recommendation based on prediction class.
    
    Args:
        class_index: Index of predicted class (0-3)
        
    Returns:
        str: Formatted recommendation text
    """
    return BRAIN_RECOMMENDATIONS.get(class_index, "No recommendation available.")
