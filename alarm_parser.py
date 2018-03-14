def remove_tag(om):
    om_new = om
    s_i = om.find("<")
    #size = om.size()
    while(s_i != -1):
        e_i = om.find(">", s_i)
        if(e_i != -1):
            #om_new = om[e_i+1:]
            om_new_1 = ''
            if(s_i > 0):
                om_new_1 = om[0:s_i]
            om_new_2 = om[e_i+1:]
            om_new_3 = om_new_1 + om_new_2 
            #print s_i, e_i
            #print "om_new_1: (" + om_new_1 + ")"
            #print "om_new_2: (" + om_new_2 + ")"
            #print "Om_new_3: (" + om_new_3 + ")"
            om_new = om_new_3
            om = om_new
            s_i = om.find("<")
        else:
            print("missing closing >")
            print om
            break
    #print "om_new: "+om_new
    
    return om_new.rstrip()
    
def remove_token(fmt):
    fmt_new = fmt
    s_i = fmt.find("%")
    while(s_i != -1):
        e_i_1 = fmt.find(":", s_i)
        e_i_2 = fmt.find(" ", s_i)
        e_i = e_i_1
        if(e_i == -1):
            e_i = e_i_2
        elif(e_i_2 != -1):
            if(e_i_2 < e_i):
                e_i = e_i_2
        if(e_i != -1):
            fmt_new_1 = ''
            if(s_i > 0):
                fmt_new_1 = fmt[0:s_i]
            fmt_new_2 = fmt[e_i:]
            fmt_new = fmt_new_1 + fmt_new_2
            fmt = fmt_new
            s_i = fmt.find("%")
        else:
            print("token not ending with space or : could be the end")
            print fmt
            if(s_i > 0):
                fmt_new = fmt[0:s_i-1]
                fmt = fmt_new
            break
    #print "fmt_new: " + fmt_new
    return fmt_new.rstrip()

text_mismatch = 0
    
def compare(om, fmt):
    global text_mismatch
    result = "No"
    om_new = remove_tag(om)
    fmt_new = remove_token(fmt)
    if( om_new == fmt_new ):
        result = "yes"
    else:
        print("om and fmt do not match...")
        print( "om:<" + om_new + ">")
        print("fmt:<" + fmt_new + ">")
        text_mismatch += 1
    return result


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
        row.insert(3, "Match")
        print row[14]
        print row
    else:
        match_act = "no"
        alarm_equate_orig = row[13]
        alarm_equate = alarm_equate_orig.strip(" ")
        #print
        #print "<<"+alarm_equate+">>"
        #print ("before");
        #print row
        act_value = alarm_dict.get(alarm_equate)      
        if act_value != None:
            match_act = compare(row[1], act_value)
            match = match +1 
            #print act_value
            #row.insert(2, act_value)
            #print("after")
            #print row
        else:
            act_value=""
            match_act = "none"
            print
            print "<<"+alarm_equate+">>"+" does not have FMT"
            
        row.insert(2, act_value)
        row.insert(3, match_act )
    writer.writerow(row)
    new_count = new_count+1
print
print "ACT has alarms: " , count, " including bad alarms: ", bad_act_alarm_count
print "Master list has alarms: ", new_count - 1
print "Matches of EQ between ACT and Master list: ", match, "mismatches: ", new_count - match -1 
print "Text mismatch between ACT and Master List: ", text_mismatch
  
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
