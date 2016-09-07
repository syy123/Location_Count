clear;clc;close all;
global receivedData1;
global receivedData2;
global receivedData3;
global receivedData4;
global totallen1;
global totallen2;
global totallen3;
global totallen4;
global tcpipClient1;
global tcpipClient2;
global tcpipClient3;
%global tcpipClient4;
global tcpipClient5;
global plotServer;
global t1;
global t2;
global t3;
% global t4;
% global t5;
global t6;

global countInt;
global schedulecount;

receivedData1 = [];
receivedData2 = [];
receivedData3 = [];
receivedData4 = [];
countInt = 0;
totallen1 = 0;
totallen2 = 0;
totallen3 = 0;
totallen4 = 0;
schedulecount = 1;



N = 1024;
tcpipClient1 = tcpip('192.168.1.101',10003,...
    'NetworkRole','Client');
set(tcpipClient1,'OutputBufferSize',1024*N);
set(tcpipClient1,'InputBufferSize',1024*N);
set(tcpipClient1,'Timeout',30);

tcpipClient2 = tcpip('192.168.1.102',10003,...
    'NetworkRole','Client');
set(tcpipClient2,'OutputBufferSize',1024*N);
set(tcpipClient2,'InputBufferSize',1024*N);
set(tcpipClient2,'Timeout',30);

tcpipClient3 = tcpip('192.168.1.107',10003,...
    'NetworkRole','Client');
set(tcpipClient3,'OutputBufferSize',1024*N);
set(tcpipClient3,'InputBufferSize',1024*N);
set(tcpipClient3,'Timeout',30);
% 
% tcpipClient4 = tcpip('192.168.1.107',10003,...
%     'NetworkRole','Client');
% set(tcpipClient4,'OutputBufferSize',1024*N);
% set(tcpipClient4,'InputBufferSize',1024*N);
% set(tcpipClient4,'Timeout',30);

tcpipClient5 = tcpip('192.168.1.104',10003,...
    'NetworkRole','Client');
set(tcpipClient5,'OutputBufferSize',1024*N);
set(tcpipClient5,'InputBufferSize',1024*N);
set(tcpipClient5,'Timeout',30);


fopen(tcpipClient1);
disp('client1 connect to server successfully');
fopen(tcpipClient2);
disp('client2 connect to server successfully');
fopen(tcpipClient3);
disp('client3 connect to server successfully');
% fopen(tcpipClient4);
% disp('client4 connect to server successfully');
fopen(tcpipClient5);
disp('client5 connect to server successfully');

plotServer = tcpip('127.0.0.1',10006,...
    'NetworkRole','Server');
set(plotServer,'OutputBufferSize',1024*N);
set(plotServer,'InputBufferSize',1024*N);
set(plotServer,'Timeout',30);
fopen(plotServer);
disp('connect to python client successfully');

% fopen(tcpipClient3);
% disp('client3 connect to server successfully');

% fwrite(tcpipClient1,'OK','char');
% fwrite(tcpipClient2,'OK','char');
% fwrite(tcpipClient3,'OK','char');
% fwrite(tcpipClient4,'OK','char');
fwrite(tcpipClient5,'predict','char');

t1 = timer('Name','ReceiverTimer1',...
    'TimerFcn',@Receiver1,...
    'period',1,...
    'StartDelay',1,...
    'BusyMode','queue',...
    'ExecutionMode','fixedRate');
set(t1,'UserData',tcpipClient1);

t2 = timer('Name','ReceiverTimer2',...
    'TimerFcn',@Receiver2,...
    'period',1,...
    'StartDelay',1,...
    'BusyMode','queue',...
    'ExecutionMode','fixedRate');
set(t2,'UserData',tcpipClient2);

t3 = timer('Name','ReceiverTimer3',...
    'TimerFcn',@Receiver3,...
    'period',1,...
    'StartDelay',1,...
    'BusyMode','queue',...
    'ExecutionMode','fixedRate');
set(t3,'UserData',tcpipClient3);
% 
% t4 = timer('Name','ReceiverTimer4',...
%     'TimerFcn',@Receiver4,...
%     'period',1,...
%     'StartDelay',1,...
%     'BusyMode','queue',...
%     'ExecutionMode','fixedRate');
% set(t4,'UserData',tcpipClient4);

% t5 = timer('Name','Process',...
%     'TimerFcn',@DataProcess,...
%     'period',1,...
%     'StartDelay',17,...
%     'BusyMode','queue',...
%     'ExecutionMode','fixedRate');

t6 = timer('Name','DataSend',...
    'TimerFcn',@DataSend,...
    'period',1,...
    'StartDelay',1,...
    'BusyMode','queue',...
    'ExecutionMode','fixedRate');
set(t6,'UserData',plotServer);

% t7 = timer('Name','ScheduleSending',...
%     'TimerFcn',@ScheduleSending,...
%     'period',0.2,...
%     'StartDelay',1,...
%     'BusyMode','queue',...
%     'ExecutionMode','fixedRate');
% set(t6,'UserData',plotClient);

%t4 = timer('Name','Plot',...
%    'TimerFcn',@testdatasend,...
%    'period',1,...
%    'StartDelay',17,...
%    'BusyMode','queue',...
%    'ExecutionMode','fixedRate');

% t4 = timer('Name','StartRecording',...
%     'TimerFcn',@StartRecording,...
%     'period',1,...
%     'StartDelay',1,...
%     'BusyMode','queue',...
%     'ExecutionMode','singleShot');
% set(t4,'UserData',tcpipClient3);

start(t1);
start(t2);
start(t3);
% start(t4);
start(t6);

% fclose(tcpipClient1);
% delete(tcpipClient1);
% fclose(tcpipClient2);
% delete(tcpipClient2);
% fclose(fp1);
% fclose(fp2);

% clear;clc;close all;
% flag1 = 0;
% flag2 = 0;
% 
% t1 = timer('Name','ReceiverTimer1',...
%     'TimerFcn',@Receiver1,...
%     'period',0.001,...
%     'StartDelay',1,...
%     'ExecutionMode','fixedDelay');
% set(t1,'UserData',flag1);
% 
% t2 = timer('Name','ReceiverTimer2',...
%     'TimerFcn',@Receiver2,...
%     'period',0.001,...
%     'StartDelay',1,...
%     'ExecutionMode','fixedDelay');
% set(t2,'UserData',flag2);
% 
% start(t1);
% start(t2);
% 

