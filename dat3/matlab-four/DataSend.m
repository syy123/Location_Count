function DataSend(obj,~)
tic;
global countInt
global receivedData1
global receivedData2
global receivedData3
global receivedData4
display('process data...');
recordrate = 200;
singalrecordlen = 215;
processlen = recordrate * 5;    %% process 5s's data one time
% allArray=[];
Array1=[];
Array2=[];
Array3=[];
% Array4=[];
tcpipClient = obj.UserData;
flag1 = (length(receivedData1) > singalrecordlen*processlen);
flag2 = (length(receivedData2) > singalrecordlen*processlen);
flag3 = (length(receivedData3) > singalrecordlen*processlen);
% flag4 = (length(receivedData4) > singalrecordlen*processlen);
% if and(and(and(flag1, flag2), flag3), flag4)
if and(and(flag1, flag2),flag3)
%%%%%%%%%%    csi1.dat       %%%%%%%%%% 
%     datatoplot1 = receivedData1((end-recordrate*singalrecordlen+1):end);
    datatoplot1 = receivedData1(1:singalrecordlen*recordrate*1);
    csi_trace=read_bf_buffer(datatoplot1);
   % disp('read_bf_buffer csi1 completed.'); 
    [p,~]=size(csi_trace);
    receivedData1 = receivedData1(recordrate*singalrecordlen+1:end);
    for i = 1 : 4 : p-1  %p 200
        csi_entry=csi_trace{i};
        if ~isempty(csi_entry)
            csi = get_scaled_csi(csi_entry);     
            csi10 = squeeze(csi(1,:,:));   %3*30 complex
            rel = real(csi10);  %3*30 double
            ima = imag(csi10);  %3*30 double
            [x,y] = size(csi10);  %x=3 y=30
            X = 0;
            sendArray=[];
            while X < x  %  ��X���ŵ�
                X = X + 1;   
%                 fprintf(fp,'%.4f  ',rel(X,:));  %��X���ŵ���30�����ز���ʵֵ
%                 fprintf(fp,'%.4f  ',ima(X,:));
                sendArray=[sendArray,rel(X,:),ima(X,:)];                   
            end  
%             fprintf(fp,'\n');
            Array1=[Array1,sendArray];                   
        end
    end 
     

%%%%%%%%%%    csi2.dat       %%%%%%%%%% 
    datatoplot2 = receivedData2(1:singalrecordlen*recordrate*1);
%     datatoplot2 = receivedData2((end-recordrate*singalrecordlen+1):end);
    csi_trace=read_bf_buffer(datatoplot2);
   % disp('read_bf_buffer csi1 completed.'); 
    [p,~]=size(csi_trace);
    receivedData2 = receivedData2(recordrate*singalrecordlen+1:end);
    for i = 1 : 4 : p-1  %p 200
        csi_entry=csi_trace{i};
        if ~isempty(csi_entry)
            csi = get_scaled_csi(csi_entry);     
            csi10 = squeeze(csi(1,:,:));   %3*30 complex
            rel = real(csi10);  %3*30 double
            ima = imag(csi10);  %3*30 double
            [x,y] = size(csi10);  %x=3 y=30
            sendArray=[];
            X = 0;
            while X < x  %  ��X���ŵ�
                X = X + 1;   
%                 fprintf(fp,'%.4f  ',rel(X,:));  %��X���ŵ���30�����ز���ʵֵ
%                 fprintf(fp,'%.4f  ',ima(X,:));
                sendArray=[sendArray,rel(X,:),ima(X,:)];                     
            end  
            Array2=[Array2,sendArray];                       
        end
    end 
  

%%%%%%%%%    csi3.dat       %%%%%%%%%% 
    datatoplot3 = receivedData3(1:singalrecordlen*recordrate*1);
