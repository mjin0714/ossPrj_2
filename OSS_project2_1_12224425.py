import pandas as pd
df=pd.read_csv("2019_kbo_for_kaggle_v2.csv")

#2-1 (1) : 각 항목별 2015년도부터 2018년도까지 best player 10명씩 출력
cols=['H','avg','HR','OBP']
years=[2015,2016,2017,2018]
for col in cols:
    for year in years:
        print(df[df['year']==year].sort_values(by=col, ascending=False).head(10))

#2-1 (2) : 각 포지션 별 2018년 승리 기여도 가장 높은 player 1명씩 출력
positions = ['포수','1루수','2루수','3루수','유격수','좌익수','중견수','우익수']
top_players = pd.DataFrame()
for position in positions:
    position_df = df[(df['year'] == 2018) & (df['cp'] == position)]
    print(position_df.sort_values(by='war', ascending=False).head(1))

#2-1 (3) : 각 항목별 corr with salary 계산하여 가장 높은 하나의 항목 출력
selected_column=['R','H','HR','RBI','SB','war','avg','OBP','SLG']
print(df[selected_column].corrwith(df.salary).sort_values(ascending=False).head(1))