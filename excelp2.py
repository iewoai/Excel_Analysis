import pandas as pd
from numpy import *
from scipy.stats import pearsonr
from tqdm import tqdm

# 提取本地excel文件
df = pd.read_excel('调查问卷.xlsx')

# 欧式距离算法
def ousi(a,b):
	v1,v2 = mat(a),mat(b)
	result = sqrt((v1-v2)*((v1-v2).T))
	return result[0,0]
# 曼哈顿距离算法
def mhd(a,b):
	v1,v2 = mat(a),mat(b)
	return sum(abs(v1-v2))
# 切比雪夫距离算法
def Chebyshev(a,b):
	v1,v2 = mat(a),mat(b)
	return abs(v1-v2).max()
# 余弦相似度算法
def mid_cos(a,b):
	result = dot(a,b)/(linalg.norm(a)*linalg.norm(b))
	return 0.5 * result + 0.5

# 提取所有评分
df_score = df.ix[:,2:].values
# 提取所有姓名
df_name = df.ix[:,[0]].values

# 评分集合
scoreLists = []
for i in df_score:
	scoreList = []
	for j in i:
		scoreList.append(j)
	scoreLists.append(scoreList)
# 姓名-评分字典
result = {}
for i,d_name in enumerate(df_name):
	result[d_name[0]] = {
						'scoreList':scoreLists[i]
							}
# name = '肖威'

# 欧式距离计算
def get_min_ousi(name):
	a = result[name]['scoreList']
	ousi_dict = {}
	for key in result:
		if not key == name:
			b = result[key]['scoreList']
			ousi_dict[key] = ousi(a,b)
	# print(ousi_dict)
	ousi_min_name = min(ousi_dict, key=ousi_dict.get)
	ousi_min = ousi_dict[ousi_min_name]
	return ousi_min_name, ousi_min
	# print('<欧式距离>调查问卷中，与%s欧式距离最小的是：%s，最小值为：%f' % (name, ousi_min_name, ousi_min))

# 曼哈顿距离计算
def get_min_mhd(name):
	a = result[name]['scoreList']
	mhd_dict = {}
	for key in result:
		if not key == name:
			b = result[key]['scoreList']
			mhd_dict[key] = mhd(a,b)
	
	mhd_min_name = min(mhd_dict, key=mhd_dict.get)
	mhd_min = mhd_dict[mhd_min_name]
	return mhd_min_name, mhd_min

	# print('<曼哈顿距离>调查问卷中，与%s曼哈顿距离最小的是：%s，最小值为：%f' % (name, mhd_min_name, mhd_min))

# 切比雪夫距离计算
def get_min_Chebyshev(name):
	a = result[name]['scoreList']
	Chebyshev_dict = {}
	for key in result:
		if not key == name:
			b = result[key]['scoreList']
			Chebyshev_dict[key] = Chebyshev(a,b)
	
	Chebyshev_min_name = min(Chebyshev_dict, key=Chebyshev_dict.get)
	Chebyshev_min = Chebyshev_dict[Chebyshev_min_name]
	return Chebyshev_min_name, Chebyshev_min
	# print('<切比雪夫距离>调查问卷中，与%s切比雪夫距离最小的是：%s，最小值为：%f' % (name, Chebyshev_min_name, Chebyshev_min))

# 皮尔森相关系数计算
def get_max_pearsonr(name):
	a = result[name]['scoreList']
	pearsonr_dict = {}
	for key in result:
		if not key == name:
			b = result[key]['scoreList']
			# print(key, pearsonr(a, b)[0])
			pearsonr_dict[key] = pearsonr(a, b)[0]
	
	pearsonr_max_name = max(pearsonr_dict, key=pearsonr_dict.get)
	pearsonr_max = pearsonr_dict[pearsonr_max_name]
	return pearsonr_max_name, pearsonr_max
	# print('<皮尔森相关系数>调查问卷中，与%s皮尔森相关系数最大的是：%s，最大值为：%e' % (name, pearsonr_max_name, pearsonr_max))

# 余弦相似度计算
def get_max_cos(name):
	a = result[name]['scoreList']
	cos_dict = {}
	for key in result:
		if not key == name:
			b = result[key]['scoreList']
			cos_dict[key] = mid_cos(a, b)
	
	cos_max_name = max(cos_dict, key=cos_dict.get)
	cos_max = cos_dict[cos_max_name]
	return cos_max_name, cos_max
	# print('<余弦相似度>调查问卷中，与%s余弦相似度最大的是：%s，最大值为：%f' % (name, cos_max_name, cos_max))

# get_min_ousi(name)
# get_min_mhd(name)
# get_min_Chebyshev(name)
# get_max_pearsonr(name)
# get_max_cos(name)

# 计算结果集合
data = []

# 进度条循环
for name in tqdm(result):
	ousi_min_name, ousi_min = get_min_ousi(name)
	mhd_min_name, mhd_min = get_min_mhd(name)
	Chebyshev_min_name, Chebyshev_min = get_min_Chebyshev(name)
	pearsonr_max_name, pearsonr_max = get_max_pearsonr(name)
	cos_max_name, cos_max = get_max_cos(name)
	d = {
		'姓名':name,
		'欧式距离最小' : ousi_min_name,
		'欧式距离最小值' : ousi_min,
		'曼哈顿距离最小' : mhd_min_name,
		'曼哈顿距离最小值' : mhd_min,
		'切比雪夫距离最小' : Chebyshev_min_name,
		'切比雪夫距离最小值' : Chebyshev_min,
		'皮尔森相关系数最大' : pearsonr_max_name,
		'皮尔森相关系数最大值' : pearsonr_max,
		'余弦相似度最大' : cos_max_name,
		'余弦相似度最大值' : cos_max
			}
	data.append(d)

# 写入excel
result_DF = pd.DataFrame(data)
result_DF.to_excel('result1.xlsx')