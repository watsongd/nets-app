module_mappings = {
    'player_career': [
        'all_star_season_totals',
        'career_all_star_season_totals',
        'college_season_career_totals',
        'college_season_totals',
        'post_season_career_totals',
        'post_season_rankings',
        'post_season_totals',
        'preseason_career_totals',
        'preseason_season_totals',
        'regular_season_career_totals',
        'regular_season_rankings',
        'regular_season_totals'
    ],
    'player_clutch_splits': [
        'last10sec_deficit_3point',
        'last1min_deficit_5point',
        'last1min_plusminus_5point',
        'last30sec_deficit_3point',
        'last30sec_plusminus_5point',
        'last3min_deficit_5point',
        'last3min_plusminus_5point',
        'last5min_deficit_5point',
        'last5min_plusminus_5point'
    ],
    #  No functions so map it to itself (this will work with the way _get_query_keys works)
    'player_defense_tracking': [ 'player_defense_tracking' ], 
    'player_game_logs': [ 'info' ],
    'player_general_splits': [
        'days_rest',
        'location',
        'month',
        'pre_post_all_star',
        'starting_position',
        'win_losses'
    ],
    'player_in_game_splits': [
        'by_actual_margin',
        'by_half',
        'by_period',
        'by_score_margin'
    ],
    'player_last_n_games_splits': [
        'last10',
        'last15',
        'last20', 
        'last5'
    ],
    # 'player_list': [ 'info' ], removed because not numerical
    'player_opponent_splits': [
        'by_conference',
        'by_division',
        'by_opponent'
    ],
    'player_pass_tracking': [
        'passes_made',
        'passes_received'
    ],
    'player_performance_splits': [
        'points_against',
        'points_scored',
        'score_differential'
    ],
    'player_profile': [
        'career_highs',
        'next_game',
        'season_highs'
    ],
    'player_rebound_log_tracking': [
        'player_rebound_log_tracking' 
    ],
    'player_rebound_tracking': [
        'num_contested_rebounding',
        'rebound_distance_rebounding',
        'shot_distance_rebounding',
        'shot_type_rebounding'
    ],
    'player_shooting_splits': [
        'assisted_by',
        'assisted_shots',
        'shot_5ft',
        'shot_8ft',
        'shot_areas',
        'shot_types_detail',
        'shot_types_summary'
    ],
    'player_shot_log_tracking': [
        'player_shot_log_tracking'
    ],
    'player_shot_tracking': [
        'closest_defender_shooting',
        'closest_defender_shooting_long',
        'dribble_shooting',
        'general_shooting',
        'shot_clock_shooting',
        'touch_time_shooting'
    ],
    # 'player_summary': [ 'info' ], removed because not numerical
    'player_vs_player': [
        'on_off_court',
        'overall',
        'player_info',
        'shot_area_off_court',
        'shot_area_overall',
        'shot_distance_off_court',
        'shot_distance_on_court',
        'shot_distance_overall',
        'vs_player_info'
    ],
    'player_year_over_year_splits': [
        'by_year'
    ]
}

x_axis_mappings = {
    'SEASON_ID': [
        'all_star_season_totals',
        'career_all_star_season_totals',
        'college_season_career_totals',
        'college_season_totals',
        'post_season_career_totals',
        'post_season_rankings',
        'post_season_totals',
        'preseason_career_totals',
        'preseason_season_totals',
        'regular_season_career_totals',
        'regular_season_rankings',
        'regular_season_totals'
    ]
}

to_remove = [
    'PLAYER_ID',
    'LEAGUE_ID',
    'TEAM_ABBREVIATION',
    'TEAM_ID',
    'SEASON_ID',
    'ORGANIZATION_ID'
]
