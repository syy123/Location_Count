%%%% extract data for analyzation %%%%
%%%% extracted data include: *csialt.txt, *csipha.txt, *rssi.txt %%%%
clear
clc
DIR = '../../Data/count/2016-5-8-22/';
dirlist = dir(DIR);
postfix = '*.dat';  % % find data with postfix '.dat', this is raw data, extracted data are saved as '.txt'

for k = 1 : length(dirlist)
    if (dirlist(k).isdir)
        if(strcmp(dirlist(k).name,'.') || strcmp(dirlist(k).name,'..'))   %% exclude dir . and ..
            continue;
        else
            subDIR = strcat(strcat(DIR,dirlist(k).name),'/');    %% get subdir
             disp(subDIR);
        end
    end

    list = dir(fullfile(subDIR,postfix));   %% find data with postfix '.dat'

    for j = 1 : length(list)  %% ergodic all the files in the subdir
        if (~list(j).isdir)
            name = strcat(subDIR, list(j,1).name);
            disp(name);
            [path,filename,format] = fileparts(name);

            csialtfile = strcat(strcat(strcat(subDIR,filename),'_csialt'),'.txt');
            disp(csialtfile);
            fp1 = fopen(csialtfile,'w');
            csiphafile = strcat(strcat(strcat(subDIR,filename),'_csipha'),'.txt');
            disp(csiphafile);
            fp2 = fopen(csiphafile,'w');
            rssifile = strcat(strcat(strcat(subDIR,filename),'_rssi'),'.txt');
            disp(rssifile)
            fp3 = fopen(rssifile,'w');

            csi_trace=read_bf_file(name);
            [p,q]=size(csi_trace);
            i=0;
            while i<p
                i=i+1;
                csi_entry=csi_trace{i};
                if ~isempty(csi_entry)
                    %%%%%%%%%%%%%%%get rssi%%%%%%%%%%%%%%%
                    csitmp = csi_entry.csi;
                    csi_sq = csitmp .* conj(csitmp);
                    csi_pwr = sum(csi_sq(:));
                    rssi_pwr = dbinv(get_total_rss(csi_entry));
                    rssi_dbm=10*log10(rssi_pwr);
                    fprintf(fp3,'%.4f \n',rssi_dbm);
                    
                    %%%%%%%%%%%%%%get csi%%%%%%%%%%%%%%%%
                    csi = get_scaled_csi(csi_entry);
                    csi1 = csi(1,:,:);

                    rel = real(csi1);
                    ima = imag(csi1);
                    altu = abs(csi1);
                    pha = atan(rel./(ima+0.0000001));
                    [x,y,z] = size(csi1);
                    X = 0; Y = 0; Z = 0;
                    
                    while Y < y
                        Y = Y + 1;
                        fprintf(fp1,'%.4f  ',altu(1,Y,:));
                        fprintf(fp2,'%.4f  ',pha(1,Y,:));
                    end                                     

%{
                    [x,y,z] = size(csi1);
                        X = 0; Y = 0; Z = 0;
                        while X < x
                            X = X + 1;
                            Z = 0;
                            Y = 0;
                            while Y < y
                                Y = Y + 1;
                                Z = 0;
                                while Z < z
                                    Z = Z + 1;
                                    csi1_elem = csi1(X,Y,Z);
                                    rel = real(csi1_elem);
                                    ima = imag(csi1_elem);
                                    altu = sqrt(rel*rel+ ima*ima);
                                    pha = atan(rel/(ima+0.00000001));
                                    fprintf(fp1,'%.4f  ',altu);
                                    fprintf(fp2,'%.4f  ',pha);
                                end
                            end
                        end
%}
                        fprintf(fp1,'\n');
                        fprintf(fp2,'\n');
                 end
            end 
            fclose(fp1);
            fclose(fp2);
            fclose(fp3);
        end
    end
end

