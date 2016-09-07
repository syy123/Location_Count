function addtest(obj,event,a,b)
    flag = obj.UserData;
    flag = flag+1;
    sum = a + b;
    fprintf('the %d times call,the sum of a + b is : %d \n',flag, sum);
    set(obj,'UserData',flag);
end

% count = 0;
% fprintf('count = %d\n',count);