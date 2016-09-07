csi_trace = read_bf_file('../../RawData/2016-3-10/trainning_data/point0/csi00.dat');
[m , n] = size(csi_trace);
%{
figure(2)
for i = 1:m
    csi_entry = csi_trace{i};
    if ~isempty(csi_entry);
        [r, s, t] = size(csi_entry.csi);
        csi = get_scaled_csi(csi_entry);
        plot(db(abs(squeeze(csi(1,:,:)).')))
        set(gca,'YTick',-20:20:40);
        hold on
        legend('RX Antenna A', 'RX Antenna B', 'RX Antenna C', 'Location', 'SouthEast' )
        xlabel('Subcarrier index')
        ylabel('SNR [dB]')
    end
end
%}
csi_t = [];
figure(3);
for i = 1:m
    csi_entry = csi_trace{i};
    if ~isempty(csi_entry);
        [r, s, t] = size(csi_entry.csi);
        csi = get_scaled_csi(csi_entry);
        csi_t(:,:,i) = db(abs(squeeze(csi(1,:,:)).'));
    end    
end
for i = 1:m
    stem3(csi_t(:,:,i));
    hold on;

end
