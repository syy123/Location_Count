function Receiver4(obj,~)
tic;
global receivedData4;
global totallen4;

% disp('Execute Receiver1.');
% ud1 = obj.UserData;
% tcpipobj1 = ud1.tcpipClient1;
% fpr1 = ud1.fp1;
% fp1 = fopen('csi1.dat','a');

tcpipobj4 = obj.UserData;
nBytes4 = get(tcpipobj4,'BytesAvailable');
if nBytes4>0
    receivedData = fread(tcpipobj4,nBytes4,'char');
%     fwrite(fp1,receivedData);
    receivedData4 = [receivedData4; receivedData];
    totallen4 = totallen4 + length(receivedData);
    fprintf('append %d bytes to receivedData4, currnet receivedData4 length is : %d, totallen4: %d \n',...
        length(receivedData),length(receivedData4), totallen4);
end

% set(ud1.tcpipClient1,tcpipobj1);
% set(ud1.fp1,fpr1);
% set(obj,'UserData',ud1);
set(obj,'UserData',tcpipobj4);
% fclose(fp1);

t = toc;
fprintf('Receiver4 cost time: %f\n',t);
end

