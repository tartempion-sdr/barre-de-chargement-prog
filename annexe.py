
import time
import os

frame = 0
okchoixplus = 0            
def afficher():
    
    name  = "python"
    ok  = ["[|]", "[/]", "[-]", "[\]","[ok]"]
    clear = lambda : os.system('clear')
    tiret = "----------------------------------------------"
    ok_choix = ok[okchoixplus]
    
        
 
    tiret2  = tiret[:int((len(tiret)/100)*frame)].replace("-","\033[102m" + "#" + '\033[0m') +  tiret[int((len(tiret)/100)*frame):]
    barre  = "|""\033[96m"+"boucle 1:  "+"\033[0m" + str(frame) + "%|"+ str(tiret2) + "|" + str(ok_choix)  

        
        
    tiret2 = tiret[:int((len(tiret)/100)*frame)].replace("-","\033[102m" + "#" + '\033[0m') +  tiret[int((len(tiret)/100)*frame):]

   
#    if frame % 2 != 0:
#       ok_choix = ok[2]           

#    else:
#        ok_choix = ok[3]   


        

    if frame > 9:
        
        #barre = "|""\033[96m"+"boucle 1:  "+"\033[0m" + str(frame) + "%|"+ str(tiret2) + "|" + str(ok_choix)
        barre_list = list(barre)
        barre_list.pop(15)
        barre = "".join(barre_list)
        
    
    
    if frame >= 100:
    
        #barre = "|""\033[96m"+"boucle 1:  "+"\033[0m" + str(frame) + "%|"+ str(tiret2) + "|" + str(ok[4])
        ok_choix = ok[4]
        barre_list = list(barre)
        #barre_list.pop(14)    
        
        
        barre_list.pop(15)
        barre = "".join(barre_list) 
        

    

    #time.sleep(1)
    print("|""------------------------------------------------------------|")
    print("|------------------------------------------------------------|")
    print("|---------------------------" + name.upper()  + "---------------------------|")
    print("|------------------------------------------------------------|")
    
    #new_barre = barre[:26 + frame] + "\033[102m" + " " + '\033[0m' + barre[frame + 26:]
    print(barre)
    time.sleep(0.2) 

    
    clear()
    
    


  
    
    
    
            
 
                
      
        
       
        