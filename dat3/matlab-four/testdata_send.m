function str=testdata_send(rel,ima,X)


relremind = roundn(rel(X,:),-4);
imaremind = roundn(ima(X,:),-4);
strMaxtri1 = num2str(relremind);
strMaxtri2 = num2str(imaremind);
strCell1 = regexp(strMaxtri1, '\s+', 'split'); 
strCell2 = regexp(strMaxtri2, '\s+', 'split');  %1*30���ַ�cell
str1= strCell1{1};
str2= strCell2{1};

for i=2:30
    D1=strCell1{i};%ȡcell��char
    %str1=sprintf('%s+%s',str1,D1);
    str1 = [str1,'+',D1];
    D2=strCell2{i};%ȡcell��char
    str2 = [str2,'+',D2];
   % str2=sprintf('%s+%s',str2,D2);
end
% 
%str = sprintf('%s+%s',str1,str2); %������¼ ��X���ŵ��� ʵֵ����ֵ
str = [str1,'+',str2];
%str=sprintf('%s  %s',strMaxtri1,strMaxtri2);

end
