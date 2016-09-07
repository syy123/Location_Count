clear;clc;close all;

tcpipServer = tcpip('0.0.0.0',10000,'NetWorkRole','Server');    
set(tcpipServer,'OutputBufferSize',1024*1024);
set(tcpipServer,'InputBufferSize',1024*1024);
disp('wait to connect');
fopen(tcpipServer);
disp('connect to server successfully');

t1 = timer('Name','timer1',...
    'TimerFcn',@testdatasend,...
    'period',1,...
    'StartDelay',3,...
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

