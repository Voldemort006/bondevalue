class MatchCustomers: 
    @classmethod
    def findmatch(cls, buyer_data, seller_data):
        buyer_data = sorted(buyer_data, key=lambda buyer: buyer.price)
        seller_data = sorted(seller_data, key=lambda seller: seller.price)
        matched = {} 
        sellers_unmatched = []
        buyers_unmatched = []
        i = 0
        j = 0
        buyer_length = len(buyer_data)
        seller_length = len(seller_data)
        while i < buyer_length:
            if j >= seller_length:
                break
            if buyer_data[i].price >= seller_data[j].price: 
                matched[i] = buyer_data[i].name, seller_data[j].name
                j+=1
            else: 
                buyers_unmatched.append(buyer_data[i].name)
            i+=1
        
        while i < buyer_length: 
            buyers_unmatched.append(buyer_data[i].name)
            i+=1
        
        while j < seller_length:
            sellers_unmatched.append(seller_data[j].name)
            j+=1

        return {"matched": matched, "unmatched_sellers": sellers_unmatched, 
                    "unmatched_buyers": buyers_unmatched }
