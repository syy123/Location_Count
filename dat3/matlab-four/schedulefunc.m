function schedulefunc()
global schedulecount;
global tcpipClient1;
global tcpipClient2;
global tcpipClient3;
global tcpipClient4;

schedulecount = schedulecount + 1;

if schedulecount > 4
    schedulecount = 1;
end

if schedulecount == 1
        fwrite(tcpipClient1,'sendallowed','char');
        fwrite(tcpipClient2,'senddenied','char');
        fwrite(tcpipClient3,'senddenied','char');
        fwrite(tcpipClient4,'senddenied','char');
        
end

if schedulecount == 2
        fwrite(tcpipClient1,'senddenied','char');
        fwrite(tcpipClient2,'sendallowed','char');
        fwrite(tcpipClient3,'senddenied','char');
        fwrite(tcpipClient4,'senddenied','char');
end

if schedulecount == 3
        fwrite(tcpipClient1,'senddenied','char');
        fwrite(tcpipClient2,'senddenied','char');
        fwrite(tcpipClient3,'sendallowed','char');
        fwrite(tcpipClient4,'senddenied','char');
end

if schedulecount == 4
        fwrite(tcpipClient1,'senddenied','char');
        fwrite(tcpipClient2,'senddenied','char');
        fwrite(tcpipClient3,'senddenied','char');
        fwrite(tcpipClient4,'sendallowed','char');
end

% switch schedulecount
%     case 1
%         fwrite(tcpipClient1,'sendallowed','char');
%         fwrite(tcpipClient2,'senddenied','char');
%         fwrite(tcpipClient3,'senddenied','char');
%         fwrite(tcpipClient4,'senddenied','char');
%     case 2
%         fwrite(tcpipClient1,'senddenied','char');
%         fwrite(tcpipClient2,'sendallowed','char');
%         fwrite(tcpipClient3,'senddenied','char');
%         fwrite(tcpipClient4,'senddenied','char');
%     case 3
%         fwrite(tcpipClient1,'senddenied','char');
%         fwrite(tcpipClient2,'senddenied','char');
%         fwrite(tcpipClient3,'sendallowed','char');
%         fwrite(tcpipClient4,'senddenied','char');
%     case 4
%         fwrite(tcpipClient1,'senddenied','char');
%         fwrite(tcpipClient2,'senddenied','char');
%         fwrite(tcpipClient3,'senddenied','char');
%         fwrite(tcpipClient4,'sendallowed','char');
%     otherwise
%         fwrite(tcpipClient1,'sendallowed','char');
%         fwrite(tcpipClient2,'senddenied','char');
%         fwrite(tcpipClient3,'senddenied','char');
%         fwrite(tcpipClient4,'senddenied','char');
% end
end