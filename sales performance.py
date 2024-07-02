import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
df = pd.read_csv('large_sales_data.csv')

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Aggregate sales data by various dimensions
sales_by_date = df.groupby('Date')['Sales'].sum().reset_index()
sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()
sales_by_product = df.groupby('Product')['Sales'].sum().reset_index()
sales_by_salesperson = df.groupby('Salesperson')['Sales'].sum().reset_index()

# Create individual plots
fig_date = px.line(sales_by_date, x='Date', y='Sales', title='Sales Over Time')
fig_region = px.bar(sales_by_region, x='Region', y='Sales', title='Sales by Region')
fig_product = px.bar(sales_by_product, x='Product', y='Sales', title='Sales by Product')
fig_salesperson = px.bar(sales_by_salesperson, x='Salesperson', y='Sales', title='Sales by Salesperson')

# Combine plots into a dashboard layout
fig = go.Figure()
fig.add_trace(fig_date.data[0])
fig.add_trace(fig_region.data[0])
fig.add_trace(fig_product.data[0])
fig.add_trace(fig_salesperson.data[0])

fig.update_layout(
    title='Sales Performance Analysis Dashboard',
    barmode='group',
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=[{'visible': [True, False, False, False]}],
                    label='Sales Over Time',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, True, False, False]}],
                    label='Sales by Region',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, False, True, False]}],
                    label='Sales by Product',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, False, False, True]}],
                    label='Sales by Salesperson',
                    method='update'
                ),
            ]),
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=0.17,
            xanchor='left',
            y=1.15,
            yanchor='top'
        ),
    ]
)

# Show the dashboard
fig.show()
