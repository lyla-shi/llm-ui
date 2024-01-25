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

# extract data from LLM output (json)
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

############################# UI DESIGN #######################################

# Initialize session state to store the order of agents
if 'agents_order' not in st.session_state:
    st.session_state.agents_order = []

# Function to create a single agent expander with checkbox
def create_agent(agent_name, description, index):
    # Check if the agent is already selected (exists in the session state)
    is_selected = agent_name in st.session_state.agents_order

    # Create checkbox and expander for the agent
    col1, col2 = st.sidebar.columns([0.05, 0.95])
    with col1:
        checkbox = st.checkbox("", value=is_selected, key=f"cb_{index}")
    with col2:
        with st.expander(f"{agent_name}"):
            st.write(description)

    # If the checkbox is checked/unchecked, update the order of agents
    if checkbox and agent_name not in st.session_state.agents_order:
        st.session_state.agents_order.insert(agent_name)  # Insert at the beginning
    elif not checkbox and agent_name in st.session_state.agents_order:
        st.session_state.agents_order.remove(agent_name)  # Remove from the list


# # Function to create and update agent order
# def update_agent_order(agent_name_list, description_list):
#     # Display agents based on the current order
#     for i, agent_name in enumerate(agent_name_list):
#         with st.sidebar.expander(agent_name):
#             st.write(description_list[i])
#
#         # Checkbox to select/deselect an agent
#         is_selected = st.sidebar.checkbox("Select", value=agent_name in st.session_state.agents_order,
#                                           key=f"select_{agent_name}")
#
#         # If the checkbox is checked/unchecked, update the order of agents
#         if is_selected and agent_name not in st.session_state.agents_order:
#             st.session_state.agents_order.insert(0, agent_name)  # Insert at the beginning
#         elif not is_selected and agent_name in st.session_state.agents_order:
#             st.session_state.agents_order.remove(agent_name)  # Remove from the list
#
#     # Rearrange the agents based on selection
#     st.session_state.agents_order = [agent for agent in agent_name_list if agent in st.session_state.agents_order] + \
#                                     [agent for agent in agent_name_list if agent not in st.session_state.agents_order]


def update_agent(agent_name_list, description_list):
    # print(st.session_state.agents_order)
    if st.session_state.agents_order != []:
        for n in range (len(st.session_state.agents_order)):
            st.sidebar.write(f"Agent {n+1}")

            #find the exact agent
            agent_index = agent_name_list.index(st.session_state.agents_order[n])

            # Create checkbox and expander for the agent
            col1, col2 = st.sidebar.columns([0.05, 0.95])
            with col1:
                checkbox = st.checkbox("", value=True, key=f"cb_{agent_index}")
            with col2:
                with st.expander(f"{agent_name_list[agent_index]}"):
                    st.write(description_list[agent_index])

                # If the checkbox is checked/unchecked, update the order of agents
            # if checkbox and agent_name_list[n] not in st.session_state.agents_order:
            #     st.session_state.agents_order.append(agent_name_list[agent_index])  # Insert at the beginning
            if not checkbox and agent_name_list[n] in st.session_state.agents_order:
                st.session_state.agents_order.remove(agent_name_list[agent_index])  # Remove from the list
                # update_agent(agent_name_list, description_list)

    # st.write("we are here 1")
    for i in range(len(agent_name_list)):
        # st.write(agent_name_list[i])
        if agent_name_list[i] in st.session_state.agents_order:
            # st.write("we are here 2")
            print("")
        else:
            # st.write("start loop")
            # Create checkbox and expander for the agent
            col1, col2 = st.sidebar.columns([0.05, 0.95])
            with col1:
                checkbox = st.checkbox("", value=False, key=f"cb_{i}")
            with col2:
                with st.expander(f"{agent_name_list[i]}"):
                    st.write(description_list[i])

            if checkbox and agent_name_list[i] not in st.session_state.agents_order:
                st.session_state.agents_order.append(agent_name_list[i])  # Insert at the beginning
                # update_agent(agent_name_list, description_list)


def debate_in_tab(tab):
    for n in range(len(st.session_state.agents_order)):


        # implement debate function
        if n<=2:
            col1, col2, col3 = tab.columns([0.1, 0.75, 0.15])
            with col1:
                st.write(f"Agent {n+1}")
            with col2:
                st.write(debate_list[n])
                col11, col22, col33 = st.columns([0.72,0.13,0.15])
                with col22:
                    st.button("up", key=f"debate_agree_{n}")
                with col33:
                    st.button("down", key=f"debate_disagree_{n}")
            with col3:
                # st.markdown(
                # "<div style='height: 100%; display: flex; flex-direction: column; justify-content: flex-end;'>",
                # unsafe_allow_html=True)
                st.button("more +", key=f"debate_more_{n}")
                st.button("less -", key=f"debate_less_{n}")
                # st.markdown("</div>", unsafe_allow_html=True)
                # Custom buttons using Streamlit's button style
                # st.markdown(f"""
                #                     <div style="display: flex; flex-direction: column; justify-content: flex-end; align-items: bottom; height: 100%;">
                #                         <button class="stButton" style="margin: 0.5em;">more +</button>
                #                         <button class="stButton" style="margin: 0.5em;">less -</button>
                #                     </div>
                #                     """, unsafe_allow_html=True)

# Title
st.title('Topic: Can alternative energy effectively replace fossil fuels?')

# Agents in Debate
st.sidebar.header('Agents in Debate')
# Display the current order of agents for debugging purposes
print('Current order of agents:', st.session_state.agents_order)


# Display agents based on the current order
# if st.session_state.agents_order == []:
#     for i in range(len(highlights_list)):
#         create_agent(highlights_list[i], descriptions_list[i], i)
# else:
#     # st.write()
#     for n in range (len(st.session_state.agents_order)):
#         st.sidebar.write(f"Agent {n+1}")
#         create_agent(highlights_list[n], descriptions_list[n], n)

update_agent(highlights_list, descriptions_list)
# update_agent_order(names_list, descriptions_list)


# Start Debate button
start_bt = st.sidebar.button('Start Debate')
if start_bt:
    if len(st.session_state.agents_order) >= 2:
        st.success('The debate has started!')
    else:
        st.warning('Please select at least two agents to start the debate.')






# Debate rounds
tab1, tab2, tab3 = st.tabs(["Round 1", "Round 2", "Round 3"])
if start_bt:
    debate_in_tab(tab1)
    col1, col2 = tab1.columns([0.1,0.9])

else:
    tab1.write("Please select at least 2 agents in the left sidebar.")