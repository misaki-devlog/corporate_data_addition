corporate_data={
    "パナソニックホールディングス":{"ROE":7.9,"営業CF":7960,"自己資本比率":49.5},
    "NEC":{"ROE":9.1,"営業CF":3444,"自己資本比率":50.3},
    "富士通":{"ROE":12.6,"営業CF":3038,"自己資本比率":62.2},
}
name=input("企業名を入力してください（パナソニックホールディングス、NEC、富士通）：")
if name in corporate_data:
    print(name+f"のROEは{corporate_data[name]["ROE"]}、営業CFは{corporate_data[name]["営業CF"]}、自己資本比率は{corporate_data[name]["自己資本比率"]}です。")
else:
    
    data = input("その企業のROE、営業CF、自己資本比率ををカンマ区切りで入力してください (例: 12,2200,50.4)： ")
    ROE,operating_profit,equity_ratio= data.split(",")
    corporate_data[name]={"ROE":ROE,"営業CF":operating_profit,"自己資本比率":equity_ratio}
    print(name+"のROEは"+corporate_data[name]["ROE"]+"、営業CFは"+corporate_data[name]["営業CF"]+"、自己資本比率"+corporate_data[name]["自己資本比率"])
print(corporate_data)