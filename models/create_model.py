
import os

table_list = [
	"app_user",
	"web_info"
]
for x in table_list:
	print(x + '\r')
	command = "sqlacodegen  --outfile " + x + ".py --table " + x + " mysql+pymysql://duchang:eA6DHMX3nB3T5zTs@222.186.150.48:3306/duchang?charset=utf8"
	os.system(command)

