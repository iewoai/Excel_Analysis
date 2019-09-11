from pyecharts import Bar3D
import pandas as pd


data=pd.DataFrame({'month':['1月','2月','3月','1月','2月','3月'],'city':['北京','北京','北京','上海','上海','上海'],'sales':[400,500,430,550,600,420]})

x_name = list(set(data.iloc[:, 0]))
y_name = list(set(data.iloc[:, 1]))

data_xyz=[]

for i in range(len(data)):

	x=x_name.index(data.iloc[i,0])

	y=y_name.index(data.iloc[i,1])

	z=data.iloc[i,2]

	data_xyz.append([x,y,z])

bar3d=Bar3D("1-3月各城市销量","单位:万件",title_pos="center",width=1200,height=800)

bar3d.add('',x_name,y_name,data_xyz,is_label_show=True,is_visualmap=True, visual_range=[0, 500],grid3d_width=150, grid3d_depth=50, is_grid3d_rotate = True)
# bar3d.add('',x_name,y_name,data_xyz,is_label_show=True,is_visualmap=True, visual_range=[0, 500],grid3d_width=150, grid3d_depth=50, is_grid3d_rotate = True)

bar3d.render("sales.html")