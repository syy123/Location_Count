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
    while X < x  %  ָ��X���ŵ�
            X = X + 1;   
           % fprintf(fp,'%.4f  ',rel(X,:)); %��X���ŵ���30�����ز���ʵֵ
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
    while X < x  %  ָ��X���ŵ�
            X = X + 1;   
           % fprintf(fp,'%.4f  ',rel(X,:)); %��X���ŵ���30�����ز���ʵֵ
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
    while X < x  %  ָ��X���ŵ�
            X = X + 1;   
           % fprintf(fp,'%.4f  ',rel(X,:)); %��X���ŵ���30�����ز���ʵֵ
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
    while X < x  %  ָ��X���ŵ�
            X = X + 1;   
           % fprintf(fp,'%.4f  ',rel(X,:)); %��X���ŵ���30�����ز���ʵֵ
           % fprintf(fp,'%.4f  ',ima(X,:));
            sendArray=[sendArray,rel(X,:),ima(X,:)];
    end  
    %fwrite(tcpipClient,sendArray,'float');
    Array4=[Array4,sendArray];
end

headChar = 255;
modeChar = 48;   %��ʾ \x30,   print '\x30' ��ʾΪ 0
fwrite(tcpipClient,headChar);
fwrite(tcpipClient,headChar);
fwrite(tcpipClient,headChar);
fwrite(tcpipClient,headChar);   %����4���ֽ�\xFF ,��ʾ֡ͷ
fwrite(tcpipClient,modeChar);   %����1���ֽ�\x00 ,��ʾ֡ģʽ
fwrite(tcpipClient,countInt,'int');  %����1��int ,��ʾ֡ʱ��
countInt = countInt + 1;
%dataLength = (length(Array1)+length(Array2)+length(Array3)+length(Array4))*4+4; %144004
dataLength = (length(Array1)+length(Array2))*4+2;   %72002
fwrite(tcpipClient,dataLength,'int');  %����1��int ,��ʾ�����򳤶�   
pointCSIcount = p/4;           
fwrite(tcpipClient,pointCSIcount,'int'); %����1��int ,��ʾÿ�������CSI����
pointOrder = 49;
fwrite(tcpipClient,pointOrder);   %����1���ֽ� ,��ʾ�ڼ�������
fwrite(tcpipClient,Array1,'float');   %�������� ,��ʾ�ڼ��������CSI����
pointOrder = pointOrder + 1;
fwrite(tcpipClient,pointOrder);
fwrite(tcpipClient,Array2,'float'); 
% pointOrder = pointOrder + 1;
% fwrite(tcpipClient,pointOrder);
% fwrite(tcpipClient,Array3,'float'); 
% pointOrder = pointOrder + 1;
% fwrite(tcpipClient,pointOrder);
% fwrite(tcpipClient,Array4,'float');   %��������� һ֡�ĳ���Ϊ144021�ֽ�

t = toc;
fprintf('DataProcess cost time: %f\n',t);

end







    