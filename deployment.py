import pandas as pd 
import numpy as np 
import pickle 
import streamlit as stl 
from PIL import Image 

# loading in the model to predict on the data 
with open('voting_regressor.pkl', 'rb') as pickle_in:
    voting_regressor = pickle.load(pickle_in)

def welcome(): 
    return 'welcome all'

# defining the function which will make the prediction using  
# the data which the user inputs 
def prediction(potential, value_eur, wage_eur, age, league_level,
       weak_foot, skill_moves, international_reputation, shooting,
       passing, dribbling, defending, physic, attacking_crossing,
       attacking_finishing, attacking_heading_accuracy,
       attacking_short_passing, attacking_volleys, skill_dribbling,
       skill_curve, skill_fk_accuracy, skill_long_passing,
       skill_ball_control, movement_acceleration, movement_sprint_speed,
       movement_agility, movement_reactions, power_shot_power,
       power_jumping, power_stamina, power_strength, power_long_shots,
       mentality_aggression, mentality_interceptions,
       mentality_positioning, mentality_vision, mentality_penalties,
       mentality_composure, defending_marking_awareness,
       defending_standing_tackle, defending_sliding_tackle, club_name,
       ls, st, rs, lw, lf, cf, rf, rw, lam, cam, ram,
       lm, lcm, cm, rcm, rm, lwb, ldm, cdm, rdm, rwb, lb,
       rb, gk ):
  prediction = voting_regressor.predict( 
        [[potential, value_eur, wage_eur, age, league_level,
       weak_foot, skill_moves, international_reputation, shooting,
       passing, dribbling, defending, physic, attacking_crossing,
       attacking_finishing, attacking_heading_accuracy,
       attacking_short_passing, attacking_volleys, skill_dribbling,
       skill_curve, skill_fk_accuracy, skill_long_passing,
       skill_ball_control, movement_acceleration, movement_sprint_speed,
       movement_agility, movement_reactions, power_shot_power,
       power_jumping, power_stamina, power_strength, power_long_shots,
       mentality_aggression, mentality_interceptions,
       mentality_positioning, mentality_vision, mentality_penalties,
       mentality_composure, defending_marking_awareness,
       defending_standing_tackle, defending_sliding_tackle, club_name,
       ls, st, rs, lw, lf, cf, rf, rw, lam, cam, ram,
       lm, lcm, cm, rcm, rm, lwb, ldm, cdm, rdm, rwb, lb,
       rb, gk 
          ]]) 
  print(prediction) 
  return prediction   

