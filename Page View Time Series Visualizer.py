import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Import the data and set the index to the date column
def import_and_clean_data():
    df = pd.read_csv('C:\\Users\\TOW Admin\\Downloads\\Test Documentation\\fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    return df

# Step 2: Clean the data
def clean_data(df):
    # Filter out days when the page views are in the top 2.5% and bottom 2.5%
    df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
    return df

# Step 3: Create a line plot using Matplotlib
def draw_line_plot(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['value'], color='r', linewidth=1)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.show()

# Step 4: Create a bar plot using Matplotlib
def draw_bar_plot(df):
    df['year'] = df.index.year
    df['month'] = df.index.month_name()
    df_pivot = df.pivot_table(index='year', columns='month', values='value', aggfunc='mean')

    fig, ax = plt.subplots(figsize=(10, 5))
    df_pivot.plot(kind='bar', ax=ax)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months")
    plt.title("Average daily page views for each month grouped by year")
    plt.show()

# Step 5: Create box plots using Seaborn
def draw_box_plots(df):
    df['year'] = df.index.year
    df['month'] = df.index.strftime('%b')

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    sns.boxplot(x='year', y='value', data=df, ax=axes[0])
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    axes[0].set_title("Year-wise Box Plot (Trend)")

    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x='month', y='value', data=df, ax=axes[1], order=months_order)
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")

    plt.tight_layout()
    plt.show()

# Step 6: Save and return the images (optional)
def save_and_return_plots():
    df = import_and_clean_data()
    draw_line_plot(df)
    draw_bar_plot(df)
    draw_box_plots(df)

    plt.savefig('line_plot.png')
    plt.savefig('bar_plot.png')
    plt.savefig('box_plot.png')

if __name__ == '__main__':
    save_and_return_plots()