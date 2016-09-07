function testdatasend_3(obj,~)


global countInt;
p=200;
Array1=[];
Array2=[];
Array3=[];
Array4=[];
tcpipClient = obj.UserData;
tic;
%csi1
for i=1 : p/4
    A = randn(2,3,30) + 1i*randn(2,3,30);
    csi1 = squeeze(A(1,:,:));   %3*30 complex
    rel = real(csi1);  %3*30 double
    ima = imag(csi1);  %3*30 double
    [x,y] = size(csi1);  %x=3 y=30
    X = 0;
    sendArray=[];
    while X < x  %  指第X个信道
            X = X + 1;   
           % fprintf(fp,'%.4f  ',rel(X,:)); %第X个信道的30个子载波的实值
           % fprintf(fp,'%.4f  ',ima(X,:));
            sendArray=[sendArray,rel(X,:),ima(X,:)];
    end  
    %fwrite(tcpipClient,sendArray,'float');
    Array1=[Array1,sendArray];
end
% fwrite(fp,Array1,'float');
% fprintf(fp,'%.4f  ',Array1);
% fwrite(fp,'hello1','char');
for i=1 : p/4
    A = randn(2,3,30) + 1i*randn(2,3,30);
    csi1 = squeeze(A(1,:,:));   %3*30 complex
    rel = real(csi1);  %3*30 double
    ima = imag(csi1);  %3*30 double
    [x,y] = size(csi1);  %x=3 y=30
    X = 0;
    sendArray=[];
    while X < x  %  指第X个信道
            X = X + 1;   
           % fprintf(fp,'%.4f  ',rel(X,:)); %第X个信道的30个子载波的实值
           % fprintf(fp,'%.4f  ',ima(X,:));
            sendArray=[sendArray,rel(X,:),ima(X,:)];
    end  
    %fwrite(tcpipClient,sendArray,'float');   
    Array2=[Array2,sendArray];
end
% fwrite(fp,Array1,'float');
% fprintf(fp,'%.4f  ',Array2);
% fwrite(fp,'hello2','char');
for i=1 : p/4
    A = randn(2,3,30) + 1i*randn(2,3,30);
    csi1 = squeeze(A(1,:,:));   %3*30 complex
    rel = real(csi1);  %3*30 double
    ima = imag(csi1);  %3*30 double
    [x,y] = size(csi1);  %x=3 y=30
    X = 0;
    sendArray=[];
    while X < x  %  指第X个信道
            X = X + 1;   
           % fprintf(fp,'%.4f  ',rel(X,:)); %第X个信道的30个子载波的实值
           % fprintf(fp,'%.4f  ',ima(X,:));
            sendArray=[sendArray,rel(X,:),ima(X,:)];
    end  
    %fwrite(tcpipClient,sendArray,'float');
    Array3=[Array3,sendArray];
end
% fwrite(fp,Array1,'float');
% fprintf(fp,'%.4f  ',Array3);
% fwrite(fp,'hello3','char');
for i=1 : p/4
    A = randn(2,3,30) + 1i*randn(2,3,30);
    csi1 = squeeze(A(1,:,:));   %3*30 complex
    rel = real(csi1);  %3*30 double
    ima = imag(csi1);  %3*30 double
    [x,y] = size(csi1);  %x=3 y=30
    X = 0;
    sendArray=[];
    while X < x  %  指第X个信道
            X = X + 1;   
           % fprintf(fp,'%.4f  ',rel(X,:)); %第X个信道的30个子载波的实值
           % fprintf(fp,'%.4f  ',ima(X,:));
            sendArray=[sendArray,rel(X,:),ima(X,:)];
    end  
    %fwrite(tcpipClient,sendArray,'float');
    Array4=[Array4,sendArray];
end

headChar = 255;
modeChar = 48;   %表示 \x30,   print '\x30' 显示为 0
fwrite(tcpipClient,headChar);
fwrite(tcpipClient,headChar);
fwrite(tcpipClient,headChar);
fwrite(tcpipClient,headChar);   %发送4个字节\xFF ,表示帧头
fwrite(tcpipClient,modeChar);   %发送1个字节\x00 ,表示帧模式
fwrite(tcpipClient,countInt,'int');  %发送1个int ,表示帧时序
countInt = countInt + 1;
%dataLength = (length(Array1)+length(Array2)+length(Array3)+length(Array4))*4+4; %144004
dataLength = (length(Array1)+length(Array2))*4+2;   %72002
fwrite(tcpipClient,dataLength,'int');  %发送1个int ,表示数据域长度   
pointCSIcount = p/4;           
fwrite(tcpipClient,pointCSIcount,'int'); %发送1个int ,表示每个监测点的CSI数量
pointOrder = 49;
fwrite(tcpipClient,pointOrder);   %发送1个字节 ,表示第几个监测点
fwrite(tcpipClient,Array1,'float');   %发送数据 ,表示第几个监测点的CSI数据
pointOrder = pointOrder + 1;
fwrite(tcpipClient,pointOrder);
fwrite(tcpipClient,Array2,'float'); 
% pointOrder = pointOrder + 1;
% fwrite(tcpipClient,pointOrder);
% fwrite(tcpipClient,Array3,'float'); 
% pointOrder = pointOrder + 1;
% fwrite(tcpipClient,pointOrder);
% fwrite(tcpipClient,Array4,'float');   %正常情况下 一帧的长度为144021字节

t = toc;
fprintf('DataProcess cost time: %f\n',t);

end







    