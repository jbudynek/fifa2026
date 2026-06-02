import pandas as pd

start_date = '2021-01-01' # date of the first match to consider for past data
competition_date = '2026-06-11' # date of the first match of the world cup 2026

# process team list and competition matches from results.csv
wc_df = pd.read_csv('input_data/results.csv')
wc_df['date'] = pd.to_datetime(wc_df['date'], errors='coerce')
wc_df = wc_df[['date', 'home_team', 'away_team', 'home_score', 'away_score']]
wc_df = wc_df[(wc_df['date'] >= competition_date)]
wc_df['win1'] = False
wc_df['win2'] = False

wc_df = wc_df.rename(columns={
    'date': 'd',
    'home_team': 't1',
    'away_team': 't2',
    'home_score': 's1',
    'away_score': 's2'
})

teams = pd.concat([wc_df['t1'], wc_df['t2']]).dropna().unique()
teams_list = sorted(teams.tolist())

print(teams_list)
print(len(teams_list))

wc_df.to_csv('input_data/wc_games_results_during_fifa26_.csv', index=False)

for line in wc_df.itertuples():
    print("#"+str(line.d)+"\n['"+line.t1+"', '"+line.t2+"'], ")

# process past matches from results.csv
results_df = pd.read_csv('input_data/results.csv')
results_df['date'] = pd.to_datetime(results_df['date'], errors='coerce')
results_df = results_df[['date', 'home_team', 'away_team', 'home_score', 'away_score']]
results_df['home_score'] = pd.to_numeric(results_df['home_score'], errors='coerce').astype('Int64')
results_df['away_score'] = pd.to_numeric(results_df['away_score'], errors='coerce').astype('Int64')
results_df['win1'] = results_df['home_score'] > results_df['away_score']
results_df['win2'] = results_df['away_score'] > results_df['home_score']
results_df = results_df[(results_df['date'] >= start_date) & (results_df['date'] < competition_date)]
results_df = results_df.rename(columns={
    'date': 'd',
    'home_team': 't1',
    'away_team': 't2',
    'home_score': 's1',
    'away_score': 's2'
})

# Keep only qualified teams
results_df = results_df[results_df['t1'].isin(teams_list) & results_df['t2'].isin(teams_list)]

results_df.to_csv('input_data/wc_games_results_before_fifa26_.csv', index=False)
