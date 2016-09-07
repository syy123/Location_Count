clear;
clc;
%%%%            segmented var        %%%%
csivar01 = load('../../Data/count/2016-5-8-22/noperson/noperson1_csivarseg.txt');        
csivar11 = load('../../Data/count/2016-5-8-22/oneperson/oneperson1_csivarseg.txt');      
csivar21 = load('../../Data/count/2016-5-8-22/twoperson/twoperson1_csivarseg.txt');      
csivar31 = load('../../Data/count/2016-5-8-22/threeperson/threeperson1_csivarseg.txt');  
csivar41 = load('../../Data/count/2016-5-8-22/fourperson/fourperson1_csivarseg.txt');  
csivar51 = load('../../Data/count/2016-5-8-22/fiveperson/fiveperson1_csivarseg.txt');  
% csivar61 = load('../../Data/count/2016-5-8-22/sixperson/sixperson1_csivarseg.txt');    

csivar02 = load('../../Data/count/2016-5-8-22/noperson/noperson2_csivarseg.txt');        
csivar12 = load('../../Data/count/2016-5-8-22/oneperson/oneperson2_csivarseg.txt');      
csivar22 = load('../../Data/count/2016-5-8-22/twoperson/twoperson2_csivarseg.txt');      
csivar32 = load('../../Data/count/2016-5-8-22/threeperson/threeperson2_csivarseg.txt');  
csivar42 = load('../../Data/count/2016-5-8-22/fourperson/fourperson2_csivarseg.txt');  
csivar52 = load('../../Data/count/2016-5-8-22/fiveperson/fiveperson2_csivarseg.txt');  
% csivar62 = load('../../Data/count/2016-5-8-22/sixperson/sixperson2_csivarseg.txt');    


% csivar03 = load('../../Data/count/2016-5-8-22/noperson/noperson3_csivarseg.txt');        
% csivar13 = load('../../Data/count/2016-5-8-22/oneperson/oneperson3_csivarseg.txt');      
% csivar23 = load('../../Data/count/2016-5-8-22/twoperson/twoperson3_csivarseg.txt');      
% csivar33 = load('../../Data/count/2016-5-8-22/threeperson/threeperson3_csivarseg.txt');  
% csivar43 = load('../../Data/count/2016-5-8-22/fourperson/fourperson3_csivarseg.txt');  
% csivar53 = load('../../Data/count/2016-5-8-22/fiveperson/fiveperson3_csivarseg.txt');  
% % csivar63 = load('../../Data/count/2016-5-8-22/sixperson/sixperson3_csivarseg.txt');    
% 
% csivar04 = load('../../Data/count/2016-5-8-22/noperson/noperson4_csivarseg.txt');        
% csivar14 = load('../../Data/count/2016-5-8-22/oneperson/oneperson4_csivarseg.txt');      
% csivar24 = load('../../Data/count/2016-5-8-22/twoperson/twoperson4_csivarseg.txt');      
% csivar34 = load('../../Data/count/2016-5-8-22/threeperson/threeperson4_csivarseg.txt');  
% csivar44 = load('../../Data/count/2016-5-8-22/fourperson/fourperson4_csivarseg.txt');  
% csivar54 = load('../../Data/count/2016-5-8-22/fiveperson/fiveperson4_csivarseg.txt');  
% % csivar64 = load('../../Data/count/2016-5-8-22/sixperson/sixperson4_csivarseg.txt');    

