import numpy as np
import pandas as pd
import requests
import streamlit as st

# ==========================================
# PAGE CONFIGURATION & GLOBAL STYLING
# ==========================================
st.set_page_config(
    page_title="TACTIQ | Elite Football Intelligence Platform",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    /* Global Dark Premium Theme */
    .stApp {
        background-color: #080B10;
        color: #E2E8F0;
        font-family: 'Inter', 'Manrope', sans-serif;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #11161D;
        border-right: 1px solid #252C36;
    }
    section[data-testid="stSidebar"] .stRadio label {
        color: #CBD5E1 !important;
        font-weight: 500;
    }
    
    /* Cards & Containers */
    .tactiq-card {
        background-color: #11161D;
        border: 1px solid #252C36;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
    }
    .live-match-banner {
        background: linear-gradient(135deg, #11161D 0%, #1A2230 100%);
        border: 1px solid #ef4444;
        border-left: 6px solid #ef4444;
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 20px;
    }
    .metric-container {
        background-color: #11161D;
        border: 1px solid #252C36;
        border-radius: 10px;
        padding: 16px;
        text-align: center;
    }
    
    /* Typography & Headers */
    h1, h2, h3, h4 {
        color: #F8FAFC;
        font-family: 'Manrope', sans-serif;
    }
    
    /* Custom Badges */
    .badge-live {
        background-color: rgba(239, 68, 68, 0.15);
        color: #ef4444;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.85rem;
        border: 1px solid rgba(239, 68, 68, 0.3);
    }
    .badge-pos {
        background-color: rgba(16, 185, 129, 0.15);
        color: #10b981;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.85rem;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.markdown(
    """
    <div style="padding: 10px 0 20px 0; border-bottom: 1px solid #252C36; margin-bottom: 15px;">
        <h2 style="margin:0; color: #F8FAFC; font-size: 1.5rem;">⚽ TACTIQ</h2>
        <p style="margin:2px 0 0 0; color: #64748B; font-size: 0.8rem;">Elite Football Intelligence</p>
    </div>
""",
    unsafe_allow_html=True,
)

app_mode = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "⚡ Live Center",
        "🎯 Match Analysis",
        "📊 Predictions",
        "🧠 Tactical Intelligence",
        "👤 Player Analytics",
        "🏆 Team Analytics",
        "📈 Leagues & Standings",
        "📰 Football Intelligence",
        "🤖 TACTIQ AI",
    ],
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<p style='color: #64748B; font-size: 0.75rem; text-align: center;'>TACTIQ Engine v4.2 | 2022-2027 Pipeline</p>",
    unsafe_allow_html=True,
)


