function testdatasend_2(obj,~)

fp=fopen('testdata12.txt','ab');

p=200;
str='';
tcpipClient = obj.UserData;
tic;
%csi1
for i=1 : 4 : p-1
    A = randn(2,3,30) + 1i*randn(2,3,30);
    csi1 = squeeze(A(1,:,:));   %3*30 complex
    rel = real(csi1);  %3*30 double
    ima = imag(csi1);  %3*30 double
    [x,y] = size(csi1);  %x=3 y=30
    X = 0; Y = 0;
    sendstr = '';
    while X < x  %  ָ��X���ŵ�
            X = X + 1;   
           % fprintf(fp,'%.4f  ',rel(X,:)); %��X���ŵ���30�����ز���ʵֵ
           % fprintf(fp,'%.4f  ',ima(X,:));
            getstr=testdata_send(rel,ima,X);
            sendstr = [sendstr,';',getstr];%������¼                    
    end  
    %fprintf(fp,'\n');
   % str=sprintf('%s,%s',str,sendstr);   
    %disp('send string successfully'); 
    str = [str,',',sendstr];
end
%fwrite(tcpipClient, str);  %ÿ�뷢��p/4����¼

%csi2
for i=1 : 4 : p-1
    A = randn(2,3,30) + 1i*randn(2,3,30);
    csi1 = squeeze(A(1,:,:));   %3*30 complex
    rel = real(csi1);  %3*30 double
    ima = imag(csi1);  %3*30 double
    [x,y] = size(csi1);  %x=3 y=30
    X = 0; Y = 0;
    sendstr = '';
    while X < x  %  ָ��X���ŵ�
            X = X + 1;   
            %fprintf(fp,'%.4f  ',rel(X,:)); %��X���ŵ���30�����ز���ʵֵ
           % fprintf(fp,'%.4f  ',ima(X,:));
            getstr=testdata_send(rel,ima,X);
            sendstr = [sendstr,';',getstr];%������¼                    
    end  
   % fprintf(fp,'\n');
    % str=sprintf('%s,%s',str,sendstr);   
    str = [str,',',sendstr];
    %disp('send string successfully');    
end
%fwrite(tcpipClient, str);  %ÿ�뷢��p/4����¼

%csi3
for i=1 : 4 : p-1
    A = randn(2,3,30) + 1i*randn(2,3,30);
    csi1 = squeeze(A(1,:,:));   %3*30 complex
    rel = real(csi1);  %3*30 double
    ima = imag(csi1);  %3*30 double
    [x,y] = size(csi1);  %x=3 y=30
    X = 0; Y = 0;
    sendstr = '';
    while X < x  %  ָ��X���ŵ�
            X = X + 1;   
           % fprintf(fp,'%.4f  ',rel(X,:)); %��X���ŵ���30�����ز���ʵֵ
           % fprintf(fp,'%.4f  ',ima(X,:));
            getstr=testdata_send(rel,ima,X);
            sendstr = [sendstr,';',getstr];%������¼                    
    end  
   % fprintf(fp,'\n');
   % str=sprintf('%s,%s',str,sendstr);   
    %disp('send string successfully');    
    str = [str,',',sendstr];
end
%fwrite(tcpipClient, str);  %ÿ�뷢��p/4����¼

%csi4
for i=1 : 4 : p-1
    A = randn(2,3,30) + 1i*randn(2,3,30);
    csi1 = squeeze(A(1,:,:));   %3*30 complex
    rel = real(csi1);  %3*30 double
    ima = imag(csi1);  %3*30 double
    [x,y] = size(csi1);  %x=3 y=30
    X = 0; Y = 0;
    sendstr = '';
    while X < x  %  ָ��X���ŵ�
            X = X + 1;   
           % fprintf(fp,'%.4f  ',rel(X,:)); %��X���ŵ���30�����ز���ʵֵ
           % fprintf(fp,'%.4f  ',ima(X,:));
            getstr=testdata_send(rel,ima,X);
           % sendstr = sprintf('%s;%s',sendstr,getstr);%������¼   
            sendstr = [sendstr,';',getstr];
    end  
    %fprintf(fp,'\n');
    %str=sprintf('%s,%s',str,sendstr);   
    %disp('send string successfully'); 
    str = [str,',',sendstr];
end
fprintf(fp,str);
fwrite(tcpipClient, str);  %ÿ�뷢��p/4����¼
t = toc;
fprintf('DataProcess cost time: %f\n',t);

end







    