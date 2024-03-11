import json

def main():
    with open ('小金伴投.json', 'r') as f:
        data = json.loads(f.read())
    
    result = '分组,名称,代码,类型,收益,收益率\n'
    for group in data:
        for key in group:
            for item in group[key]:
                productName = item['tplData']['jump']['viewProperty']['productName']
                productId = item['tplData']['jump']['viewProperty']['productId']
                
                productDetail = item['tplData']['productInfo']['productDetail']

                incomeTitle = item['tplData']['productProfitInfo']['incomeTitle']
                expectYearProfitRate = item['tplData']['productProfitInfo']['expectYearProfitRate']

                result += '{},{},{},{},{},{}\n'.format(key,productName,productId,productDetail,incomeTitle,expectYearProfitRate)

    with open ('小金伴投.csv', 'w') as f:
        f.write(result)

main()