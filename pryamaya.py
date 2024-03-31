import plotly.graph_objects as go

def plot_graph_temperatyre(y, y2, y3, y4, x):

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=x, name="Датчик 1"))
    fig.add_trace(go.Scatter(x=x, y=y2, name="Датчик 2"))
    fig.add_trace(go.Scatter(x=x, y=y3, name="Датчик 3"))
    fig.add_trace(go.Scatter(x=x, y=y4, name="Датчик 4"))
    fig.update_layout(legend_orientation="h",
                      legend=dict(x=.5, xanchor="center"),
                      title="Теплица",
                      xaxis_title="Время t, мин",
                      yaxis_title="Температура t, C",
                      margin=dict(l=0, r=0, t=30, b=0))


    fig.write_image("pryamaya.png")


x = [7, 10, 13, 15, 20]

y = [20, 30, 40]

y2 = [15, 15, 15, 15, 15]

y3 = [12, 12, 12, 12, 12]

y4 = [7, 7, 7, 7, 7]


plot_graph_temperatyre(y, y2, y3, y4, x)
