function DataProcess(~,~)
tic;
global VAR1;
global VAR2;
global csialtu1;
global csialtu2;
global testdata;
global receivedData1;
global receivedData2;
global datatoprocess1;
global datatoprocess2;

display('process data...');
% name1 = 'csi1.dat';
% name2 = 'csi2.dat';
% name3 = 'csi3.dat';
% name4 = 'csi4.dat';

csialtu1 = [];
csialtu2 = [];
datatoprocess1 = [];
datatoprocess2 = [];

recordrate = 200;
singalrecordlen = 215;
processlen = recordrate * 5;    %% process 5s's data one time
display('inite completed!');
%%%%%%%%%%    csi1.dat       %%%%%%%%%%
if and((length(receivedData1) > singalrecordlen*processlen),...
       (length(receivedData2) > singalrecordlen*processlen))
    datatoprocess1 = receivedData1(1:singalrecordlen*processlen);
    disp('get datatoprocess1!');
    csi_trace=read_bf_buffer(datatoprocess1);
    disp('read_bf_buffer csi1 completed.');
    receivedData1 = receivedData1(recordrate*singalrecordlen+1:end);
    [p,~]=size(csi_trace);
    i=0;
    fprintf('csi1.dat recorded items is: %d\n',p);
    % if p>1000       %%only use the first 1000 data
    %     p = 1000;
    % end
    while i<p
        i=i+1;
        csi_entry=csi_trace{i};
        if ~isempty(csi_entry)
            csi = get_scaled_csi(csi_entry);
            csi1 = csi(1,:,:);
            csi2 = squeeze(abs(csi1));
            csialtu1(i,1:30)  = csi2(1,:);
            csialtu1(i,31:60) = csi2(2,:);
            csialtu1(i,61:90) = csi2(3,:);                      
        end
    end
    disp('get csialtu1 completed.');

    %%%%%%%%%%    csi2.dat       %%%%%%%%%%
    datatoprocess2 = receivedData2(1:singalrecordlen*processlen);
    disp('get datatoprocess2!');
    csi_trace=read_bf_buffer(datatoprocess2);
    disp('read_bf_buffer csi2 completed.');
    receivedData2 = receivedData2(recordrate*singalrecordlen+1:end);
    [p,~]=size(csi_trace);
    i=0;
    fprintf('csi2.dat recorded items is: %d\n',p);
    % if p>1000       %%only use the first 1000 data
    %     p = 1000;
    % end
    while i<p
        i=i+1;
        csi_entry=csi_trace{i};
        if ~isempty(csi_entry)
            csi = get_scaled_csi(csi_entry);
            csi1 = csi(1,:,:);
            csi2 = squeeze(abs(csi1));
            csialtu2(i,1:30)  = csi2(1,:);
            csialtu2(i,31:60) = csi2(2,:);
            csialtu2(i,61:90) = csi2(3,:);
        end
    end
    disp('get csialtu2 completed.');

    %{
    %%%%%%%%%%    csi3.dat       %%%%%%%%%%
    csi_trace=read_bf_file(name3);
    [p,~]=size(csi_trace);
    i=0;
    while i<p
        i=i+1;
        csi_entry=csi_trace{i};
        if ~isempty(csi_entry)
            csi = get_scaled_csi(csi_entry);
            csi1 = csi(1,:,:);
            csialtu3 = abs(csi1);
        end
    end

    %%%%%%%%%%    csi4.dat       %%%%%%%%%%
    csi_trace=read_bf_file(name4);
    [p,~]=size(csi_trace);
    i=0;
    while i<p
        i=i+1;
        csi_entry=csi_trace{i};
        if ~isempty(csi_entry)
            csi = get_scaled_csi(csi_entry);
            csi1 = csi(1,:,:);
            csialtu4 = abs(csi1);
        end
    end
    %}

    %{
    segment_len = 1000;
    slide_distance = 50;

    [m, ~] = size(csialtu1);
    for i = 1 : slide_distance : m-segment_len
        VAR1 = var(csialtu1(i:i+segment_len,:),1,1);
    end

    [m, ~] = size(csialtu2);
    for i = 1 : slide_distance : m-segment_len
        VAR2 = var(csialtu2(i:i+segment_len,:),1,1);
    end

    [m, ~] = size(csialtu3);
    for i = 1 : slide_distance : m-segment_len
        VAR3 = var(csialtu3(i:i+segment_len,:),1,1);
    end

    [m, ~] = size(csialtu4);
    for i = 1 : slide_distance : m-segment_len
        VAR4 = var(csialtu4(i:i+segment_len,:),1,1);
    end
    %}
    VAR1 = var(csialtu1,1,1);
    disp('get VAR1 completed.');
    VAR2 = var(csialtu2,1,1);
    disp('get VAR2 completed.');

    %%%%%%%      SVM classfication      %%%%%%%%%%
    testdata(1,1:90) = VAR1(1,:);
    testdata(1,91:180) = VAR2(1,:);
    % testdata(1,181:270) = VAR3(1,:);
    % testdata(1,271:360) = VAR4(1,:);

%     model = loadmodel('libsvm_model',180);
%     [predict_label,accuracy,dicision_values] = svmpredict(0,testdata,model);
%     fprintf('predict_label is: %d\n\n',predict_label);
end

t = toc;
fprintf('DataProcess cost time: %f\n',t);
end
















