clear;
clc;
%%%%            segmented var        %%%%
%%%%      first day    %%%%
csivar011 = load('../../Data/count/2016-5-5-22/noperson/noperson1_csivarseg.txt');        
csivar111 = load('../../Data/count/2016-5-5-22/oneperson/oneperson1_csivarseg.txt');      
csivar211 = load('../../Data/count/2016-5-5-22/twoperson/twoperson1_csivarseg.txt');      
csivar311 = load('../../Data/count/2016-5-5-22/threeperson/threeperson1_csivarseg.txt');  
csivar411 = load('../../Data/count/2016-5-5-22/fourperson/fourperson1_csivarseg.txt');  
csivar511 = load('../../Data/count/2016-5-5-22/fiveperson/fiveperson1_csivarseg.txt');  
% csivar611 = load('../../Data/count/2016-5-5-22/sixperson/sixperson1_csivarseg.txt');    

csivar012 = load('../../Data/count/2016-5-5-22/noperson/noperson2_csivarseg.txt');        
csivar112 = load('../../Data/count/2016-5-5-22/oneperson/oneperson2_csivarseg.txt');      
csivar212 = load('../../Data/count/2016-5-5-22/twoperson/twoperson2_csivarseg.txt');      
csivar312 = load('../../Data/count/2016-5-5-22/threeperson/threeperson2_csivarseg.txt');  
csivar412 = load('../../Data/count/2016-5-5-22/fourperson/fourperson2_csivarseg.txt');  
csivar512 = load('../../Data/count/2016-5-5-22/fiveperson/fiveperson2_csivarseg.txt');  
% csivar612 = load('../../Data/count/2016-5-5-22/sixperson/sixperson2_csivarseg.txt');    

csivar013 = load('../../Data/count/2016-5-5-22/noperson/noperson3_csivarseg.txt');        
csivar113 = load('../../Data/count/2016-5-5-22/oneperson/oneperson3_csivarseg.txt');      
csivar213 = load('../../Data/count/2016-5-5-22/twoperson/twoperson3_csivarseg.txt');      
csivar313 = load('../../Data/count/2016-5-5-22/threeperson/threeperson3_csivarseg.txt');  
csivar413 = load('../../Data/count/2016-5-5-22/fourperson/fourperson3_csivarseg.txt');  
csivar513 = load('../../Data/count/2016-5-5-22/fiveperson/fiveperson3_csivarseg.txt');  
% csivar613 = load('../../Data/count/2016-5-5-22/sixperson/sixperson3_csivarseg.txt');    

csivar014 = load('../../Data/count/2016-5-5-22/noperson/noperson4_csivarseg.txt');        
csivar114 = load('../../Data/count/2016-5-5-22/oneperson/oneperson4_csivarseg.txt');      
csivar214 = load('../../Data/count/2016-5-5-22/twoperson/twoperson4_csivarseg.txt');      
csivar314 = load('../../Data/count/2016-5-5-22/threeperson/threeperson4_csivarseg.txt');  
csivar414 = load('../../Data/count/2016-5-5-22/fourperson/fourperson4_csivarseg.txt');  
csivar514 = load('../../Data/count/2016-5-5-22/fiveperson/fiveperson4_csivarseg.txt');  
% csivar614 = load('../../Data/count/2016-5-5-22/sixperson/sixperson4_csivarseg.txt');    
%%%%      second day    %%%%
csivar021 = load('../../Data/count/2016-5-6-22/noperson/noperson1_csivarseg.txt');        
csivar121 = load('../../Data/count/2016-5-6-22/oneperson/oneperson1_csivarseg.txt');      
csivar221 = load('../../Data/count/2016-5-6-22/twoperson/twoperson1_csivarseg.txt');      
csivar321 = load('../../Data/count/2016-5-6-22/threeperson/threeperson1_csivarseg.txt');  
csivar421 = load('../../Data/count/2016-5-6-22/fourperson/fourperson1_csivarseg.txt');  
csivar521 = load('../../Data/count/2016-5-6-22/fiveperson/fiveperson1_csivarseg.txt');  
% csivar621 = load('../../Data/count/2016-5-6-22/sixperson/sixperson1_csivarseg.txt');    