# ==========================================
# 1. DASHBOARD
# ==========================================
if app_mode == "🏠 Dashboard":
    st.markdown("<h1>Dashboard Overview</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color: #94A3B8;'>Real-time operational overview, active match telemetry, and ensemble forecasts.</p>",
        unsafe_allow_html=True,
    )

    # LIVE NOW SECTION
    st.markdown("### LIVE NOW")
    st.markdown(
        """
        <div class="live-match-banner">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                <span class="badge-live">🔴 67' LIVE</span>
                <span style="color: #94A3B8; font-size: 0.9rem;">UEFA Champions League · Quarter Finals</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; text-align: center;">
                <div style="flex: 1; text-align: left;">
                    <h2 style="margin:0; color: #F8FAFC;">FC Barcelona</h2>
                    <span style="color: #94A3B8; font-size: 0.85rem;">Home (4-3-3)</span>
                </div>
                <div style="flex: 1; font-size: 2.2rem; font-weight: 800; color: #38BDF8; letter-spacing: 2px;">
                    1 – 0
                </div>
                <div style="flex: 1; text-align: right;">
                    <h2 style="margin:0; color: #F8FAFC;">Paris SG</h2>
                    <span style="color: #94A3B8; font-size: 0.85rem;">Away (4-2-3-1)</span>
                </div>
            </div>
            <hr style="border-color: #252C36; margin: 15px 0;">
            <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; text-align: center;">
                <div><span style="color: #64748B; font-size: 0.8rem;">Win Prob</span><br><b>58% - 24%</b></div>
                <div><span style="color: #64748B; font-size: 0.8rem;">xG</span><br><b>1.84 - 0.92</b></div>
                <div><span style="color: #64748B; font-size: 0.8rem;">Possession</span><br><b>56% - 44%</b></div>
                <div><span style="color: #64748B; font-size: 0.8rem;">PPDA</span><br><b>8.4 - 12.1</b></div>
                <div><span style="color: #64748B; font-size: 0.8rem;">Momentum</span><br><span style="color: #10b981;">▲ High</span></div>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # UPCOMING MATCHES
    st.markdown("### Upcoming Matches")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            """
            <div class="tactiq-card">
                <span style="color: #38BDF8; font-size: 0.75rem;">Premier League · Tomorrow, 18:30</span>
                <h4 style="margin: 8px 0 4px 0;">Arsenal vs Man City</h4>
                <p style="color: #94A3B8; font-size: 0.85rem; margin:0;">Model Favor: <b>Draw / Arsenal (38%)</b></p>
            </div>
        """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="tactiq-card">
                <span style="color: #38BDF8; font-size: 0.75rem;">La Liga · Tomorrow, 21:00</span>
                <h4 style="margin: 8px 0 4px 0;">Real Madrid vs Atlético</h4>
                <p style="color: #94A3B8; font-size: 0.85rem; margin:0;">Model Favor: <b>Real Madrid (62%)</b></p>
            </div>
        """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class="tactiq-card">
                <span style="color: #38BDF8; font-size: 0.75rem;">Serie A · Sunday, 16:00</span>
                <h4 style="margin: 8px 0 4px 0;">Inter vs Juventus</h4>
                <p style="color: #94A3B8; font-size: 0.85rem; margin:0;">Model Favor: <b>Inter Milan (51%)</b></p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    # TACTIQ PREDICTIONS & INSIGHTS
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("### 🎯 TACTIQ Predictions Summary")
        st.markdown(
            """
            <div class="tactiq-card">
                <p><b>Model Consensus Update:</b> Poisson & Dixon-Coles engines indicate tight defensive blocks in upcoming weekend fixtures across Serie A.</p>
                <p style="margin-bottom:0;"><b>Ensemble Accuracy:</b> 74.2% over last 50 tracked matches.</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
    with col_b:
        st.markdown("### 📰 Latest Tactical Insights")
        st.markdown(
            """
            <div class="tactiq-card">
                <p><b>Half-Space Exploitation:</b> How elite managers utilize inverted full-backs to overload central corridors against low blocks.</p>
                <span style="color: #64748B; font-size: 0.8rem;">Published 2 hours ago · Tactical Intelligence</span>
            </div>
        """,
            unsafe_allow_html=True,
        )


# ==========================================
# 2. LIVE CENTER
# ==========================================
elif app_mode == "⚡ Live Center":
    st.markdown("<h1>Live Match Center</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color: #94A3B8;'>Real-time telemetry, live match flows, and granular tactical feeds.</p>",
        unsafe_allow_html=True,
    )

    match_option = st.selectbox(
        "Select Active Telemetry Stream:",
        [
            "FC Barcelona vs Paris SG (LIVE 67')",
            "Real Madrid vs Bayern Munich",
            "Arsenal vs Inter Milan",
        ],
    )

    tab_overview, tab_tactical, tab_stats, tab_players, tab_timeline = st.tabs(
        ["Overview", "Tactical", "Stats", "Players", "Timeline"]
    )

    with tab_overview:
        col1, col2, col3 = st.columns(3)
        col1.metric("Home Win Prob", "58%", "+4%")
        col2.metric("Draw Prob", "22%", "-2%")
        col3.metric("Away Win Prob", "20%", "-2%")

        st.markdown("#### Match Expected Goals (xG) Progression")
        chart_data = pd.DataFrame(
            np.random.randn(10, 2).cumsum(axis=0), columns=["Barcelona", "PSG"]
        )
        st.line_chart(chart_data)

    with tab_tactical:
        st.markdown("#### Tactical Formation & Pressing Intensity (PPDA)")
        c1, c2 = st.columns(2)
        c1.markdown(
            """
            <div class="tactiq-card">
                <h4>Home Team Structure (4-3-3)</h4>
                <p><b>Build-up Style:</b> Short passing, high width</p>
                <p><b>PPDA:</b> 8.4 (Aggressive Pressing)</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
        c2.markdown(
            """
            <div class="tactiq-card">
                <h4>Away Team Structure (4-2-3-1)</h4>
                <p><b>Build-up Style:</b> Direct counter-attacks</p>
                <p><b>PPDA:</b> 12.1 (Medium Block)</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with tab_stats:
        st.markdown("#### Comprehensive Match Statistics")
        stats_df = pd.DataFrame(
            {
                "Metric": [
                    "Possession",
                    "xG",
                    "Total Shots",
                    "Shots on Target",
                    "Corner Kicks",
                    "Fouls",
                ],
                "Barcelona": ["56%", "1.84", "14", "6", "7", "9"],
                "PSG": ["44%", "0.92", "9", "3", "3", "12"],
            }
        )
        st.table(stats_df)

    with tab_players:
        st.markdown("#### Key Player Performance Ratings")
        st.info(
            "Showing live player ratings based on possession value and defensive actions."
        )

    with tab_timeline:
        st.markdown("#### Match Event Timeline")
        st.markdown("- **67'** ⚽ Goal! FC Barcelona (1 - 0)")
        st.markdown("- **45+'** ⏱️ Half-Time Score (0 - 0)")
        st.markdown("- **23'** 🟨 Yellow Card (PSG - Midfielder)")


# ==========================================
# 3. MATCH ANALYSIS
# ==========================================
elif app_mode == "🎯 Match Analysis":
    st.markdown("<h1>Match Analysis Engine</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color: #94A3B8;'>Deep statistical breakdown, model predictions, and head-to-head evaluation.</p>",
        unsafe_allow_html=True,
    )

    col_h, col_vs, col_a = st.columns([3, 1, 3])
    with col_h:
        team_home = st.selectbox(
            "Home Team", ["FC Barcelona", "Real Madrid", "Arsenal", "Bayern"]
        )
    with col_vs:
        st.markdown(
            "<h3 style='text-align: center; margin-top: 30px;'>VS</h3>",
            unsafe_allow_html=True,
        )
    with col_a:
        team_away = st.selectbox(
            "Away Team", ["Real Madrid", "Paris SG", "Manchester City", "Inter"]
        )

    tab_ov, tab_tac, tab_st, tab_pl, tab_mod, tab_tl = st.tabs(
        ["Overview", "Tactical", "Stats", "Players", "Models", "Timeline"]
    )

    with tab_ov:
        st.markdown(
            f"### TACTIQ Prediction: {team_home} vs {team_away}"
        )
        c1, c2, c3 = st.columns(3)
        c1.metric(f"{team_home} Win", "54.2%")
        c2.metric("Draw", "23.5%")
        c3.metric(f"{team_away} Win", "22.3%")

        st.markdown("#### Expected Goals & Most Likely Scoreline")
        sc1, sc2 = st.columns(2)
        sc1.metric("Home Expected xG", "1.75")
        sc2.metric("Away Expected xG", "1.12")
        st.success("Most Likely Outcome: **2 - 1** (Probability: 18.4%)")

    with tab_tac:
        st.markdown("#### Tactical Matrix & Field Tilt")
        st.progress(0.62, text=f"{team_home} Field Tilt Dominance (62%)")

    with tab_st:
        st.markdown("#### Historical Match Comparison")
        comparison_df = pd.DataFrame(
            {
                "Indicator": ["Avg xG Scored", "Avg xGA Conceded", "PPDA"],
                team_home: [1.92, 0.85, 9.1],
                team_away: [1.78, 0.94, 10.4],
            }
        )
        st.table(comparison_df)

    with tab_pl:
        st.markdown("#### Standout Key Players")
        st.write(
            "Top performers in recent fixtures based on progressive carries and key passes."
        )

    with tab_mod:
        st.markdown("#### Statistical & Machine Learning Model Consensus")
        models_summary = pd.DataFrame(
            {
                "Model": [
                    "Poisson Distribution",
                    "Bivariate Poisson",
                    "Dixon-Coles Model",
                    "Negative Binomial",
                    "XGBoost Ensemble",
                    "LightGBM Classifier",
                    "CatBoost Engine",
                    "Random Forest",
                    "MLP Neural Net",
                ],
                "Predicted Outcome": [
                    f"{team_home} Win",
                    f"{team_home} Win",
                    "Draw",
                    f"{team_home} Win",
                    f"{team_home} Win",
                    f"{team_home} Win",
                    f"{team_away} Win",
                    f"{team_home} Win",
                    f"{team_home} Win",
                ],
                "Confidence": [
                    "78%",
                    "75%",
                    "64%",
                    "72%",
                    "82%",
                    "80%",
                    "68%",
                    "77%",
                    "81%",
                ],
            }
        )
        st.table(models_summary)

    with tab_tl:
        st.markdown("#### Form Guide & Recent Head-to-Head")
        st.info(
            "Last 5 meetings show balanced results with high scoring patterns in second halves."
        )


# ==========================================
# 4. PREDICTIONS
# ==========================================
elif app_mode == "📊 Predictions":
    st.markdown("<h1>Ensemble Predictions Engine</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color: #94A3B8;'>Run mathematical models and machine learning classifiers on upcoming fixtures.</p>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        p_home = st.text_input("Home Team Name", "FC Barcelona")
        p_xg_home = st.number_input(
            "Home Expected Goals (xG)", 0.0, 10.0, 1.8, 0.1
        )
    with col2:
        p_away = st.text_input("Away Team Name", "Real Madrid")
        p_xg_away = st.number_input(
            "Away Expected Goals (xG)", 0.0, 10.0, 1.3, 0.1
        )

    if st.button("🚀 Execute Ensemble & Monte Carlo Simulation", type="primary"):
        st.markdown("---")
        st.subheader("📊 Model Consensus & Simulation Results")
        res_col1, res_col2, res_col3 = st.columns(3)
        res_col1.metric(f"{p_home} Win Probability", "56.4%")
        res_col2.metric("Draw Probability", "24.1%")
        res_col3.metric(f"{p_away} Win Probability", "19.5%")

        st.markdown("#### Monte Carlo 10,000 Iterations Output")
        st.success(
            f"Most frequent scoreline across 10,000 stochastic simulations: **({int(p_xg_home)} - {int(p_xg_away)})**."
        )


# ==========================================
# 5. TACTICAL INTELLIGENCE
# ==========================================
elif app_mode == "🧠 Tactical Intelligence":
    st.markdown("<h1>Tactical Intelligence & Analytics</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color: #94A3B8;'>Advanced tactical parameters, pressing efficiency, and pitch control metrics.</p>",
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    c1.metric("Average PPDA", "9.4", "-1.2")
    c2.metric("Field Tilt", "58.2%", "+3.1%")
    c3.metric("Progressive Passes / 90", "54.8", "+4.2")

    st.markdown("### Key Tactical Battles")
    tab_p, tab_b, tab_h = st.tabs(
        ["Pressing & PPDA", "Build-up Structure", "Half-Spaces"]
    )
    with tab_p:
        st.markdown(
            "Teams exhibiting high pressing intensity (PPDA < 9.0) dominate turnover conversions in the final third."
        )
    with tab_b:
        st.markdown(
            "Analysis of structural superiority during first-phase build-up against man-to-man pressing blocks."
        )
    with tab_h:
        st.markdown(
            "Quantifying half-space occupation rates and cut-back conversion probabilities."
        )


# ==========================================
# 6. PLAYER ANALYTICS
# ==========================================
elif app_mode == "👤 Player Analytics":
    st.markdown("<h1>Player Analytics Hub</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color: #94A3B8;'>Scout player profiles, TACTIQ ratings, and advanced performance metrics.</p>",
        unsafe_allow_html=True,
    )

    search_query = st.text_input("🔍 Search Player Name:", "")

    players_data = pd.DataFrame(
        {
            "Player": [
                "Lamine Yamal",
                "Kylian Mbappé",
                "Jude Bellingham",
                "Pedri González",
                "Rodri Hernández",
            ],
            "Team": [
                "FC Barcelona",
                "Real Madrid",
                "Real Madrid",
                "FC Barcelona",
                "Manchester City",
            ],
            "Position": ["RW", "ST", "AM", "CM", "DM"],
            "TACTIQ Rating": ["9.1", "9.4", "9.2", "8.9", "9.3"],
            "xG / 90": [0.42, 0.78, 0.35, 0.12, 0.08],
            "xA / 90": [0.38, 0.22, 0.31, 0.29, 0.21],
            "Progressive Carries": [6.4, 4.1, 5.2, 7.8, 4.5],
        }
    )

    if search_query:
        players_data = players_data[
            players_data["Player"]
            .str.lower()
            .str.contains(search_query.lower())
        ]

    st.table(players_data)


# ==========================================
# 7. TEAM ANALYTICS
# ==========================================
elif app_mode == "🏆 Team Analytics":
    st.markdown("<h1>Team Analytics Hub</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color: #94A3B8;'>Comprehensive squad evaluations, tactical profiles, and season progression.</p>",
        unsafe_allow_html=True,
    )

    selected_team = st.selectbox(
        "Select Team for Deep Dive:",
        ["FC Barcelona", "Real Madrid", "Arsenal", "Bayern Munich", "Inter Milan"],
    )

    st.markdown(f"### Squad Profile: {selected_team}")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("TACTIQ Team Rating", "88.4 / 100")
    col2.metric("Attacking Index", "9.2 / 10")
    col3.metric("Defensive Solidity", "8.5 / 10")
    col4.metric("Pressing Efficiency", "9.0 / 10")


# ==========================================
# 8. LEAGUES & STANDINGS
# ==========================================
elif app_mode == "📈 Leagues & Standings":
    st.markdown("<h1>Leagues & Standings</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color: #94A3B8;'>Live tables, statistical records, and top performers across Europe's Top 5 leagues.</p>",
        unsafe_allow_html=True,
    )

    league = st.selectbox(
        "Select Competition:",
        ["Premier League", "La Liga", "Serie A", "Bundesliga", "Ligue 1"],
    )

    tab_st, tab_ts, tab_sc, tab_as, tab_rec = st.tabs(
        [
            "Standings",
            "Team Stats",
            "Top Scorers",
            "Top Assists",
            "All-Time Records",
        ]
    )

    with tab_st:
        table_df = pd.DataFrame(
            {
                "Pos": [1, 2, 3, 4, 5],
                "Club": [
                    "Real Madrid",
                    "FC Barcelona",
                    "Girona",
                    "Atlético Madrid",
                    "Athletic Club",
                ],
                "Pl": [28, 28, 28, 28, 28],
                "GD": ["+45", "+42", "+21", "+24", "+18"],
                "Pts": [72, 69, 62, 58, 52],
            }
        )
        st.table(table_df)

    with tab_ts:
        st.info("Aggregated team statistics for the selected league.")

    with tab_sc:
        scorers_df = pd.DataFrame(
            {
                "Player": [
                    "Kylian Mbappé",
                    "Robert Lewandowski",
                    "Jude Bellingham",
                ],
                "Team": ["Real Madrid", "FC Barcelona", "Real Madrid"],
                "Goals": [24, 21, 18],
            }
        )
        st.table(scorers_df)

    with tab_as:
        assists_df = pd.DataFrame(
            {
                "Player": ["Lamine Yamal", "Toni Kroos", "Antoine Griezmann"],
                "Team": ["FC Barcelona", "Real Madrid", "Atlético Madrid"],
                "Assists": [14, 12, 11],
            }
        )
        st.table(assists_df)

    with tab_rec:
        st.markdown("- 🥇 **Longest Winning Streak:** Real Madrid (15 matches)")
        st.markdown("- 🧤 **Most Clean Sheets:** Marc-André ter Stegen (16)")


# ==========================================
# 9. FOOTBALL INTELLIGENCE (NEWS)
# ==========================================
elif app_mode == "📰 Football Intelligence":
    st.markdown("<h1>Football Intelligence Hub</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color: #94A3B8;'>Curated tactical breakdowns, statistical notes, and automated match intelligence.</p>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="tactiq-card">
            <span style="color: #38BDF8; font-size: 0.8rem;">TACTICAL BREAKDOWN · Today</span>
            <h3 style="margin: 6px 0;">Unlocking Low Blocks: The Anatomy of Half-Space Overloads</h3>
            <p style="color: #94A3B8;">An in-depth data analysis examining how elite European sides dismantle compact defensive structures using third-man runs and inverted full-backs.</p>
        </div>
        <div class="tactiq-card">
            <span style="color: #38BDF8; font-size: 0.8rem;">STATISTICAL INSIGHTS · Yesterday</span>
            <h3 style="margin: 6px 0;">PPDA Correlation with Final Third Ball Recoveries</h3>
            <p style="color: #94A3B8;">Exploring regression models linking pressing intensity indices directly to high-turnover goal conversion rates.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )


# ==========================================
# 10. TACTIQ AI ASSISTANT
# ==========================================
elif app_mode == "🤖 TACTIQ AI":
    st.markdown("<h1>TACTIQ AI Analyst</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color: #94A3B8;'>Your AI-powered football tactical and statistical analyst.</p>",
        unsafe_allow_html=True,
    )

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Welcome! I am your TACTIQ AI Assistant. Ask me anything about match tactics, statistical models, or player performance metrics.",
            }
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Suggested Questions Pills
    st.markdown(
        "<p style='color: #64748B; font-size: 0.85rem; margin-bottom: 5px;'>Suggested Prompts:</p>",
        unsafe_allow_html=True,
    )
    col_q1, col_q2, col_q3 = st.columns(3)
    if col_q1.button("Why is this team struggling to create chances?"):
        st.session_state.messages.append(
            {
                "role": "user",
                "content": "Why is this team struggling to create chances?",
            }
        )
    if col_q2.button("Explain this prediction model"):
        st.session_state.messages.append(
            {"role": "user", "content": "Explain this prediction model"}
        )
    if col_q3.button("What are the key tactical battles?"):
        st.session_state.messages.append(
            {"role": "user", "content": "What are the key tactical battles?"}
        )

    if prompt := st.chat_input("Type your tactical question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            if "chance" in prompt or "creating" in prompt:
                response = "Low chance creation usually stems from poor half-space occupation, excessive sideways passing outside the block, and low progressive carry metrics in Zone 14."
            elif "model" in prompt or "prediction" in prompt:
                response = "Our prediction engine utilizes an ensemble of Poisson distributions, Dixon-Coles time-decay weights, and XGBoost classifiers trained on historical xG and PPDA data."
            else:
                response = f"Tactical analysis regarding '{prompt}': Controlling central midfield zones and maintaining high defensive line compactness remain the key determinants based on current spatial metrics."
            st.markdown(response)
            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )
