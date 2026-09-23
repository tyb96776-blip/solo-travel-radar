# 旅行低价雷达（Solo Travel Radar）

v2：正式整理版项目骨架。

功能规划：
- 每周一扫描未来 4–8 周的低价旅行机会
- 每日记录价格变化，仅对明显降价/异常低价提醒
- Metz / Luxembourg / Strasbourg / Paris 等出发地
- 2–5 晚组合、单人真实价格
- 交通 + 住宿 + 当地交通总成本
- 住宿评分、评价数量
- 历史价格、天气、签证、文化活动接口
- 不做主观“最佳目的地”排名

当前没有接入真实机票、酒店、天气或活动 API，collector 是可替换接口。

本地运行：
```bash
pip install -r requirements.txt
python src/main.py weekly
python src/main.py daily
```