%%%%               eig value              %%%%
% csieig01 = load('../../Data/count/2016-5-8-22/noperson/noperson1_csieig.txt');        
% csieig11 = load('../../Data/count/2016-5-8-22/oneperson/oneperson1_csieig.txt');      
% csieig21 = load('../../Data/count/2016-5-8-22/twoperson/twoperson1_csieig.txt');      
% csieig31 = load('../../Data/count/2016-5-8-22/threeperson/threeperson1_csieig.txt');  
% csieig41 = load('../../Data/count/2016-5-8-22/fourperson/fourperson1_csieig.txt');  
% csieig51 = load('../../Data/count/2016-5-8-22/fiveperson/fiveperson1_csieig.txt');  
% csieig61 = load('../../Data/count/2016-5-8-22/sixperson/sixperson1_csieig.txt');    
% 
% csieig02 = load('../../Data/count/2016-5-8-22/noperson/noperson2_csieig.txt');        
% csieig12 = load('../../Data/count/2016-5-8-22/oneperson/oneperson2_csieig.txt');      
% csieig22 = load('../../Data/count/2016-5-8-22/twoperson/twoperson2_csieig.txt');      
% csieig32 = load('../../Data/count/2016-5-8-22/threeperson/threeperson2_csieig.txt');  
% csieig42 = load('../../Data/count/2016-5-8-22/fourperson/fourperson2_csieig.txt');  
% csieig52 = load('../../Data/count/2016-5-8-22/fiveperson/fiveperson2_csieig.txt');  
% csieig62 = load('../../Data/count/2016-5-8-22/sixperson/sixperson2_csieig.txt');    
% 
% csieig03 = load('../../Data/count/2016-5-8-22/noperson/noperson3_csieig.txt');        
% csieig13 = load('../../Data/count/2016-5-8-22/oneperson/oneperson3_csieig.txt');      
% csieig23 = load('../../Data/count/2016-5-8-22/twoperson/twoperson3_csieig.txt');      
% csieig33 = load('../../Data/count/2016-5-8-22/threeperson/threeperson3_csieig.txt');  
% csieig43 = load('../../Data/count/2016-5-8-22/fourperson/fourperson3_csieig.txt');  
% csieig53 = load('../../Data/count/2016-5-8-22/fiveperson/fiveperson3_csieig.txt');  
% csieig63 = load('../../Data/count/2016-5-8-22/sixperson/sixperson3_csieig.txt');    
% 
% csieig04 = load('../../Data/count/2016-5-8-22/noperson/noperson4_csieig.txt');        
% csieig14 = load('../../Data/count/2016-5-8-22/oneperson/oneperson4_csieig.txt');      
% csieig24 = load('../../Data/count/2016-5-8-22/twoperson/twoperson4_csieig.txt');      
% csieig34 = load('../../Data/count/2016-5-8-22/threeperson/threeperson4_csieig.txt');  
% csieig44 = load('../../Data/count/2016-5-8-22/fourperson/fourperson4_csieig.txt');  
% csieig54 = load('../../Data/count/2016-5-8-22/fiveperson/fiveperson4_csieig.txt');  
% csieig64 = load('../../Data/count/2016-5-8-22/sixperson/sixperson4_csieig.txt');    

m = 290;
% n = 150;

% data(1:m,1:10) = csivar01(1:m,1:10);
% data(1:m,11:20) = csivar02(1:m,1:10);
% data(1:m,21:30) = csivar03(1:m,1:10);
% data(1:m,31:40) = csivar04(1:m,1:10);
% 
% data(m+1:2*m,1:10) = csivar11(1:m,1:10);
% data(m+1:2*m,11:20) = csivar12(1:m,1:10);
% data(m+1:2*m,21:30) = csivar13(1:m,1:10);
% data(m+1:2*m,31:40) = csivar14(1:m,1:10);
% 
% data(2*m+1:3*m,1:10) = csivar21(1:m,1:10);
% data(2*m+1:3*m,11:20) = csivar22(1:m,1:10);
% data(2*m+1:3*m,21:30) = csivar23(1:m,1:10);
% data(2*m+1:3*m,31:40) = csivar24(1:m,1:10);
% 
% data(3*m+1:4*m,1:10) = csivar31(1:m,1:10);
% data(3*m+1:4*m,11:20) = csivar32(1:m,1:10);
% data(3*m+1:4*m,21:30) = csivar33(1:m,1:10);
% data(3*m+1:4*m,31:40) = csivar34(1:m,1:10);


data(1:m,1:90) = csivar01(1:m,:);                   %%   noperson's trainning data
data(1:m,91:180) = csivar02(1:m,:);
% data(1:m,181:270) = csivar03(1:m,:);
% data(1:m,271:360) = csivar04(1:m,:);

% data(1:m,361) = csieig01(1:m,:);                    %%  eig value
% data(1:m,362) = csieig02(1:m,:);
% data(1:m,363) = csieig03(1:m,:);
% data(1:m,364) = csieig04(1:m,:);

data(m+1:2*m,1:90) = csivar11(1:m,:);               %%   oneperson's trainning data
data(m+1:2*m,91:180) = csivar12(1:m,:);
% data(m+1:2*m,181:270) = csivar13(1:m,:);
% data(m+1:2*m,271:360) = csivar14(1:m,:);

% data(m+1:2*m,361) = csieig11(1:m,:);
% data(m+1:2*m,362) = csieig12(1:m,:);
% data(m+1:2*m,363) = csieig13(1:m,:);
% data(m+1:2*m,364) = csieig14(1:m,:);

