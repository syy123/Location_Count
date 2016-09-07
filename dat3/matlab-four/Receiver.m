function Receiver(obj,event,tcpipClient,fp)
% ud = obj.UserData;
% tcpipClient = ud.tcpipClient1;
% fp = ud.fp1;
disp('Execute Receiver.');
while(1)
    nBytes = get(tcpipClient,'BytesAvailable');
    if nBytes>0
        break;
    end
end

receivedData = fread(tcpipClient,nBytes,'int8');
count = fwrite(fp,receivedData);
fprintf('write %d bytes to %d\n',count,fp);
end