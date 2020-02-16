
import random
import copy
import time
import requests

start_host = "https://5ka.pw/stufffseller/"

chars_list = ['a' , 'b' , 'c' ,'d' ,'e' , 'f' , 'g' , 'h', 'i' ,'j','k','l','m','n','o','p','q','r','s',
't','u','v','w','x','y','z', '1' , '2' , '3' , '4' , '5' ,'6', '7', '8', '9' ,'0' ]


def generation(sequence):
    new_sequence = copy.copy(sequence)
    random.shuffle(new_sequence)
    return new_sequence[0:33]

def generate_url():
    new_char_list = ''.join(generation(chars_list))
    return start_host + new_char_list
with open("card5ka.txt" , 'w') as f:
    def main():
        
            new_card = generate_url()
            response = requests.get(new_card)
            valid_link = requests.get("https://5ka.pw/stufffseller/f149354f54f47021aa2866ba2e3d8f55")
            bad_link = requests.get("https://5ka.pw/stufffseller/ck47g2aidry0qpm5houwlnv968sefbtj3")
        
            if response.status_code == 200:
                f.write(new_card + " - " + 'Валид' + "\n")
            else:
                f.write(new_card + " - " + "Невалид" + "\n")

        

    while True:
        
        time.sleep(0.2)
        main()

    