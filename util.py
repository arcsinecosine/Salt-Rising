import csv
import pickle
import os


def load_image(name):
    fullname = os.path.join('data',name)
    try:
        image = pygame.image.load(fullname)
    except:
        raise SystemError
    return image









def generate_end(string):
    length = 21 - len(string)
    end = " "*length
    return (end+"|")

def print_line(n,type = 1):
    if (type == 1):
        for i in range(n):
            print ("-"*23)
    elif (type == 2):
        for i in range(n):
            print ("*"*23)
    elif (type == 3):
        for i in range(n):
            print ("~"*23)

def container_text(string):
    if (len(string) >= 21):
        print ("String too large")
    else:
        start = "|%s" % (string)
        end = generate_end(string)
        total = start+end
        print (total)

def file_reader(name):
    name_file = (name)
    with open("%s.txt" % (name_file), "r") as f:
        reader = csv.reader(f)
        for row in reader:
            temp_list = row
            temp_string = "".join((temp_list))
            print(temp_string)
