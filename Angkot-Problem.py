from queue import PriorityQueue
from prettytable import PrettyTable

# path_text=""

angkot = {
        'F': {'Joyoboyo', 'THR', 'Pegirian', 'Endrosono'},
        'G1' : {'Joyoboyo', 'Karang Menjangan', 'Menur'},
        'V' :  {'Joyoboyo', 'Basuki Rahmat', 'THR', 'Krampung'},
        'J': {'Joyoboyo', 'Banyu Urip', 'Tidar', 'Kalianak'},
        'JK': {'Joyoboyo', 'Gubeng', 'Jagiran', 'Kenjeran'},
        'T2': {'Joyoboyo', 'Kalasan', 'Mulyosari', 'Kenjeran'},
        'O' : {'Jembatan Merah', 'Peneleh', 'Krampung', 'Karang Menjangan', 'Keputih'},
        'R1': {'Jembatan Merah', 'Kapasan', 'Krampung', 'Kenjeran'},
        'K': {'Jembatan Merah', 'Indrapura', 'Perak', 'Rajawali'},
        'N': {'Jembatan Merah', 'Genteng Kali', 'Pucang', 'Bratang'},
        'Q': {'Jembatan Merah', 'Tidar', 'Dr.Soetomo', 'Bratang'},
        'BJ': {'Benowo- Tanjungsari', 'Dupak', 'Rajawali'},
        'C': {'Karang Menjangan', 'Ambengan', 'Pasar Turi', 'Sedayu'},
        'W': {'Dukuh Kupang', 'Pandegiling', 'Gubeng', 'Karang Menjangan'},
        'MLK': {'Manukan', 'Praban', 'Jagiran', 'Kenjeran'}
        }


GRAPH = {
        'Joyoboyo' : {'THR':25, 'Karang Menjangan':23, 'Banyu Urip':20, 'Gubeng':22, 'Basuki Rahmat':20,'Kalasan':27},
'Kalasan':{'Joyoboyo':27,'Mulyosari':21},
'THR' :{'Joyoboyo':25, 'Pegirian':20, 'Krampung':15, 'Basuki Rahmat':17},
'Pegirian':{'Endrosono':13, 'THR':20},
'Keputih':{'Karang Menjangan':25},
'Endrosono':{'Pegirian':13},
'Karang Menjangan':{'Joyoboyo':23, 'Menur':13, 'Krampung':18, 'Keputih':25, 'Ambengan':16, 'Gubeng':15},
'Menur':{'Karang Menjangan':13},
'Krampung':{'THR':15, 'Karang Menjangan':18, 'Kenjeran':18,'Kapasan':15,'Peneleh':18},
'Jembatan Merah': {'Peneleh':15 , 'Kapasan':15, 'Indrapura':14,'Genteng Kali':17,'Tidar':18},
'Kapasan':{'Jembatan Merah':15 , 'Krampung':15},
'Peneleh':{'Jembatan Merah':15, 'Krampung':18},
'Kenjeran':{'Krampung':18, 'Jagiran':21, 'Mulyosari':24},
'Basuki Rahmat':{'Joyoboyo':20, 'THR':17},
'Banyu Urip':{'Joyoboyo':20,'Tidar':17},
'Tidar':{'Banyu Urip':17, 'Kalianak':29, 'Jembatan Merah':18, 'Dr.Soetomo':17},
'Kalianak':{'Tidar':29},
'Jagiran':{'Gubeng':19,'Kenjeran':21,'Praban':18},
'Gubeng':{'Joyoboyo':22,'Jagiran':19,'Pandegiling':15,'Karang Menjangan':15},
'Dr.Soetomo':{'Bratang':20,'Tidar':17},
'Mulyosari':{'Kalasan':21,'Kenjeran':24},
'Indrapura':{'Jembatan Merah':14,'Perak':14},
'Perak':{'Rajawali':14,'Indrapura':14},
'Rajawali':{'Perak':14,'Dupak':17},
'Genteng Kali':{'Pucang':20,'Jembatan Merah':17},
'Pucang':{'Genteng Kali':20,'Bratang':12},
'Bratang':{'Pucang':12,'Dr.Soetomo':20},
'Tanjung Sari':{'Benowo':26,'Dupak':18},
'Benowo':{'Tanjung Sari':26},
'Dupak':{'Tanjung Sari':18,'Rajawali':17},
'Ambengan':{'Pasar Turi':17,'Karang Menjangan':16},
'Pasar Turi':{'Ambengan':17,'Sedayu':16},
'Sedayu':{'Pasar Turi':16},
'Dukuh Kupang':{'Pandegiling':17},
'Pandegiling':{'Dukuh Kupang':17,'Gubeng':15},
'Manukan':{'Praban':28},
'Praban':{'Jagiran':18,'Manukan':28}

        }

straigth_line = {
        'Joyoboyo': 38,
        'THR' :18,
        'Kalasan': 14,
        'Pegirian' : 37,
        'Endrosono': 51 ,
        'Karang Menjangan':11 ,
        'Menur' :20,
        'Krampung':24,
        'Jembatan Merah' :38,
        'Peneleh' : 20,
        'Keputih': 51 ,
        'Kapasan':32,
        'Kenjeran': 60 ,
        'Basuki Rahmat' :11,
        'Banyu Urip' :31,
        'Tidar' : 36,
        'Kalianak': 70 ,
        'Jagiran' : 18,
        'Gubeng': 0,
        'Dr.Soetomo' : 22,
        'Mulyosari':49,
        'Indrapura' :41,
        'Perak' :60,
        'Rajawali' :41,
        'Genteng Kali' : 17,
        'Pucang' :21,
        'Bratang' : 34,
        'Benowo':120,
        'Tanjung Sari':62 ,
        'Dupak' : 38,
        'Ambengan':14,
        'Pasar Turi':32 ,
        'Sedayu' : 48,
        'Dukuh Kupang' :48,
        'Pandegiling' :20,
        'Manukan' :91,
        'Praban':22
                }

