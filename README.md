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

## Round 1 results

| Game | My pronostic | Real winner | Score |
| :--- | :--- | :--- | :---: |
| **Part 1** | | | |
| CZE vs RSA | **CZE** | Draw (1-1) | ❌ |
| MEX vs KOR | **MEX** | **MEX** (1-0) | ✅ |
| SUI vs BIH | **SUI** | **SUI** (2-0) | ✅ |
| CAN vs QAT | **CAN** | **CAN** (6-0) | ✅ |
| SCO vs MAR | **MAR** | **MAR** (1-0) | ✅ |
| BRA vs HAI | **BRA** | **BRA** (3-0) | ✅ |
| USA vs AUS | **AUS** | **USA** (2-1) | ❌ |
| TUR vs PAR | **TUR** | **PAR** (2-0) | ❌ |
| GER vs CIV | **GER** | **GER** (3-1) | ✅ |
| ECU vs CUW | **ECU** | **ECU** (1-0) | ✅ |
| NED vs SWE | **NED** | **NED** (2-1) | ✅ |
| TUN vs JPN | **JPN** | **JPN** (1-0) | ✅ |
| BEL vs IRN | **BEL** | Draw (0-0) | ❌ |
| NZL vs EGY | **EGY** | Draw (1-1) | ❌ |
| ESP vs KSA | **ESP** | **ESP** (4-0) | ✅ |
| URU vs CPV | **URU** | Draw (2-2) | ❌ |
| FRA vs IRQ | **FRA** | **FRA** (3-0) | ✅ |
| NOR vs SEN | **NOR** | **NOR** (2-1) | ✅ |
| ARG vs AUT | **ARG** | **ARG** (2-0) | ✅ |
| JOR vs ALG | **ALG** | **ALG** (2-1) | ✅ |
| POR vs UZB | **POR** | **POR** (2-0) | ✅ |
| COL vs COD | **COL** | **COL** (1-0) | ✅ |
| ENG vs GHA | **ENG** | Draw (1-1) | ❌ |
| PAN vs CRO | **CRO** | **CRO** (1-0) | ✅ |
| **Part 2** | | | |
| MEX vs CZE | **MEX** | **MEX** (3-0) | ✅ |
| RSA vs KOR | **KOR** | **RSA** (1-0) | ❌ |
| CAN vs SUI | **SUI** | **SUI** (2-1) | ✅ |
| BIH vs QAT | **QAT** | **BIH** (3-1) | ❌ |
| SCO vs BRA | **BRA** | **BRA** (2-0) | ✅ |
| MAR vs HAI | **MAR** | **MAR** (2-0) | ✅ |
| USA vs TUR | **USA** | **TUR** (3-2) | ❌ |
| PAR vs AUS | **PAR** | **AUS** (1-0) | ❌ |
| CUW vs CIV | **CIV** | **CIV** (2-0) | ✅ |
| ECU vs GER | **GER** | **ECU** (2-1) | ❌ |
| JPN vs SWE | **JPN** | Draw (1-1) | ❌ |
| TUN vs NED | **NED** | **NED** (3-1) | ✅ |
| EGY vs IRN | **IRN** | Draw (1-1) | ❌ |
| NZL vs BEL | **BEL** | **BEL** (5-1) | ✅ |
| CPV vs KSA | **CPV** | Draw (0-0) | ❌ |
| URU vs ESP | **ESP** | **ESP** (1-0) | ✅ |
| NOR vs FRA | **FRA** | **FRA** (4-1) | ✅ |
| SEN vs IRQ | **SEN** | **SEN** (5-0) | ✅ |
| ALG vs AUT | **AUT** | Draw (3-3) | ❌ |
| JOR vs ARG | **ARG** | **ARG** (3-1) | ✅ |
| COL vs POR | **POR** | Draw (0-0) | ❌ |
| COD vs UZB | **UZB** | **COD** (3-1) | ❌ |
| PAN vs ENG | **ENG** | **ENG** (2-0) | ✅ |
| CRO vs GHA | **CRO** | **CRO** (2-1) | ✅ |
| **Part 3** | | | |
| MEX vs RSA | **MEX** | **MEX** (2-0) | ✅ |
| KOR vs CZE | **KOR** | **KOR** (2-1) | ✅ |
| CAN vs BIH | **CAN** | Draw (1-1) | ❌ |
| USA vs PAR | **PAR** | **USA** (1-0) | ❌ |
| QAT vs SUI | **SUI** | Draw (0-0) | ❌ |
| BRA vs MAR | **MAR** | Draw (1-1) | ❌ |
| HAI vs SCO | **SCO** | **SCO** (2-1) | ✅ |
| AUS vs TUR | **AUS** | **AUS** (1-0) | ✅ |
| GER vs CUW | **GER** | **GER** (6-0) | ✅ |
| CIV vs ECU | **ECU** | **CIV** (2-1) | ❌ |
| NED vs JPN | **JPN** | Draw (2-2) | ❌ |
| SWE vs TUN | **TUN** | **SWE** (2-0) | ❌ |
| BEL vs EGY | **BEL** | Draw (2-2) | ❌ |
| IRN vs NZL | **IRN** | Draw (0-0) | ❌ |
| ESP vs CPV | **ESP** | Draw (0-0) | ❌ |
| KSA vs URU | **URU** | Draw (1-1) | ❌ |
| FRA vs SEN | **FRA** | **FRA** (3-1) | ✅ |
| IRQ vs NOR | **NOR** | **NOR** (4-0) | ✅ |
| ARG vs ALG | **ALG** | **ARG** (3-0) | ❌ |
| AUT vs JOR | **AUT** | **AUT** (2-0) | ✅ |
| POR vs COD | **POR** | **POR** (2-0) | ✅ |
| UZB vs COL | **COL** | **COL** (2-1) | ✅ |
| ENG vs CRO | **CRO** | **ENG** (1-0) | ❌ |
| GHA vs PAN | **PAN** | **GHA** (2-0) | ❌ |

My stats:
- **Number of games:** 72
- **Good pronostics:** 41
- **Bad pronostics:** 31 (including Draws)
- **Success rate:** ~57 %

## Round 1 pronostics

![Pool3](boxplots/_03_whisk-2014-06-12-2026-07-20.png)

![Pool2](boxplots/_02_whisk-2014-06-12-2026-07-20.png)

![Pool1](boxplots/_01_whisk-2024-06-03-2026-05-31.png)