data(2*m+1:3*m,1:90) = csivar21(1:m,:);             %%   twoperson's trainning data
data(2*m+1:3*m,91:180) = csivar22(1:m,:);
% data(2*m+1:3*m,181:270) = csivar23(1:m,:);
% data(2*m+1:3*m,271:360) = csivar24(1:m,:);

% data(2*m+1:3*m,361) = csieig21(1:m,:);
% data(2*m+1:3*m,362) = csieig22(1:m,:);
% data(2*m+1:3*m,363) = csieig23(1:m,:);
% data(2*m+1:3*m,364) = csieig24(1:m,:);

data(3*m+1:4*m,1:90) = csivar31(1:m,:);             %%   threeperson's trainning data
data(3*m+1:4*m,91:180) = csivar32(1:m,:);
% data(3*m+1:4*m,181:270) = csivar33(1:m,:);
% data(3*m+1:4*m,271:360) = csivar34(1:m,:);

% data(3*m+1:4*m,361) = csieig31(1:m,:);
% data(3*m+1:4*m,362) = csieig32(1:m,:);
% data(3*m+1:4*m,363) = csieig33(1:m,:);
% data(3*m+1:4*m,364) = csieig34(1:m,:);


data(4*m+1:5*m,1:90) = csivar41(1:m,:);             %%   fourperson's trainning data
data(4*m+1:5*m,91:180) = csivar42(1:m,:);
% data(4*m+1:5*m,181:270) = csivar43(1:m,:);
% data(4*m+1:5*m,271:360) = csivar44(1:m,:);

% data(4*m+1:5*m,361) = csieig41(1:m,:);
% data(4*m+1:5*m,362) = csieig42(1:m,:);
% data(4*m+1:5*m,363) = csieig43(1:m,:);
% data(4*m+1:5*m,364) = csieig44(1:m,:);


data(5*m+1:6*m,1:90) = csivar51(1:m,:);             %%   fiveperson's trainning data
data(5*m+1:6*m,91:180) = csivar52(1:m,:);
% data(5*m+1:6*m,181:270) = csivar53(1:m,:);
% data(5*m+1:6*m,271:360) = csivar54(1:m,:);

% data(5*m+1:6*m,361) = csieig51(1:m,:);
% data(5*m+1:6*m,362) = csieig52(1:m,:);
% data(5*m+1:6*m,363) = csieig53(1:m,:);
% data(5*m+1:6*m,364) = csieig54(1:m,:);

%{
data(6*m+1:7*m,1:90) = csivar61(1:m,:);             %%   sixperson's trainning data
data(6*m+1:7*m,91:180) = csivar62(1:m,:);
data(6*m+1:7*m,181:270) = csivar63(1:m,:);
data(6*m+1:7*m,271:360) = csivar64(1:m,:);

% data(6*m+1:7*m,361) = csieig61(1:m,:);
% data(6*m+1:7*m,362) = csieig62(1:m,:);
% data(6*m+1:7*m,363) = csieig63(1:m,:);
% data(6*m+1:7*m,364) = csieig64(1:m,:);
%}

label(1:m,1) = 0;
label(m+1:2*m,1) = 1;
label(2*m+1:3*m,1) = 2;
label(3*m+1:4*m,1) = 3;
label(4*m+1:5*m,1) = 4;
label(5*m+1:6*m,1) = 5;
% label(6*m+1:7*m,1) = 6;

% model = svmtrain(label,data,'-t 1 -d 2');
% model = svmtrain(label,data,'-t 2 -c 3.5 -g 0.000015 -e 0.000001');
model = svmtrain(label,data,'-t 2 -c 4 -g 0.00006 -e 0.000001');
% [predict_label,accuracy,dicision_values] = svmpredict(label,data,model);
savemodel('libsvm_model',model);

