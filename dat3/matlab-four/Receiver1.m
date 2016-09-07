function Receiver1(obj,~)
tic;
global receivedData1;
global totallen1;

% disp('Execute Receiver1.');
% ud1 = obj.UserData;
% tcpipobj1 = ud1.tcpipClient1;
% fpr1 = ud1.fp1;
% fp1 = fopen('csi1.dat','a');

tcpipobj1 = obj.UserData;
nBytes1 = get(tcpipobj1,'BytesAvailable');
if nBytes1>0
    receivedData = fread(tcpipobj1,nBytes1,'char');
%     fwrite(fp1,receivedData);
    receivedData1 = [receivedData1; receivedData];
    totallen1 = totallen1 + length(receivedData);
    fprintf('append %d bytes to receivedData1, currnet receivedData1 length is : %d, totallen1: %d \n',...
        length(receivedData),length(receivedData1), totallen1);
end

% set(ud1.tcpipClient1,tcpipobj1);
% set(ud1.fp1,fpr1);
% set(obj,'UserData',ud1);
set(obj,'UserData',tcpipobj1);
% fclose(fp1);

t = toc;
fprintf('Receiver1 cost time: %f\n',t);
end

