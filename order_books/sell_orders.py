import heapq

class SellOrders:
    def __init__(self, order_list) -> None:
        order_list_copy = order_list.copy()
        heapq.heapify(order_list_copy)
        self.order_pq = order_list_copy

    def pop(self) -> int:
        if len(self.order_pq) == 0:
            return None
        return heapq.heappop(self.order_pq)

    def push(self, val) -> None:
        heapq.heappush(self.order_pq, val)

    def get_top(self) -> int:
        if len(heapq.nsmallest(1, self.order_pq)) == 1:
            return heapq.nsmallest(1, self.order_pq)[0]
        return None