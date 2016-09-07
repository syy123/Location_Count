clear;
clc;
%%%%            segmented var        %%%%
csivar01 = load('../../Data/count/2016-5-7-22/noperson/noperson1_csivarseg.txt');        
csivar11 = load('../../Data/count/2016-5-7-22/oneperson/oneperson1_csivarseg.txt');      
csivar21 = load('../../Data/count/2016-5-7-22/twoperson/twoperson1_csivarseg.txt');      
csivar31 = load('../../Data/count/2016-5-7-22/threeperson/threeperson1_csivarseg.txt');  
csivar41 = load('../../Data/count/2016-5-7-22/fourperson/fourperson1_csivarseg.txt');  
csivar51 = load('../../Data/count/2016-5-7-22/fiveperson/fiveperson1_csivarseg.txt');  
% csivar61 = load('../../Data/count/2016-5-7-22/sixperson/sixperson1_csivarseg.txt');    

csivar02 = load('../../Data/count/2016-5-7-22/noperson/noperson2_csivarseg.txt');        
csivar12 = load('../../Data/count/2016-5-7-22/oneperson/oneperson2_csivarseg.txt');      
csivar22 = load('../../Data/count/2016-5-7-22/twoperson/twoperson2_csivarseg.txt');      
csivar32 = load('../../Data/count/2016-5-7-22/threeperson/threeperson2_csivarseg.txt');  
csivar42 = load('../../Data/count/2016-5-7-22/fourperson/fourperson2_csivarseg.txt');  
csivar52 = load('../../Data/count/2016-5-7-22/fiveperson/fiveperson2_csivarseg.txt');  
% csivar62 = load('../../Data/count/2016-5-7-22/sixperson/sixperson2_csivarseg.txt');    


csivar03 = load('../../Data/count/2016-5-7-22/noperson/noperson3_csivarseg.txt');        
csivar13 = load('../../Data/count/2016-5-7-22/oneperson/oneperson3_csivarseg.txt');      
csivar23 = load('../../Data/count/2016-5-7-22/twoperson/twoperson3_csivarseg.txt');      
csivar33 = load('../../Data/count/2016-5-7-22/threeperson/threeperson3_csivarseg.txt');  
csivar43 = load('../../Data/count/2016-5-7-22/fourperson/fourperson3_csivarseg.txt');  
csivar53 = load('../../Data/count/2016-5-7-22/fiveperson/fiveperson3_csivarseg.txt');  
% csivar63 = load('../../Data/count/2016-5-7-22/sixperson/sixperson3_csivarseg.txt');    

csivar04 = load('../../Data/count/2016-5-7-22/noperson/noperson4_csivarseg.txt');        
csivar14 = load('../../Data/count/2016-5-7-22/oneperson/oneperson4_csivarseg.txt');      
csivar24 = load('../../Data/count/2016-5-7-22/twoperson/twoperson4_csivarseg.txt');      
csivar34 = load('../../Data/count/2016-5-7-22/threeperson/threeperson4_csivarseg.txt');  
csivar44 = load('../../Data/count/2016-5-7-22/fourperson/fourperson4_csivarseg.txt');  
csivar54 = load('../../Data/count/2016-5-7-22/fiveperson/fiveperson4_csivarseg.txt');  
% csivar64 = load('../../Data/count/2016-5-7-22/sixperson/sixperson4_csivarseg.txt');    

m = 270;

data(1:m,1:10) = csivar01(1:m,1:10);   
data(1:m,11:20) = csivar01(1:m,31:40);
data(1:m,21:30) = csivar01(1:m,61:70);
data(1:m,31:40) = csivar02(1:m,1:10);
data(1:m,41:50) = csivar02(1:m,31:40);
data(1:m,51:60) = csivar02(1:m,61:70);
data(1:m,61:70) = csivar03(1:m,1:10);
data(1:m,71:80) = csivar03(1:m,31:40);
data(1:m,81:90) = csivar03(1:m,61:70);
data(1:m,91:100) = csivar04(1:m,1:10);
data(1:m,101:110) = csivar04(1:m,31:40);
data(1:m,111:120) = csivar04(1:m,61:70);

data(m+1:2*m,1:10) = csivar11(1:m,1:10);                   
data(m+1:2*m,11:20) = csivar11(1:m,31:40);
data(m+1:2*m,21:30) = csivar11(1:m,61:70);
data(m+1:2*m,31:40) = csivar12(1:m,1:10);
data(m+1:2*m,41:50) = csivar12(1:m,31:40);
data(m+1:2*m,51:60) = csivar12(1:m,61:70);
data(m+1:2*m,61:70) = csivar13(1:m,1:10);
data(m+1:2*m,71:80) = csivar13(1:m,31:40);
data(m+1:2*m,81:90) = csivar13(1:m,61:70);
data(m+1:2*m,91:100) = csivar14(1:m,1:10);
data(m+1:2*m,101:110) = csivar14(1:m,31:40);
data(m+1:2*m,111:120) = csivar14(1:m,61:70);