csivar022 = load('../../Data/count/2016-5-6-22/noperson/noperson2_csivarseg.txt');        
csivar122 = load('../../Data/count/2016-5-6-22/oneperson/oneperson2_csivarseg.txt');      
csivar222 = load('../../Data/count/2016-5-6-22/twoperson/twoperson2_csivarseg.txt');      
csivar322 = load('../../Data/count/2016-5-6-22/threeperson/threeperson2_csivarseg.txt');  
csivar422 = load('../../Data/count/2016-5-6-22/fourperson/fourperson2_csivarseg.txt');  
csivar522 = load('../../Data/count/2016-5-6-22/fiveperson/fiveperson2_csivarseg.txt');  
% csivar622 = load('../../Data/count/2016-5-6-22/sixperson/sixperson2_csivarseg.txt');    

csivar023 = load('../../Data/count/2016-5-6-22/noperson/noperson3_csivarseg.txt');        
csivar123 = load('../../Data/count/2016-5-6-22/oneperson/oneperson3_csivarseg.txt');      
csivar223 = load('../../Data/count/2016-5-6-22/twoperson/twoperson3_csivarseg.txt');      
csivar323 = load('../../Data/count/2016-5-6-22/threeperson/threeperson3_csivarseg.txt');  
csivar423 = load('../../Data/count/2016-5-6-22/fourperson/fourperson3_csivarseg.txt');  
csivar523 = load('../../Data/count/2016-5-6-22/fiveperson/fiveperson3_csivarseg.txt');  
% csivar623 = load('../../Data/count/2016-5-6-22/sixperson/sixperson3_csivarseg.txt');    

csivar024 = load('../../Data/count/2016-5-6-22/noperson/noperson4_csivarseg.txt');        
csivar124 = load('../../Data/count/2016-5-6-22/oneperson/oneperson4_csivarseg.txt');      
csivar224 = load('../../Data/count/2016-5-6-22/twoperson/twoperson4_csivarseg.txt');      
csivar324 = load('../../Data/count/2016-5-6-22/threeperson/threeperson4_csivarseg.txt');  
csivar424 = load('../../Data/count/2016-5-6-22/fourperson/fourperson4_csivarseg.txt');  
csivar524 = load('../../Data/count/2016-5-6-22/fiveperson/fiveperson4_csivarseg.txt');  
% csivar624 = load('../../Data/count/2016-5-6-22/sixperson/sixperson4_csivarseg.txt'); 



m = 290;
% n = 150;


data(1:m,1:90) = csivar011(1:m,:);                   %%   noperson's trainning data
data(1:m,91:180) = csivar012(1:m,:);
data(1:m,181:270) = csivar013(1:m,:);
data(1:m,271:360) = csivar014(1:m,:);

data(m+1:2*m,361:450) = csivar021(1:m,:);
data(m+1:2*m,451:540) = csivar022(1:m,:);
data(m+1:2*m,541:630) = csivar023(1:m,:);
data(m+1:2*m,631:720) = csivar024(1:m,:);

data(2*m+1:3*m,1:90) = csivar111(1:m,:);               %%   oneperson's trainning data
data(2*m+1:3*m,91:180) = csivar112(1:m,:);
data(2*m+1:3*m,181:270) = csivar113(1:m,:);
data(2*m+1:3*m,271:360) = csivar114(1:m,:);

data(3*m+1:4*m,361:450) = csivar121(1:m,:);
data(3*m+1:4*m,451:540) = csivar122(1:m,:);
data(3*m+1:4*m,541:630) = csivar123(1:m,:);
data(3*m+1:4*m,631:720) = csivar124(1:m,:);

