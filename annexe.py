from dataclasses import dataclass
import time
import os



name = "python"
frame = 0
ok = ["[\/]", "[/\]", "[ok]"]

clear = lambda: os.system('clear')

tiret = "----------------------------------------------"
@dataclass

class LotDeFonction:
  
    #frame: int = 0
    
    def depart():
        
        tiret2 = tiret[:int((len(tiret)/100)*frame)].replace("-","\033[102m" + "#" + '\033[0m') +  tiret[int((len(tiret)/100)*frame):]

        if frame % 2 == 0:
            ok_choix = ok[0]


        if frame % 2 != 0:
            ok_choix = ok[1]
            
        barre = "|""\033[96m"+"boucle 1:  "+"\033[0m" + str(frame) + "%|"+ str(tiret2) + "|" + str(ok_choix)

        #time.sleep(1)
        print("|""------------------------------------------------------------|")
        print("|------------------------------------------------------------|")
        print("|---------------------------" + name.upper()  + "---------------------------|")
        print("|------------------------------------------------------------|")
        
        #new_barre = barre[:26 + frame] + "\033[102m" + " " + '\033[0m' + barre[frame + 26:]
       
        
        if frame > 9:
            
            barre = "|""\033[96m"+"boucle 1:  "+"\033[0m" + str(frame) + "%|"+ str(tiret2) + "|" + str(ok_choix)
            barre_list = list(barre)
            barre_list.pop(15)
            barre = "".join(barre_list)
            
        
        
        if frame == 100:
        
            barre = "|""\033[96m"+"boucle 1:  "+"\033[0m" + str(frame) + "%|"+ str(tiret2) + "|" + str(ok[2])
            barre_list = list(barre)
            barre_list.pop(14)    
            barre_list.pop(15)
     
            barre = "".join(barre_list)
            
        
        

        print(barre)
    
        time.sleep(0.2) 
        
        clear()   
        
            
            
 
                
      
        
       
        