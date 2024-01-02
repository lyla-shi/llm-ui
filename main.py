import streamlit as st

# demo info from LLM
title = "Can alternative energy effectively replace fossil fuels?"
ini_persona_json = [
  {
    "name": "Dr. Green",
    "stance": "support",
    "highlight": "Advocate for Renewable Transition",
    "description": "An environmental scientist who strongly supports the shift to alternative energy for a sustainable future."
  },
  {
    "name": "Mr. Volt",
    "stance": "support",
    "highlight": "Believer in Electric Potential",
    "description": "An electric vehicle entrepreneur who believes electric power can replace fossil fuels in transportation."
  },
  {
    "name": "Ms. Sunny",
    "stance": "support",
    "highlight": "Solar Energy Enthusiast",
    "description": "A solar energy startup founder who sees solar power as a key player in energy replacement."
  },
  {
    "name": "The Economist",
    "stance": "neutral",
    "highlight": "Economic Transition Analyst",
    "description": "An economist analyzing the feasibility and economic impact of the transition from fossil fuels to alternative energy."
  },
  {
    "name": "Grid Master",
    "stance": "neutral",
    "highlight": "Energy Grid Pragmatist",
    "description": "A power grid operator who is neutral and focuses on the challenges of integrating renewable energy into existing grids."
  },
  {
    "name": "Policy Advisor",
    "stance": "neutral",
    "highlight": "Legislative Impact Assessor",
    "description": "A government advisor who takes a balanced approach, assessing the impacts of energy policy changes."
  },
  {
    "name": "Oil Baron",
    "stance": "deny",
    "highlight": "Fossil Fuel Advocate",
    "description": "A veteran oil industry lobbyist who denies the practicality of replacing fossil fuels with alternative energy."
  },
  {
    "name": "Coal Proponent",
    "stance": "deny",
    "highlight": "Coal Industry Defender",
    "description": "A spokesperson for the coal industry who believes coal is irreplaceable in the energy sector."
  },
  {
    "name": "Nuclear Pro",
    "stance": "deny",
    "highlight": "Pro-Nuclear Energy Argument",
    "description": "A nuclear engineer who argues that nuclear power is a more reliable and powerful alternative than renewable sources."
  }
]

def json_to_lists(json_data):
    # Initialize empty lists for each key
    names = []
    highlights = []
    descriptions = []

    # Loop through each item in the JSON data and append to respective lists
    for item in json_data:
        names.append(item['name'])
        highlights.append(item['highlight'])
        descriptions.append(item['description'])

    return names, highlights, descriptions

names_list, highlights_list, descriptions_list = json_to_lists(ini_persona_json)


debate_list = [
    "Ladies and gentlemen, I stand before you as a staunch supporter of our planet's future. The science is unequivocal; renewable energy sources are not only viable but necessary for a sustainable future. Solar, wind, and hydroelectric power offer us a clean, inexhaustible supply of energy that could effectively replace fossil fuels. While the upfront costs and transition efforts are considerable, the long-term environmental and health benefits far outweigh these initial investments. We must act now to mitigate the effects of climate change and protect our environment for future generations. The transition to renewable energy is a pivotal step in this direction.",
    "Dr. Green presents a compelling case for the environmental imperatives of alternative energy. However, from an economic standpoint, the transition from fossil fuels to alternative energy sources requires careful consideration of feasibility and impact. While renewables have become more cost-competitive, the energy sector's intricate ties to global economies cannot be understated. Job markets, existing infrastructure, and the uneven global distribution of technology and resources present significant challenges. An abrupt shift could lead to economic disruptions. A phased and well-planned approach is essential to balance environmental benefits with economic stability.",
    "I appreciate the insights shared by Dr. Green and The Economist. However, I must emphasize that coal remains a cornerstone of energy production, particularly in developing economies. It is a reliable and affordable source of energy that supports numerous jobs and industries. The proposition that alternative energy can effectively replace fossil fuels does not fully account for the reliability and energy security provided by coal. Furthermore, technologies like clean coal and carbon capture offer a path to reducing emissions without abandoning a resource that has powered our progress for centuries. We cannot overlook the role of coal in meeting our current and future energy demands."
]

