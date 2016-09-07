%%%% data to be analyzed are in txt format %%%%
%%%% they are obtained by ExtractDataForCounting.m %%%%
clear
clc
% matlabpool local 4;
tic;
DIR = '../../Data/count/2016-5-8-22/';
dirlist = dir(DIR);
postfix = '*.txt';

for k = 1 : length(dirlist)
    if (dirlist(k).isdir)
        if(strcmp(dirlist(k).name,'.') || strcmp(dirlist(k).name,'..'))  %% exclude dir . and ..
            continue;
        else
            subDIR = strcat(strcat(DIR,dirlist(k).name),'/');    %% get subdir
        end
    end
    
    
    list = dir(fullfile(subDIR,postfix));  %% list all files in the subdir
    
    rssivarfile = strcat(subDIR,'rssiVar.txt');   %% var file of rssi
    disp(rssivarfile);
    fp1 = fopen(rssivarfile,'w');
    
    
    for j = 1 : length(list)   %% ergodic all the files in the dir
        if (~list(j).isdir)
            name = strcat(subDIR, list(j,1).name);  %% add absolute dir to filename
            [path,filename,format] = fileparts(name);
            flag = strfind(filename,'_csialt');
            if(flag)   %% a file, not a dir

                %%%% first applying moving average filter to csialt data  %%%%
                smoothedfilename = strrep(filename,'_csialt','_csismoothed');
                smoothedfile = strcat(strcat(subDIR,smoothedfilename),'.txt');
                disp(smoothedfile);
                fp = fopen(smoothedfile,'w');                
                csialt = load(name);
                
                window_size = 5;
                [m,n] = size(csialt);
                smoothedcsialt = zeros(m,n);
                for i = 1 : n
                    smoothedcsialt(:,i) = smooth(csialt(:,i),window_size,'moving');
                end
%{                
                for i = 1 : m
                    fprintf(fp,'%.4f  ',smoothedcsialt(i,:));
                    fprintf(fp,'\n');
                end
%}
                fclose(fp);
                
                %%%% get overall variance of csi amplitude %%%%
                varfilename = strrep(filename,'_csialt','_csivarall');
                varfile = strcat(strcat(subDIR,varfilename),'.txt');
                disp(varfile);
                fp = fopen(varfile,'w');
%                 csialt = load(name);
                VAR = var(csialt,1,1);           %% calculate the overall var for all the data
                fprintf(fp,'%.4f  ',VAR(1:30));  %% save the var according to three diffrent antenna
                fprintf(fp,'\n');                %% every line correspond to an antenna
                fprintf(fp,'%.4f  ',VAR(31:60));
                fprintf(fp,'\n');
                fprintf(fp,'%.4f  ',VAR(61:90));
                fprintf(fp,'\n');
                fclose(fp);
                
                %%%% get overall mean of csi amplitude %%%%
                meanfilename = strrep(filename,'_csialt','_csimeanall');
                meanfile = strcat(strcat(subDIR,meanfilename),'.txt');
                disp(meanfile);
                fp = fopen(meanfile,'w');
                csialt = load(name);
                MEAN = mean(csialt);              %% calculate the overall mean for all the data
                fprintf(fp,'%.4f  ',MEAN(1:30));  %% save the mean according to three diffrent antenna
                fprintf(fp,'\n');                 %% every line correspond to an antenna
                fprintf(fp,'%.4f  ',MEAN(31:60));
                fprintf(fp,'\n');
                fprintf(fp,'%.4f  ',MEAN(61:90));
                fprintf(fp,'\n');
                fclose(fp);
                
                %%%% get variance of segmented csi amplitude data %%%%
                segment_len = 1000;    %% segment length
                slide_distance = 200;
                
                segvarfilename = strrep(filename,'_csialt','_csivarseg');
                segvarfile = strcat(strcat(subDIR,segvarfilename),'.txt');
                disp(segvarfile);
                fp = fopen(segvarfile,'w');
                
                [m, n] = size(csialt);    %%%  here we can use raw csi amplitude data or smoothed
                                                  %%%  or smoothed csi amplitude data 
