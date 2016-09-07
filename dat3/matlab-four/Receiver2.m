function Receiver2(obj,~)
tic;
global receivedData2;
global totallen2;

% disp('Execute Receiver1.');
% ud2 = obj.UserData;
% tcpipobj2 = ud2.tcpipClient2;
% fpr2 = ud2.fp2;
% fp2 = fopen('csi2.dat','a');

tcpipobj2 = obj.UserData;
nBytes2 = get(tcpipobj2,'BytesAvailable');
if nBytes2>0
    receivedData = fread(tcpipobj2,nBytes2,'char');
%     fwrite(fp2,receivedData);
    receivedData2 = [receivedData2; receivedData];
    totallen2 = totallen2 + length(receivedData);
    fprintf('append %d bytes to receivedData2, current receivedData2 length is : %d, totallen2: %d \n',...
        length(receivedData),length(receivedData2), totallen2);
end

% set(ud2.tcpipClient2,tcpipobj2);
% set(ud2.fp2,fpr2);
% set(obj,'UserData',ud2);
set(obj,'UserData',tcpipobj2);
% fclose(fp2);

t = toc;
fprintf('Receiver2 cost time: %f\n',t);
end