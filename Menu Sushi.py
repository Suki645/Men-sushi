#delivery
import os #os.system
pikachu_roll=4500
otaku_roll= 5000
pulpo_roll = 5200
anguila_roll= 4800
cont_pika = 0
cont_otaku = 0
cont_pulpo = 0
cont_anguila = 0
while True:
    try:
        print ("----------------Menú----------------")
        print("[1]Pikachu Roll = 4500")
        print("[2]Anguila Eléctrica Roll = 4800")
        print("[3]Otaku Roll = 5000")
        print("[4]Pulpo Venenoso Roll = 5200")
        print("[5]Continuar con pago")
        print ("------------------------------------")
        roll = int(input("Seleccione una opcion: "))
        match roll:
            case 1:
                cont_pika += 1
            case 2:
                cont_anguila += 1
            case 3:
                cont_otaku +=1
            case 4:
                cont_pulpo +=1
            case 5:
                break
    except: 
        print("ingrese una opcion valida")

descuento = input ("ingrese codigo de descuento:")
if descuento == "soyotaku":
    print("descuento valido")
else:
    print("usted no posee descuento")
productos = cont_pulpo + cont_anguila + cont_pika + cont_otaku
os.system("cls")

print ("------------------------------------")
print (f"Total de productos: {productos}")
print ("------------------------------------")
print("Pikachu Roll:",cont_pika)
print("Anguila Eléctrica Roll:",cont_anguila)
print("Otaku Roll: ",cont_otaku)
print("Pulpo Venenoso Roll:",cont_pulpo)
print ("------------------------------------")
subtotal= (cont_pulpo * pulpo_roll) + (cont_anguila * anguila_roll) + (cont_otaku * otaku_roll)+ (cont_pika * pikachu_roll)
print ("su subtotal es: ",subtotal)
if descuento == "soyotaku":
    total=subtotal
    total1 = (subtotal * 0.1)
    print ("su total es:",total-total1)
else:
    total = subtotal 
    print ("su total es:",total)