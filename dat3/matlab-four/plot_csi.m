csi_trace0 = read_bf_file('../../Data/count/2016-4-20/noperson/noperson1.dat');
csi_trace1 = read_bf_file('../../Data/count/2016-4-20/oneperson/oneperson1.dat');
csi_trace2 = read_bf_file('../../Data/count/2016-4-20/twoperson/twoperson1.dat');
csi_trace3 = read_bf_file('../../Data/count/2016-4-20/threeperson/threeperson1.dat');

m = 40;

figure(1)
color = {'y';'m';'c';'r';'g';'b';'w';'k'};
for i = 1:m
    csi_entry0 = csi_trace0{i};
    
    if ~isempty(csi_entry0);
        [r, s, t] = size(csi_entry0.csi);
        csi = get_scaled_csi(csi_entry0);
        plot(db(abs(squeeze(csi(1,:,:)).')))
%         drawnow;
        hold on;
        legend('RX Antenna A', 'RX Antenna B', 'RX Antenna C', 'Location', 'SouthEast' )
        xlabel('Subcarrier index')
        ylabel('SNR [dB]') 
    
%%%%%%%%%%%%%%%ploting csi's real and image part%%%%%%%%%%%%%%%%
%    for j = 1:29
%{
        j = 5;
        csi1 = csi(1,1,j);
        x = real(csi1);
        y = imag(csi1);
        k = mod(j,8);
        param = strcat(char(color(k+1)),'*');
        plot(x,y,param)
        hold on
%}
%    end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %        end
     %   end
    end
end

figure(2)
for i = 1:m
    csi_entry1 = csi_trace1{i}; 
    
    if ~isempty(csi_entry1);
        [r, s, t] = size(csi_entry1.csi);
        csi = get_scaled_csi(csi_entry1);
        plot(db(abs(squeeze(csi(1,:,:)).')))
%         drawnow;
        hold on;
        legend('RX Antenna A', 'RX Antenna B', 'RX Antenna C', 'Location', 'SouthEast' )
        xlabel('Subcarrier index')
        ylabel('SNR [dB]')
    end 
end

figure(3)
for i = 1:m
    csi_entry2 = csi_trace2{i}; 
    
    if ~isempty(csi_entry2);
        [r, s, t] = size(csi_entry2.csi);
        csi = get_scaled_csi(csi_entry2);
        plot(db(abs(squeeze(csi(1,:,:)).')))
%         drawnow;
        hold on;
        legend('RX Antenna A', 'RX Antenna B', 'RX Antenna C', 'Location', 'SouthEast' )
        xlabel('Subcarrier index')
        ylabel('SNR [dB]')
    end 
end

figure(4)
for i = 1:m
    csi_entry3 = csi_trace3{i};
    
    if ~isempty(csi_entry3);
        [r, s, t] = size(csi_entry3.csi);
        csi = get_scaled_csi(csi_entry3);
        plot(db(abs(squeeze(csi(1,:,:)).')))
%         drawnow;
        hold on;
        legend('RX Antenna A', 'RX Antenna B', 'RX Antenna C', 'Location', 'SouthEast' )
        xlabel('Subcarrier index')
        ylabel('SNR [dB]')
    end  
end





