
import json
from collections import Counter
from datetime import datetime

import pandas as pd
import plotly.express as px

COLORS = {
    "forest": "#153E36",
    "teal": "#267B6C",
    "terracotta": "#C87558",
    "gold": "#D6A05A",
    "sage": "#B9D9C9",
}

STATUS_COLORS = {
    "Pending": COLORS["gold"],
    "Reviewed": COLORS["teal"],
    "Needs more information": COLORS["terracotta"],
}


def review_activity_chart(reviews):
    """Number of document reviews created each day."""
    if not reviews:
        return None

    df = pd.DataFrame(reviews)
    df["date"] = pd.to_datetime(
        df["created_at"], errors="coerce"
    ).dt.date
    df = df.dropna(subset=["date"])

    if df.empty:
        return None

    daily = (
        df.groupby("date")
        .size()
        .reset_index(name="reviews")
    )

    fig = px.line(
        daily,
        x="date",
        y="reviews",
        markers=True,
        color_discrete_sequence=[COLORS["teal"]],
        labels={"date": "Date", "reviews": "Reviews"},
    )
    fig.update_traces(line_width=3, marker_size=9)
    return style_chart(fig)


def review_status_chart(reviews, get_action):
    """Distribution of human follow-up statuses."""
    if not reviews:
        return None

    labels = {
        "pending": "Pending",
        "reviewed": "Reviewed",
        "needs_more_information": "Needs more information",
    }

    counts = Counter(
        labels.get(
            get_action(r["id"])["state"], "Pending"
        )
        for r in reviews
    )

    df = pd.DataFrame([
        {"status": label, "count": count}
        for label, count in counts.items()
    ])

    fig = px.pie(
        df,
        names="status",
        values="count",
        hole=0.62,
        color="status",
        color_discrete_map=STATUS_COLORS,
    )
    fig.update_traces(
        textinfo="percent",
        marker=dict(line=dict(color="#FFFFFF", width=3)),
        hovertemplate="%{label}: %{value}<extra></extra>",
    )
    return style_chart(fig)


def requirements_chart(reviews):
    """Count evidenced requirements across saved reviews."""
    counts = Counter()

    for review in reviews:
        try:
            skills = json.loads(
                review.get("supported_skills", "[]")
            )
            counts.update(set(skills))
        except (ValueError, TypeError):
            continue

    if not counts:
        return None

    df = pd.DataFrame(
        counts.most_common(10),
        columns=["skill", "count"],
    )

    fig = px.bar(
        df,
        x="count",
        y="skill",
        orientation="h",
        color="count",
        color_continuous_scale=[
            COLORS["sage"],
            COLORS["teal"],
            COLORS["forest"],
        ],
        labels={
            "count": "Reviews with evidence",
            "skill": "Requirement",
        },
    )
    fig.update_layout(
        coloraxis_showscale=False,
        yaxis={"categoryorder": "total ascending"},
    )
    return style_chart(fig)


def style_chart(fig):
    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font=dict(
            family="Arial",
            color="#29483B",
            size=13,
        ),
        margin=dict(l=24, r=24, t=30, b=24),
        height=335,
        hoverlabel=dict(bgcolor="#153E36", font_color="white"),
        legend_title_text="",
    )
    return fig


def skill_constellation_chart(reviews):
    """Decorative interactive Plotly network of *mentions*, not proficiency scores."""
    import math
    from collections import Counter
    counts = Counter()
    for review in reviews:
        try:
            skills = json.loads(review.get('supported_skills') or '[]')
            if isinstance(skills, list):
                counts.update(set(str(skill) for skill in skills))
        except (ValueError, TypeError):
            continue
    items = counts.most_common(14)
    if not items:
        return None
    import plotly.graph_objects as go
    n = len(items)
    xs, ys = [], []
    for i in range(n):
        angle = 2 * math.pi * i / n - math.pi / 2
        radius = 1.1 + (i % 3) * .16
        xs.append(radius * math.cos(angle))
        ys.append(radius * math.sin(angle))
    fig = go.Figure()
    for i in range(n):
        fig.add_trace(go.Scatter(x=[0, xs[i]], y=[0, ys[i]], mode='lines',
            line=dict(color='rgba(107,208,177,.28)', width=1.6), hoverinfo='skip', showlegend=False))
    fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers+text', text=['HIREFLOW'], textposition='middle center',
        textfont=dict(color='#FFFFFF',size=12,family='Arial Black'), marker=dict(size=82,color='#216E62',line=dict(color='#72D6B3',width=2)),
        hoverinfo='skip',showlegend=False))
    fig.add_trace(go.Scatter(x=xs,y=ys,mode='markers+text',text=[name.title() for name,_ in items],
        textposition='top center', textfont=dict(color='#D7F4EA',size=11),
        marker=dict(size=[22+min(count,20)*2 for _,count in items],color=[count for _,count in items],
                    colorscale=[[0,'#6F5BEF'],[.5,'#42C6B2'],[1,'#D6B4FF']],showscale=False,
                    line=dict(color='#A7E9D6',width=1)),
        customdata=[count for _,count in items],hovertemplate='%{text}<br>%{customdata} reviews with mentions<extra></extra>',showlegend=False))
    fig.update_layout(height=410,margin=dict(l=45,r=45,t=40,b=35),
        paper_bgcolor='#102A2B',plot_bgcolor='#102A2B',
        xaxis=dict(visible=False,range=[-1.9,1.9],fixedrange=True),
        yaxis=dict(visible=False,range=[-1.7,1.7],scaleanchor='x',scaleratio=1,fixedrange=True),
        hoverlabel=dict(bgcolor='#1E4C45',font_color='#FFFFFF'),dragmode=False)
    return fig
