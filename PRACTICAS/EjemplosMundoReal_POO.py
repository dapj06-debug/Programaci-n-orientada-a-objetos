class estudiante:

    def __init__(self, nombre, apellido, valor):
        self.nombre = nombre
        self.apellido = apellido
        self.valor = valor
        self.reporte_de_pagos = [] 

    def registrar_pago(self, valor):
        nuevo_pago = valor
        self.reporte_de_pagos.append(nuevo_pago)
        print(f"Pago registrado: {nuevo_pago}")

    def mostrar_reporte_de_pagos(self):
        print("Reporte de pagos:")
        for pago in self.reporte_de_pagos:
            print(f"- {pago}")
    
    def total_pagos(self):
        total = sum(self.reporte_de_pagos)
        return total
    
    def saldo_pendiente(self):
        saldo = self.valor - self.total_pagos()
        return saldo
    
    def mostrar_estado_de_pagos(self):
        print(f"Estado de pagos para {self.nombre} {self.apellido}:")
        print(f"Valor total a pagar: {self.valor}")
        print(f"Total pagado: {self.total_pagos()}")
        print(f"Saldo pendiente: {self.saldo_pendiente()}")

class pago:

    def __init__(self, estudiante, valor):
        self.estudiante = estudiante
        self.valor = valor
        self.estudiante.registrar_pago(self.valor)
        print(f"Pago de {self.valor} realizado para {self.estudiante.nombre} {self.estudiante.apellido}")

def main():
    estudiante1 = estudiante("Ana", "Gomez", 350)
    estudiante2 = estudiante("Luis", "Martinez", 400)
    estudiante3 = estudiante("Carla", "Lopez", 300)

    pago1 = pago(estudiante1, 35)
    pago2 = pago(estudiante1, 70)
    pago3 = pago(estudiante2, 80)
    pago4 = pago(estudiante2, 30)
    pago5 = pago(estudiante3, 30)
    pago6 = pago(estudiante3, 60)
    pago7 = pago(estudiante1, 40)

    estudiante1.mostrar_estado_de_pagos()
    estudiante2.mostrar_estado_de_pagos()
    estudiante3.mostrar_estado_de_pagos()
 
if __name__ == "__main__":
    main()