%{
a = 0; b = 0; c = 0; d = 0; e = 0; f = 0; g = 0;
for i = 1:n
    testdata(1,1:90) = csivar01(i+m,:);
    testdata(1,91:180) = csivar02(i+m,:);
    testdata(1,181:270) = csivar03(i+m,:);
    testdata(1,271:360) = csivar04(i+m,:);

%     testdata(1,361) = csieig01(i+m,:);
%     testdata(1,362) = csieig02(i+m,:);
%     testdata(1,363) = csieig03(i+m,:);
%     testdata(1,364) = csieig04(i+m,:);
    
    testlabel = 0;
    [predict_label,accuracy,dicision_values] = svmpredict(testlabel,testdata,model);
    switch predict_label
        case 0
            a = a + 1;
        case 1
            b = b + 1;
        case 2
            c = c + 1;
        case 3
            d = d + 1;
        case 4
            e = e + 1;
        case 5
            f = f + 1;  
        case 6
            g = g + 1;
    end
end
result0(1) = a;
result0(2) = b;
result0(3) = c;
result0(4) = d;
result0(5) = e;
result0(6) = f;
result0(7) = g;
accuray0 = a/n;

a = 0; b = 0; c = 0; d = 0; e = 0; f = 0; g = 0;
for i = 1:n
    testdata(1,1:90) = csivar11(i+m,:);
    testdata(1,91:180) = csivar12(i+m,:);
    testdata(1,181:270) = csivar13(i+m,:);
    testdata(1,271:360) = csivar14(i+m,:);

%     testdata(1,361) = csieig11(i+m,:);
%     testdata(1,362) = csieig12(i+m,:);
%     testdata(1,363) = csieig13(i+m,:);
%     testdata(1,364) = csieig14(i+m,:);
    
    testlabel = 1;
    [predict_label,accuracy,dicision_values] = svmpredict(testlabel,testdata,model);
    switch predict_label
        case 0
            a = a + 1;
        case 1
            b = b + 1;
        case 2
            c = c + 1;
        case 3
            d = d + 1;
        case 4
            e = e + 1;
        case 5
            f = f + 1;      
        case 6
            g = g + 1;
    end
end
result1(1) = a;
result1(2) = b;
result1(3) = c;
result1(4) = d;
result1(5) = e;
result1(6) = f;
result1(7) = g;
accuray1 = b/n;

a = 0; b = 0; c = 0; d = 0; e = 0; f = 0; g = 0;
for i = 1:n
    testdata(1,1:90) = csivar21(i+m,:);
    testdata(1,91:180) = csivar22(i+m,:);
    testdata(1,181:270) = csivar23(i+m,:);
    testdata(1,271:360) = csivar24(i+m,:);

%     testdata(1,361) = csieig21(i+m,:);
%     testdata(1,362) = csieig22(i+m,:);
%     testdata(1,363) = csieig23(i+m,:);
%     testdata(1,364) = csieig24(i+m,:);
    
    testlabel = 2;
    [predict_label,accuracy,dicision_values] = svmpredict(testlabel,testdata,model);
    switch predict_label
        case 0
            a = a + 1;
        case 1
            b = b + 1;
        case 2
            c = c + 1;
        case 3
            d = d + 1;
        case 4
            e = e + 1;
        case 5
            f = f + 1;  
        case 6
            g = g + 1;            
    end
end
result2(1) = a;
result2(2) = b;
result2(3) = c;
result2(4) = d;
result2(5) = e;
result2(6) = f;
result2(7) = g;
accuray2 = c/n;

a = 0; b = 0; c = 0; d = 0; e = 0; f = 0; g = 0;
for i = 1:n
    testdata(1,1:90) = csivar31(i+m,:);
    testdata(1,91:180) = csivar32(i+m,:);
    testdata(1,181:270) = csivar33(i+m,:);
    testdata(1,271:360) = csivar34(i+m,:);

%     testdata(1,361) = csieig31(i+m,:);
%     testdata(1,362) = csieig32(i+m,:);
%     testdata(1,363) = csieig33(i+m,:);
%     testdata(1,364) = csieig34(i+m,:);
    
    testlabel = 3;
    [predict_label,accuracy,dicision_values] = svmpredict(testlabel,testdata,model);
    switch predict_label
        case 0
            a = a + 1;
        case 1
            b = b + 1;
        case 2
            c = c + 1;
        case 3
            d = d + 1;
        case 4
            e = e + 1;
        case 5
            f = f + 1;            
        case 6
            g = g + 1; 
    end
end
result3(1) = a;
result3(2) = b;
result3(3) = c;
result3(4) = d;
result3(5) = e;
result3(6) = f;
result3(7) = g;
accuray3 = d/n;

a = 0; b = 0; c = 0; d = 0; e = 0; f = 0; g = 0;
for i = 1:n
    testdata(1,1:90) = csivar41(i+m,:);
    testdata(1,91:180) = csivar42(i+m,:);
    testdata(1,181:270) = csivar43(i+m,:);
    testdata(1,271:360) = csivar44(i+m,:);

%     testdata(1,361) = csieig41(i+m,:);
%     testdata(1,362) = csieig42(i+m,:);
%     testdata(1,363) = csieig43(i+m,:);
%     testdata(1,364) = csieig44(i+m,:);
    
    testlabel = 4;
    [predict_label,accuracy,dicision_values] = svmpredict(testlabel,testdata,model);
    switch predict_label
        case 0
            a = a + 1;
        case 1
            b = b + 1;
        case 2
            c = c + 1;
        case 3
            d = d + 1;
        case 4
            e = e + 1;
        case 5
            f = f + 1; 
        case 6
            g = g + 1; 
    end
end
result4(1) = a;
result4(2) = b;
result4(3) = c;
result4(4) = d;
result4(5) = e;
result4(6) = f;
result4(7) = g;
accuray4 = e/n;


a = 0; b = 0; c = 0; d = 0; e = 0; f = 0; g = 0;
for i = 1:n
    testdata(1,1:90) = csivar51(i+m,:);
    testdata(1,91:180) = csivar52(i+m,:);
    testdata(1,181:270) = csivar53(i+m,:);
    testdata(1,271:360) = csivar54(i+m,:);

%     testdata(1,361) = csieig51(i+m,:);
%     testdata(1,362) = csieig52(i+m,:);
%     testdata(1,363) = csieig53(i+m,:);
%     testdata(1,364) = csieig54(i+m,:);
    
    testlabel = 5;
    [predict_label,accuracy,dicision_values] = svmpredict(testlabel,testdata,model);
    switch predict_label
        case 0
            a = a + 1;
        case 1
            b = b + 1;
        case 2
            c = c + 1;
        case 3
            d = d + 1;
        case 4
            e = e + 1;
        case 5
            f = f + 1;     
        case 6
            g = g + 1; 
    end
end
result5(1) = a;
result5(2) = b;
result5(3) = c;
result5(4) = d;
result5(5) = e;
result5(6) = f;
result5(7) = g;
accuray5 = f/n;

a = 0; b = 0; c = 0; d = 0; e = 0; f = 0; g = 0;
for i = 1:n
    testdata(1,1:90) = csivar61(i+m,:);
    testdata(1,91:180) = csivar62(i+m,:);
    testdata(1,181:270) = csivar63(i+m,:);
    testdata(1,271:360) = csivar64(i+m,:);

%     testdata(1,361) = csieig61(i+m,:);
%     testdata(1,362) = csieig62(i+m,:);
%     testdata(1,363) = csieig63(i+m,:);
%     testdata(1,364) = csieig64(i+m,:);
    
    testlabel = 6;
    [predict_label,accuracy,dicision_values] = svmpredict(testlabel,testdata,model);
    switch predict_label
        case 0
            a = a + 1;
        case 1
            b = b + 1;
        case 2
            c = c + 1;
        case 3
            d = d + 1;
        case 4
            e = e + 1;
        case 5
            f = f + 1;     
        case 6
            g = g + 1; 
    end
end
result6(1) = a;
result6(2) = b;
result6(3) = c;
result6(4) = d;
result6(5) = e;
result6(6) = f;
result6(7) = g;
accuray6 = g/n;
%}


