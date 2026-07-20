"""
Global styles for FinTwin AI.
"""

import streamlit as st

def load_global_styles():
    st.markdown(
        """
<style>

/* -----------------------------
   Google Font
------------------------------*/
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* -----------------------------
   Global
------------------------------*/

html, body, [class*="css"]{
    font-family: 'Inter', sans-serif;
}

/* -----------------------------
   Main App
------------------------------*/

.stApp{
    background:#0B1120;
    color:#F8FAFC;
}

/* -----------------------------
   Hide Streamlit Branding
------------------------------*/

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* -----------------------------
Sidebar
------------------------------*/

[data-testid="stSidebar"]{
    background:#111827;
    border-right:1px solid rgba(255,255,255,0.08);
}

/* -----------------------------
Buttons
------------------------------*/

.stButton>button{

    width:100%;

    background:#2563EB;

    color:white;

    border:none;

    border-radius:12px;

    padding:0.7rem;

    font-weight:600;

    transition:0.3s;
}

.stButton>button:hover{

    background:#1D4ED8;

    transform:translateY(-2px);

    box-shadow:0 12px 30px rgba(37,99,235,.35);

}

/* -----------------------------
Inputs
------------------------------*/

.stTextInput input{

    border-radius:12px;

    border:1px solid #374151;

    background:#1F2937;

    color:white;
}

.stNumberInput input{

    border-radius:12px;

    border:1px solid #374151;

    background:#1F2937;

    color:white;
}

.stSelectbox div[data-baseweb="select"]{

    background:#1F2937;

    border-radius:12px;

}

/* -----------------------------
Cards
------------------------------*/

.metric-card{

    background:#111827;

    padding:25px;

    border-radius:18px;

    border:1px solid rgba(255,255,255,.08);

    transition:0.3s;

    box-shadow:
    0 10px 35px rgba(0,0,0,.35);

}

.metric-card:hover{

    transform:translateY(-5px);

    border-color:#2563EB;

}

/* -----------------------------
Titles
------------------------------*/

.page-title{

    font-size:42px;

    font-weight:800;

    margin-bottom:5px;

}

.page-subtitle{

    color:#94A3B8;

    font-size:18px;

    margin-bottom:30px;

}

/* -----------------------------
Section Header
------------------------------*/

.section-title{

    font-size:24px;

    font-weight:700;

    margin-top:25px;

    margin-bottom:15px;

}

/* -----------------------------
Metric
------------------------------*/

.metric-value{

    font-size:38px;

    font-weight:800;

    color:white;

}

.metric-label{

    color:#94A3B8;

    font-size:15px;

}

/* -----------------------------
Success
------------------------------*/

.success-box{

    background:#052E16;

    border-left:5px solid #22C55E;

    padding:15px;

    border-radius:10px;

}

/* -----------------------------
Warning
------------------------------*/

.warning-box{

    background:#451A03;

    border-left:5px solid #F59E0B;

    padding:15px;

    border-radius:10px;

}

/* -----------------------------
Error
------------------------------*/

.error-box{

    background:#450A0A;

    border-left:5px solid #EF4444;

    padding:15px;

    border-radius:10px;

}

/* -----------------------------
Scrollbar
------------------------------*/

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-thumb{

    background:#374151;

    border-radius:10px;

}

::-webkit-scrollbar-thumb:hover{

    background:#4B5563;

}

/* -----------------------------
Fade Animation
------------------------------*/

.fade-in{

    animation:fade 0.6s ease-in-out;

}

@keyframes fade{

    from{

        opacity:0;

        transform:translateY(15px);

    }

    to{

        opacity:1;

        transform:translateY(0);

    }

}

</style>
""",
        unsafe_allow_html=True,
    )