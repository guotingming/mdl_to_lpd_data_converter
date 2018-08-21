import numpy as np
import pandas as pd
import math
from Gamma_converter import *
filename='8818-1_8GHz-LPSweep_Dev3.mdf'
#datas=[]

def calculate_Pav(a1_real,a1_imag):
    Pav=(a1_real*a1_real+a1_imag*a1_imag)/2
    Pav=10*math.log10(1000*Pav)
    return Pav
def calculate_Pout(a2_real,a2_imag,b2_real,b2_imag):
    Pout=(b2_real*b2_real+b2_imag*b2_imag-a2_imag*a2_imag-a2_real*a2_real)/2
    Pout=10*math.log10(1000*Pout)
    return Pout
def calculate_PAE(Pout,V2,I2, b1_real, b1_imag, Pav):
    Pout=float(Pout)
    V2=float(V2)
    I2=float(I2)
    Pref=(b1_real*b1_real+b1_imag*b1_imag)/2
    Pin=math.pow(10,Pav/10)/1000-Pref
    PAE=(math.pow(10,Pout/10)/1000-Pin)/(V2*I2)*1000*100
    return PAE
def converter_data(filename,savename_dir):
    print(filename)
    errors=[]
    out_except=[]
    try:
        t = filename.split('.mdf')
        print(t)
    except Exception as e:
        print(e)
        error='获取文件名出错'
        print(error)
        out_except.append(str(e))
        errors.append(error)
    else:
        t = t[0]
        Dev= t[-4:]
        print(Dev)
    try:
        with open(filename) as file:
            DATA=[]
            freq_key='3612345600'
            for line in file:
                data=line
                #print(data[0:19])
                freq_line=data[0:23]
                if(freq_line=='!	Fundamental Frequency'):
                    freq_datas=data.split()
                    print(freq_datas)
                    global freq_data
                    freq_data=freq_datas[3]
                    print(freq_key)
                    freq_key=float(freq_data[:-3])
                    freq_key = str(int(freq_key * 1000000000))
                    print(freq_key)
                    print(freq_data[:-3])
                VAR_realLoad=data[0:19]
                if(VAR_realLoad=='VAR realLoad (real)'):
                    #print(data[22:])
                    realLoad=float(data[22:])
                    DATA.append(realLoad)
                VAR_imagload=data[0:19]
                if (VAR_imagload == 'VAR imagload (real)'):
                    #print(data[22:])
                    imagLoad=float(data[22:])
                    DATA.append(imagLoad)
                f0_drive=data[0:19]
                if (f0_drive == 'VAR f0_drive (real)'):
                    #print(data[22:])
                    f0_drive=float(data[22:])
                    DATA.append(f0_drive)
                numdata=line[0:10]
                '''
                if(len(freq_key)<10):
                    freq_key=freq_key+' '
                print('len(freq_key)=', len(freq_key))
                '''
                #print(freq_key)
                if(numdata==freq_key):
                    #print(data[11:30])
                    datas=data.split()
                    #print(len(datas))
                    '''
                    a1=complex(float(datas[1]),float(datas[2]))
                    a2=complex(float(datas[5]),float(datas[6]))
                    b2=complex(float(datas[7]),float(datas[8]))
                    print(a1,a2,b2)
                    DATA.append(a1.real)
                    DATA.append(a1.imag)
                    DATA.append(a2.real)
                    DATA.append(a2.imag)
                    DATA.append(b2.real)
                    DATA.append(b2.imag)
                    '''
                    a1_real=float(datas[1])
                    a1_imag=float(datas[2])
                    b1_real=float(datas[3])
                    b1_imag=float(datas[4])
                    a2_real=float(datas[5])
                    a2_imag=float(datas[6])
                    b2_real=float(datas[7])
                    b2_imag=float(datas[8])
                    V1=float(datas[9])
                    I1=float(datas[11])
                    V2=float(datas[13])
                    I2=float(datas[15])
                    DATA.append(a1_real)
                    DATA.append(a1_imag)
                    DATA.append(b1_real)
                    DATA.append(b1_imag)
                    DATA.append(a2_real)
                    DATA.append(a2_imag)
                    DATA.append(b2_real)
                    DATA.append(b2_imag)
                    #DATA.append(V1)
                    #DATA.append(I1)
                    #DATA.append(V2)
                    #DATA.append(I2)
                numdata_2=line[0:9]
                #print(freq_key)
                if(numdata_2==freq_key):
                    #print(data[11:30])
                    datas=data.split()
                    #print(len(datas))
                    '''
                    a1=complex(float(datas[1]),float(datas[2]))
                    a2=complex(float(datas[5]),float(datas[6]))
                    b2=complex(float(datas[7]),float(datas[8]))
                    print(a1,a2,b2)
                    DATA.append(a1.real)
                    DATA.append(a1.imag)
                    DATA.append(a2.real)
                    DATA.append(a2.imag)
                    DATA.append(b2.real)
                    DATA.append(b2.imag)
                    '''
                    a1_real=float(datas[1])
                    a1_imag=float(datas[2])
                    b1_real=float(datas[3])
                    b1_imag=float(datas[4])
                    a2_real=float(datas[5])
                    a2_imag=float(datas[6])
                    b2_real=float(datas[7])
                    b2_imag=float(datas[8])
                    V1=float(datas[9])
                    I1=float(datas[11])
                    V2=float(datas[13])
                    I2=float(datas[15])
                    DATA.append(a1_real)
                    DATA.append(a1_imag)
                    DATA.append(b1_real)
                    DATA.append(b1_imag)
                    DATA.append(a2_real)
                    DATA.append(a2_imag)
                    DATA.append(b2_real)
                    DATA.append(b2_imag)
                    #DATA.append(V1)
                    #DATA.append(I1)
                    #DATA.append(V2)
                    #DATA.append(I2)
                DCline=data[0]
                if(DCline=='0'):
                    datas = data.split()
                    #print(datas)
                    V1=float(datas[9])
                    I1=float(datas[11])*1000*1000
                    V2=float(datas[13])
                    I2=float(datas[15])*1000
                    #print(V1,I1,V2,I2)
                    DATA.append(V1)
                    DATA.append(I1)
                    DATA.append(V2)
                    DATA.append(I2)
            #print(DATA)
        file.close()
    except Exception as e:
        print(e)
        error='处理数据时出错'
        errors.append(error)
        out_except.append(str(e))
        print('处理数据时出错')
    DATA=np.array(DATA,dtype='float64')
    print(len(DATA))
    #print(DATA)
    try:
        DATA=DATA.reshape(int(len(DATA)/15),15)
    except Exception as e:
        print(e)
        print('数据不完整')
        error='数据不完整'
        errors.append(error)
        out_except.append(str(e))
    #print(DATA)
    try:
        DATA=pd.DataFrame(DATA,columns=['realload','imagload','f0_drive','V1[V]','I1[uA]','V2[V]','I2[mA]','a1_real','a1_imag','b1_real','b1_imag','a2_real','a2_imag'
                                        ,'b2_real','b2_imag'])
        DATA.to_csv('DATA_test.csv',sep=',')
    except Exception as e:
        print(e)
        print('DATA转换成DataFrame时出现错误')
        error='DATA转换成DataFrame时出现错误'
        errors.append(error)
        out_except.append(str(e))
    #转换阻抗值格式
    try:
        loads=DATA.iloc[:,0:2].values
        load_data_mag=[]
        load_data_phase=[]
        for i in loads:
            mag=xy_to_Magphase_Mag(i[0],i[1])
            phase=xy_to_Magphase_phase(i[0],i[1])
            load_data_mag.append(mag)
            load_data_phase.append(phase)
        load_data_mag=pd.Series(load_data_mag)
        load_data_phase=pd.Series(load_data_phase)
        load_data_Gammma=pd.DataFrame(load_data_mag,columns=['Gamma'])
        load_data_Phase=pd.DataFrame(load_data_phase,columns=['Phase'])
        #print(load_data_Gammma)
        DATA=pd.concat([DATA,load_data_Gammma],axis=1)
        DATA=pd.concat([DATA,load_data_Phase],axis=1)
    except Exception as e:
        print(e)
        print('转换阻抗格式出错')
        error='转换阻抗格式出错'
        errors.append(error)
        out_except.append(str(e))
    #计算Pav
    try:
        Pav_data=[]
        a1_data=DATA.iloc[:,7:9].values
        #print(a1_data)
        for i in a1_data:
            Pav=calculate_Pav(i[0],i[1])
            Pav_data.append(Pav)
        Pav_data=pd.Series(Pav_data)
        Pav_data=pd.DataFrame(Pav_data,columns=['Pav(dBm)'])
        DATA=pd.concat([DATA,Pav_data],axis=1)
        #计算Pout
        a2_b2_data=DATA.iloc[:,11:15].values
        #print(a2_b2_data)
        Pout_data=[]
        for i in a2_b2_data:
            Pout=calculate_Pout(i[0],i[1],i[2],i[3])
            Pout_data.append(Pout)
        Pout_data=pd.Series(Pout_data)
        Pout_data=pd.DataFrame(Pout_data,columns=['Pout(dBm)'])
        DATA=pd.concat([DATA,Pout_data],axis=1)
    except Exception as e:
        print(e)
        print('计算Pav，Pout时出错')
        error='计算Pav，Pout时出错'
        errors.append(error)
        out_except.append(str(e))
    try:
        #计算PAE
        V2_data=DATA.iloc[:,5:7]
        b1_data=DATA.iloc[:, 9:11]
        V2_Pout_data=pd.concat([Pout_data,V2_data],axis=1)
        V2_Pout_data=pd.concat([V2_Pout_data,b1_data],axis=1)
        V2_Pout_data=pd.concat([V2_Pout_data,Pav_data],axis=1)
        V2_Pout_data=V2_Pout_data.values
        PAE_data=[]
        #print(V2_Pout_data)
        for i in V2_Pout_data:
            print(i[0],i[1],i[2],i[3], i[4], i[5])
            PAE=calculate_PAE(i[0],i[1],i[2],i[3],i[4],i[5])
            PAE_data.append(PAE)
        PAE_data=pd.Series(PAE_data)
        PAE_data=pd.DataFrame(PAE_data,columns=['PAE'])
        DATA=pd.concat([DATA,PAE_data],axis=1)
    except Exception as e:
        print(e)
        print('计算PAE出错')
        error='计算PAE出错'
        errors.append(error)
        out_except.append(str(e))
    try:
        #计算Gain
        Pav_data.columns=['P']
        Pout_data.columns=['P']
        Gain=Pout_data-Pav_data
        Gain.columns=['Gain']
        #print(Gain)
        DATA=pd.concat([DATA,Gain],axis=1)
    except Exception as e:
        print(e)
        print('计算Gain出错')
        error='计算Gain出错'
        errors.append(error)
        out_except.append(str(e))
    #print(load_data_phase)
    #simple_data=DATA.loc[DATA.f0_drive==-14,['Gamma','Phase','Pav(dBm)','Pout(dBm)','PAE','Gain','V1','I1','V2','I2']]
    try:
        #计算f0的数值和区间
        find_f0=DATA['realload']
        a=find_f0.value_counts()
        b=np.array(a)
        count=int(b[0])
        f0_drive_data=DATA['f0_drive']
        f0_drive_data=f0_drive_data.iloc[0:0+count]
        f0_drive_data=np.array(f0_drive_data)
        print(f0_drive_data)
    except Exception as e:
        print(e)
        print('计算f0_drive数值区间时出错')
        error='计算f0_drive数值区间时出错'
        errors.append(error)
        out_except.append(str(e))
    #freq=1.8
    try:
        #生成lpd文件
        for f0_drive in f0_drive_data:
            output_data=DATA.loc[DATA.f0_drive==f0_drive,['Gamma','Phase','Pav(dBm)','Pout(dBm)','Gain','V1','I1','V2','I2','PAE']]
            output_data=output_data.values
            #print(output_data)
            outfilename = savename_dir+'/'+freq_data + '_' +'f0drive'+str(f0_drive)+Dev+'.lpd'
            with open(outfilename, 'w') as outfile:
                outfile.write("! Source Pull Measurement Data\n")
                outfile.write("! Source Frequencies = F0: " + freq_data + "GHz\n")
                outfile.write("!--------------------------------------------------------\n")
                outfile.write("Point  Gamma  Phase[deg]  Pin[dBm]  Pout[dBm]  Gain[dB]  V1[V]  I1[uA]  V2[V]  I2[mA]  PAEffWaves[%]\n")
                point=0
                for row in output_data:
                    col=len(row)
                    outfile.write(str(point).zfill(3))
                    for i in range(col):
                        outfile.write("     "+str(row[i]))
                    outfile.write("\n")
                    point=point+1
            outfile.close()
            DATA.to_csv(savename_dir+'/'+'DATA.csv',sep=',')
    except Exception as e:
        print(e)
        print('生成lpd文件时出错')
        error='生成lpd文件时出错'
        errors.append(error)
        out_except.append(str(e))

    #print(out_except)
    #print(errors)

    with open('errorfile.txt', 'w') as errorfile:

        a=0
        for i in errors:
            #errorfile.write(error[a])
            #errorfile.write("\n")
            errorfile.write(i)
            print(i)
            errorfile.write("\n")
            #a=a+1
        for t in out_except:
             errorfile.write(t)
             errorfile.write("\n")

    return errors

#converter_data(filename,'D:')
