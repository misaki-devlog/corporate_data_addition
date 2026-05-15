corporate_data={
    "パナソニックホールディングス":{"ROE":7.9,"営業CF":7960,"自己資本比率":49.5},
    "NEC":{"ROE":9.1,"営業CF":3444,"自己資本比率":50.3},
    "富士通":{"ROE":12.6,"営業CF":3038,"自己資本比率":62.2},
}
name=input("企業名を入力してください（パナソニックホールディングス、NEC、富士通）:")
if name in corporate_data:
    print(name+f"のROEは{corporate_data[name]["ROE"]}、営業CFは{corporate_data[name]["営業CF"]}、自己資本比率は{corporate_data[name]["自己資本比率"]}です。")
else:
    roe=input("その企業のROEの値を教えてください(10%なら10と入力):")
    operating_profit=input("その企業の営業CFの値を教えてください(3000なら3000と入力):")
    equity_ratio=input("その企業の自己資本比率の値を教えてください(50%なら50と入力):")
    corporate_data[name]={}
    corporate_data[name]["ROE"]=roe
    corporate_data[name]["営業CF"]=operating_profit
    corporate_data[name]["自己資本比率"]=equity_ratio
    print(name+"のROEは"+str(corporate_data[name]["ROE"])+"、営業CFは"+str(corporate_data[name]["営業CF"])+"、自己資本比率"+str(corporate_data[name]["自己資本比率"]))
print(corporate_data)