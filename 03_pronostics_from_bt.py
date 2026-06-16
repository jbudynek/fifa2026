import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from pronostics import pronostics
from conf import ALL_GAMES, BOUNDS, TITLE, ALL_TEAMS, ALL_TEAMS_SHORT

t2t = {}
for i,t in enumerate(ALL_TEAMS):
    t2t[t] = ALL_TEAMS_SHORT[i]

whisk = {}
for match in ALL_GAMES:
    whisk[tuple([t2t[match[0]],t2t[match[1]]])] = []

for idx, val in enumerate(BOUNDS):
    if idx == 0:
        continue

    start_date = BOUNDS[idx - 1]
    end_date = BOUNDS[-1]

    df2 = pd.read_csv(f"bt3/matrix_from_bradley_terry_{idx:02}.csv", index_col=0)

    print(f"** Using data from {start_date} to {end_date} **")
    for match in ALL_GAMES:
        prob1, prob2 = pronostics(match, df2)
        #whisk[tuple(match)].append(prob1)
        whisk[tuple([t2t[match[0]],t2t[match[1]]])].append(prob1)

print(f"** Game - list of prob - average prob - med prob - winner **")
for k, v in whisk.items():
    formatted_data = ', '.join([f'{value:.2f}' for value in v])
    av = np.average(v)
    me = np.median(v)
    ppp = (av+me)/2

    print(f"{k} [{formatted_data}] {av:.2f} {me:.2f} {k[int(ppp<=0.5)]}")


plt.ylim(0, 1)
plt.boxplot(whisk.values(), tick_labels=whisk.keys())
plt.xticks(rotation=45)
plt.title( 
    f"Boxplots for {TITLE}\nusing data from {BOUNDS[0]} to {BOUNDS[-1]}"
)
plt.ylabel("Probability that team 1 wins")
plt.axhline(0.5, color="r", linestyle="--")
plt.tight_layout(pad=2.0)
#plt.show()
fn = f"boxplots/whisk-{BOUNDS[0]}-{BOUNDS[-1]}.png"
plt.savefig(fn)
