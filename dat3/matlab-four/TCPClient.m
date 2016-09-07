clear;clc;close all;

% construct feedback data
 N = 1024;
% t = [1:N]/N*4*pi;
% signal = sin(t) + 0.05*rand(1,N);
% figure;
% plot(t,signal);
% grid on;
% title('signal on the end of B.')

% construct tcp/ip object on client side
tcpipClient = tcpip('127.0.0.1',10001,...
    'NetworkRole','Client');
set(tcpipClient,'OutputBufferSize',8*N); 
set(tcpipClient,'InputBufferSize',1024); 
set(tcpipClient,'Timeout',60); 

% open connection object
fopen(tcpipClient); 

% wait for receive order
% receive order
a = 255;
fwrite(tcpipClient,a);
fwrite(tcpipClient,a);
fwrite(tcpipClient,a);
fwrite(tcpipClient,a);

mode = 0;
fwrite(tcpipClient,mode);

% % feedback data
% fwrite(tcpipClient,signal,'double');


fclose(tcpipClient);
delete(tcpipClient);