csivar01 = load('../../Data/count/2016-5-8-22/noperson/noperson1_csivarseg.txt');        
csivar11 = load('../../Data/count/2016-5-8-22/oneperson/oneperson1_csivarseg.txt');      
csivar21 = load('../../Data/count/2016-5-8-22/twoperson/twoperson1_csivarseg.txt');      
csivar31 = load('../../Data/count/2016-5-8-22/threeperson/threeperson1_csivarseg.txt');  
csivar41 = load('../../Data/count/2016-5-8-22/fourperson/fourperson1_csivarseg.txt');  
csivar51 = load('../../Data/count/2016-5-8-22/fiveperson/fiveperson1_csivarseg.txt');  
% csivar61 = load('../../Data/count/2016-5-8-22/sixperson/sixperson1_csivarseg.txt');    

csivar02 = load('../../Data/count/2016-5-8-22/noperson/noperson2_csivarseg.txt');        
csivar12 = load('../../Data/count/2016-5-8-22/oneperson/oneperson2_csivarseg.txt');      
csivar22 = load('../../Data/count/2016-5-8-22/twoperson/twoperson2_csivarseg.txt');      
csivar32 = load('../../Data/count/2016-5-8-22/threeperson/threeperson2_csivarseg.txt');  
csivar42 = load('../../Data/count/2016-5-8-22/fourperson/fourperson2_csivarseg.txt');  
csivar52 = load('../../Data/count/2016-5-8-22/fiveperson/fiveperson2_csivarseg.txt');  
% csivar62 = load('../../Data/count/2016-5-8-22/sixperson/sixperson2_csivarseg.txt');    