# this is the main function in which we define our webpage  
def main(): 
      # giving the webpage a title 
    stl.title("A Football Player's Overall Rating Prediction") 
      
    # here we define some of the front end elements of the web page like  
    # the font and background color, the padding and the text to be displayed 
    html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Overall Rating Voting Regressor ML App </h1> 
    </div> 
    """
      
    # this line allows us to display the front end aspects we have  
    # defined in the above code 
    stl.markdown(html_temp, unsafe_allow_html = True) 
      
    # the following lines create text boxes in which the user can enter  
    # the data required to make the prediction     
    potential = stl.number_input("potential", 0) 
    value_eur = stl.number_input("value (eur)", 0)
    wage_eur = stl.number_input("wage (eur)", 0)
    age = stl.number_input("age", 0)
    league_level = stl.number_input("league_level", 0)
    weak_foot = stl.number_input("weak_foot", 0)
    skill_moves = stl.number_input("skill_moves", 0)
    international_reputation = stl.number_input("international_reputation", 0)
    shooting = stl.number_input("shooting", 0)
    passing = stl.number_input("passing", 0)
    dribbling = stl.number_input("dribbling", 0)
    defending = stl.number_input("defending", 0)
    physic = stl.number_input("physic", 0)
    attacking_crossing = stl.number_input("attacking_crossing", 0)
    attacking_finishing = stl.number_input("attacking_finishing", 0)
    attacking_heading_accuracy = stl.number_input("attacking_heading_accuracy", 0)
    attacking_short_passing = stl.number_input("attacking_short_passing", 0)
    attacking_volleys = stl.number_input("attacking_volleys", 0)
    skill_dribbling = stl.number_input("skill_dribbling", 0)
    skill_curve = stl.number_input("skill_curve", 0)
    skill_fk_accuracy = stl.number_input("skill_fk_accuracy", 0)
    skill_long_passing = stl.number_input("skill_long_passing", 0)
    skill_ball_control = stl.number_input("skill_ball_control", 0)
    movement_acceleration = stl.number_input("movement_acceleration", 0)
    movement_sprint_speed = stl.number_input("movement_sprint_speed", 0)
    movement_agility = stl.number_input("movement_agility", 0)
    movement_reactions = stl.number_input("movement_reactions", 0)
    power_shot_power = stl.number_input("power_shot_power", 0)
    power_jumping = stl.number_input("power_jumping", 0)
    power_stamina = stl.number_input("power_stamina", 0)
    power_strength = stl.number_input("power_strength", 0)
    power_long_shots = stl.number_input("power_long_shots", 0)
    mentality_aggression = stl.number_input("mentality_aggression", 0)
    mentality_interceptions = stl.number_input("mentality_interceptions", 0)
    mentality_positioning = stl.number_input("mentality_positioning", 0)
    mentality_vision = stl.number_input("mentality_vision", 0)
    mentality_penalties = stl.number_input("mentality_penalties", 0)
    mentality_composure = stl.number_input("mentality_composure", 0)
    defending_marking_awareness = stl.number_input("defending_marking_awareness", 0)
    defending_standing_tackle = stl.number_input("defending_standing_tackle", 0)
    defending_sliding_tackle = stl.number_input("defending_sliding_tackle", 0)
    club_name = stl.number_input("club_name", 0)
    ls = stl.number_input("ls", 0)
    st = stl.number_input("st", 0)
    rs = stl.number_input("rs", 0)
    lw = stl.number_input("lw", 0)
    lf = stl.number_input("lf", 0)
    cf = stl.number_input("cf", 0)
    rf = stl.number_input("rf", 0)
    rw = stl.number_input("rw", 0)
    lam = stl.number_input("lam", 0)
    cam = stl.number_input("cam", 0)
    ram = stl.number_input("ram", 0)
    lm = stl.number_input("lm", 0)
    lcm = stl.number_input("lcm", 0)
    cm = stl.number_input("cm", 0)
    rcm = stl.number_input("rcm", 0)
    rm = stl.number_input("rm", 0)
    lwb = stl.number_input("lwb", 0)
    ldm = stl.number_input("ldm", 0)
    cdm = stl.number_input("cdm", 0)
    rdm = stl.number_input("rdm", 0)
    rwb = stl.number_input("rwb", 0)
    lb = stl.number_input("lb", 0)
    rb = stl.number_input("rb", 0)
    gk = stl.number_input("gk", 0)
    result ="" 
      
    # the below line ensures that when the button called 'Predict' is clicked,  
    # the prediction function defined above is called to make the prediction  
    # and store it in the variable result 
    if stl.button("Predict"): 
        result = prediction(potential, value_eur, wage_eur, age, league_level,
       weak_foot, skill_moves, international_reputation, shooting,
       passing, dribbling, defending, physic, attacking_crossing,
       attacking_finishing, attacking_heading_accuracy,
       attacking_short_passing, attacking_volleys, skill_dribbling,
       skill_curve, skill_fk_accuracy, skill_long_passing,
       skill_ball_control, movement_acceleration, movement_sprint_speed,
       movement_agility, movement_reactions, power_shot_power,
       power_jumping, power_stamina, power_strength, power_long_shots,
       mentality_aggression, mentality_interceptions,
       mentality_positioning, mentality_vision, mentality_penalties,
       mentality_composure, defending_marking_awareness,
       defending_standing_tackle, defending_sliding_tackle, club_name,
       ls, st, rs, lw, lf, cf, rf, rw, lam, cam, ram,
       lm, lcm, cm, rcm, rm, lwb, ldm, cdm, rdm, rwb, lb,
       rb, gk ) 
    stl.success(f'The output is {int(result[0])}') 
     
if __name__=='__main__': 
    main() 