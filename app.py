from flask import Flask, render_template, request, jsonify
from nba_py import player
from module_mappings import module_mappings, x_axis_mappings, to_remove
import html

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    print("INITIAL")
    if request.method == "POST":
        print("GETTING IN HERE")
        j = request.get_json()
        if 'paramDict' in j:
            return jsonify(data=get_query_keys(convert_json(j)))
        elif 'dataDict' in j:
            return jsonify(data=get_query_values(convert_json(j)))
        else:
            return
    return render_template('index.html', query=get_query_keys)

def get_x_axis_key(function_name):
    for key, lst in x_axis_mappings.items():
        if function_name in lst:
            return key

def convert_json(json):
    ret = {}
    if 'paramDict' in json:
        json = json['paramDict']
    elif 'dataDict' in json:
        json = json['dataDict']
    for ob in json:
        if ob['value'] != '':
            if ob['key'] == 'fullName':
                names = ob['value'].split()
                first, last = names[0], names[-1]
                ret['first_name'] = first
                ret['last_name'] = last
            elif ob['key'] == 'currentlySelected':
                ret['function'] = ob['value']
            else:
                ret[ob['key']] = ob['value']
    return ret

def get_stat(json_lst, stat_name):
    lst = list(json_lst)
    ret = []
    for ob in lst:
        ret.append(ob[stat_name])
    return ret

def assign_submodule(params={}):
    f = params['function']
    for key, lst in module_mappings.items():
        if f in lst:
            params['sub_module'] = key
    return params

def get_query_keys(params={}):
    params = assign_submodule(params)
    return _get_query_results(params, flatten_keys=True)


def get_query_values(params={}):
    params = assign_submodule(params)
    return _get_query_results(params, flatten_keys=False)