debate_list2 = [
    "Let's address the elephant in the room: the true cost of coal and fossil fuels is hidden in their environmental impact, a cost that future generations will bear. Recent studies have shown that the cost of renewable energy sources, such as solar and wind, have dramatically decreased, to the point where they are at parity or even cheaper than coal in many regions. Moreover, renewable infrastructure has the potential to create more jobs than the fossil fuel industry currently does. We have a moral and scientific obligation to prioritize long-term sustainability over short-term convenience. The evidence is clear: renewable energy not only can but must replace fossil fuels for an equitable and livable planet.",
    "While the coal industry has historically been a linchpin of the economy, we cannot ignore the externalities it imposes on health and the environment, which in turn have economic repercussions. The healthcare costs of pollution, the environmental degradation, and the economic impact of climate change-related weather events often do not factor into the price of coal. Transitioning to alternative energies represents not only an environmental investment but also an economic strategy for sustainable growth. The question we should be asking is not if we can afford this transition, but if we can afford not to make it.",
    "Renewable energy is indeed advancing, but the reliability and energy density of coal are not matched by current renewable technologies. Intermittency issues with solar and wind energy require substantial investment in storage solutions, which are not yet advanced enough to handle baseline loads. While the environmental concerns are valid, coal technology is evolving with cleaner alternatives, and we are seeing advancements in carbon capture and storage that can mitigate its environmental impact. The energy transition is more complex than a simple switch, and coal will continue to play a significant role in ensuring energy security and meeting industrial needs during this transition period."
]

###################################UI design############################################

# Initialize the session state for the selected views and debate status
if 'selected_views' not in st.session_state:
    st.session_state.selected_views = []

if 'debate_started' not in st.session_state:
    st.session_state.debate_started = False

if 'next_round' not in st.session_state:
    st.session_state.next_round = False

# Function to handle the selection of views
def select_view(view_content):
    # Check if the view is already selected
    if view_content not in st.session_state.selected_views:
        # If three views are already selected, remove the oldest one
        if len(st.session_state.selected_views) == 3:
            st.session_state.selected_views.pop(0)
        # Add the new view
        st.session_state.selected_views.append(view_content)

# Function to create the debate interface
def create_debate_interface():
    # st.header("Topic: Is golfer athletes?")
    st.subheader("Debate Round 1:")
    for i in range(1, 4):
        st.subheader(f"V{i} Argument")
        col1, col2 = st.columns([0.85, 0.15], gap="small")
        with col1:
            st.write(f"{debate_list[i-1]}" , key=f"p{i}_args")
        # col1, col2 = st.columns(2)
        with col2:
            button_placeholder = st.empty()
            if button_placeholder.button(f"Attack", key=f"attack_{i}"):
                button_placeholder.markdown("""
                        <style>
                        .fake-button {
                            border: none;
                            color: white;
                            padding: 0.375rem 0.75rem;
                            text-align: center;
                            text-decoration: none;
                            display: inline-block;
                            font-size: 1rem;
                            margin: 4px 2px;
                            transition-duration: 0.4s;
                            cursor: pointer;
                            background-color: #ff4b4b; /* Red color */
                            color: white;
                            border-radius: 0.25rem;
                        }
                        </style>
                        <div class="fake-button">Attack</div>
                """, unsafe_allow_html=True)

            button_placeholder2 = st.empty()
            if button_placeholder2.button(f"Defend", key=f"defend_{i}"):
                button_placeholder2.markdown("""
                                       <style>
                                       .fake-button {
                                           border: none;
                                           color: white;
                                           padding: 0.375rem 0.75rem;
                                           text-align: center;
                                           text-decoration: none;
                                           display: inline-block;
                                           font-size: 1rem;
                                           margin: 4px 2px;
                                           transition-duration: 0.4s;
                                           cursor: pointer;
                                           background-color: #007bff; /* blue color */
                                           color: white;
                                           border-radius: 0.25rem;
                                       }
                                       </style>
                                       <div class="fake-button">Defend</div>
                               """, unsafe_allow_html=True)
    if st.button("start next round debate"):
        st.session_state.next_round = True

    # Add Attack and Defend buttons for each selected view in the sidebar
    # for i, view_content in enumerate(st.session_state.selected_views, start=1):
    #     # st.sidebar.write(f"View {i}")
    #     # st.sidebar.write(view_content or "No content selected")
    #     col1, col2 = st.sidebar.columns(2)
    #     with col1:
    #         st.button(f"Attack View {i}", key=f"attack_{i}")
    #     with col2:
    #         st.button(f"Defend View {i}", key=f"defend_{i}")

