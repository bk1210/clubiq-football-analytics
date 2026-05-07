# ⚽ ClubIQ — Full Stack Football Analytics Platform

> Match Intelligence · Player Ratings · Load Monitoring

[![Live Demo](https://img.shields.io/badge/🤗_Live_Demo-HuggingFace-yellow)](https://huggingface.co/spaces/bk1210/clubiq-football-analytics)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Live-red)](https://streamlit.io)

---

## 🎯 Overview

ClubIQ is a production-ready football analytics platform built on **StatsBomb open event data**, designed to give coaching staff, analysts, and management data-driven insights across three key areas:

| Module | Description |
|---|---|
| 🏟️ Match Intelligence | Goals, shots, pressing intensity, pass accuracy by team |
| 🌟 Player Ratings | Composite 100-point rating across attacking, defensive & passing actions |
| 💪 Load Monitoring | Per-player fatigue risk score based on high-intensity event frequency |

---

## 📊 Dataset

- **Source:** StatsBomb Open Data — La Liga 2015/16
- **Scale:** 380 matches · 1,295,354 events · 546 players
- **Storage:** SQLite database (`clubiq.db`)

---

## 🏗️ Architecture
StatsBomb API
↓
statsbombpy (Python)
↓
Pandas Feature Engineering
↓
SQLite Database (3 tables: matches, players, events)
↓
┌─────────────────────────────────┐
│  Module 1: Match Intelligence   │
│  Module 2: Player Ratings       │
│  Module 3: Load Monitoring      │
└─────────────────────────────────┘
↓              ↓           ↓
Streamlit App   Power BI    Tableau
(HuggingFace)  Dashboard   Dashboard

---

## 🔑 Key Results

- 🥇 **Top Rated Player:** Neymar da Silva Santos Junior (100.0)
- ⚠️ **Highest Fatigue Risk:** Augusto Matías Fernández — Celta Vigo (73.3%)
- ⚽ **Most Goals:** Luis Alberto Suárez Díaz — Barcelona (40)
- 🔵 **Top Pressing Team:** Valencia CF

---

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| Data Pull | `statsbombpy` |
| Processing | `pandas`, `numpy` |
| Storage | `SQLite` via `sqlalchemy` |
| Visualization 1 | `Streamlit` + `Plotly` |
| Visualization 2 | `Power BI Desktop` |
| Visualization 3 | `Tableau Public` |
| Deployment | HuggingFace Spaces |

---

## 🚀 Run Locally

```bash
git clone https://github.com/bk1210/clubiq-football-analytics
cd clubiq-football-analytics
pip install -r requirements.txt
streamlit run app.py
```

---

## 📁 File Structure

clubiq-football-analytics/
├── app.py                  # Streamlit dashboard
├── requirements.txt        # Dependencies
├── match_shots.csv         # Module 1 data
├── match_passes.csv        # Module 1 data
├── match_pressure.csv      # Module 1 data
├── player_ratings.csv      # Module 2 data
├── load_summary.csv        # Module 3 data
└── matches.csv             # Base match data

---

## 🔗 Links

- 🤗 **Live App:** [HuggingFace Space](https://huggingface.co/spaces/bk1210/clubiq-football-analytics)
- 📓 **Kaggle Notebook:** [ClubIQ Pipeline](https://kaggle.com/bharathkesav)
- 👤 **Author:** Bharath Kesav R — Integrated M.Sc. Data Science, Amrita Vishwa Vidyapeetham

---

## 📌 Note for Clubs

> This platform is built on professional-grade StatsBomb data.
> The same pipeline can be deployed on any club's internal match data
> to generate real-time player ratings, fatigue flags, and match intelligence.

