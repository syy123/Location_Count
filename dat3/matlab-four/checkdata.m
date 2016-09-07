function checkdata(buf)
for i = 1 : 215 : length(buf)
    fprintf('buf[%d] = %d, buf[%d] = %d\n',i,buf(i),i+1,buf(i+1));
end
end