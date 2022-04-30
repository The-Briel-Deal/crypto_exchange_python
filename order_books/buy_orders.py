import heapq

class BuyOrders:
    def __init__(self, order_list) -> None:
        for price_index, price in enumerate(order_list):
            order_list[price_index] = -price
        order_list_copy = order_list.copy()
        heapq.heapify(order_list_copy)
        self.order_pq = order_list_copy

    def pop(self) -> int:
        if len(self.order_pq) == 0:
            return None
        return -1*heapq.heappop(self.order_pq)

    def push(self, val) -> None:
        heapq.heappush(self.order_pq, -1*val)
    
    def get_top(self) -> int:
        if len(heapq.nsmallest(1, self.order_pq)) == 1:
            return -1*(heapq.nsmallest(1, self.order_pq)[0])
        return None