data(2*m+1:3*m,1:10) = csivar21(1:m,1:10);  
data(2*m+1:3*m,11:20) = csivar21(1:m,31:40);
data(2*m+1:3*m,21:30) = csivar21(1:m,61:70);
data(2*m+1:3*m,31:40) = csivar22(1:m,1:10);
data(2*m+1:3*m,41:50) = csivar22(1:m,31:40);
data(2*m+1:3*m,51:60) = csivar22(1:m,61:70);
data(2*m+1:3*m,61:70) = csivar23(1:m,1:10);
data(2*m+1:3*m,71:80) = csivar23(1:m,31:40);
data(2*m+1:3*m,81:90) = csivar23(1:m,61:70);
data(2*m+1:3*m,91:100) = csivar24(1:m,1:10);
data(2*m+1:3*m,101:110) = csivar24(1:m,31:40);
data(2*m+1:3*m,111:120) = csivar24(1:m,61:70);

data(3*m+1:4*m,1:10) = csivar31(1:m,1:10);  
data(3*m+1:4*m,11:20) = csivar31(1:m,31:40);
data(3*m+1:4*m,21:30) = csivar31(1:m,61:70);
data(3*m+1:4*m,31:40) = csivar32(1:m,1:10);
data(3*m+1:4*m,41:50) = csivar32(1:m,31:40);
data(3*m+1:4*m,51:60) = csivar32(1:m,61:70);
data(3*m+1:4*m,61:70) = csivar33(1:m,1:10);
data(3*m+1:4*m,71:80) = csivar33(1:m,31:40);
data(3*m+1:4*m,81:90) = csivar33(1:m,61:70);
data(3*m+1:4*m,91:100) = csivar34(1:m,1:10);
data(3*m+1:4*m,101:110) = csivar34(1:m,31:40);
data(3*m+1:4*m,111:120) = csivar34(1:m,61:70);

data(4*m+1:5*m,1:10) = csivar41(1:m,1:10);  
data(4*m+1:5*m,11:20) = csivar41(1:m,31:40);
data(4*m+1:5*m,21:30) = csivar41(1:m,61:70);
data(4*m+1:5*m,31:40) = csivar42(1:m,1:10);
data(4*m+1:5*m,41:50) = csivar42(1:m,31:40);
data(4*m+1:5*m,51:60) = csivar42(1:m,61:70);
data(4*m+1:5*m,61:70) = csivar43(1:m,1:10);
data(4*m+1:5*m,71:80) = csivar43(1:m,31:40);
data(4*m+1:5*m,81:90) = csivar43(1:m,61:70);
data(4*m+1:5*m,91:100) = csivar44(1:m,1:10);
data(4*m+1:5*m,101:110) = csivar44(1:m,31:40);
data(4*m+1:5*m,111:120) = csivar44(1:m,61:70);

data(5*m+1:6*m,1:10) = csivar51(1:m,1:10);  
data(5*m+1:6*m,11:20) = csivar51(1:m,31:40);
data(5*m+1:6*m,21:30) = csivar51(1:m,61:70);
data(5*m+1:6*m,31:40) = csivar52(1:m,1:10);
data(5*m+1:6*m,41:50) = csivar52(1:m,31:40);
data(5*m+1:6*m,51:60) = csivar52(1:m,61:70);
data(5*m+1:6*m,61:70) = csivar53(1:m,1:10);
data(5*m+1:6*m,71:80) = csivar53(1:m,31:40);
data(5*m+1:6*m,81:90) = csivar53(1:m,61:70);
data(5*m+1:6*m,91:100) = csivar54(1:m,1:10);
data(5*m+1:6*m,101:110) = csivar54(1:m,31:40);
data(5*m+1:6*m,111:120) = csivar54(1:m,61:70);

%{
data(6*m+1:7*m,1:70) = csivar61(1:m,:);             %%   sixperson's trainning data
data(6*m+1:7*m,91:180) = csivar62(1:m,:);
data(6*m+1:7*m,181:270) = csivar63(1:m,:);
data(6*m+1:7*m,271:360) = csivar64(1:m,:);
%}

label(1:m,1) = 0;
label(m+1:2*m,1) = 1;
label(2*m+1:3*m,1) = 2;
label(3*m+1:4*m,1) = 3;
label(4*m+1:5*m,1) = 4;
label(5*m+1:6*m,1) = 5;
% label(6*m+1:7*m,1) = 6;

% model = svmtrain(label,data,'-t 1 -d 2');
model = svmtrain(label,data,'-t 2 -c 4 -g 0.0002 -e 0.000001');
% model = svmtrain(label,data,'-t 2 -c 4 -g 0.00006 -e 0.000001');
% [predict_label,accuracy,dicision_values] = svmpredict(label,data,model);


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

n = 270;

