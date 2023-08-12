import pyecharts.options as opts
from pyecharts.charts import Scatter
import pandas as pd
"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.apache.org/examples/editor.html?c=scatter-simple

目前无法实现的功能:

1、暂无
"""

data = pd.read_csv(r'./data/for_chart_sd.csv')
data = data.sort_values(by=["PM2_5(μg/m3)"])

x_data = data["PM2_5(μg/m3)"].astype(float).apply(lambda x: round(x, 2)).tolist()
y_data = data["TEMPERATURE(℃)"].astype(float).apply(lambda x: round(x, 2)).tolist()


(
    Scatter()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="",
        y_axis=y_data,
        symbol_size=5,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_series_opts()
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(
            type_="value", splitline_opts=opts.SplitLineOpts(is_show=True)
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        tooltip_opts=opts.TooltipOpts(is_show=False),
    )
    .render("pm2.5_tem.html")
)
