import csv
import statistics
 
def hipertension():
    with open('data.csv', mode='r', encoding='utf-8-sig') as archivo:
        presiones= csv.reader(archivo)
        suc=input().split()
 
        lista_suc=[]  
        for i in range (len(suc)):
            lista_suc.append(int(suc[i]))
        lista_suc.sort() 
 
        for i in range(len(lista_suc)):
            if lista_suc[i] >=1 and  lista_suc[i] <=32:
                archivo.seek(0)
                cantMediSoli_M=0
                cantMediSoli_F=0
                sumaMedicaSoli=0
                sumaMediEntre=0
                cantMediEntre_M=0
                cantMediEntre_F=0
                dosisMediMin=0
                dosisMediMax=0
                listaMedicaSolici=[]
                listaMediEntre=[]
                for item in presiones:
                    if str(lista_suc[i])== item[5]:
                        sucursal=item[5]
                        municipio=item[3]
                        departamento=item[4]
                        if item[2]== "m":
                            cantMediSoli_M+=1
                        else:
                            cantMediSoli_F+=1 
                        listaMedicaSolici.append(int(item[7]))
                        sumaMedicaSoli+=int(item[7])
                        proEntregas=0
                        if int(item[8]) < 85 and int(item[9]) < 65:
                            proEntregas=1
 
                        elif 85 <= int(item[8]) < 125 and 65 <= int(item[9]) < 85:
                            pass
 
                        elif 125 <= int(item[8]) < 135 and 85 <= int(item[9]) < 90:
                            pass
 
                        elif 135 <= int(item[8])  < 145 and 90 <= int(item[9]) < 95:
                            proEntregas=1
 
                        elif 145 <= int(item[8])  < 165 and 95 <= int(item[9]) < 105:
                            proEntregas=1
                        elif 165 <= int(item[8])  < 185 and 105 <= int(item[9]) < 115:
                            proEntregas=1
 
                        elif int(item[8])  >= 185 and int(item[9]) >= 115:
                            proEntregas=1
 
                        elif int(item[8]) >= 145 and int(item[9]) < 95: 
                            proEntregas=1
 
                        if proEntregas == 1:
                            if item[2] == "m":
                                cantMediEntre_M+=1
                            else:
                                cantMediEntre_F+=1  
                            listaMediEntre.append(int(item[7]))
                            sumaMediEntre+=int(item[7]) 
                            if len(listaMediEntre)==1:
 
                                    nombreMin=item[0]
                                    apellidoMin=item[1]
                                    generoMin=item[2]
                                    medicinaMin=int(item[6])
                                    dosisMediMin=int(item[7])
 
                                    nombreMax=item[0]
                                    apellidoMax=item[1]
                                    generoMax=item[2]
                                    medicinaMax=int(item[6])
                                    dosisMediMax=int(item[7])
 
                            if len(listaMediEntre)>1:
 
                                if int(item[7]) < dosisMediMin:
                                    nombreMin=item[0]
                                    apellidoMin=item[1]
                                    generoMin=item[2]
                                    medicinaMin=int(item[6])
                                    dosisMediMin=int(item[7])
 
                                if int(item[7]) > dosisMediMax:
                                    nombreMax=item[0]
                                    apellidoMax=item[1]
                                    generoMax=item[2]
                                    medicinaMax=int(item[6])
                                    dosisMediMax=int(item[7])
 
 
                PromMedicSolici = sumaMedicaSoli/(cantMediSoli_M+cantMediSoli_F)
                StdMedicSolici = statistics.stdev(listaMedicaSolici)
                max_MedicSolici= max(listaMedicaSolici)
                min_MedicSolici= min(listaMedicaSolici)
                PromMedientre= sumaMediEntre/(cantMediEntre_M+cantMediEntre_F)
                StdMedicEntre = statistics.stdev(listaMediEntre)
                max_MedicEntre= max(listaMediEntre)
                min_MedicEntre= min(listaMediEntre)
 
                print(sucursal, municipio, departamento)
                print('patients')
                print("male", cantMediSoli_M)
                print("female", cantMediSoli_F)  
                print('total', cantMediSoli_M+cantMediSoli_F)
                print("medicine quantity")
                print("mean",f"{PromMedicSolici:,.2f}")
                print("std",f"{StdMedicSolici:,.2f}")
                print("min",min_MedicSolici)
                print("max",max_MedicSolici)
                print("total",sumaMedicaSoli)
                print("scheduled patients")
                print("male",cantMediEntre_M)
                print("female",cantMediEntre_F)
                print('total', cantMediEntre_M+cantMediEntre_F)
                print("scheduled medicine quantity")
                print("mean",f"{PromMedientre:.2f}")
                print("std",f"{StdMedicEntre:,.2f}")
                print("min",min_MedicEntre, nombreMin, apellidoMin, generoMin, medicinaMin)
                print("max",max_MedicEntre, nombreMax, apellidoMax, generoMax, medicinaMax)
                print("total",sumaMediEntre)
hipertension()