a = 0; b = 0; c = 0; d = 0; e = 0; f = 0; g = 0;
for i = 1:n                              %% noperson
    testdata(1,1:10) = csivar01(i,1:10);   
    testdata(1,11:20) = csivar01(i,31:40);
    testdata(1,21:30) = csivar01(i,61:70);
    testdata(1,31:40) = csivar02(i,1:10);
    testdata(1,41:50) = csivar02(i,31:40);
    testdata(1,51:60) = csivar02(i,61:70);
    testdata(1,61:70) = csivar03(i,1:10);
    testdata(1,71:80) = csivar03(i,31:40);
    testdata(1,81:90) = csivar03(i,61:70);
    testdata(1,91:100) = csivar04(i,1:10);
    testdata(1,101:110) = csivar04(i,31:40);
    testdata(1,111:120) = csivar04(i,61:70);
    

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
    testdata(1,1:10) = csivar11(i,1:10);   
    testdata(1,11:20) = csivar11(i,31:40);
    testdata(1,21:30) = csivar11(i,61:70);
    testdata(1,31:40) = csivar12(i,1:10);
    testdata(1,41:50) = csivar12(i,31:40);
    testdata(1,51:60) = csivar12(i,61:70);
    testdata(1,61:70) = csivar13(i,1:10);
    testdata(1,71:80) = csivar13(i,31:40);
    testdata(1,81:90) = csivar13(i,61:70);
    testdata(1,91:100) = csivar14(i,1:10);
    testdata(1,101:110) = csivar14(i,31:40);
    testdata(1,111:120) = csivar14(i,61:70);

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
    testdata(1,1:10) = csivar21(i,1:10);   
    testdata(1,11:20) = csivar21(i,31:40);
    testdata(1,21:30) = csivar21(i,61:70);
    testdata(1,31:40) = csivar22(i,1:10);
    testdata(1,41:50) = csivar22(i,31:40);
    testdata(1,51:60) = csivar22(i,61:70);
    testdata(1,61:70) = csivar23(i,1:10);
    testdata(1,71:80) = csivar23(i,31:40);
    testdata(1,81:90) = csivar23(i,61:70);
    testdata(1,91:100) = csivar24(i,1:10);
    testdata(1,101:110) = csivar24(i,31:40);
    testdata(1,111:120) = csivar24(i,61:70);
    
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
    testdata(1,1:10) = csivar31(i,1:10);   
    testdata(1,11:20) = csivar31(i,31:40);
    testdata(1,21:30) = csivar31(i,61:70);
    testdata(1,31:40) = csivar32(i,1:10);
    testdata(1,41:50) = csivar32(i,31:40);
    testdata(1,51:60) = csivar32(i,61:70);
    testdata(1,61:70) = csivar33(i,1:10);
    testdata(1,71:80) = csivar33(i,31:40);
    testdata(1,81:90) = csivar33(i,61:70);
    testdata(1,91:100) = csivar34(i,1:10);
    testdata(1,101:110) = csivar34(i,31:40);
    testdata(1,111:120) = csivar34(i,61:70);
    
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
    testdata(1,1:10) = csivar41(i,1:10);   
    testdata(1,11:20) = csivar41(i,31:40);
    testdata(1,21:30) = csivar41(i,61:70);
    testdata(1,31:40) = csivar42(i,1:10);
    testdata(1,41:50) = csivar42(i,31:40);
    testdata(1,51:60) = csivar42(i,61:70);
    testdata(1,61:70) = csivar43(i,1:10);
    testdata(1,71:80) = csivar43(i,31:40);
    testdata(1,81:90) = csivar43(i,61:70);
    testdata(1,91:100) = csivar44(i,1:10);
    testdata(1,101:110) = csivar44(i,31:40);
    testdata(1,111:120) = csivar44(i,61:70);
    
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
    testdata(1,1:10) = csivar51(i,1:10);   
    testdata(1,11:20) = csivar51(i,31:40);
    testdata(1,21:30) = csivar51(i,61:70);
    testdata(1,31:40) = csivar52(i,1:10);
    testdata(1,41:50) = csivar52(i,31:40);
    testdata(1,51:60) = csivar52(i,61:70);
    testdata(1,61:70) = csivar53(i,1:10);
    testdata(1,71:80) = csivar53(i,31:40);
    testdata(1,81:90) = csivar53(i,61:70);
    testdata(1,91:100) = csivar54(i,1:10);
    testdata(1,101:110) = csivar54(i,31:40);
    testdata(1,111:120) = csivar54(i,61:70);
    
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
%{
a = 0; b = 0; c = 0; d = 0; e = 0; f = 0; g = 0;
for i = 1:n                              %% sixperson
    testdata(1,1:70) = csivar61(i,:);
    testdata(1,91:180) = csivar62(i,:);
    testdata(1,181:270) = csivar63(i,:);
    testdata(1,271:360) = csivar64(i,:);
    
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