def _get_query_results(params={}, flatten_keys=False):
    if 'module' not in params or 'sub_module' not in params or 'function' not in params:
        return []
    if not flatten_keys and 'value_query' not in params:
        return []
    if params['module'] == 'player':
        if 'first_name' not in params:
            return []
        first = params['first_name']
        last = params['last_name'] if 'last_name' in params else None
        team_id = params['team_id'] if 'team_id' in params else 0
        measure_type = params['measure_type'] if 'measure_type' in params else 'Base'
        per_mode = params['per_mode'] if 'per_mode' in params else 'PerGame'
        plus_minus = params['plus_minus'] if 'plus_minus' in params else 'N'
        pace_adjust = params['pace_adjust'] if 'pace_adjust' in params else 'N'
        rank = params['rank'] if 'rank' in params else 'N'
        league_id = params['league_id'] if 'league_id' in params else '00'
        season = params['season'] if 'season' in params else '2016-17'
        season_type = params['season_type'] if 'season_type' in params else 'Regular Season'
        po_round = params['po_round'] if 'po_round' in params else '0'
        outcome = params['outcome'] if 'outcome' in params else ''
        location = params['location'] if 'location' in params else ''
        month = params['month'] if 'month' in params else '0'
        season_segment = params['season_segment'] if 'season_segment' in params else ''
        date_from = params['date_from'] if 'date_from' in params else ''
        date_to = params['date_to'] if 'date_to' in params else ''
        opponent_team_id = params['opponent_team_id'] if 'opponent_team_id' in params else '0'
        vs_conference = params['vs_conference'] if 'vs_conference' in params else ''
        vs_division = params['vs_division'] if 'vs_division' in params else ''
        game_segment = params['game_segment'] if 'game_segment' in params else ''
        period = params['period'] if 'period' in params else '0'
        shot_clock_range = params['shot_clock_range'] if 'shot_clock_range' in params else ''
        last_n_games = params['last_n_games'] if 'last_n_games' in params else '0'
        only_current = params['only_current'] if 'only_current' in params else 0
        just_id = params['just_id'] if 'just_id' in params else True
        player_id = player.get_player(first, last_name=last, season=season, only_current=only_current, just_id=just_id)
        if params['sub_module'] == 'player_career':
            career = player.PlayerCareer(player_id)
            if params['function'] == 'all_star_season_totals':
                temp = career.all_star_season_totals()
            elif params['function'] == 'career_all_star_season_totals':
                temp = career.career_all_star_season_totals()
            elif params['function'] == 'college_season_career_totals':
                temp = career.college_season_career_totals()
            elif params['function'] == 'college_season_totals':
                temp = career.college_season_totals()
            elif params['function'] == 'post_season_career_totals':
                temp = career.post_season_career_totals()
            elif params['function'] == 'post_season_rankings':
                temp = career.post_season_rankings()
            elif params['function'] == 'post_season_totals':
                temp = career.post_season_totals()
            elif params['function'] == 'preseason_career_totals':
                temp = career.preseason_career_totals()
            elif params['function'] == 'preseason_season_totals':
                temp = career.preseason_season_totals()   
            elif params['function'] == 'regular_season_career_totals':
                temp = career.regular_season_career_totals()
            elif params['function'] == 'regular_season_rankings':
                temp = career.regular_season_rankings()
            elif params['function'] == 'regular_season_totals':
                temp = career.regular_season_totals()
            else:
                return []
        elif params['sub_module'] == 'player_clutch_splits':
            clutch = player.PlayerClutchSplits(player_id, team_id=team_id, measure_type=measure_type, per_mode=per_mode, plus_minus=plus_minus, \
                pace_adjust=pace_adjust, rank=rank, league_id=league_id, season=season, season_type=season_type, po_round=po_round, outcome=outcome, \
                location=location, month=month, season_segment=season_segment, date_from=date_from, date_to=date_to, opponent_team_id=opponent_team_id, \
                vs_conference=vs_conference, vs_division=vs_division, game_segment=game_segment, period=period, shot_clock_range=shot_clock_range, \
                last_n_games=last_n_games
            )
            if params['function'] == 'last10sec_deficit_3point':
                temp = clutch.last10sec_deficit_3point()
            elif params['function'] == 'last1min_deficit_5point':
                temp = clutch.last1min_deficit_5point()
            elif params['function'] == 'last1min_plusminus_5point':
                temp = clutch.last1min_plusminus_5point()
            elif params['function'] == 'last30sec_deficit_3point':
                temp = clutch.last30sec_deficit_3point()
            elif params['function'] == 'last30sec_plusminus_5point':
                temp = clutch.last30sec_plusminus_5point()
            elif params['function'] == 'last3min_deficit_5point':
                temp = clutch.last3min_deficit_5point()
            elif params['function'] == 'last3min_plusminus_5point':
                temp = clutch.last3min_plusminus_5point()
            elif params['function'] == 'last5min_deficit_5point':
                temp = clutch.last5min_deficit_5point()
            elif params['function'] == 'last5min_plusminus_5point':
                temp = clutch.last5min_plusminus_5point()
            else:
                return []
        elif params['sub_module'] == 'player_defense_tracking':
            temp = player.PlayerDefenseTracking(player_id, team_id=team_id, measure_type=measure_type, per_mode=per_mode, plus_minus=plus_minus, \
                pace_adjust=pace_adjust, rank=rank, league_id=league_id, season=season, season_type=season_type, po_round=po_round, outcome=outcome, \
                location=location, month=month, season_segment=season_segment, date_from=date_from, date_to=date_to, opponent_team_id=opponent_team_id, \
                vs_conference=vs_conference, vs_division=vs_division, game_segment=game_segment, period=period, shot_clock_range=shot_clock_range, \
                last_n_games=last_n_games
            )
        elif params['sub_module'] == 'player_game_logs':
            if params['function'] == 'info':
                temp = player.PlayerGameLogs(player_id, league_id=league_id, season=season, season_type=season_type)
            else:
                return []
        elif params['sub_module'] == 'player_general_splits':
            splits = player.PlayerGeneralSplits(player_id, team_id=team_id, measure_type=measure_type, per_mode=per_mode, plus_minus=plus_minus, \
                pace_adjust=pace_adjust, rank=rank, league_id=league_id, season=season, season_type=season_type, po_round=po_round, outcome=outcome, \
                location=location, month=month, season_segment=season_segment, date_from=date_from, date_to=date_to, opponent_team_id=opponent_team_id, \
                vs_conference=vs_conference, vs_division=vs_division, game_segment=game_segment, period=period, shot_clock_range=shot_clock_range, \
                last_n_games=last_n_games
            )
            if params['function'] == 'days_rest':
                temp = splits.days_rest()
            elif params['function'] == 'location':
                temp = splits.location()
            elif params['function'] == 'month':
                temp = splits.month()
            elif params['function'] == 'pre_post_all_star':
                temp = splits.pre_post_all_star()
            elif params['function'] == 'starting_position':
                temp = splits.starting_position()
            elif params['function'] == 'win_losses':        
                temp = splits.win_losses()
            else:
                return []
        elif params['sub_module'] == 'player_in_game_splits':
            if params['function'] == 'by_actual_margin':
                temp = splits.by_actual_margin()
            elif params['function'] == 'by_half':
                temp = splits.by_half()        
            elif params['function'] == 'by_period':
                temp = splits.by_period()        
            elif params['function'] == 'by_score_margin':
                temp = splits.by_score_margin()    
            else:
                return []    
        elif params['sub_module'] == 'player_last_n_games_splits':
            n_splits = player.PlayerLastNGamesSplits(player_id, team_id=team_id, measure_type=measure_type, per_mode=per_mode, plus_minus=plus_minus, \
                pace_adjust=pace_adjust, rank=rank, league_id=league_id, season=season, season_type=season_type, po_round=po_round, outcome=outcome, \
                location=location, month=month, season_segment=season_segment, date_from=date_from, date_to=date_to, opponent_team_id=opponent_team_id, \
                vs_conference=vs_conference, vs_division=vs_division, game_segment=game_segment, period=period, shot_clock_range=shot_clock_range, \
                last_n_games=last_n_games
            )
            if params['function'] == 'game_number':
                temp = n_splits.gamenumber()
            elif params['function'] == 'last10':
                temp = n_splits.last10()
            elif params['function'] == 'last15':
                temp = n_splits.last15()
            elif params['function'] == 'last20':
                temp = n_splits.last20()
            elif params['function'] == 'last5':
                temp = n_splits.last5()
            else:
                return []
        elif params['sub_module'] == 'player_list':
            player_list = player.PlayerList(league_id=league_id, season=season, only_current=only_current)
            if params['function'] == 'info':
                temp = player_list.info()
            else:
                return []
        elif params['sub_module'] == 'player_opponent_splits':
            op_splits = player.PlayerOpponentSplits(player_id, team_id=team_id, measure_type=measure_type, per_mode=per_mode, plus_minus=plus_minus, \
                pace_adjust=pace_adjust, rank=rank, league_id=league_id, season=season, season_type=season_type, po_round=po_round, outcome=outcome, \
                location=location, month=month, season_segment=season_segment, date_from=date_from, date_to=date_to, opponent_team_id=opponent_team_id, \
                vs_conference=vs_conference, vs_division=vs_division, game_segment=game_segment, period=period, shot_clock_range=shot_clock_range, \
                last_n_games=last_n_games
            )
            if params['function'] == 'by_conference':
                temp = op_splits.by_conference()
            elif params['function'] == 'by_division':
                temp = op_splits.by_division()
            elif params['function'] == 'by_opponent':
                temp = op_splits.by_opponent()
            else:
                return []
        elif params['sub_module'] == 'player_pass_tracking':
            pass_tracking = player.PlayerPassTracking(player_id, team_id=team_id, measure_type=measure_type, per_mode=per_mode, plus_minus=plus_minus, \
                pace_adjust=pace_adjust, rank=rank, league_id=league_id, season=season, season_type=season_type, po_round=po_round, outcome=outcome, \
                location=location, month=month, season_segment=season_segment, date_from=date_from, date_to=date_to, opponent_team_id=opponent_team_id, \
                vs_conference=vs_conference, vs_division=vs_division, game_segment=game_segment, period=period, shot_clock_range=shot_clock_range, \
                last_n_games=last_n_games
            )
            if params['function'] == 'passes_made':
                temp = pass_tracking.passes_made()
            elif params['function'] == 'passes_received':
                temp = pass_tracking.passes_received()
            else:
                return []        
        elif params['sub_module'] == 'player_performance_splits':
            performance_splits = player.PlayerPerformanceSplits(player_id, team_id=team_id, measure_type=measure_type, per_mode=per_mode, plus_minus=plus_minus, \
                pace_adjust=pace_adjust, rank=rank, league_id=league_id, season=season, season_type=season_type, po_round=po_round, outcome=outcome, \
                location=location, month=month, season_segment=season_segment, date_from=date_from, date_to=date_to, opponent_team_id=opponent_team_id, \
                vs_conference=vs_conference, vs_division=vs_division, game_segment=game_segment, period=period, shot_clock_range=shot_clock_range, \
                last_n_games=last_n_games
            )
            if params['function'] == 'points_against':
                temp = performance_splits.points_against()
            elif params['function'] == 'points_scored':
                temp = performance_splits.points_scored()
            elif params['function'] == 'score_differential':
                temp = performance_splits.score_differential()
            else:
                return []
        elif params['sub_module'] == 'player_profile':
            prof = player.PlayerProfile(per_mode=per_mode, league_id=league_id)
            if params['function'] == 'career_highs':
                temp = prof.career_highs()
            elif params['function'] == 'next_game':
                temp = prof.next_game()
            elif params['function'] == 'season_highs':
                temp = prof.season_highs()
            else:
                return []
        elif params['sub_module'] == 'player_rebound_log_tracking':
            temp = player.PlayerReboundLogTracking(player_id, team_id=team_id, measure_type=measure_type, per_mode=per_mode, plus_minus=plus_minus, \
                pace_adjust=pace_adjust, rank=rank, league_id=league_id, season=season, season_type=season_type, po_round=po_round, outcome=outcome, \
                location=location, month=month, season_segment=season_segment, date_from=date_from, date_to=date_to, opponent_team_id=opponent_team_id, \
                vs_conference=vs_conference, vs_division=vs_division, game_segment=game_segment, period=period, shot_clock_range=shot_clock_range, \
                last_n_games=last_n_games
            )
        elif params['sub_module'] == 'player_rebound_tracking':
            rb_tracking = player.PlayerReboundTracking(player_id, team_id=team_id, measure_type=measure_type, per_mode=per_mode, plus_minus=plus_minus, \
                pace_adjust=pace_adjust, rank=rank, league_id=league_id, season=season, season_type=season_type, po_round=po_round, outcome=outcome, \
                location=location, month=month, season_segment=season_segment, date_from=date_from, date_to=date_to, opponent_team_id=opponent_team_id, \
                vs_conference=vs_conference, vs_division=vs_division, game_segment=game_segment, period=period, shot_clock_range=shot_clock_range, \
                last_n_games=last_n_games
            )
            if params['function'] == 'num_contested_rebounding':
                temp = rb_tracking.num_contested_rebounding()
            elif params['function'] == 'rebound_distance_rebounding':
                temp = rb_tracking.rebound_distance_rebounding()
            elif params['function'] == 'shot_distance_rebounding':
                temp = rb_tracking.shot_distance_rebounding()
            elif params['function'] == 'shot_type_rebounding':
                temp = rb_tracking.shot_type_rebounding()
            else:
                return []
        elif params['sub_module'] == 'player_shooting_splits':
            if params['function'] == 'assisted_by':
                temp = rb_tracking.assisted_by()
            elif params['function'] == 'assisted_shots':
                temp = rb_tracking.assisted_shots()
            elif params['function'] == 'shot_5ft':
                temp = rb_tracking.shot_5ft()
            elif params['function'] == 'shot_8ft':
                temp = rb_tracking.shot_8ft()
            elif params['function'] == 'shot_areas':
                temp = rb_tracking.shot_areas()
            elif params['function'] == 'shot_types_detail':
                temp = rb_tracking.shot_types_detail()
            elif params['function'] == 'shot_types_summary':
                temp = rb_tracking.shot_types_summary()
            else:
                return []
        elif params['sub_module'] == 'player_shot_log_tracking':
            temp = player.PlayerShotLogTracking(player_id, team_id=team_id, measure_type=measure_type, per_mode=per_mode, plus_minus=plus_minus, \
                pace_adjust=pace_adjust, rank=rank, league_id=league_id, season=season, season_type=season_type, po_round=po_round, outcome=outcome, \
                location=location, month=month, season_segment=season_segment, date_from=date_from, date_to=date_to, opponent_team_id=opponent_team_id, \
                vs_conference=vs_conference, vs_division=vs_division, game_segment=game_segment, period=period, shot_clock_range=shot_clock_range, \
                last_n_games=last_n_games
            )
            if params['function'] == 'closest_defender_shooting':
                temp = rb_tracking.closest_defender_shooting()
            elif params['function'] == 'closest_defender_shooting_long':
                temp = rb_tracking.closest_defender_shooting_long()
            elif params['function'] == 'dribble_shooting':
                temp = rb_tracking.dribble_shooting()
            elif params['function'] == 'general_shooting':
                temp = rb_tracking.general_shooting()
            elif params['function'] == 'shot_clock_shooting':
                temp = rb_tracking.shot_clock_shooting()
            elif params['function'] == 'touch_time_shooting':
                temp = rb_tracking.touch_time_shooting()
            else:
                return []
        # elif params['sub_module'] == 'player_shot_tracking':
        # elif params['sub_module'] == 'player_summary':
        # elif params['sub_module'] == 'player_vs_player':
        # elif params['sub_module'] == 'player_year_over_year_splits':
    elif params['module'] == 'game':
        pass
    elif params['module'] == 'team':
        pass
    else:
        # Failure case.
        pass
    if flatten_keys:
        return [l for l in list(set([el for o in temp for el in o.keys()])) if l not in to_remove]
    else:
        return {
            'data': [o[params['value_query']] for o in temp],
            'labels': [o[get_x_axis_key(params['function'])] for o in temp]
        }

if __name__ == "__main__":
    app.run()