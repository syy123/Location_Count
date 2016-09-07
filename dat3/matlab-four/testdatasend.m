function testdatasend(obj,~)

fp=fopen('testdata13.txt','ab');

p=200;
str='';
tcpipServer = obj.UserData;
tic;
for i=1 : 4 : p-1
    A = randn(2,3,30) + 1i*randn(2,3,30);
    csi1 = squeeze(A(1,:,:));   %3*30 complex
    rel = real(csi1);  %3*30 double
    ima = imag(csi1);  %3*30 double
    [x,y] = size(csi1);  %x=3 y=30
    X = 0; Y = 0;
    sendstr = '';
    while X < x  %  指第X个信道
            X = X + 1;   
            fprintf(fp,'%.4f  ',rel(X,:)); %第X个信道的30个子载波的实值
            fprintf(fp,'%.4f  ',ima(X,:));
            getstr=testdata_send(rel,ima,X);
            sendstr = sprintf('%s;%s',sendstr,getstr);%单条记录                    
    end  
    fprintf(fp,'\n');
    str=sprintf('%s,%s',str,sendstr);   
    %disp('send string successfully');    
end
fwrite(tcpipServer, str);  %每秒发送p/4条记录
t = toc;
fprintf('DataProcess cost time: %f\n',t);
end







    