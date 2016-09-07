%{
csi_trace = read_bf_file('../../RawData/2016-3-10/trainning_data/point1/csi22.dat');
[m , n] = size(csi_trace);
figure(1)

for i = 1:m
    csi_entry = csi_trace{i};
    if ~isempty(csi_entry);
        csi = csi_entry.csi;
        csi_sq = csi .* conj(csi);
        csi_pwr = sum(csi_sq(:));
        rssi_pwr = dbinv(get_total_rss(csi_entry));
       rssi_dbm=10*log10(rssi_pwr);
       plot(i,rssi_dbm,'r-o');
       hold on
    end
end
%}
clear
clc
for m=0:3
    for n=0:5
        figure(m*n+1)
        for point = 0:3
            path = strcat(strcat('../../RawData/2016-3-10/trainning_data/point',num2str(point)),'/');
            file_name = strcat(strcat(strcat('RSSI',num2str(2*n)),num2str(2*m)),'.txt');
            name = strcat(path,file_name);
            rssi_data = load(name);
            subplot(4,1,point+1);
            plot(rssi_data,'b-o')
            if point == 0
                title(strcat(strcat('RSSI',num2str(2*n)),num2str(2*m)))
            end
        end
    end
end

figure(16)
for point = 0:3
            path = strcat(strcat('../../RawData/2016-3-10/trainning_data/point',num2str(point)),'/');
            file_name = 'RSSInoperson.txt';
            name = strcat(path,file_name);
            rssi_data = load(name);
            subplot(4,1,point+1);
            plot(rssi_data,'b-o')
            if point == 0
                title(file_name)
            end
end



