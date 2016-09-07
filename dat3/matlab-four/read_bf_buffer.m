
function ret = read_bf_buffer(buf)
disp('in read_bf_buffer function....');

len = length(buf);
fprintf('the file length is: %d\n',len);

ret = cell(ceil(len/95),1);     % Holds the return values - 1x1 CSI is 95 bytes big, so this should be upper bound
cur = 0;                        % Current offset into file
count = 0;                      % Number of records output
broken_perm = 0;                % Flag marking whether we've encountered a broken CSI yet
triangle = [1 3 6];             % What perm should sum to for 1,2,3 antennas
pos = 1;

% Need 3 bytes -- 2 byte size field and 1 byte code
while cur < (len - 3 - 215)
    field_len = buf(pos)*256 + buf(pos+1);
%     fprintf('the field_len is: %d  \n',field_len);
    pos = pos + 2;
    code = buf(pos);
    pos = pos + 1;
    cur = cur+3;
%     fprintf('pos is: %d, cur is:%d, code is: %d  \n',pos, cur, code);
    
%     If unhandled code, skip (seek over) the record and continue
    if (code == 187) % get beamforming or phy data
%         fprintf('pos is: %d, cur is: %d, field_len is: %d \n', pos, cur, field_len);
        bytes = buf(pos : (pos + field_len-2));

        pos = pos + field_len - 1;
        cur = cur + field_len - 1;
        charbytes = uint8(bytes);
        
%         fprintf('pos is: %d, cur is: %d, length of bytes is: %d  \n', pos, cur, length(bytes));
%         fprintf('the bytes is: \n');
%         fprintf('%d  ',bytes);
%         fprintf('\n');
        
        if (length(bytes) ~= field_len-1)
%             break;
            return;
        end
    else
        pos = pos - 1;
        cur = cur - 1;

        continue;
    end
    
    if (code == 187) %hex2dec('bb')) Beamforming matrix -- output a record
        count = count + 1;
        ret{count} = read_bfee(charbytes);
        
        perm = ret{count}.perm;
        Nrx = ret{count}.Nrx;
        if Nrx == 1 % No permuting needed for only 1 antenna
            continue;
        end
        if sum(perm) ~= triangle(Nrx) % matrix does not contain default values
            if broken_perm == 0
                broken_perm = 1;
                fprintf('WARN ONCE: Found CSI (%s) with Nrx=%d and invalid perm=[%s]\n', filename, Nrx, int2str(perm));
            end
        else
            ret{count}.csi(:,perm(1:Nrx),:) = ret{count}.csi(:,1:Nrx,:);
        end
    end
end
fprintf('cur : %d  pos : %d\n',cur, pos);

ret = ret(1:count);

end
