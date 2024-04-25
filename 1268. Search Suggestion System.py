class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        retList = []
        products.sort()
        for i,c in enumerate(searchWord):
            products = [p for p in products if len(p) > i and p[i] == c]
            retList.append(products[:3])
        return retList
