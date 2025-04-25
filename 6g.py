import streamlit as st
import random
import matplotlib.pyplot as plt

# Title and Description
st.set_page_config(page_title="AI for RF Pollution & Space Debris - Game Prototype")
# Displaying the uploaded image as a header
st.image("C:/Users/darsh/OneDrive/Pictures/Screenshots/Screenshot 2025-04-15 125900.png", use_container_width=True)

st.title("🌐 AI-Driven Sustainable 6G Game")
st.markdown("""
Welcome to the **AI-Powered Network Optimization Game**! 
Make eco-friendly routing decisions and beat RF Pollution & Space Debris while maximizing network performance.
""")

# Input State
st.sidebar.header("📥 Simulation Inputs")
user_density = st.sidebar.slider("User Density", 0, 100, 50)
rf_pollution = st.sidebar.slider("RF Pollution Level", 0, 100, 40)
satellite_count = st.sidebar.slider("Satellite Count", 0, 100, 30)

state = {
    'user_density': user_density,
    'rf_pollution': rf_pollution,
    'satellite_count': satellite_count,
}

# DQN Model Decision
def dqn_predict(state):
    if state['user_density'] > 70:
        return 'satellite'
    elif state['user_density'] > 40:
        return 'aerial'
    else:
        return 'terrestrial'

# Swarm Intelligence
def swarm_enhance(decision, rf, satellites):
    if rf > 70:
        penalty = 15
    elif rf > 50:
        penalty = 10
    else:
        penalty = 5

    if satellites > 60:
        boost = -10
    else:
        boost = 10

    eco_boost = {'terrestrial': 20, 'aerial': 10, 'satellite': -5}
    base = 100 - (rf * 0.4 + satellites * 0.4)
    return max(0, min(100, round(base + boost + eco_boost[decision] - penalty, 2)))

# Final Hybrid Selection
def hybrid_network_select(state):
    decision = dqn_predict(state)
    eco_score = swarm_enhance(decision, state['rf_pollution'], state['satellite_count'])

    latency_mod = {'terrestrial': 1.0, 'aerial': 0.9, 'satellite': 0.75}
    final_latency = round(50 * latency_mod[decision], 2)

    return decision, final_latency, eco_score

# Game Logic Execution
decision, final_latency, eco_score = hybrid_network_select(state)

# Visual Outputs
st.subheader("🧠 AI Decision Result")
st.success(f"Selected Mode: **{decision.upper()}**")
st.metric("Final Latency (ms)", final_latency)
st.metric("Eco Sustainability Score", f"{eco_score}/100")

# Reward Level
if eco_score > 80:
    st.success("🎉 Excellent! You've created a sustainable 6G route!")
elif eco_score > 60:
    st.info("🙂 Good Job! Room for improvement in sustainability.")
else:
    st.warning("⚠️ Try optimizing again. Too much interference or debris!")

# Visual Dashboard - Eco Score
fig, ax = plt.subplots()
ax.bar(['Eco Score'], [eco_score], color='green' if eco_score > 80 else 'orange')
ax.set_ylim(0, 100)
ax.set_ylabel("Eco Score")
ax.set_title("🌿 Sustainability Dashboard")
st.pyplot(fig)

st.markdown("""
---
**Game Engine:** Reinforcement Learning (DQN), ACO, Bee Algorithm  
**Architecture:** Hybrid Network - Terrestrial, Aerial, Satellite
**Model By:** Darshana P BTITECH01
""")
