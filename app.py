
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="ClubIQ", page_icon="⚽", layout="wide")

# Load data
@st.cache_data
def load_data():
    shots    = pd.read_csv("match_shots.csv")
    pressure = pd.read_csv("match_pressure.csv")
    passes   = pd.read_csv("match_passes.csv")
    ratings  = pd.read_csv("player_ratings.csv")
    load     = pd.read_csv("load_summary.csv")
    matches  = pd.read_csv("matches.csv")
    return shots, pressure, passes, ratings, load, matches

shots, pressure, passes, ratings, load, matches = load_data()

# Sidebar
st.sidebar.image("https://img.icons8.com/emoji/96/soccer-ball-emoji.png", width=80)
st.sidebar.title("ClubIQ ⚽")
st.sidebar.markdown("**Full Stack Football Analytics**")
st.sidebar.markdown("---")
page = st.sidebar.radio("Navigate", ["🏟️ Match Intelligence", "🌟 Player Ratings", "💪 Load Monitoring"])

# ─── PAGE 1: MATCH INTELLIGENCE ───
if page == "🏟️ Match Intelligence":
    st.title("🏟️ Match Intelligence")
    st.markdown("Shooting efficiency, pressing intensity and pass accuracy across La Liga 2015/16")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Matches", len(matches))
    col2.metric("Total Goals", int(shots["goals"].sum()))
    col3.metric("Total Shots", int(shots["total_shots"].sum()))

    st.markdown("---")

    # Top teams by goals
    team_goals = shots.groupby("team")["goals"].sum().sort_values(ascending=False).reset_index().head(10)
    fig1 = px.bar(team_goals, x="team", y="goals", color="goals",
                  color_continuous_scale="Reds", title="Top 10 Teams by Goals Scored")
    st.plotly_chart(fig1, use_container_width=True)

    col4, col5 = st.columns(2)

    # Pressing intensity
    with col4:
        top_press = pressure.groupby("team")["total_pressures"].sum().sort_values(ascending=False).reset_index().head(10)
        fig2 = px.bar(top_press, x="team", y="total_pressures", color="total_pressures",
                      color_continuous_scale="Blues", title="Top 10 Teams by Pressing Intensity")
        st.plotly_chart(fig2, use_container_width=True)

    # Pass accuracy
    with col5:
        passes["pass_acc"] = (passes["completed_passes"] / passes["total_passes"] * 100).round(1)
        top_pass = passes.groupby("team")["pass_acc"].mean().sort_values(ascending=False).reset_index().head(10)
        fig3 = px.bar(top_pass, x="team", y="pass_acc", color="pass_acc",
                      color_continuous_scale="Greens", title="Top 10 Teams by Pass Accuracy (%)")
        st.plotly_chart(fig3, use_container_width=True)

# ─── PAGE 2: PLAYER RATINGS ───
elif page == "🌟 Player Ratings":
    st.title("🌟 Player Ratings")
    st.markdown("Composite ClubIQ rating based on goals, passing, dribbling, pressing and defensive actions")

    top_n = st.slider("Show Top N Players", 5, 50, 20)
    selected_team = st.selectbox("Filter by Team", ["All"] + sorted(ratings["team"].unique().tolist()))

    df = ratings.copy()
    if selected_team != "All":
        df = df[df["team"] == selected_team]
    df = df.sort_values("rating_100", ascending=False).head(top_n)

    fig4 = px.bar(df, x="rating_100", y="player_name", orientation="h",
                  color="rating_100", color_continuous_scale="Viridis",
                  hover_data=["team","goals","pass_accuracy"],
                  title=f"Top {top_n} Players — ClubIQ Rating")
    fig4.update_layout(yaxis={"categoryorder": "total ascending"}, height=600)
    st.plotly_chart(fig4, use_container_width=True)

    st.markdown("### 📋 Full Table")
    st.dataframe(df[["player_name","team","goals","total_shots","dribbles_won",
                      "pressures","interceptions","pass_accuracy","rating_100"]]
                 .reset_index(drop=True), use_container_width=True)

# ─── PAGE 3: LOAD MONITORING ───
elif page == "💪 Load Monitoring":
    st.title("💪 Load Monitoring")
    st.markdown("Player fatigue risk based on high-intensity actions per match")

    min_matches = st.slider("Minimum Matches Played", 5, 30, 10)
    df_load = load[load["total_matches"] >= min_matches].sort_values("fatigue_risk", ascending=False)

    col6, col7, col8 = st.columns(3)
    col6.metric("Players Monitored", len(df_load))
    col7.metric("Avg Load Score", round(df_load["avg_load"].mean(), 1))
    col8.metric("High Risk Players (>60%)", int((df_load["fatigue_risk"] > 60).sum()))

    st.markdown("---")

    fig5 = px.scatter(df_load.head(50), x="avg_load", y="fatigue_risk",
                      size="total_matches", color="fatigue_risk",
                      hover_name="player_name", hover_data=["team","total_matches"],
                      color_continuous_scale="RdYlGn_r",
                      title="Load vs Fatigue Risk (Top 50 Players)")
    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("### ⚠️ High Risk Players")
    st.dataframe(df_load[df_load["fatigue_risk"] > 50]
                 [["player_name","team","avg_load","max_load","high_load_matches","total_matches","fatigue_risk"]]
                 .reset_index(drop=True), use_container_width=True)
