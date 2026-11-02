import streamlit as st
from summarizer import generate_summary

# Full Screen Page Configuration
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="✨",
    layout="wide"
)

# Custom Styling (28px font for text input and paragraph result card)
st.markdown("""
    <style>
    /* Full width container spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 95% !important;
    }
    
    /* Main Gradient Header Banner */
    .header-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 35px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .header-title {
        font-size: 3.2rem;
        font-weight: 800;
        margin: 0;
    }
    
    .header-sub {
        font-size: 1.35rem;
        opacity: 0.95;
        margin-top: 10px;
    }

    /* Custom Label Styling */
    .custom-label {
        font-size: 1.4rem;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 8px;
    }

    /* Text Area Input Font Size 28px */
    .stTextArea textarea {
        font-size: 28px !important;
        line-height: 1.5 !important;
    }

    /* Output Card Styling for Paragraph Format (28px Font & Proper Wrapping) */
    .result-card {
        background-color: #f0f4f8;
        border-left: 6px solid #667eea;
        padding: 25px;
        border-radius: 10px;
        font-size: 28px !important;
        font-weight: 500 !important;
        line-height: 1.6 !important;
        color: #1a202c !important;
        margin-top: 15px;
        white-space: pre-wrap;
        word-wrap: break-word;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State for input text management
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# Attractive Header Banner
st.markdown("""
    <div class="header-box">
        <div class="header-title">🤖 AI Text Summarizer</div>
        <div class="header-sub">Transform long articles into clear, short summaries in seconds</div>
    </div>
""", unsafe_allow_html=True)

# Main Input Section with Clear Button
col_label, col_btn = st.columns([8, 1])
with col_label:
    st.markdown('<div class="custom-label">📄 Paste your long text/article here:</div>', unsafe_allow_html=True)
with col_btn:
    st.write("") 
    if st.button("🗑️ Clear Text", use_container_width=True):
        st.session_state.input_text = ""
        st.rerun()

input_text = st.text_area("", value=st.session_state.input_text, height=250, placeholder="Type or paste your text here...", label_visibility="collapsed")
st.session_state.input_text = input_text

# Sliders Side by Side
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="custom-label" style="font-size: 1.15rem;">📏 Max Summary Length</div>', unsafe_allow_html=True)
    max_len = st.slider("", 50, 300, 150, label_visibility="collapsed")
with col2:
    st.markdown('<div class="custom-label" style="font-size: 1.15rem;">📐 Min Summary Length</div>', unsafe_allow_html=True)
    min_len = st.slider("", 14, 100, 26, label_visibility="collapsed")

# Generate Button
if st.button("✨ Generate Summary", type="primary", use_container_width=True):
    if input_text.strip():
        with st.spinner("⚡ Summarizing your text..."):
            summary_result = generate_summary(input_text, max_length=max_len, min_length=min_len)
            
            if isinstance(summary_result, list):
                summary_result = summary_result[0]

        st.markdown("### 🎯 Summary Result:")
        
        # Displaying result inside a styled paragraph card (28px font with proper text wrapping)
        st.markdown(f'<div class="result-card">{summary_result}</div>', unsafe_allow_html=True)
        
        # Detailed Reduction Metrics
        orig_words = len(input_text.split())
        summ_words = len(summary_result.split())
        reduction_pct = round(((orig_words - summ_words) / orig_words) * 100, 1) if orig_words > 0 else 0
        
        st.write("")
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("Original Words", orig_words)
        col_m2.metric("Summary Words", summ_words)
        col_m3.metric("Reduction", f"{reduction_pct}%")
        
        # Download as Text File (.txt)
        st.download_button(
            label="📥 Download Summary as Text File",
            data=summary_result,
            file_name="ai_summary.txt",
            mime="text/plain",
            use_container_width=True
        )
        
    else:
        st.warning("⚠️ Please paste some text first!")