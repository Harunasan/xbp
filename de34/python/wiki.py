important 

# 駅の接続情報（西鎌倉駅）
stations = {
    'Nishikamakura Station': {'ohuna Station': 9, 'shounannenoshima Station': 5},
    'ohuna Station': {'totsuka Station': 5, 'Shibuya Station': 10},
    'Shibuya Station': {'Tokyo Station': 30, 'Shinjuku Station': 10},
}

# ダイクストラ法による最短経路計算
def dijkstra(start, end, stations):
    # 最短経路の初期化
    distances = {station: float('inf') for station in stations}
    distances[start] = 0
    priority_queue = [(0, start)]  # (距離, 駅名)

    while priority_queue:
        current_distance, current_station = heapq.heappop(priority_queue)

        if current_station == end:
            return current_distance

        for neighbor, travel_time in stations[current_station].items():
            distance = current_distance + travel_time
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return float('inf')  # 経路が見つからない場合

# 使用例
start_station = 'Tokyo Station'
end_station = 'Shibuya Station'

shortest_time = dijkstra(start_station, end_station, stations)
print(f"最短時間: {shortest_time} 分")




