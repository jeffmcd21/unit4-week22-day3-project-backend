
from .models import Team_Info
from .models import Batter_Info
from rest_framework import serializers

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Team_Info
        fields=('id','Sport', 'Sport_Short_Description', 'League_Division', 'League', 'League_Short_Description', 'Division', 'Team', 'Team_Location', 'Team_Name', 'Location_Code', 'Image')

class BatterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Batter_Info
        fields=('id','last_name' ,'first_name' ,'player_id' ,'year' ,'player_age' ,'b_ab' ,'b_total_pa' ,'b_total_hits' ,'b_single' ,'b_double' ,'b_triple' ,'b_home_run' ,'b_strikeout' ,'b_walk' ,'b_k_percent' ,'b_bb_percent' ,'batting_avg' ,'slg_percent' ,'on_base_percent' ,'on_base_plus_slg' ,'isolated_power' ,'b_rbi' ,'b_lob' ,'b_total_bases' ,'r_total_caught_stealing' ,'r_total_stolen_base' ,'b_ab_scoring' ,'b_ball' ,'b_called_strike' ,'b_catcher_interf' ,'b_foul' ,'b_foul_tip' ,'b_game' ,'b_gnd_into_dp' ,'b_gnd_into_tp' ,'b_gnd_rule_double' ,'b_hit_by_pitch' ,'b_hit_ground' ,'b_hit_fly' ,'b_hit_into_play' ,'b_hit_line_drive' ,'b_hit_popup' ,'b_out_fly' ,'b_out_ground' ,'b_out_line_drive' ,'b_out_popup' ,'b_intent_ball' ,'b_intent_walk' ,'b_interference' ,'b_pinch_hit' ,'b_pinch_run' ,'b_pitchout' ,'b_played_dh' ,'b_sac_bunt' ,'b_sac_fly' ,'b_swinging_strike' ,'r_caught_stealing_2b' ,'r_caught_stealing_3b' ,'r_caught_stealing_home' ,'r_defensive_indiff' ,'r_interference' ,'r_pickoff_1b' ,'r_pickoff_2b' ,'r_pickoff_3b' ,'r_run' ,'r_stolen_base_2b' ,'r_stolen_base_3b' ,'r_stolen_base_home' ,'b_total_ball' ,'b_total_sacrifices' ,'b_total_strike' ,'b_total_swinging_strike' ,'b_total_pitches' ,'r_stolen_base_pct' ,'r_total_pickoff' ,'b_reached_on_error' ,'b_walkoff' ,'b_reached_on_int')
        