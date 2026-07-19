# Professional Plotly charts for FinTwin AI.

import plotly.graph_objects as go

def financial_health_gauge(score: float):

    fig = go.Figure(
        go.Indicator(

            mode="gauge+number",

            value=score,

            number={
                "suffix": "/100",
                "font": {
                    "size": 42,
                    "color": "white"
                }
            },

            title={
                "text": "Financial Health",
                "font": {
                    "size": 22,
                    "color": "white"
                }
            },

            gauge={

                "axis": {
                    "range": [0, 100]
                },

                "bar": {
                    "color": "#2563EB"
                },

                "bgcolor": "#1F2937",

                "borderwidth": 0,

                "steps": [

                    {
                        "range": [0, 40],
                        "color": "#EF4444"
                    },

                    {
                        "range": [40, 70],
                        "color": "#F59E0B"
                    },

                    {
                        "range": [70, 100],
                        "color": "#22C55E"
                    }

                ],
            },
        )
    )

    fig.update_layout(

        height=320,

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20,
        ),

        paper_bgcolor="#0B1120",

        font=dict(
            color="white"
        ),
    )

    return fig


def financial_ratios_chart(
    savings_rate,
    debt_ratio,
    investment_ratio,
):

    fig = go.Figure()

    fig.add_bar(
        x=["Savings", "Debt", "Investment"],

        y=[
            savings_rate,
            debt_ratio,
            investment_ratio,
        ],

        marker_color=[
            "#22C55E",
            "#EF4444",
            "#2563EB",
        ],
    )

    fig.update_layout(

        title="Financial Ratios",

        height=350,

        paper_bgcolor="#0B1120",

        plot_bgcolor="#0B1120",

        font=dict(
            color="white"
        ),

        yaxis_title="%",

        xaxis_title="",
    )

    return fig