data(4*m+1:5*m,1:90) = csivar211(1:m,:);             %%   twoperson's trainning data
data(4*m+1:5*m,91:180) = csivar212(1:m,:);
data(4*m+1:5*m,181:270) = csivar213(1:m,:);
data(4*m+1:5*m,271:360) = csivar214(1:m,:);

data(5*m+1:6*m,361:450) = csivar221(1:m,:);
data(5*m+1:6*m,451:540) = csivar222(1:m,:);
data(5*m+1:6*m,541:630) = csivar223(1:m,:);
data(5*m+1:6*m,631:720) = csivar224(1:m,:);

data(6*m+1:7*m,1:90) = csivar311(1:m,:);             %%   threeperson's trainning data
data(6*m+1:7*m,91:180) = csivar312(1:m,:);
data(6*m+1:7*m,181:270) = csivar313(1:m,:);
data(6*m+1:7*m,271:360) = csivar314(1:m,:);

data(7*m+1:8*m,361:450) = csivar321(1:m,:);
data(7*m+1:8*m,451:540) = csivar322(1:m,:);
data(7*m+1:8*m,541:630) = csivar323(1:m,:);
data(7*m+1:8*m,631:720) = csivar324(1:m,:);

data(8*m+1:9*m,1:90) = csivar411(1:m,:);             %%   fourperson's trainning data
data(8*m+1:9*m,91:180) = csivar412(1:m,:);
data(8*m+1:9*m,181:270) = csivar413(1:m,:);
data(8*m+1:9*m,271:360) = csivar414(1:m,:);

data(9*m+1:10*m,361:450) = csivar421(1:m,:);
data(9*m+1:10*m,451:540) = csivar422(1:m,:);
data(9*m+1:10*m,541:630) = csivar423(1:m,:);
data(9*m+1:10*m,631:720) = csivar424(1:m,:);

data(10*m+1:11*m,1:90) = csivar511(1:m,:);             %%   fiveperson's trainning data
data(10*m+1:11*m,91:180) = csivar512(1:m,:);
data(10*m+1:11*m,181:270) = csivar513(1:m,:);
data(10*m+1:11*m,271:360) = csivar514(1:m,:);

data(11*m+1:12*m,361:450) = csivar521(1:m,:);
data(11*m+1:12*m,451:540) = csivar522(1:m,:);
data(11*m+1:12*m,541:630) = csivar523(1:m,:);
data(11*m+1:12*m,631:720) = csivar524(1:m,:);

%{
data(12*m+1:13*m,1:90) = csivar611(1:m,:);             %%   sixperson's trainning data
data(12*m+1:13*m,91:180) = csivar612(1:m,:);
data(12*m+1:13*m,181:270) = csivar613(1:m,:);
data(12*m+1:13*m,271:360) = csivar614(1:m,:);

data(13*m+1:14*m,361:450) = csivar621(1:m,:);             %%   sixperson's trainning data
data(13*m+1:14*m,451:540) = csivar622(1:m,:);
data(13*m+1:14*m,541:630) = csivar623(1:m,:);
data(13*m+1:14*m,631:720) = csivar624(1:m,:);
%}

label(1:2*m,1) = 0;
label(2*m+1:4*m,1) = 1;
label(4*m+1:6*m,1) = 2;
label(6*m+1:8*m,1) = 3;
label(8*m+1:10*m,1) = 4;
label(10*m+1:12*m,1) = 5;
% label(12*m+1:14*m,1) = 6;

% model = svmtrain(label,data,'-t 1 -d 2');
model = svmtrain(label,data,'-t 2 -c 3.5 -g 0.00001 -e 0.000001');
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


n = 290;

a = 0; b = 0; c = 0; d = 0; e = 0; f = 0; g = 0;
for i = 1:n                              %% noperson
    testdata(1,1:90) = csivar01(i,:);
    testdata(1,91:180) = csivar02(i,:);
    testdata(1,181:270) = csivar03(i,:);
    testdata(1,271:360) = csivar04(i,:);

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
    testdata(1,1:90) = csivar61(i,:);
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








