"""
Financial Digital Twin Onboarding Wizard
"""

import streamlit as st
from auth.session import get_current_user
from services.profile_service import ProfileService
from ui.styles import load_global_styles
from ui.components import page_header
from ui.cards import inject_card_styles, glass_container

TOTAL_STEPS = 5

def progress_bar(step: int):

    percentage = int((step / TOTAL_STEPS) * 100)

    st.markdown(
        f"""
<div style="
margin-bottom:30px;
">

<div style="
display:flex;
justify-content:space-between;
margin-bottom:10px;
color:#94A3B8;
">

<span>Step {step}</span>

<span>{TOTAL_STEPS}</span>

</div>

<div style="
width:100%;
height:10px;
background:#1F2937;
border-radius:50px;
overflow:hidden;
">

<div style="
height:100%;
width:{percentage}%;
background:linear-gradient(
90deg,
#2563EB,
#06B6D4,
#10B981
);
transition:1s;
"></div>

</div>

</div>
""",
        unsafe_allow_html=True,
    )


def render_financial_profile():

    load_global_styles()

    inject_card_styles()

    user = get_current_user()

    if "wizard_step" not in st.session_state:
        st.session_state.wizard_step = 1

    page_header(
        "👤 Financial Digital Twin",
        "Let's build your financial profile."
    )

    progress_bar(st.session_state.wizard_step)

    step = st.session_state.wizard_step

    # STEP 1
    if step == 1:

        glass_container("<h2>💰 Monthly Income</h2>")

        income = st.number_input(
            "Monthly Income",
            min_value=0.0,
            step=1000.0,
        )

        if st.button(
            "Continue →",
            use_container_width=True
        ):

            st.session_state.monthly_income = income

            st.session_state.wizard_step = 2

            st.rerun()

    # STEP 2
    elif step == 2:

        glass_container("<h2>🚑 Emergency Fund</h2>")

        emergency = st.number_input(
            "Emergency Fund",
            min_value=0.0,
            step=1000.0,
        )

        if st.button(
            "Continue →",
            use_container_width=True
        ):

            st.session_state.emergency_fund = emergency

            st.session_state.wizard_step = 3

            st.rerun()

    # STEP 3
    elif step == 3:

        glass_container("<h2>📈 Investments</h2>")

        investments = st.number_input(
            "Total Investments",
            min_value=0.0,
            step=1000.0,
        )

        if st.button(
            "Continue →",
            use_container_width=True
        ):

            st.session_state.investments = investments

            st.session_state.wizard_step = 4

            st.rerun()

    # STEP 4
    elif step == 4:

        glass_container("<h2>💳 Loans</h2>")

        loans = st.number_input(
            "Outstanding Loans",
            min_value=0.0,
            step=1000.0,
        )

        if st.button(
            "Continue →",
            use_container_width=True
        ):

            st.session_state.loans = loans

            st.session_state.wizard_step = 5

            st.rerun()

    # STEP 5
    else:

        glass_container("<h2>⚙ Final Details</h2>")

        insurance = st.number_input(
            "Insurance Cover",
            min_value=0.0,
            step=1000.0,
        )

        budget = st.number_input(
            "Monthly Budget",
            min_value=0.0,
            step=1000.0,
        )

        risk = st.selectbox(
            "Risk Appetite",
            [
                "Low",
                "Medium",
                "High"
            ]
        )

        style = st.selectbox(
            "Investment Style",
            [
                "Conservative",
                "Balanced",
                "Aggressive"
            ]
        )

        if st.button(
            "🚀 Create My Financial Twin",
            use_container_width=True,
            type="primary",
        ):

            ProfileService.update_profile(

                user_id=user["user_id"],

                monthly_income=st.session_state.monthly_income,

                emergency_fund=st.session_state.emergency_fund,

                total_investments=st.session_state.investments,

                total_loans=st.session_state.loans,

                insurance_cover=insurance,

                risk_appetite=risk,

                investment_style=style,

                preferred_currency="INR",

                monthly_budget=budget,
            )

            st.success(
                "🎉 Financial Digital Twin created successfully!"
            )

            st.balloons()