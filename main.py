from colorama import Fore
from command.command import define_cd,create_dotnet_project,build_project,run_project

ascii_art = r"""
 m                      .mm                                
]W[       ][            ]P"W       ][             ][       
]W[ ][ ][]WWW  dWb      ][ ][ dWb ]WWW ]bWW, dWb ]WWW      
W W ][ ][ ][  ]P T[     ][ ][]P T[ ][  ]P ][]bmd[ ][       
WWW ][ ][ ][  ][ ][     ][ ][][ ][ ][  ][ ][]P""` ][       
W W,]bmW[ ]bm 'WmW`     ]bmW 'WmW` ]bm ][ ]['Wmm[ ]bm      
'` '`""'` "" '"`         '""   '"`  "" '`'`  '""   """""

def main():
    print(Fore.RED + ascii_art)
    print(Fore.BLUE + "\n[1] Define CD")
    print("[2] Create dotnet project")
    print("[3] Build project")
    print("[4] Run project")
    print("[5] Exit")
    while True:
        try:
            num_select = int(input_user("Action Id",Fore.RED))
        except Exception as exception:
            print(Fore.YELLOW + str(exception))
            continue
        if num_select == 1:
            cd = input_user("new cd",Fore.RED)
            define_cd(cd)
        elif num_select == 2:
            type = input_user(Fore.RED + "type dotnet project",Fore.RED)
            create_dotnet_project(type)
        elif num_select == 3:
            build_project()
        elif num_select == 4:
            run_project()
        elif num_select == 5:
            break

def input_user(text:str,color):
    response = input(Fore.LIGHTBLUE_EX + "user@autodotnet" + Fore.CYAN + ":" + color + text + Fore.GREEN + " ~$" + Fore.WHITE)
    return response


if __name__ == "__main__":
    main()