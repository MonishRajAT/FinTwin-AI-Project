"""
Premium SaaS cards for FinTwin AI.
"""

import streamlit as st

def inject_card_styles():
    st.markdown("""
    <style>

    .ft-card{
        position:relative;
        padding:24px;
        border-radius:22px;
        background:linear-gradient(180deg,#151C2C,#0F172A);
        border:1px solid rgba(255,255,255,.08);
        overflow:hidden;
        transition:.35s;
        margin-bottom:20px;
        box-shadow:
            0 10px 40px rgba(0,0,0,.35);
    }

    .ft-card:before{

        content:"";

        position:absolute;

        top:0;
        left:0;

        width:100%;
        height:2px;

        background:linear-gradient(
            90deg,
            #2563EB,
            #06B6D4,
            #10B981
        );

    }

    .ft-card:hover{

        transform:translateY(-6px);

        border:1px solid rgba(37,99,235,.35);

        box-shadow:
            0 18px 60px rgba(37,99,235,.18);

    }

    .ft-title{

        color:#94A3B8;

        font-size:15px;

        margin-top:12px;

    }

    .ft-value{

        font-size:40px;

        font-weight:800;

        color:white;

        margin-top:6px;

    }

    .ft-change{

        color:#22C55E;

        margin-top:10px;

        font-weight:600;

    }

    .progress-container{

        width:100%;

        height:10px;

        background:#1F2937;

        border-radius:50px;

        margin-top:18px;

        overflow:hidden;

    }

    .progress-fill{

        height:100%;

        border-radius:50px;

        background:linear-gradient(
            90deg,
            #2563EB,
            #06B6D4,
            #10B981
        );

        animation:grow 1s ease;

    }

    @keyframes grow{

        from{

            width:0;

        }

    }

    </style>
    """, unsafe_allow_html=True)


def kpi_card(
        title,
        value,
        icon,
        change,
        progress=75
):

    st.markdown(
        f"""
<div class="ft-card">

<div style="font-size:38px;">
{icon}
</div>

<div class="ft-title">
{title}
</div>

<div class="ft-value">
{value}
</div>

<div class="ft-change">
{change}
</div>

<div class="progress-container">

<div
class="progress-fill"
style="width:{progress}%;">
</div>

</div>

</div>
""",
        unsafe_allow_html=True
    )


def glass_container(content):

    st.markdown(
        f"""
<div class="ft-card">

{content}

</div>
""",
        unsafe_allow_html=True
    )