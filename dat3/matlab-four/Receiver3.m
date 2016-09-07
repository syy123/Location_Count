function Receiver3(obj,~)
tic;
global receivedData3;
global totallen3;

% disp('Execute Receiver1.');
% ud1 = obj.UserData;
% tcpipobj1 = ud1.tcpipClient1;
% fpr1 = ud1.fp1;
% fp1 = fopen('csi1.dat','a');

tcpipobj3 = obj.UserData;
nBytes3 = get(tcpipobj3,'BytesAvailable');
if nBytes3>0
    receivedData = fread(tcpipobj3,nBytes3,'char');
%     fwrite(fp1,receivedData);
    receivedData3 = [receivedData3; receivedData];
    totallen3 = totallen3 + length(receivedData);
    fprintf('append %d bytes to receivedData3, currnet receivedData3 length is : %d, totallen3: %d \n',...
        length(receivedData),length(receivedData3), totallen3);
end

% set(ud1.tcpipClient1,tcpipobj1);
% set(ud1.fp1,fpr1);
% set(obj,'UserData',ud1);
set(obj,'UserData',tcpipobj3);
% fclose(fp1);

t = toc;
fprintf('Receiver3 cost time: %f\n',t);
end

