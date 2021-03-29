#!/usr/bin/env python3

class Order:
        def __init__(self):
            self.quantity=0
            self.price=0.0
            self.type=""
            self.id=0

        def PrintOrder(self):
            print("         " + self.type + " " + str(self.quantity) + "@" + str(self.price) + " id=" + str(self.id))

class Book:
        def __init__(self,book1):
            self.listOrder=[]
            self.name=book1
            self.nbactions=0

        def insert_buy(self,Q,P):
            self.nbactions = self.nbactions + 1
            order1 = Order()
            order1.type="BUY"
            order1.quantity=Q
            order1.price=P
            order1.id = self.nbactions
            
            if self.listOrder == []:
                self.listOrder=self.listOrder+[order1]
            else:
                k=0
                while(self.listOrder[k].price > order1.price and k != len(self.listOrder) - 1):
                    k = k+1
                while(self.listOrder[k].price >= order1.price and self.listOrder[k].quantity > order1.quantity and k != len(self.listOrder) - 1):
                    k = k+1
                if self.listOrder[k].price >= order1.price and self.listOrder[k].quantity > order1.quantity and k == len(self.listOrder) - 1:
                    self.listOrder = self.listOrder + [order1]
                else:    
                    self.listOrder.insert(k, order1)
            
            print(" --- Insert BUY " + str(Q) + "@" + str(P) + "id=" + str(self.nbactions) + " on " + self.name)
            print("Book on " + self.name)
            for i in range(len(self.listOrder)):
                self.listOrder[i].PrintOrder()

        def insert_sell(self,Q,P):
            self.nbactions = self.nbactions + 1
            order2 = Order()
            order2.type="SELL"
            order2.quantity=Q
            order2.price=P
            order2.id=self.nbactions
            print(" --- Insert SELL " + str(Q) + "@" + str(P) + "id=" + str(self.nbactions) + " on " + self.name)
            
            Index=[]
            for i in range(len(self.listOrder)):
                if self.listOrder[i].type == "BUY" and self.listOrder[i].price >= order2.price and order2.quantity > 0:
                    if self.listOrder[i].quantity <= order2.quantity:
                        print("Execute " + str(self.listOrder[i].quantity) + " at " + str(self.listOrder[i].price) + " on " + self.name)
                        order2.quantity = order2.quantity - self.listOrder[i].quantity
                        Index = [i] + Index
                    else:
                        print("Execute " + str(order2.quantity) + " at " + str(self.listOrder[i].price) + " on " + self.name)
                        self.listOrder[i].quantity = self.listOrder[i].quantity - order2.quantity
                        order2.quantity=0
            
            for j in range(len(Index)):
                del(self.listOrder[Index[j]])
                
            print("Book on " + self.name)
            
            if order2.quantity > 0:
                if self.listOrder == []:
                    self.listOrder=self.listOrder+[order2]
                else:
                    k=0
                    while(self.listOrder[k].price > order2.price and k != len(self.listOrder) - 1):
                        k = k+1
                    while(self.listOrder[k].price >= order2.price and self.listOrder[k].quantity > order2.quantity and k != len(self.listOrder) - 1):
                        k = k+1
                    if self.listOrder[k].price >= order2.price and self.listOrder[k].quantity > order2.quantity and k == len(self.listOrder) - 1:
                        self.listOrder = self.listOrder + [order2]
                    else:    
                        self.listOrder.insert(k, order2)
            
            for i in range(len(self.listOrder)):
                self.listOrder[i].PrintOrder()
