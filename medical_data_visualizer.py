import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import data
df = pd.read_csv("medical_examination.csv")

# 2. Add 'overweight' column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3. Normalize cholesterol and gluc
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Categorical plot function
def draw_cat_plot():
    # 5. Create DataFrame for cat plot
    df_cat = pd.melt(df,
                     id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Group and reformat data
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()
    df_cat.rename(columns={'size': 'total'}, inplace=True)

    # 7. Draw the catplot
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio',
                      kind='bar', data=df_cat).fig

    return fig

# 8. Heat map function
def draw_heat_map():
    # 9. Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 10. Calculate correlation matrix
    corr = df_heat.corr()

    # 11. Generate mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 12. Set up matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 13. Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", center=0,
                vmax=0.3, vmin=-0.1, square=True, linewidths=.5, cbar_kws={"shrink": 0.5})

    return fig
