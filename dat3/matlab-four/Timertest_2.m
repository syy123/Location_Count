clear;clc;close all;

global countInt;
countInt = 0;


tcpipServer = tcpip('127.0.0.1',10006,'NetWorkRole','Server');    
set(tcpipServer,'OutputBufferSize',1024*1024);
set(tcpipServer,'InputBufferSize',1024*1024);
fopen(tcpipServer);
disp('connect to client successfully');
% fwrite(tcpipServer, 'Im Server', 'char');
t1 = timer('Name','timer1',...
    'TimerFcn',@testdatasend_3,...
    'period',1,...
    'StartDelay',1,...
    'ExecutionMode','fixedDelay');
set(t1,'UserData',tcpipServer);

% set(t1,'TimerFcn',{@addtest,a,b});

% t2 = timer('Name','timer2',...
%     'period',2,...
%     'StartDelay',1,...
%     'TasksToExecute',20,...
%     'ExecutionMode','fixedDelay');
% set(t2,'TimerFcn',{@addtest,'a','b'});

start(t1);
% start(t2);

