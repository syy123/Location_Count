clear
clc
result_file = '../../RawData/2016-3-10/result_file.txt';
fp1 = fopen(result_file,'w');
for point = 0:3
    %fprintf(fp1,'%s:\n',strcat('point',num2str(point)));
    for m=0:3
        for n=0:5
            path = strcat(strcat('../../RawData/2016-3-10/trainning_data/point',num2str(point)),'/');
            file_name1 = strcat(strcat(strcat('RSSI',num2str(2*n)),num2str(2*m)),'.txt');
            name1 = strcat(path,file_name1);
            csi_trace=read_bf_file(name1);
            [p,q]=size(csi_trace);
            fp=fopen(name1,'rt+');
            [rssi,count] = fscanf(fp,'%f');
            
           rssi_mean = mean(rssi);
           rssi_var = std(rssi) * std(rssi);
           fprintf(fp1,'%.3f     %.3f \n',rssi_mean,rssi_var);
            
            fclose(fp);
        end
    end
end

%fprintf(fp1,'%s:\n','no person');
for point = 0:3
    path = strcat(strcat('../../RawData/2016-3-10/trainning_data/point',num2str(point)),'/');
    file_name1 = 'RSSInoperson.txt';
    name1 = strcat(path,file_name1);
    csi_trace=read_bf_file(name1);
    [p,q]=size(csi_trace);
    fp=fopen(name1,'rt+');
    [rssi,count] = fscanf(fp,'%f');
    
   rssi_mean = mean(rssi);
   rssi_var = std(rssi) * std(rssi);
   fprintf(fp1,'%.3f     %.3f \n',rssi_mean,rssi_var);
    
   fclose(fp);
end


data = load(result_file);
mean(data(1:24,1:2),1)
data(97,1:2)
mean(data(25:48,1:2),1)
data(98,1:2)
mean(data(49:72,1:2),1)
data(99,1:2)
mean(data(73:96,1:2),1)
data(100,1:2)




