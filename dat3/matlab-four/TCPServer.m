clear;clc;close all;


% construct tcp/ip object on server end
tcpipServer = tcpip('0.0.0.0',10000,'NetWorkRole','Server');
set(tcpipServer,'Timeout',10);
N = 1024;
set(tcpipServer,'InputBufferSize',8*N);
set(tcpipServer,'OutputBufferSize',1024);


% open connection object
fopen(tcpipServer);


% send instruction
instruction =1.141;
fwrite(tcpipServer,instruction,'double');
% disp('Instruction sending succeeds.');
% numSent = get(tcpipServer,'valuesSent');
% disp(strcat('Bytes of instruction is :',numSent));
% 
% 
% % wait for receiving data
% while(1)
%     nBytes = get(tcpipServer,'BytesAvailable');
%     if nBytes > 0
%         break;
%     end
% end
% 
% 
% % receive data
% recvRaw = fread(tcpipServer,nBytes/8,'double');
% 
% figure;
% plot(recvRaw);grid on;
% title('received signal from B');

fclose(tcpipServer);
delete(tcpipServer);
