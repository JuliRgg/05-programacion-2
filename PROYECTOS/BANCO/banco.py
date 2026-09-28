class Cuenta:
    def __init__(self, numero, titular, saldo_inicial = 0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo_inicial 

    def depositar(self, monto):
        self.saldo += monto
        print(f"Se ha depositado {monto}. Nuevo saldo: {self.saldo}")

    def extraer(self, monto):
        self.saldo -= monto
        print(f"Se ha extraído {monto}. Nuevo saldo: {self.saldo}")

    def __str__(self):
        return f"Número de cuenta: {self.numero}, Titular: {self.titular}, Saldo: {self.saldo}"

cuenta_ana = Cuenta("123456", "Ana", 1000)
print("Cuenta Ana creada.")
print(cuenta_ana)

cuenta_ana.depositar(-500)
cuenta_ana.extraer(20000)
print("Información actualizada de la cuenta Ana:")
print(cuenta_ana)

print("\nCreando cuenta de Juan...")
cuenta_juan = Cuenta("654321", "Juan")
print(cuenta_juan)

print("Realizando operaciones en la cuenta de Juan desde fuera")
cuenta_juan.saldo = 5000
print(cuenta_juan)