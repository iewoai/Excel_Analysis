import pandas as pd
import pickle, sys, os

# path = 'all.xlsx'
# df = pd.read_excel(path)
# # 读取所有天数的宝贝数据，
# print(df)

sort_list = pickle.load(open('sort_list.p', 'rb'))
print(sort_list)
path = 'D:\\PyStudy\\appium\\xianyuData'

def order_dict(sort_list, df):
	dict_after = {}
	for order in sort_list:
		if order[0] in df.keys():
			dict_after[order[0]] = df[order[0]]

	return dict_after

for data_path in os.listdir(path):
	file_name = 'D:\\PyStudy\\excel\\xianyu\\%s' % data_path
	date, suf = os.path.splitext(data_path)
	df_pr = pd.read_excel(os.path.join(path, data_path))
	df_af = {col:df_pr[col].tolist() for col in df_pr.columns[1:]}
	for k in df_af.keys():
		if k not in sort_list:
			sort_list.append(k)
	dict_after = order_dict(sort_list, df_af)
	result_DF = pd.DataFrame(dict_after, index = ['想要', '超赞', '浏览'])
	result_DF.T.to_excel(file_name)
with open('sort_list.p', 'wb') as f:
	print('开始储存————————')
	pickle.dump(sort_list, f)
	f.close()
print('储存成功————————')
# sys.exit()

