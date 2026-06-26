
import streamlit as st

st.set_page_config(page_title="Sharps Blueprint", layout="centered")

st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Go to:", ["The Blueprint (Big Wins)", "The Spread Sandbox"])

if page == "The Blueprint (Big Wins)":
    st.title("💰 The Blueprint: From Broke to $3K")
    st.caption("Don't let anyone tell you it's impossible. I've got the receipts.")
    st.markdown("---")
    st.subheader("🔥 The Reality of the Mega-Hit")
    st.write("We've all been there—down to pocket change, looking at a board of games, and stringing together a monster 15-legger. A couple of hours later, the final whistle blows and you're up $2,000 or $3,000. It's real, it happens, and anyone telling you 'never play parlays' doesn't know the feeling of a pure max-payout heater.")
    st.markdown("### 🚀 Scale Your Moonshot")
    col1, col2 = st.columns(2)
    with col1:
        ticket_legs = st.slider("How many legs on the ticket?", min_value=10, max_value=16, value=15)
        spare_change = st.slider("Your wager amount (Keep it to spare change)", min_value=1, max_value=5, value=2)
    with col2:
        hypothetical_odds = (1.85 ** ticket_legs) * 100
        payout = spare_change * (hypothetical_odds / 100)
        st.metric(label="🎯 Real Potential Payout", value=f"${payout:,.2f}")
    st.markdown("---")
    st.subheader("🔑 The Secret to Staying in the Game")
    rule1, rule2 = st.columns(2)
    with rule1:
        st.success("### 🟢 The $2 Professional Dart")
        st.markdown("**Why this is the Sharp play:**\n* You get 100% of the thrill.\n* You get the exact same $2,000+ payout.\n* If the chain breaks, you lose the price of a soda.")
    with rule2:
        st.error("### 🔴 The $50 Sucker Trap")
        st.markdown("**Why this breaks you:**\n* The sportsbook wants you to bet this much.\n* Three misses in a week drains $150.\n* You go broke and miss the night the actual 15-legger hits.")

elif page == "The Spread Sandbox":
    st.title("⚡ The Spread Sandbox")
    st.markdown("---")
    st.subheader("1. Pick Your Numbers")
    col1, col2 = st.columns(2)
    with col1:
        spread = st.slider("What is the Spread?", min_value=0.5, max_value=14.5, value=3.5, step=0.5)
    with col2:
        fav_score = st.slider("Favorite's Final Score", min_value=0, max_value=50, value=24)
        und_score = st.slider("Underdog's Final Score", min_value=0, max_value=50, value=21)
    score_difference = fav_score - und_score
    st.subheader("🏁 The Result")
    card_fav, card_und = st.columns(2)
    with card_fav:
        if score_difference > spread:
            st.success("### 🟢 FAVORITE: WIN")
        else:
            st.error("### 🔴 FAVORITE: LOSS")
    with card_und:
        if score_difference < spread:
            st.success("### 🟢 UNDERDOG: WIN")
        else:
            st.error("### 🔴 UNDERDOG: LOSS")