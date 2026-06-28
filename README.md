# FIFA World Cup 2026

Simple pronostics for FIFA 2026 football World Cup based on Bradley-Terry and some past data. 
See also https://github.com/jbudynek/rugby2023 and https://github.com/jbudynek/uefa2024

## HOWTO Initialize

The data comes from this great repo that has results for all soccer games ever!
https://github.com/martj42/international_results/

- Get source data with `wget https://github.com/martj42/international_results/raw/refs/heads/master/results.csv -O input_data/results.csv`
- Run `00_process_data.py` (adapt if necessary)
- in `conf.py`
    - update all teams short and all teams long (get list from `00_process_data.py`)
    - update `BOUNDS` (6 months increments, or something that makes more sense)
- in `01_make_games_list.py`
    - update the code to read the two new files (see line 5) and create the games list

## HOWTO run each round

- Update source data with `wget https://github.com/martj42/international_results/raw/refs/heads/master/results.csv -O input_data/results.csv`
- or, in `input_data\wc_games_results_during_fifa26.csv`
    - update file with games and results since competition started
- in `conf.py`
    - update `ALL_GAMES` with the games you want a pronostic for, and `TITLE` with the title you want for the graph that will be generated
    - update `BOUNDS`

Then:
- Run `00_process_data.py` (if you updated the source data)
- Run `01_make_games_list.py`
- Run `02_bradley_terry.py`
- Run `03_pronostics_from_bt.py`
- See in the terminal for easy to read pronostics, and see in `boxplots/` for a nice graph.


## Round of sixteen

![RoundOfSixteen](boxplots/_04_whisk-2014-06-12-2026-07-20.png)

## Round 1 pronostics

![Pool3](boxplots/_03_whisk-2014-06-12-2026-07-20.png)

![Pool2](boxplots/_02_whisk-2014-06-12-2026-07-20.png)

![Pool1](boxplots/_01_whisk-2024-06-03-2026-05-31.png)
