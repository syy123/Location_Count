function StartRecording(obj,~)
    tcpipobj = obj.UserData;
    fwrite(tcpipobj,'OK','char');
    set(obj,'UserData',tcpipobj);
end