csivar03 = load('../../Data/count/2016-5-8-22/noperson/noperson3_csivarseg.txt');        
csivar13 = load('../../Data/count/2016-5-8-22/oneperson/oneperson3_csivarseg.txt');      
csivar23 = load('../../Data/count/2016-5-8-22/twoperson/twoperson3_csivarseg.txt');      
csivar33 = load('../../Data/count/2016-5-8-22/threeperson/threeperson3_csivarseg.txt');  
csivar43 = load('../../Data/count/2016-5-8-22/fourperson/fourperson3_csivarseg.txt');  
csivar53 = load('../../Data/count/2016-5-8-22/fiveperson/fiveperson3_csivarseg.txt');  
% csivar63 = load('../../Data/count/2016-5-8-22/sixperson/sixperson3_csivarseg.txt');    

csivar04 = load('../../Data/count/2016-5-8-22/noperson/noperson4_csivarseg.txt');        
csivar14 = load('../../Data/count/2016-5-8-22/oneperson/oneperson4_csivarseg.txt');      
csivar24 = load('../../Data/count/2016-5-8-22/twoperson/twoperson4_csivarseg.txt');      
csivar34 = load('../../Data/count/2016-5-8-22/threeperson/threeperson4_csivarseg.txt');  
csivar44 = load('../../Data/count/2016-5-8-22/fourperson/fourperson4_csivarseg.txt');  
csivar54 = load('../../Data/count/2016-5-8-22/fiveperson/fiveperson4_csivarseg.txt');  
% csivar64 = load('../../Data/count/2016-5-8-22/sixperson/sixperson4_csivarseg.txt');    

%%%%      eig value     %%%%
% csieig01 = load('../../Data/count/2016-5-8-22/noperson/noperson1_csieig.txt');        
% csieig11 = load('../../Data/count/2016-5-8-22/oneperson/oneperson1_csieig.txt');      
% csieig21 = load('../../Data/count/2016-5-8-22/twoperson/twoperson1_csieig.txt');      
% csieig31 = load('../../Data/count/2016-5-8-22/threeperson/threeperson1_csieig.txt');  
% csieig41 = load('../../Data/count/2016-5-8-22/fourperson/fourperson1_csieig.txt');  
% csieig51 = load('../../Data/count/2016-5-8-22/fiveperson/fiveperson1_csieig.txt');  
% csieig61 = load('../../Data/count/2016-5-8-22/sixperson/sixperson1_csieig.txt');    
% 
% csieig02 = load('../../Data/count/2016-5-8-22/noperson/noperson2_csieig.txt');        
% csieig12 = load('../../Data/count/2016-5-8-22/oneperson/oneperson2_csieig.txt');      
% csieig22 = load('../../Data/count/2016-5-8-22/twoperson/twoperson2_csieig.txt');      
% csieig32 = load('../../Data/count/2016-5-8-22/threeperson/threeperson2_csieig.txt');  
% csieig42 = load('../../Data/count/2016-5-8-22/fourperson/fourperson2_csieig.txt');  
% csieig52 = load('../../Data/count/2016-5-8-22/fiveperson/fiveperson2_csieig.txt');  
% csieig62 = load('../../Data/count/2016-5-8-22/sixperson/sixperson2_csieig.txt');    
% 
% csieig03 = load('../../Data/count/2016-5-8-22/noperson/noperson3_csieig.txt');        
% csieig13 = load('../../Data/count/2016-5-8-22/oneperson/oneperson3_csieig.txt');      
% csieig23 = load('../../Data/count/2016-5-8-22/twoperson/twoperson3_csieig.txt');      
% csieig33 = load('../../Data/count/2016-5-8-22/threeperson/threeperson3_csieig.txt');  
% csieig43 = load('../../Data/count/2016-5-8-22/fourperson/fourperson3_csieig.txt');  
% csieig53 = load('../../Data/count/2016-5-8-22/fiveperson/fiveperson3_csieig.txt');  
% csieig63 = load('../../Data/count/2016-5-8-22/sixperson/sixperson3_csieig.txt');    
% 
% csieig04 = load('../../Data/count/2016-5-8-22/noperson/noperson4_csieig.txt');        
% csieig14 = load('../../Data/count/2016-5-8-22/oneperson/oneperson4_csieig.txt');      
% csieig24 = load('../../Data/count/2016-5-8-22/twoperson/twoperson4_csieig.txt');      
% csieig34 = load('../../Data/count/2016-5-8-22/threeperson/threeperson4_csieig.txt');  
% csieig44 = load('../../Data/count/2016-5-8-22/fourperson/fourperson4_csieig.txt');  
% csieig54 = load('../../Data/count/2016-5-8-22/fiveperson/fiveperson4_csieig.txt');  
% csieig64 = load('../../Data/count/2016-5-8-22/sixperson/sixperson4_csieig.txt');    

