from os import system
import time
print(" Algorithms :")
print(' ----------\n')
choice = 0

while choice!=5:

    print("1. GREEDY\n2. Baseline\n3. Block\n4. Experiments\n5. Exit\n")
    choice = int(input("Enter your choice: "))
    system('cls')

    if choice == 1:
        print("1. All Configurations\n2. Max cluster Rectangle")
        cc = 0
        cc = int(input("Enter your choice: "))
        if cc==1:
            from all_config import config_shape
            from all_config import alg_class
            from all_config import addon
            from all_config import set_universe
            c = 0
            print("1. Square\n2. Rectangle\n3. Diamond\n4. Hole in  a square")
            c = int(input("Enter your choice: "))
            if c == 1:
                ch = 0
                while ch!=6:
                    size = int(input("Enter dimension of stadium: "))
                    mfamily = int(input("Enter max family size: "))
                    print("\n")
                    #system("cls")
                    #obj = alg_class.compute_arrangement(size,mfamily)
                    while ch!=6:
                         obj = alg_class.compute_arrangement(size,mfamily)
                         obj.total = len(obj.uncovered)
                         print("1. Print final arrangement\n2. Print universal set\n3. Print all the allowed configurations\n4. Step by step analysis\n5.New entry\n6.Exit")
                         ch = int(input("Enter your choice: "))
                         system("cls")
                         if ch==1:
                              start = time.time()
                              shapes = obj.seq(mfamily)
                              configs = obj.printconfig(shapes)
                              obj.add_final(configs)
                              print("% occupance = ",(obj.occ/obj.total)*100)
                              #print("Diversity Set = ",obj.div)
                              #mean_div = obj.mean()
                              #print("Mean family size chosen: ",mean_div)
                              end = time.time()
                              print("Runtime: ",end-start)
                              obj.print_format()


                         if ch==2:
                             shapes = obj.seq(mfamily)
                             configs = obj.printconfig(shapes)
                             universe = obj.allsets(configs)
                             print(universe)
                             char = input("Press enter to continue")
                             system("cls")

                         if ch==3:
                                 shapes = obj.seq(mfamily)
                                 con = obj.printconfig(shapes)
                                 for j in con:
                                     #print(j[0])
                                     for r in range(j[1]):
                                         for c in range(j[2]):
                                             if ((r*j[2]) + c) in j[0]:

                                                 print(" ",end='   ')
                                             else:
                                                 print('1',end='   ')
                                         print("\n")
                                     char = input("Press enter for next configuration: ")
                                     system("cls")

                         if ch==4:
                             shapes = obj.seq(mfamily)
                             configs = obj.printconfig(shapes)
                             obj.step_by_step(configs)
                         if ch==5:
                             system("cls")
                             break
                         if ch==6:
                             system("cls")
                             break
            if c==2:
                ch = 0
                while ch!=6:
                    l = int(input("Enter length of stadium: "))
                    b = int(input("Enter breadth of stadium: "))
                    size = max([l,b])
                    mfamily = int(input("Enter max family size: "))
                    print("\n")
                    #system("cls")
                    #obj = alg_class.compute_arrangement(size,mfamily)
                    while ch!=6:
                         obj = alg_class.compute_arrangement(size,mfamily)
                         #print(obj.uncovered)
                         obj.uncovered = addon.rectangle_shape(obj.uncovered,size,l,b)
                         obj.wasted = addon.rectangle_waste(obj.wasted,size,l,b)
                         obj.init_covered = obj.wasted
                         obj.total = len(obj.uncovered)
                        # print(obj.uncovered)
                        # print(obj.wasted)
                         print("1. Print final arrangement\n2. Print universal set\n3. Print all the allowed configurations\n4. Step by step analysis\n5.New entry\n6.Exit")
                         ch = int(input("Enter your choice: "))
                         system("cls")
                         if ch==1:
                              shapes = obj.seq(mfamily)
                              configs = obj.printconfig(shapes)
                              obj.add_final(configs)
                              print("% occupance = ",(obj.occ/obj.total)*100)
                              obj.print_format()

                         if ch==2:
                             shapes = obj.seq(mfamily)
                             configs = obj.printconfig(shapes)
                             universe = obj.allsets(configs)
                             print(universe)
                             char = input("Press enter to continue")
                             system("cls")
                         if ch==3:

                                 shapes = obj.seq(mfamily)
                                 con = obj.printconfig(shapes)
                                 for j in con:
                                     #print(j[0])
                                     for r in range(j[1]):
                                         for c in range(j[2]):
                                             if ((r*j[2]) + c) in j[0]:

                                                 print(" ",end='   ')
                                             else:
                                                 print('1',end='   ')
                                         print("\n")
                                     char = input("Press enter for next configuration: ")
                                     system("cls")
                         if ch==4:
                             shapes = obj.seq(mfamily)
                             configs = obj.printconfig(shapes)


                             obj.step_by_step(configs)
                         if ch==5:
                             system("cls")
                             break
                         if ch==6:
                             system("cls")
                             break
            if c==3:
                ch = 0
                while ch!=6:
                    size = int(input("Enter dimension of stadium: "))
                    mfamily = int(input("Enter max family size: "))
                    print("\n")
                    #system("cls")
                    #obj = alg_class.compute_arrangement(size,mfamily)
                    while ch!=6:
                         obj = alg_class.compute_arrangement(size,mfamily)
                         #print(obj.uncovered)
                         obj.uncovered = addon.diamond_shape(obj.uncovered,size)
                         obj.wasted = addon.diamond_waste(obj.wasted,size)
                         obj.init_covered = obj.wasted
                         obj.total = len(obj.uncovered)
                         #print(obj.uncovered)
                         #print(obj.init_covered)
                         print("1. Print final arrangement\n2. Print universal set\n3. Print all the allowed configurations\n4. Step by step analysis\n5.New entry\n6.Exit")
                         ch = int(input("Enter your choice: "))
                         system("cls")
                         if ch==1:
                              shapes = obj.seq(mfamily)
                              configs = obj.printconfig(shapes)
                              obj.add_final(configs)
                              print("% occupance = ",(obj.occ/obj.total)*100)
                              obj.print_format()

                         if ch==2:
                             shapes = obj.seq(mfamily)
                             configs = obj.printconfig(shapes)
                             universe = obj.allsets(configs)
                             print(universe)
                             char = input("Press enter to continue")
                             system("cls")
                         if ch==3:
                            shapes = obj.seq(mfamily)
                            con = obj.printconfig(shapes)
                            for j in con:
                                #print(j[0])
                                for r in range(j[1]):
                                    for c in range(j[2]):
                                        if ((r*j[2]) + c) in j[0]:

                                            print(" ",end='   ')
                                        else:
                                            print('1',end='   ')
                                    print("\n")
                                char = input("Press enter for next configuration: ")
                                system("cls")
                         if ch==4:
                             shapes = obj.seq(mfamily)
                             configs = obj.printconfig(shapes)

                             obj.step_by_step(configs)
                         if ch==5:
                             system("cls")
                             break
                         if ch==6:
                             system("cls")
                             break
            if c==4:
                 ch = 0
                 while ch!=6:
                    size = int(input("Enter dimension of stadium: "))
                    le = int(input("Enter length of hole"))
                    br  = int(input("Enter breadth of hole"))
                    mfamily = int(input("Enter max family size: "))
                    print("\n")
                    #system("cls")
                    #obj = alg_class.compute_arrangement(size,mfamily)
                    while ch!=6:
                         obj = alg_class.compute_arrangement(size,mfamily)
                         #print(obj.uncovered)
                         obj.uncovered = addon.hole_shape(obj.uncovered,size,le,br)
                         obj.wasted = addon.hole_waste(obj.wasted,size,le,br)
                         obj.init_covered = obj.wasted
                         obj.total = len(obj.uncovered)
                         #print(obj.uncovered)
                         #print(obj.init_covered)
                         print("1. Print final arrangement\n2. Print universal set\n3. Print all the allowed configurations\n4. Step by step analysis\n5.New entry\n6.Exit")
                         ch = int(input("Enter your choice: "))
                         system("cls")
                         if ch==1:
                              shapes = obj.seq(mfamily)
                              configs = obj.printconfig(shapes)
                              obj.add_final(configs)

                              print("% occupance = ",(obj.occ/obj.total)*100)
                              obj.print_format()

                         if ch==2:
                             shapes = obj.seq(mfamily)
                             configs = obj.printconfig(shapes)

                             universe = obj.allsets(configs)
                             print(universe)
                             char = input("Press enter to continue")
                             system("cls")
                         if ch==3:

                                 shapes = obj.seq(mfamily)
                                 con = obj.printconfig(shapes)
                                 for j in con:
                                     #print(j[0])
                                     for r in range(j[1]):
                                         for c in range(j[2]):
                                             if ((r*j[2]) + c) in j[0]:

                                                 print(" ",end='   ')
                                             else:
                                                 print('1',end='   ')
                                         print("\n")
                                     char = input("Press enter for next configuration: ")
                                     system("cls")
                         if ch==4:
                             shapes = obj.seq(mfamily)
                             configs = obj.printconfig(shapes)

                             obj.step_by_step(configs)
                         if ch==5:
                             system("cls")
                             break
                         if ch==6:
                             system("cls")
                             break
        if cc==2:
            from max_cluster_rectangle import config_shape
            from max_cluster_rectangle import alg_class
            from max_cluster_rectangle import addon
            from max_cluster_rectangle import set_universe
            from max_cluster_rectangle import stadium_sample
            c = 0
            print("1. Square\n2. Rectangle\n3. Diamond\n4. Hole in  a square\n5. Hole in a rectangle(Stadium stand-max cluster rectangle)\n6. Trapezium(Stadium stand-max cluster rectangle)")
            #print("Enter your choice: ")
            c = int(input("Enter your choice: "))
            if c == 1:
                ch = 0
                while ch!=6:
                    size = int(input("Enter dimension of stadium: "))
                    length = int(input("Enter cluster length: "))
                    breadth = int(input("Enter cluster breadth: "))
                    print("\n")
                    #system("cls")
                    #obj = alg_class.compute_arrangement(size,mfamily)
                    while ch!=6:
                         obj = alg_class.compute_arrangement(size,length,breadth)
                         obj.total = len(obj.uncovered)
                         print("1. Print final arrangement\n2. Print universal set\n3. Step by step analysis\n4. Print all allowed configurations\n5. New entry\n6. Exit")
                         ch = int(input("Enter your choice: "))
                         system("cls")
                         if ch==1:
                              shapes = obj.seq(length,breadth)
                              configs = obj.printconfig(shapes)
                              obj.add_final(configs)
                              print("% occupance = ",(obj.occ/obj.total)*100)
                              print("Diversity Distribution: ",obj.div)
                              mean_div = obj.mean()
                              print("Mean family size chosen: ",mean_div)
                              obj.print_format()
                         if ch==2:
                             shapes = obj.seq(length,breadth)
                             configs = obj.printconfig(shapes)
                             universe = obj.allsets(configs)
                             print(universe)
                             char = input("Press enter to continue")
                             system("cls")
                         if ch==3:
                             shapes = obj.seq(length,breadth)
                             configs = obj.printconfig(shapes)
                             obj.step_by_step(configs)
                         if ch==4:
                             config_shape.show_configs_of_size(length,breadth)
                         if ch==5:
                             system("cls")
                             break
                         if ch==6:
                             system("cls")
                             break
            if c==2:
                ch = 0
                while ch!=5:
                    l = int(input("Enter length of stadium: "))
                    b = int(input("Enter breadth of stadiom: "))
                    size = max([l,b])
                    length = int(input("Enter cluster length: "))
                    breadth = int(input("Enter cluster breadth: "))
                    print("\n")
                    #system("cls")
                    #obj = alg_class.compute_arrangement(size,mfamily)
                    while ch!=5:
                         obj = alg_class.compute_arrangement(size,length,breadth)
                         #print(obj.uncovered)
                         obj.uncovered = addon.rectangle_shape(obj.uncovered,size,l,b)
                         obj.wasted = addon.rectangle_waste(obj.wasted,size,l,b)
                         obj.init_covered = obj.wasted
                         obj.total = len(obj.uncovered)
                        # print(obj.uncovered)
                        # print(obj.wasted)
                         print("1. Print final arrangement\n2. Print universal set\n3. Step by step analysis\n4.New entry\n5.Exit")
                         ch = int(input("Enter your choice: "))
                         system("cls")
                         if ch==1:
                              shapes = obj.seq(length,breadth)
                              configs = obj.printconfig(shapes)
                              obj.add_final(configs)
                              print("% occupance = ",(obj.occ/obj.total)*100)
                              print("Total occupied seats: ",obj.occ)
                              print("Total number of seats: ",obj.total)
                              obj.print_format()

                         if ch==2:
                             shapes = obj.seq(length,breadth)
                             configs = obj.printconfig(shapes)

                             universe = obj.allsets(configs)
                             print(universe)
                             char = input("Press enter to continue")
                             system("cls")
                         if ch==3:
                             shapes = obj.seq(length,breadth)
                             configs = obj.printconfig(shapes)

                             obj.step_by_step(configs)
                         if ch==4:
                             system("cls")
                             break
                         if ch==5:
                             system("cls")
                             break
            if c==3:
                ch = 0
                while ch!=5:
                    size = int(input("Enter dimension of stadium: "))
                    length = int(input("Enter cluster length: "))
                    breadth = int(input("Enter cluster breadth: "))
                    print("\n")
                    #system("cls")
                    #obj = alg_class.compute_arrangement(size,mfamily)
                    while ch!=5:
                         obj = alg_class.compute_arrangement(size,length,breadth)
                         #print(obj.uncovered)
                         obj.uncovered = addon.diamond_shape(obj.uncovered,size)
                         obj.wasted = addon.diamond_waste(obj.wasted,size)
                         obj.init_covered = obj.wasted
                         obj.total = len(obj.uncovered)
                         #print(obj.uncovered)
                         #print(obj.init_covered)
                         print("1. Print final arrangement\n2. Print universal set\n3. Step by step analysis\n4.New entry\n5.Exit")
                         ch = int(input("Enter your choice: "))
                         system("cls")
                         if ch==1:
                              shapes = obj.seq(length,breadth)
                              configs = obj.printconfig(shapes)
                              obj.add_final(configs)
                              print("% occupance = ",(obj.occ/obj.total)*100)
                              obj.print_format()

                         if ch==2:
                             shapes = obj.seq(length,breadth)
                             configs = obj.printconfig(shapes)

                             universe = obj.allsets(configs)
                             print(universe)
                             char = input("Press enter to continue")
                             system("cls")
                         if ch==3:
                             shapes = obj.seq(length,breadth)
                             configs = obj.printconfig(shapes)
                             obj.add_final(configs)
                             obj.step_by_step(configs)
                         if ch==4:
                             system("cls")
                             break
                         if ch==5:
                             system("cls")
                             break
            if c==4:
                 ch = 0
                 while ch!=6:
                    size = int(input("Enter dimension of stadium: "))
                    le = int(input("Enter length of hole"))
                    br  = int(input("Enter breadth of hole"))
                    length = int(input("Enter max cluster length: "))
                    breadth = int(input("Enter max cluster breadth: "))
                    print("\n")
                    #system("cls")
                    #obj = alg_class.compute_arrangement(size,mfamily)
                    while ch!=6:
                         obj = alg_class.compute_arrangement(size,length,breadth)
                         #print(obj.uncovered)
                         obj.uncovered = addon.hole_shape(obj.uncovered,size,le,br)
                         obj.wasted = addon.hole_waste(obj.wasted,size,le,br)
                         obj.init_covered = obj.wasted
                         obj.total = len(obj.uncovered)
                         #print(obj.uncovered)
                         #print(obj.init_covered)
                         print("1. Print final arrangement\n2. Print universal set\n3. Print all the allowed configurations\n4. Step by step analysis\n5.New entry\n6.Exit")
                         ch = int(input("Enter your choice: "))
                         system("cls")
                         if ch==1:
                              shapes = obj.seq(length,breadth)
                              configs = obj.printconfig(shapes)
                              obj.add_final(configs)

                              print("% occupance = ",(obj.occ/obj.total)*100)
                              obj.print_format()

                         if ch==2:
                             shapes = obj.seq(length,breadth)
                             configs = obj.printconfig(shapes)

                             universe = obj.allsets(configs)
                             print(universe)
                             char = input("Press enter to continue")
                             system("cls")
                         if ch==3:

                                 shapes = obj.seq(length,breadth)
                                 con = obj.printconfig(shapes)
                                 for j in con:
                                     #print(j[0])
                                     for r in range(j[1]):
                                         for c in range(j[2]):
                                             if ((r*j[2]) + c) in j[0]:

                                                 print(" ",end='   ')
                                             else:
                                                 print('1',end='   ')
                                         print("\n")
                                     char = input("Press enter for next configuration: ")
                                     system("cls")
                         if ch==4:
                             shapes = obj.seq(length,breadth)
                             configs = obj.printconfig(shapes)
                             obj.step_by_step(configs)
                         if ch==5:
                             system("cls")
                             break
                         if ch==6:
                             system("cls")
                             break
            if c==5:
                ch = 0
                while ch!=5:
                    l = int(input("Enter length of stadium: "))
                    b = int(input("Enter breadth of stadium: "))
                    size = max([l,b])
                    length = int(input("Enter cluster length: "))
                    breadth = int(input("Enter cluster breadth: "))
                    print("\n")
                    #system("cls")
                    #obj = alg_class.compute_arrangement(size,mfamily)
                    while ch!=5:
                         obj = alg_class.compute_arrangement(size,length,breadth)
                         #print(obj.uncovered)
                         obj.uncovered = stadium_sample.rectangle_with_hole(obj.uncovered,size,l,b)
                         obj.wasted = stadium_sample.rectangle_with_hole_waste(obj.wasted,size,l,b)
                         obj.init_covered = obj.wasted
                         obj.total = len(obj.uncovered)
                        # print(obj.uncovered)
                        # print(obj.wasted)
                         print("1. Print final arrangement\n2. Print universal set\n3. Step by step analysis\n4.New entry\n5.Exit")
                         ch = int(input("Enter your choice: "))
                         system("cls")
                         if ch==1:
                              shapes = obj.seq(length,breadth)
                              configs = obj.printconfig(shapes)
                              obj.add_final(configs)
                              print("% occupance = ",(obj.occ/obj.total)*100)
                              print("Total occupied seats: ",obj.occ)
                              print("Total number of seats: ",obj.total)
                              obj.print_format()

                         if ch==2:
                             shapes = obj.seq(length,breadth)
                             configs = obj.printconfig(shapes)

                             universe = obj.allsets(configs)
                             print(universe)
                             char = input("Press enter to continue")
                             system("cls")
                         if ch==3:
                             shapes = obj.seq(length,breadth)
                             configs = obj.printconfig(shapes)

                             obj.step_by_step(configs)
                         if ch==4:
                             system("cls")
                             break
                         if ch==5:
                             system("cls")
                             break

            if c==6:
                ch = 0
                while ch!=5:
                    b = int(input("Enter number of rows: "))
                    size = int(input("Enter longest row"))
                    length = int(input("Enter cluster length: "))
                    breadth = int(input("Enter cluster breadth: "))
                    print("\n")
                    #system("cls")
                    #obj = alg_class.compute_arrangement(size,mfamily)
                    while ch!=5:
                         obj = alg_class.compute_arrangement(size,length,breadth)
                         #print(obj.uncovered)
                         obj.uncovered = stadium_sample.staircase_shape(obj.uncovered,size,b)
                         obj.wasted = stadium_sample.staircase_wasted(obj.wasted,size,b)
                         obj.init_covered = obj.wasted
                         obj.total = len(obj.uncovered)
                        # print(obj.uncovered)
                        # print(obj.wasted)
                         print("1. Print final arrangement\n2. Print universal set\n3. Step by step analysis\n4.New entry\n5.Exit")
                         ch = int(input("Enter your choice: "))
                         system("cls")
                         if ch==1:
                              shapes = obj.seq(length,breadth)
                              configs = obj.printconfig(shapes)
                              obj.add_final(configs)
                              print("% occupance = ",(obj.occ/obj.total)*100)
                              print("Total occupied seats: ",obj.occ)
                              print("Total number of seats: ",obj.total)
                              obj.print_format()

                         if ch==2:
                             shapes = obj.seq(length,breadth)
                             configs = obj.printconfig(shapes)

                             universe = obj.allsets(configs)
                             print(universe)
                             char = input("Press enter to continue")
                             system("cls")
                         if ch==3:
                             shapes = obj.seq(length,breadth)
                             configs = obj.printconfig(shapes)

                             obj.step_by_step(configs)
                         if ch==4:
                             system("cls")
                             break
                         if ch==5:
                             system("cls")
                             break

    if choice == 2:
        from baseline import base_line
        ccc = 0

        while(ccc!=4):
            print("1. Rectangle\n2. Diamond\n3. Hole in a square\n4. Exit")
            ccc = input("Enter your choice: ")
            if ccc in ['1','2','3']:
                base_line.baseline_print(int(ccc))
                char=input('Press Enter to Continue')
                system('cls')
            else:
                print('\nPlease enter a valid choice\n')

        system('cls')

    if choice == 3:
        from block import Block_algo
        l = int(input("Enter numbr of rows: "))
        b = int(input("Enter number of columns: "))
        m = int(input("Enter max cluster size: "))
        Block_algo.print_format(l,b,m)
        char=input('Press Enter to Continue')
        system('cls')

    if choice == 4:

        c = 0
        while c != 5:
            print("1. All Configs\n2. Max cluster Rectangle\n3. Diversity Comparison\n4. Block Algorithm   \n5. Exit")
            c = int(input("Enter your choice: "))
            if c == 1:
                from graphs import experiments_allconfig
                from all_config import config_shape
                cc = 0
                while cc !=11:
                    print("1. Plot varying square dimensions\n2. Plot varying diamond dimension\n3. Plot varying cluster sizes for square\n4. Plot varying cluster sizes for rectangle\n5. Plot varying cluster sizes for hole\n6. Plot varying cluster sizes for diamond\n7. Plot configurations\n8. Exit")
                    cc = int(input("Enter your choice: "))
                    if cc == 1:
                        experiments_allconfig.square_comparison_dimension()
                        char = input("Press enter to continue")
                        system("cls")
                    if cc == 2:
                        experiments_allconfig.diamond_comparison_dimension()
                        char = input("Press enter to continue")
                        system("cls")
                    if cc == 3:
                        experiments_allconfig.square_comparison_csize()
                        char = input("Press enter to continue")
                        system("cls")
                    if cc == 4:
                        experiments_allconfig.rectangle_comparison_csize()
                        char = input("Press enter to continue")
                        system("cls")
                    if cc == 5:
                        experiments_allconfig.hole_comparison_csize()
                        char = input("Press enter to continue")
                        system("cls")
                    if cc == 6:
                        experiments_allconfig.diamond_comparison_csize()
                        char = input("Press enter to continue")
                        system("cls")
                    if cc == 7:
                        config_shape.plot_config()
                    if cc == 8:
                        break

            if c == 2:
                from graphs import experiments_mcr
                from max_cluster_rectangle import config_shape
                cc = 0
                while cc != 6:
                    print("1. Plot varying square dimensions\n2. Plot varying diamond dimension\n3. Plot varying cluster sizes for rectangle\n4. Plot varying cluster sizes for hole\n5. Plot configurations\n6. Exit")
                    cc = int(input("Enter your choice: "))
                    if cc == 1:
                        experiments_mcr.square_comparison_dimension()
                        char = input("Press enter to continue")
                        system("cls")
                    if cc == 2:
                        experiments_mcr.diamond_comparison_dimension()
                        char = input("Press enter to continue")
                        system("cls")
                    if cc == 3:
                        experiments_mcr. rectangle_comparison_family()
                        char = input("Press enter to continue")
                        system("cls")
                    if cc == 4:
                        experiments_mcr.hole_comparison_family()
                        char = input("Press enter to continue")
                        system("cls")
                    if cc == 5:
                        config_shape.plot_config()
                        char = input("Press enter to continue")
                        system("cls")
                    if cc == 6:
                        break

            if c == 3:
                from graphs import experiments_compare_diversity
                experiments_compare_diversity.plot_diversity_comparison()

            if c == 4:
                from graphs import experiments_allconfig
                from all_config import config_shape
                cc = 0
                while cc !=3:
                    print('1. Plot varying Square dimensions \n2. Plot varying cluster sizes for rectangle \n3. Exit')
                    cc = int(input("Enter your choice: "))
                    if cc == 1:
                        experiments_allconfig.block_comparison_dimension()
                        char = input("Press enter to continue")
                        system("cls")
                    if cc == 2:
                        experiments_allconfig.block_rectangle_comparison_csize()
                        char = input("Press enter to continue")
                        system("cls")
                    if cc == 3:
                        system("cls")
                        break

            if c == 5:
                system("cls")
                break

    if choice == 5:
        system('cls')
        break
