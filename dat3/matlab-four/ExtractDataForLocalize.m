clear
clc
DIR = '../../Data/loc/2016-5-13-21/';
dirlist1 = dir(DIR);     %%  Test_data & Trainning_data
postfix = '*.dat';

for k = 1 : length(dirlist1)
    if (dirlist1(k).isdir)
        if(strcmp(dirlist1(k).name,'.') || strcmp(dirlist1(k).name,'..'))   %% exclude dir . and ..
            continue;
        else
            subDIR1 = strcat(strcat(DIR,dirlist1(k).name),'/');   
            disp(subDIR1);
            dirlist2 = dir(subDIR1);      %% point0 & point1 & point2 & point3
            for m = 1 : length(dirlist2)
                if (dirlist2(m).isdir)
                    if(strcmp(dirlist2(m).name,'.') || strcmp(dirlist2(m).name,'..'))   %% exclude dir . and ..
                        continue;
                    else
                        subDIR2 = strcat(strcat(subDIR1,dirlist2(m).name),'/');
                        disp(subDIR2);
                        
                        list = dir(fullfile(subDIR2,postfix));   %% dat files
                        for j = 1 : length(list)
                            name1 = strcat(subDIR2, list(j,1).name);
                            disp(name1);
                            [path,filename,format] = fileparts(name1);
                            name2 = strcat(strcat(subDIR2,filename),'.txt');
                            disp(name2);

                            csi_trace=read_bf_file(name1);
                            [p,q]=size(csi_trace);
                            fp=fopen(name2,'w');

                            i=0;
                            while i<p
                                i=i+1;
                                csi_entry=csi_trace{i};
                                if ~isempty(csi_entry)
                                    csi = get_scaled_csi(csi_entry);
                                    csi1 = squeeze(csi(1,:,:));

                                    rel = real(csi1);
                                    ima = imag(csi1);
                                    %altu = abs(csi1);
                                    %pha = atan(rel./(ima+0.0000001));
                                    [x,y] = size(csi1);
                                    X = 0; Y = 0;

                                    while X < x
                                        X = X + 1;
                                        fprintf(fp,'%.4f  ',rel(X,:));
                                        fprintf(fp,'%.4f  ',ima(X,:));
                                    end  
                                    fprintf(fp,'\n');
                                end
                            end
                            fclose(fp);
                        end
                    end
                end
            end
        end
    end

end

%{
for point = 0:3
    path = strcat(strcat('../../Data/loc/2016-3-10/trainning_data/point',num2str(point)),'/');
    file_name1 = 'csinoperson.dat';
    file_name2 = 'CSInoperson.txt';
    name1 = strcat(path,file_name1);
    name2 = strcat(path,file_name2);
    csi_trace=read_bf_file(name1);
    [p,q]=size(csi_trace);
    fp=fopen(name2,'w');

    i=0;
    count=0;
    while i<p
        i=i+1;
        csi_entry=csi_trace{i};
        if ~isempty(csi_entry)
            csi = get_scaled_csi(csi_entry);
            csi1 = csi(1,:,:);

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
                        fprintf(fp,'%.4f  ',rel);
                        fprintf(fp,'%.4f  ',ima);
                    end
                end
            end
            fprintf(fp,'\n');
         end
    end
    fclose(fp);
end
%}