%{
n = 290;

a = 0; b = 0; c = 0; d = 0; e = 0; f = 0; g = 0;
for i = 1:n                              %% noperson
    testdata(1,1:90) = csivar01(i,:);
    testdata(1,91:180) = csivar02(i,:);
    testdata(1,181:270) = csivar03(i,:);
    testdata(1,271:360) = csivar04(i,:);
    
%     testdata(1,361) = csieig01(i,:);
%     testdata(1,362) = csieig02(i,:);
%     testdata(1,363) = csieig03(i,:);
%     testdata(1,364) = csieig04(i,:);

    testlabel = 0;
    [predict_label,accuracy,dicision_values] = svmpredict(testlabel,testdata,model);
    switch predict_label
        case 0
            a = a + 1;
        case 1
            b = b + 1;
        case 2
            c = c + 1;
        case 3
            d = d + 1;
        case 4
            e = e + 1;
        case 5
            f = f + 1;  
        case 6
            g = g + 1;
    end
end
result0(1) = a;
result0(2) = b;
result0(3) = c;
result0(4) = d;
result0(5) = e;
result0(6) = f;
result0(7) = g;
accuray0 = a/n;

a = 0; b = 0; c = 0; d = 0; e = 0; f = 0; g = 0;
for i = 1:n                              %% oneperson
    testdata(1,1:90) = csivar11(i,:);
    testdata(1,91:180) = csivar12(i,:);
    testdata(1,181:270) = csivar13(i,:);
    testdata(1,271:360) = csivar14(i,:);
        
%     testdata(1,361) = csieig11(i,:);
%     testdata(1,362) = csieig12(i,:);
%     testdata(1,363) = csieig13(i,:);
%     testdata(1,364) = csieig14(i,:);

    
    testlabel = 1;
    [predict_label,accuracy,dicision_values] = svmpredict(testlabel,testdata,model);
    switch predict_label
        case 0
            a = a + 1;
        case 1
            b = b + 1;
        case 2
            c = c + 1;
        case 3
            d = d + 1;
        case 4
            e = e + 1;
        case 5
            f = f + 1;  
        case 6
            g = g + 1;
    end
end
result1(1) = a;
result1(2) = b;
result1(3) = c;
result1(4) = d;
result1(5) = e;
result1(6) = f;
result1(7) = g;
accuray1 = b/n;

a = 0; b = 0; c = 0; d = 0; e = 0; f = 0; g = 0;
for i = 1:n                              %% twoperson
    testdata(1,1:90) = csivar21(i,:);
    testdata(1,91:180) = csivar22(i,:);
    testdata(1,181:270) = csivar23(i,:);
    testdata(1,271:360) = csivar24(i,:);
    
%     testdata(1,361) = csieig21(i,:);
%     testdata(1,362) = csieig22(i,:);
%     testdata(1,363) = csieig23(i,:);
%     testdata(1,364) = csieig24(i,:);
    
    testlabel = 2;
    [predict_label,accuracy,dicision_values] = svmpredict(testlabel,testdata,model);
    switch predict_label
        case 0
            a = a + 1;
        case 1
            b = b + 1;
        case 2
            c = c + 1;
        case 3
            d = d + 1;
        case 4
            e = e + 1;
        case 5
            f = f + 1;  
        case 6
            g = g + 1;
    end
end
result2(1) = a;
result2(2) = b;
result2(3) = c;
result2(4) = d;
result2(5) = e;
result2(6) = f;
result2(7) = g;
accuray2 = c/n;

a = 0; b = 0; c = 0; d = 0; e = 0; f = 0; g = 0;
for i = 1:n                              %% threeperson
    testdata(1,1:90) = csivar31(i,:);
    testdata(1,91:180) = csivar32(i,:);
    testdata(1,181:270) = csivar33(i,:);
    testdata(1,271:360) = csivar34(i,:);
        
%     testdata(1,361) = csieig31(i,:);
%     testdata(1,362) = csieig32(i,:);
%     testdata(1,363) = csieig33(i,:);
%     testdata(1,364) = csieig34(i,:);
    
    testlabel = 3;
    [predict_label,accuracy,dicision_values] = svmpredict(testlabel,testdata,model);
    switch predict_label
        case 0
            a = a + 1;
        case 1
            b = b + 1;
        case 2
            c = c + 1;
        case 3
            d = d + 1;
        case 4
            e = e + 1;
        case 5
            f = f + 1;  
        case 6
            g = g + 1;
    end
end
result3(1) = a;
result3(2) = b;
result3(3) = c;
result3(4) = d;
result3(5) = e;
result3(6) = f;
result3(7) = g;
accuray3 = d/n;


a = 0; b = 0; c = 0; d = 0; e = 0; f = 0; g = 0;
for i = 1:n                              %% fourperson
    testdata(1,1:90) = csivar41(i,:);
    testdata(1,91:180) = csivar42(i,:);
    testdata(1,181:270) = csivar43(i,:);
    testdata(1,271:360) = csivar44(i,:);
        
%     testdata(1,361) = csieig41(i,:);
%     testdata(1,362) = csieig42(i,:);
%     testdata(1,363) = csieig43(i,:);
%     testdata(1,364) = csieig44(i,:);
    
    testlabel = 4;
    [predict_label,accuracy,dicision_values] = svmpredict(testlabel,testdata,model);
    switch predict_label
        case 0
            a = a + 1;
        case 1
            b = b + 1;
        case 2
            c = c + 1;
        case 3
            d = d + 1;
        case 4
            e = e + 1;
        case 5
            f = f + 1;  
        case 6
            g = g + 1;
    end
end
result4(1) = a;
result4(2) = b;
result4(3) = c;
result4(4) = d;
result4(5) = e;
result4(6) = f;
result4(7) = g;
accuray4 = e/n;


a = 0; b = 0; c = 0; d = 0; e = 0; f = 0; g = 0;
for i = 1:n                              %% fiveperson
    testdata(1,1:90) = csivar51(i,:);
    testdata(1,91:180) = csivar52(i,:);
    testdata(1,181:270) = csivar53(i,:);
    testdata(1,271:360) = csivar54(i,:);
        
%     testdata(1,361) = csieig51(i,:);
%     testdata(1,362) = csieig52(i,:);
%     testdata(1,363) = csieig53(i,:);
%     testdata(1,364) = csieig54(i,:);
    
    testlabel = 5;
    [predict_label,accuracy,dicision_values] = svmpredict(testlabel,testdata,model);
    switch predict_label
        case 0
            a = a + 1;
        case 1
            b = b + 1;
        case 2
            c = c + 1;
        case 3
            d = d + 1;
        case 4
            e = e + 1;
        case 5
            f = f + 1;  
        case 6
            g = g + 1;
    end
end
result5(1) = a;
result5(2) = b;
result5(3) = c;
result5(4) = d;
result5(5) = e;
result5(6) = f;
result5(7) = g;
accuray5 = f/n;
%}

%{
a = 0; b = 0; c = 0; d = 0; e = 0; f = 0; g = 0;
for i = 1:n                              %% sixperson
    testdata(1,1:90) = csivar61(i,:);
    testdata(1,91:180) = csivar62(i,:);
    testdata(1,181:270) = csivar63(i,:);
    testdata(1,271:360) = csivar64(i,:);
        
%     testdata(1,361) = csieig61(i,:);
%     testdata(1,362) = csieig62(i,:);
%     testdata(1,363) = csieig63(i,:);
%     testdata(1,364) = csieig64(i,:);
    
    testlabel = 6;
    [predict_label,accuracy,dicision_values] = svmpredict(testlabel,testdata,model);
    switch predict_label
        case 0
            a = a + 1;
        case 1
            b = b + 1;
        case 2
            c = c + 1;
        case 3
            d = d + 1;
        case 4
            e = e + 1;
        case 5
            f = f + 1;  
        case 6
            g = g + 1;
    end
end
result6(1) = a;
result6(2) = b;
result6(3) = c;
result6(4) = d;
result6(5) = e;
result6(6) = f;
result6(7) = g;
accuray6 = g/n;
%}