%     datatoplot3 = receivedData3((end-recordrate*singalrecordlen+1):end);
    csi_trace=read_bf_buffer(datatoplot3);
   % disp('read_bf_buffer csi1 completed.'); 
    [p,~]=size(csi_trace);
    receivedData3 = receivedData3(recordrate*singalrecordlen+1:end);
    for i = 1 : 4 : p-1  %p 200
        csi_entry=csi_trace{i};
        if ~isempty(csi_entry)
            csi = get_scaled_csi(csi_entry);     
            csi10 = squeeze(csi(1,:,:));   %3*30 complex
            rel = real(csi10);  %3*30 double
            ima = imag(csi10);  %3*30 double
            [x,y] = size(csi10);  %x=3 y=30
            sendArray=[];
            X = 0;
            while X < x  %  ��X���ŵ�
                X = X + 1;   
%                 fprintf(fp,'%.4f  ',rel(X,:));  %��X���ŵ���30�����ز���ʵֵ
%                 fprintf(fp,'%.4f  ',ima(X,:));
                sendArray=[sendArray,rel(X,:),ima(X,:)];                                
            end  
            Array3=[Array3,sendArray];           
        end
    end 
    
 
%%%%%%%%%%    csi4.dat       %%%%%%%%%% 
%     datatoplot4 = receivedData4(1:singalrecordlen*recordrate*1);
% %     datatoplot4 = receivedData4((end-recordrate*singalrecordlen+1):end);
%     csi_trace=read_bf_buffer(datatoplot4);
%    % disp('read_bf_buffer csi1 completed.'); 
%     [p,~]=size(csi_trace);
%     receivedData4 = receivedData4(recordrate*singalrecordlen+1:end);
%     for i = 1 : 4 : p-1  %p 200
%         csi_entry=csi_trace{i};
%         if ~isempty(csi_entry)
%             csi = get_scaled_csi(csi_entry);     
%             csi10 = squeeze(csi(1,:,:));   %3*30 complex
%             rel = real(csi10);  %3*30 double
%             ima = imag(csi10);  %3*30 double
%             [x,y] = size(csi10);  %x=3 y=30
%             sendArray=[];
%             X = 0;
%             while X < x  %  ��X���ŵ�
%                 X = X + 1;   
% %                 fprintf(fp,'%.4f  ',rel(X,:));  %��X���ŵ���30�����ز���ʵֵ
% %                 fprintf(fp,'%.4f  ',ima(X,:));
%                 sendArray=[sendArray,rel(X,:),ima(X,:)];                    
%             end  
%             Array4=[Array4,sendArray];       
%         end
%     end 
    headChar = 255;
    modeChar = 48;
    fwrite(tcpipClient,headChar);
    fwrite(tcpipClient,headChar);
    fwrite(tcpipClient,headChar);
    fwrite(tcpipClient,headChar);   %����4���ֽ�\xFF ,��ʾ֡ͷ
    fwrite(tcpipClient,modeChar);   %����1���ֽ�\x00 ,��ʾ֡ģʽ
    fwrite(tcpipClient,countInt,'int');  %����1��int ,��ʾ֡ʱ��
    countInt = countInt + 1;
   % dataLength = (length(Array1)+length(Array2)+length(Array3)+length(Array4))*4+4; 
%     dataLength = (length(Array1)+length(Array2))*4+2; 
    dataLength = (length(Array1)+length(Array2)+length(Array3))*4+3; 
    fwrite(tcpipClient,dataLength,'int');  %����1��int ,��ʾ�����򳤶�
    pointCSIcount = p/4;
    fwrite(tcpipClient,pointCSIcount,'int'); %����1��int ,��ʾÿ�������CSI����
    pointOrder = 49;
    fwrite(tcpipClient,pointOrder);   %����1���ֽ� ,��ʾ�ڼ�������
    fwrite(tcpipClient,Array1,'float');   %�������� ,��ʾ�ڼ��������CSI����
    pointOrder = pointOrder + 1;
    fwrite(tcpipClient,pointOrder);
    fwrite(tcpipClient,Array2,'float'); 
    pointOrder = pointOrder + 1;
    fwrite(tcpipClient,pointOrder);
    fwrite(tcpipClient,Array3,'float'); 
%     pointOrder = pointOrder + 1;
%     fwrite(tcpipClient,pointOrder);
%     fwrite(tcpipClient,Array4,'float');   %��������� һ֡�ĳ���Ϊ144021�ֽ�

end
set(obj,'UserData',tcpipClient);
t = toc;
fprintf('DataSend cost time: %f\n',t);
end