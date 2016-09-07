function StopPredict()
global tcpipClient1;
global tcpipClient2;
global tcpipClient3;
%global tcpipClient4;
global tcpipClient5;
global t1;
global t2;
global t3;
% global t4;
% global t5;
global t6;
disp('stop predict');

fwrite(tcpipClient1,'Q','char');
pause(1);
fwrite(tcpipClient2,'Q','char');
pause(1);
fwrite(tcpipClient3,'Q','char');
pause(1);
%fwrite(tcpipClient4,'Q','char');
%pause(1);
fwrite(tcpipClient5,'Quit','char');
pause(1);

stop(t1);
stop(t2);
stop(t3);
%stop(t4);
stop(t6);

fclose(tcpipClient1);
fclose(tcpipClient2);
fclose(tcpipClient3);
%fclose(tcpipClient4);
fclose(tcpipClient5);

end
