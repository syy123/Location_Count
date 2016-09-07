clear
clc
fig = 1;

Fs = 5;   %sample rate
Fp = 0.8;   %frequence of stop band
Fc = 0.1;   %frequence of pass band
N = 0;    %order of filter
Rp = 1;  %attenuation of  pass band
Rs = 60;  %attenuation of stop band
na = sqrt(10^(0.1*Rp)-1);
ea = sqrt(10^(0.1*Rs)-1);
N = ceil(log10(ea/na)/log10(Fp/Fc));

Wn = Fp * 2 / Fs;
[Bb, Ba] = butter(N, Wn, 'low');
[Bh, Bw] = freqz(Bb, Ba);
h = 20*log10(abs(Bh));
figure(1);
plot(Bw, h);



for m=0:3
    for n=0:5
%        for point = 0:3
            fig = fig + 1;
            figure(fig);
            point = 0;
            path = strcat(strcat('../../Data/loc/2016-3-10/trainning_data/point',num2str(point)),'/');
            file_name1 = strcat(strcat(strcat('csi',num2str(2*n)),num2str(2*m)),'.dat');
            file_name2 = strcat(strcat(strcat('CSI',num2str(2*n)),num2str(2*m)),'.txt');
            name1 = strcat(path,file_name1);
            name2 = strcat(path,file_name2);
             csi_trace=read_bf_file(name1);
             [p,q]=size(csi_trace);

             phase = [];
            i=0;
            while i<p
                i=i+1;
                csi_entry=csi_trace{i};
                if ~isempty(csi_entry)
                    csi = get_scaled_csi(csi_entry);
                    csi1 = csi(1,:,:);
                    csi1_elem = csi1(1,1,10);
                    rel = real(csi1_elem);
                    ima = imag(csi1_elem);
                    pha_ang = atan( ima / rel );
                    phase(i) = pha_ang;
                end
            end
            plot(phase,'o-b');
            fig = fig +1;
            figure(fig);
            filt_ph = filter(Bb, Ba, phase);
            plot(filt_ph,'o-b');
            
%        end
    end
end
