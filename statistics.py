import csv
from collections import Counter

def find_mean(weight_data):
    total=0
    for i in weight_data:
        total+=i

    mean=total/len(weight_data)

    print('Mean (Average) is -> '+str(mean))

def find_median(weight_data):
    weight_data.sort()
    n=len(weight_data)

    if n%2==0:
        median1=weight_data[(n//2)-1]
        median2=weight_data[n//2]
        median=(median1+median2)/2
    else:
        median=weight_data[n//2]

    print('Median is '+str(median))

def find_mode(weight_data):
    data=Counter(weight_data)
    mode_data_for_range={'75-85':0,'85-95':0,'95-105':0,'105-115':0,'115-125':0,'125-135':0,'135-145':0,'145-150':0}

    for weight,occurance in data.items():
        if 75<weight<85:
            mode_data_for_range['75-85']+=occurance

        elif 85<weight<95:
            mode_data_for_range['85-95']+=occurance

        elif 95<weight<105:
            mode_data_for_range['95-105']+=occurance
        
        elif 105<weight<115:
            mode_data_for_range['105-115']+=occurance
        
        elif 115<weight<125:
            mode_data_for_range['115-125']+=occurance
        
        elif 125<weight<135:
            mode_data_for_range['125-135']+=occurance
        
        elif 135<weight<145:
            mode_data_for_range['135-145']+=occurance
        
        elif 145<weight<150:
            mode_data_for_range['145-150']+=occurance

    mode_range=0
    mode_occurance=0

    for range,occurance in mode_data_for_range.items():
        if occurance>mode_occurance:
            mode_range,mode_occurance=range,occurance
    
    num1,num2=mode_range.split('-')
    mean=(int(num1)+int(num2))/2

    print('Mode is -> '+str(int(mean)))

def main():
    with open('SOCR-HeightWeight.csv',newline='') as f:
        reader=csv.reader(f)
        file_data=list(reader)

    file_data.pop(0)
    weight_data=[]
    for i in range(len(file_data)):
        num=file_data[i][2]
        weight_data.append(float(num))

    find_mean(weight_data)
    find_median(weight_data)
    find_mode(weight_data)

if __name__ == '__main__':
    main()