%                for i = 1 : segment_len/2 : m-segment_len
                for i = 1 : slide_distance : m-segment_len
                    VAR = var(csialt(i:i+segment_len,:),1,1);   %% cal the var of a data segment
                    fprintf(fp,'%.4f  ',VAR);           %% save the var to one line
                    fprintf(fp,'\n');
                end
                fclose(fp);

                
                %%%% get mean of segmented csi amplitude data %%%%
                segmeanfilename = strrep(filename,'_csialt','_csimeanseg');
                segmeanfile = strcat(strcat(subDIR,segmeanfilename),'.txt');
                disp(segmeanfile);
                fp = fopen(segmeanfile,'w');
                
                [m, n] = size(smoothedcsialt);
                for i = 1 : segment_len/2 : m-segment_len
                    MEAN = mean(smoothedcsialt(i:i+segment_len,:));   %% calculate the mean of a data segment
                    fprintf(fp,'%.4f  ',MEAN);            %% save the mean to one line
                    fprintf(fp,'\n');
                end
                fclose(fp);                
                
                %%%% get var and mean of the variance of segmented csi amplitude data %%%%
                varmean_Of_segvarfilename = strrep(filename,'_csialt','_var&meanOfsegvar');
                varmean_Of_segvarfile = strcat(strcat(subDIR,varmean_Of_segvarfilename),'.txt');
                disp(varmean_Of_segvarfile);
                fp = fopen(varmean_Of_segvarfile,'w');
                
                segvar = load(segvarfile);
                varOfsegvar = var(segvar,1,1);    %% var of the segmented data's variance
                meanOfsegvar = mean(segvar);      %% mean of the segmented data's variance
                [m,n] = size(varOfsegvar);
                for i = 1 : n
                    fprintf(fp,'%.4f  %.4f\n',meanOfsegvar(i),varOfsegvar(i));
                end
                fclose(fp);
                
%{                
                %%%%      get flucation of csi amplitude        %%%%                
                flufilename = strrep(filename,'_csialt','_csiflu');
                flufile = strcat(strcat(subDIR,flufilename),'.txt');
                disp(flufile)
                fp = fopen(flufile,'w');
                
                [m, n] = size(csialt);
                csialt1 = csialt;
                csialt1(m+1,:) = 0;
                csialt2 = csialt;
                csialt2(m+1,:) = 0;
                i = m+1;
                while i >1
                    csialt2(i,:) = csialt2(i-1,:);
                    i=i-1;
                end
                csiflu = csialt1 - csialt2;
                csiflu(m+1,:) = [];
                for i = 1 : m
                    fprintf(fp, '%.4f  ', csiflu(i,:));   
                    fprintf(fp, '\n');
                end
                fclose(fp);
%}
%{                
                %%%%   get maximum eigen value of correction mat   %%%%
                eigfilename = strrep(filename,'_csialt','_csieig');
                eigfile = strcat(strcat(subDIR,eigfilename),'.txt');
                disp(eigfile)
                fp = fopen(eigfile,'w');

                [m,n] = size(csialt);
                csialt1 = csialt(slide_distance:end,:);
                maxeig = 1 : 1 : m-slide_distance;
                
%                 for i = 1 : slide_distance : m - slide_distance
%                     cor= corrcoef(csialt(i,:),csialt(i+slide_distance,:));
%                     maxeig = [maxeig,max(eig(cor))];
%                 end
                for i = 1 : 1 : m - slide_distance
                    cor= corrcoef(csialt(i,:),csialt1(i,:));
                    maxeig(i) = max(eig(cor));
                end
                
                for i = 1 : slide_distance :m - 2*slide_distance
                    segeig = maxeig(i:i+slide_distance);
                    %%%%   here we can use the minimum value, median value, mean value or other
                    %%%%   value as the eigen value of that segment
                    eigvalue = mean(segeig);   
                    fprintf(fp, '%.4f\n', eigvalue);
                end
                fclose(fp);
%}
            end

            %%%%   get variance of rssi    %%%%
            flag = strfind(filename,'_rssi');
            if(flag)
                rssi = load(name);
                rssiVar = var(rssi,1,1);
                fprintf(fp1,'%.4f  ',rssiVar);
                fprintf(fp1,'\n');
            end
        end
    end
end
fclose(fp1);
t = toc;
% matlabpool close;




