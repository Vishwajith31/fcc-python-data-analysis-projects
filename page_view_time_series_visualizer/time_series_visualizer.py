import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'])

# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots(figsize=(15,5))
    ax.plot(df.index, df['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True) 
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month_name()

    grouped_df_bar = df_bar.groupby(['year', 'month'])['value'].mean()

    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    grouped_df_bar = grouped_df_bar.unstack().reindex(columns=month_order)

    # Draw bar plot
    colors = [
        '#0066cc', '#3399ff', '#66ccff', '#99ccff', '#cce5ff', '#e6f2ff',
        '#ffcccc', '#ff9999', '#ff6666', '#ff3333', '#cc0000', '#990000'
    ]

    fig, ax = plt.subplots(figsize=(12, 6))
    grouped_df_bar.plot(kind='bar', color=colors, ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', bbox_to_anchor=(1,1), loc='upper left')
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    # Draw box plots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))

    year_palette = sns.color_palette("husl", len(df_box['year'].unique()))
    month_palette = sns.color_palette("coolwarm", 12)

    sns.boxplot(x='year', y='value', data=df_box, palette=year_palette, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df_box,
                order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                palette=month_palette, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig
    fig.savefig('box_plot.png')
    return fig
