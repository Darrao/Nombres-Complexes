import math

class Complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def somme(self,complex2):
        a_empreint = self.a + complex2.a
        b_empreint = self.b + complex2.b
        return str(a_empreint)+"+"+str(b_empreint)+"i" if self.b>0 else str(a_empreint)+str(b_empreint)+"i"

    def soustraction(self,complex2):
        a_empreint = self.a - complex2.a
        b_empreint = self.b - complex2.b
        return str(a_empreint)+ str(b_empreint) + "i" if self.b < 0 else str(a_empreint)+ str(b_empreint) + "i"

    def produit(self,complex2):
        a_empreint = self.a * complex2.a
        b_empreint = (self.b * complex2.b) * -1
        return a_empreint + b_empreint

    def quotient(self,complex2):
        if self.a!=0 or self.b!=0:
            a_empreint = self.a / complex2.a
            b_empreint = (self.b / complex2.b) * -1
            return a_empreint + b_empreint

    def partie_reel(self):
        return self.a

    def partie_imaginaire(self):
        return str(self.b)+"i"

    def module(self):
        return (self.racine((self.a * self.a) + (self.b * self.b)))

    def argument(self):
        if self.a == 0 and self.b > 0:
            return (str(self.module()) + str(90 * (math.pi/180)))+'i'
        elif self.a ==0 and self.b < 0:
            return (str(self.module()) + str(-90 * (math.pi/180)))+'i'
        elif self.b == 0 and self.a > 0:
            return (str(self.module()) + str(0 * (math.pi/180)))+'i'
        elif self.b == 0 and self.a < 0:
            return (str(self.module()) + str(180 * (math.pi/180)))+'i'
        elif self.a!= 0 and b!=0:
            return (str(self.module()) + str(math.atan(self.b/self.a)))+'i'

    def cartesienne(self):
        if self.a == 0 and self.b > 0:
            return (str(self.module() * math.cos(90 * (math.pi/180))) + "+" + str(math.sin(90 * (math.pi/180)))+"i")
        elif self.a ==0 and self.b < 0:
            return (str(self.module() * math.cos(-90 * (math.pi/180))) + "+" + str(math.sin(-90 * (math.pi/180)))+"i")
        elif self.b == 0 and self.a > 0:
            return (str(self.module() * math.cos(0 * (math.pi/180))) + "+" + str(math.sin(0 * (math.pi/180)))+"i")
        elif self.b == 0 and self.a < 0:
            return (str(self.module() * math.cos(180 * (math.pi/180))) + "+" + str(math.sin(180 * (math.pi/180)))+"i")
        elif self.a!= 0 and self.b!= 0:
            return (str(self.module() * math.cos(math.atan(self.b/self.a))) + "+" + str(self.module() *math.sin(math.atan(self.b /self.a)))+"i")

    def polar(self):
        if self.a == 0 and self.b > 0:
            return (str(self.module())+"+"+str(90 * (math.pi/180))+"i")
        elif self.a ==0 and self.b < 0:
            return (str(self.module())+"+"+str(-90 * (math.pi/180))+"i")
        elif self.b == 0 and self.a > 0:
            return (str(self.module())+"+"+str(0 * (math.pi/180))+"i")
        elif self.b == 0 and self.a < 0:
            return (str(self.module())+"+"+str(180 * (math.pi/180))+"i")
        elif self.a!= 0 and self.b!= 0:
            return (str(self.module())+"+"+str(math.atan(self.b/self.a))+"i")

    def conjugue(self):
        if self.b >0:
            return (str(self.a)+"-"+str(self.b)+"i")
        else:
            return (str(self.a) + "+" + str(self.b)+"i")

    def racine(self,nombre):
        return ((nombre)**(1/2))

if __name__ =="__main__":
    a = Complex(-14,5)
    b = Complex(-6, 15)
    print(a.somme(b))
    print(a.soustraction(b))
    print(a.produit(b))
    print(a.quotient(b))
    print(a.partie_reel())
    print(a.partie_imaginaire())
    print(a.module())
    print(a.argument())
    print(a.cartesienne())
    print(a.polar())
    print(a.conjugue())