tabelSiswa = PrettyTable(["Nama Angkot", "Trayek"])
tabelSiswa.add_row(["F" ,"Joyoboyo - THR-Pegirian - Endrosono"])
tabelSiswa.add_row(["G1" ,"Joyoboyo - Karang Menjangan - Menur"])
tabelSiswa.add_row(["V" ,"Joyoboyo - Basuki Rahmat -THR- Krampung"])
tabelSiswa.add_row(["J" ,"Joyoboyo - Banyu Urip - Tidar - Kalianak"])
tabelSiswa.add_row(["JK" ,"Joyoboyo - Gubeng- Jagiran- Kenjeran"])
tabelSiswa.add_row(["T2" ,"Joyoboyo - Kalasan - Mulyosari - Kenjeran"])
tabelSiswa.add_row(["O" ,"Jembatan Merah - Peneleh - Krampung - Karang Menjangan - Keputih"])
tabelSiswa.add_row(["R1" ,"Jembatan Merah - Kapasan - Krampung - Kenjeran"])
tabelSiswa.add_row(["K" ,"Jembatan Merah - Indrapura - Perak -Rajawali"])
tabelSiswa.add_row(["N" ,"Jembatan Merah - Genteng Kali- Pucang - Bratang"])
tabelSiswa.add_row(["Q" ,"Jembatan Merah- Tidar - Dr.Soetomo - Bratang"])
tabelSiswa.add_row(["BJ" ,"Benowo- Tanjungsari- Dupak- Rajawali"])
tabelSiswa.add_row(["C" ,"Karang Menjangan -Ambengan- Pasar Turi- Sedayu"])
tabelSiswa.add_row(["W" ,"Dukuh Kupang- Pandegiling- Gubeng- Karang Menjangan"])
tabelSiswa.add_row(["MLK" ,"Manukan -Praban- Jagiran- Kenjeran"])


def astar(graph, start, goal):
    prior_queue = PriorityQueue()
    explored = {}

    """Parameter PriorityQueue (est_cost, cost so far, node saat ini, path yang telah dilalui)"""
    prior_queue.put((straigth_line[start], 0, start, [start]))

    explored[start] = straigth_line[start]

    while prior_queue:
        (est_cost, cost, node, path) = prior_queue.get()

        if node == goal:
            return est_cost, cost, path

        for neighbour in graph[node].keys():
            current_cost = cost + graph[node][neighbour]
            heuristic = straigth_line[neighbour]
            est_cost = current_cost + heuristic

            if neighbour not in explored or explored[neighbour] >= est_cost:
                explored[neighbour] = est_cost
                prior_queue.put((est_cost, current_cost, neighbour, path + [neighbour]))

    if node != goal:
        return("No skippable path")

def CariAngkot():
    start = input("The starting point of the journey:  ")
    goal = input("The destination point of the journey: ")
    #start = start_var.get()
    #goal = goal_var.get()
    
    if start not in GRAPH:
        # path_text='Correct'
        print('Error, Inserted starting point not detected')
    elif goal not in GRAPH:
        print('Error, inserted destination point not detected')
    else:
        print("\nA* Search: ")
        heuristic, cost, astar_path = astar(GRAPH, start, goal)
        print('Cheapest Path: ' + ' -> '.join(city for city in astar_path))
        print('\n You can ride angkot', end='')
        prev=None
        for n in range(len(astar_path)-1):
            for neighbour in angkot:
                if astar_path[n] in angkot[neighbour] and astar_path[n+1] in angkot[neighbour]:
                    if neighbour is not prev:
                        print ('\n'+neighbour, astar_path[n], '->', astar_path[n+1], end=' ')
                        prev = neighbour
                    else:
                        print ('->', astar_path[n+1], end=' ')
        # angkot_path = angkot_find(astar)
        # print('Estimated Path Cost(Heuristic): ' + str(heuristic))
        # print('Path Cost: ' + str(cost))

def main():
    print("==========  WELCOME IN ANGKOTKU  ==========")
    print("======== By Sukolilo-Membara Group ========")
    print("================== MENU ===================")
    print("1.Check Angkot")
    print("2.List Trayek Angkot")
    option=int(input("What do you need? ⇒ "))
    if option==1:
        CariAngkot()
        print("\n\n1.Back to Menu")
        print("2.Stop")
        option2=int(input("Enter your choice? ⇒ "))
        if option2==1:
            main()
        elif option2==2:
            print("\n\n====== THANK YOU, HAVE A NICE DAY ======")
        else:
            print("your code is wrong\n\n")
    elif option==2:
        print(tabelSiswa)
        print("\n\n1.Back to Menu")
        print("2.Stop")
        option2=int(input("Enter your choice? ⇒ "))
        if option2==1:
            main()
        elif option==2:
            print("\n\n====== THANK YOU, HAVE A NICE DAY ======")
        else:
            print("your code is wrong\n\n")
    else:
        print("your code is wrong\n\n")
    
if __name__ == '__main__':
    main()



