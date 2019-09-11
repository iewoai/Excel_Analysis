import pandas as pd
from pyecharts import Bar3D
from pyecharts import Bar
import os, sys, time, pickle

t0 = time.time()
path = 'D:\\PyStudy\\appium\\xianyu'

# path2 = 'D:\\PyStudy\\appium\\2019-08-19_09-22-05.xlsx'
dataset = {}

# 时间
days = []

# 属性
index = []

# 商品名
keys = []

# xyz坐标
xyz = []

for data_path in os.listdir(path):
	date, suf = os.path.splitext(data_path)
	df_pr = pd.read_excel(os.path.join(path, data_path))
	print(data_path)
	for i in list(df_pr.iloc[:, 0]):
		index.append(i)
	df_af = {col:df_pr[col].tolist() for col in df_pr.columns[1:]}
	for k in df_af.keys():
		keys.append(k)
	dataset[date] = df_af
	days.append(date)

# 将不同日期的数据全部放到字典里，key为日期
# print(days)
# print(index)

# x为商品名，y为日期，z为浏览
for y, day in enumerate(dataset):
	for x, key in enumerate(set(keys)):
		# 因为每天发布的宝贝不一样，因此
		try:
			xyz.append([x, y, dataset[day][key][-1]])
		except Exception as e:
			# print(e)
			# print([x, y, 0])
			xyz.append([x, y, 0])

# print(xyz)

bar3d=Bar3D("闲鱼商品数据3D图",title_pos="center", width=1800, height=1000)

bar3d.add('', list(set(keys)), days , xyz, is_label_show=True,is_visualmap=True, visual_range=[0, 500], grid3d_width=100, xaxis3d_name_size = 12, grid3d_height= 100, grid3d_depth=150, is_grid3d_rotate = True, xaxis3d_name = '商品名', xaxis3d_interval = 0)
bar3d.render("xianyuData3D.html")

print('生成成功，耗时：%ds' % (time.time() - t0))
sort_list = []
for i, key in enumerate(set(keys)):
	sort_list.append((key, i))
print(sort_list)

with open('sort_list.p', 'wb') as f:
	print('开始储存————————')
	pickle.dump(sort_list, f)
	f.close()
print('储存成功————————')
# 3d图只包括浏览
# 写个程序判断超赞、想要变化
'''

# 提取本地excel文件
df1 = pd.read_excel(path1)
# # df2 = pd.read_excel(path2)
df = {col:df1[col].tolist() for col in df1.columns[1:]}

indexs = list(df1.iloc[:, 0])
keys = list(df.keys())

bar = Bar('闲鱼数据可视化', width=3200, height=4000)

for i, index in enumerate(indexs):
	# is_convert翻转x,y轴, is_label_show显示标签；label_pos,标签位置；is_random颜色是否随机生成；is_visualmap视觉映射插件；visual_range
	# index为(想要，浏览，超赞)
	# keys为商品名

	bar.add(index, keys, [df[d][i] for d in df], is_convert = True, is_label_show = True, label_pos='right', is_random = True, is_legend_show = True)#, is_visualmap=True,  visual_range=[0, 500])

# bar3d.add()

bar.render(r'xianyuData.html')
'''