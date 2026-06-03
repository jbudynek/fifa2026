# FIFA World Cup 2026

Simple pronostics for FIFA 2026 football World Cup based on Bradley-Terry and some past data. 
See also https://github.com/jbudynek/rugby2023 and https://github.com/jbudynek/uefa2024

## HOWTO Initialize

The source data comes from this great repo that has results for all soccer games ever!
https://github.com/martj42/international_results/

We need to create two files in `input_data` (See `00_process_data.py` for helper code):
- create file `wc_games_results_before_fifa26.csv` with past games and results (18 months? 2 years?) - Columns: `d,t1,t2,s1,s2,win1,win2`
    - example: 2023-03-23,Kazakhstan,Slovenia,1,2,False,True
    - draw is FALSE,FALSE
- create file `wc_games_results_during_fifa26.csv` with games and results since competition started (empty score if not played yet)

Then:
- in `conf.py`
    - update all teams short and all teams long (get it from `00_process_data.py`)
    - update `BOUNDS` (6 months increments, or something that makes more sense)
- in `01_make_games_list.py`
    - update the code to read the two new files (see line 5) and create the games list

## HOWTO run each round

- in `input_data\wc_games_results_during_fifa26.csv`
    - update file with games and results since competition started
- in `conf.py`
    - update `ALL_GAMES` with the games you want a pronostic for, and `TITLE` with the title you want for the graph that will be generated
    - update `BOUNDS`

Then:
- Run `01_make_games_list.py`
- Run `02_bradley_terry.py`
- Run `03_pronostics_from_bt.py`
- See in the terminal for easy to read pronostics, and see in `boxplots/` for a nice graph.

## Round 1 pronostics

![Pool1](boxplots/_01_whisk-2024-06-03-2026-05-31.png)
