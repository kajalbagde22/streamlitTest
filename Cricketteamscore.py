import streamlit as st

# Function to update the score
def update_score(team, runs, wickets):
    score[team]['runs'] += runs
    score[team]['wickets'] += wickets

# Initialize the score dictionary
score = {
    'Team A': {'runs': 0, 'wickets': 0},
    'Team B': {'runs': 0, 'wickets': 0}
}

# Streamlit app layout
st.title("Cricket Team Score App")

# Select the team
team = st.selectbox("Select Team", ["Team A", "Team B"])

# Input runs and wickets
runs = st.number_input("Runs", min_value=0, step=1)
wickets = st.number_input("Wickets", min_value=0, max_value=10, step=1)

# Button to update the score
if st.button("Update Score"):
    update_score(team, runs, wickets)
    st.success(f"Updated {team}'s score!")

# Display the current score
st.write("### Current Score")
st.write(f"**Team A**: {score['Team A']['runs']} runs, {score['Team A']['wickets']} wickets")
st.write(f"**Team B**: {score['Team B']['runs']} runs, {score['Team B']['wickets']} wickets")

# Reset scores
if st.button("Reset Scores"):
    score = {
        'Team A': {'runs': 0, 'wickets': 0},
        'Team B': {'runs': 0, 'wickets': 0}
    }
    st.success("Scores have been reset!")