def create_2round_interface():
    st.subheader("Debate Round 2:")
    for i in range(1, 4):
        st.subheader(f"V{i} Argument")
        col1, col2 = st.columns([0.85, 0.15], gap="small")
        with col1:
            st.write(f"{debate_list2[i-1]}" , key=f"p{i}_args")
        # col1, col2 = st.columns(2)
        with col2:
            button_placeholder = st.empty()
            if button_placeholder.button(f"Attack", key=f"attack2_{i}"):
                button_placeholder.markdown("""
                        <style>
                        .fake-button {
                            border: none;
                            color: white;
                            padding: 0.375rem 0.75rem;
                            text-align: center;
                            text-decoration: none;
                            display: inline-block;
                            font-size: 1rem;
                            margin: 4px 2px;
                            transition-duration: 0.4s;
                            cursor: pointer;
                            background-color: #ff4b4b; /* Red color */
                            color: white;
                            border-radius: 0.25rem;
                        }
                        </style>
                        <div class="fake-button">Attack</div>
                """, unsafe_allow_html=True)

            button_placeholder2 = st.empty()
            if button_placeholder2.button(f"Defend", key=f"defend2_{i}"):
                button_placeholder2.markdown("""
                                       <style>
                                       .fake-button {
                                           border: none;
                                           color: white;
                                           padding: 0.375rem 0.75rem;
                                           text-align: center;
                                           text-decoration: none;
                                           display: inline-block;
                                           font-size: 1rem;
                                           margin: 4px 2px;
                                           transition-duration: 0.4s;
                                           cursor: pointer;
                                           background-color: #007bff; /* blue color */
                                           color: white;
                                           border-radius: 0.25rem;
                                       }
                                       </style>
                                       <div class="fake-button">Defend</div>
                               """, unsafe_allow_html=True)
    st.button("continue next round debate")
        # st.session_state.next_round = True


# Sidebar for roundtable debate personas
st.sidebar.header("Roundtable Debate Personas")
# Display the selected views in the sidebar
for i, view_content in enumerate(st.session_state.selected_views, start=1):
    st.sidebar.write(f"View {i}")
    st.sidebar.info(view_content or "No content selected")  # Show a message if no content

# Only show the button if more than two views have been selected
if len(st.session_state.selected_views) > 2 and not st.session_state.debate_started:
    if st.sidebar.button("Finish Selection Start Debate"):
        st.session_state.debate_started = True

# Main content area for the topic
st.title(f"Topic: {title}")

if not st.session_state.debate_started:
    # Content and view selection buttons are shown here
    # Define the view contents
    view_contents = [
        "Support - Content for View 1", "Support - Content for View 2", "Support - Content for View 3",
        "Neutral - Content for View 4", "Neutral - Content for View 5", "Neutral - Content for View 6",
        "Deny - Content for View 7", "Deny - Content for View 8", "Deny - Content for View 9"
    ]

    # Create buttons for each view in the main content area
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Support")
        for i in range(3):
            with st.expander(highlights_list[i]):
                st.write(descriptions_list[i])
                if st.button("select", key=i):
                    select_view(highlights_list[i])

    with col2:
        st.subheader("Neutral")
        for i in range(3, 6):
            with st.expander(highlights_list[i]):
                st.write(descriptions_list[i])
                if st.button("select", key=i):
                    select_view(highlights_list[i])

    with col3:
        st.subheader("Deny")
        for i in range(6, 9):
            with st.expander(highlights_list[i]):
                st.write(descriptions_list[i])
                if st.button("select", key=i):
                    select_view(highlights_list[i])

if st.session_state.debate_started and not st.session_state.next_round:
    create_debate_interface()

    if st.sidebar.button("Back"):
        st.session_state.debate_started = False
        st.session_state.debate_started = False
        st.session_state.selected_views.clear()


# When the next round starts, clear the page and show the new round message
if st.session_state.next_round:

    st.session_state.debate_started = False  # Reset debate started state
    create_2round_interface()
    st.session_state.next_round = False  # Reset next round state
    # st.experimental_rerun()  # Rerun the app to clear the page/

# else:
#     # Show the debate starting message and a "Back" button to reset the view
#     # Once the debate starts, create the new interface based on the sketch
#     # placeholder=st.empty()
#     # placeholder.empty()
#     create_debate_interface()
# import streamlit as st
#

