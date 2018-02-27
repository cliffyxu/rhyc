count = 0
bad_act_alarm_count = 0
alarm_dict={}
with open('C:/Data/xuc/python/taipei.alma') as alarm_file:
    for alarm in alarm_file.readlines():
        fmt_index = alarm.find("FMT")
        fmt_index_end = alarm.find("\"", fmt_index + 6)
        
        eq_index = alarm.find("EQ")
        eq_index_end = alarm.find(" ", eq_index)
        
        count = count + 1
        if(fmt_index_end != -1 and eq_index_end != -1) :
            fmt_str = alarm[fmt_index:fmt_index_end+1]
            #print fmt_str
            fmt = fmt_str.split("=")
            eq_str = alarm[eq_index:eq_index_end]
            eq = eq_str.split("=")
            #print eq[1]
            #print fmt[1]
            alarm_dict[eq[1]]=fmt[1].strip("\"")
        else:
            print("bad alarm record: %d", count)
            print alarm
            bad_act_alarm_count = bad_act_alarm_count + 1
    
    #print alarm_dict
    print " ACT alarms: ",len(alarm_dict)
alarm_file.close()    
        

import csv
alarm_old = open("C:/Data/xuc/python/tcl_alarms.csv", "rb")
alarm_new = open( "C:/Data/xuc/python/tcl_alarms_act.csv", "wb")

writer = csv.writer(alarm_new)
new_count = 0
match = 0
for row in csv.reader(alarm_old):
    if new_count == 0:
        row.insert(2, "Alarm From Act File")
        print row[14]
        print row
    else:
        alarm_equate_orig = row[13]
        alarm_equate = alarm_equate_orig.strip(" ")
        #print
        #print "<<"+alarm_equate+">>"
        #print ("before");
        #print row
        act_value = alarm_dict.get(alarm_equate)      
        if act_value != None:
            match = match +1 
            #print act_value
            #row.insert(2, act_value)
            #print("after")
            #print row
        else:
            act_value=""
            print
            print "<<"+alarm_equate+">>"+" does not have FMT"
            
        row.insert(2, act_value)
    writer.writerow(row)
    new_count = new_count+1
print
print "ACT has alarms: " , count, " including bad alarms: ", bad_act_alarm_count
print "Master list has alarms: ", new_count - 1
print "Matches between ACT and Master list: ", match, "mismatches: ", new_count - match -1 

  
alarm_old.close()
alarm_new.close()


#num = 1
#for keys,values in alarm_dict.items():
    #print
    #print "Number:", num
    #num = num + 1
    #print keys
    #print values
    
#print "BLOCK_DETECTOR_NRO"
#print alarm_dict["BLOCK_DETECTOR_NRO"]
