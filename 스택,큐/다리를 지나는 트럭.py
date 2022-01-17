def solution(bridge_length, weight, truck_weights):    
    time_count = 0
    
    truck_count = [] #건너고 있는 트럭
    len_count = [] # 건너고 있는 트럭 시간 카운트
        
    while truck_weights or truck_count:    
        time_count += 1        
        
        if len_count and len_count[0] >= bridge_length:                        
            len_count.pop(0)
            truck_count.pop(0)
            
        if truck_weights and weight >= sum(truck_count) + truck_weights[0]:            
            truck_count.append(truck_weights[0])
            truck_weights.pop(0)
            len_count.append(0)                        
                
        if len_count:
            for i in range(len(len_count)):
                len_count[i] += 1    
            
    return time_count
