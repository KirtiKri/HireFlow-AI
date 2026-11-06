
import json
from collections import Counter
from datetime import datetime

import pandas as pd
import plotly.express as px

COLORS = {
    "forest": "#194B43",
    "teal": "#368F85",
    "terracotta": "#C16A45",
    "gold": "#D5A547",
    "sage": "#A8B8A1",
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
        paper_bgcolor="#FAF9F6",
        plot_bgcolor="#FAF9F6",
        font=dict(
            family="Arial",
            color="#263630",
            size=13,
        ),
        margin=dict(l=15, r=15, t=25, b=15),
        height=330,
        legend_title_text="",
    )
    return fig
