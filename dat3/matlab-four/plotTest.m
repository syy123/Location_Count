csivar01 = load('../../Data/count/2016-5-5-22/noperson/noperson1_csivarseg.txt');
csivar02 = load('../../Data/count/2016-5-8-22/noperson/noperson1_csivarseg.txt');
csivar11 = load('../../Data/count/2016-5-5-22/oneperson/oneperson1_csivarseg.txt');
csivar12 = load('../../Data/count/2016-5-8-22/oneperson/oneperson1_csivarseg.txt');
csivar21 = load('../../Data/count/2016-5-5-22/twoperson/twoperson1_csivarseg.txt');
csivar22 = load('../../Data/count/2016-5-8-22/twoperson/twoperson1_csivarseg.txt');
csivar31 = load('../../Data/count/2016-5-5-22/threeperson/threeperson1_csivarseg.txt');
csivar32 = load('../../Data/count/2016-5-8-22/threeperson/threeperson1_csivarseg.txt');
csivar41 = load('../../Data/count/2016-5-5-22/fourperson/fourperson1_csivarseg.txt');
csivar42 = load('../../Data/count/2016-5-8-22/fourperson/fourperson1_csivarseg.txt');
csivar51 = load('../../Data/count/2016-5-5-22/fiveperson/fiveperson1_csivarseg.txt');
csivar52 = load('../../Data/count/2016-5-8-22/fiveperson/fiveperson1_csivarseg.txt');
csivar61 = load('../../Data/count/2016-5-5-22/sixperson/sixperson1_csivarseg.txt');
csivar62 = load('../../Data/count/2016-5-8-22/sixperson/sixperson1_csivarseg.txt');


index = input('please input the index of the subcarrier, 0 to quit:');
m = 1;
n = 290;
while index ~= 0
    figure(1)
    clf;
    [f,xi] = ksdensity(csivar01(m:n,index));
    plot(xi,f,'r');
    hold on;
    [f,xi] = ksdensity(csivar02(m:n,index));
    plot(xi,f,'g');
    hold on;
    title('noperson');
    legend('5-5-22', '5-8-22', 'Location', 'SouthEast');
    
    figure(2)
    clf;
    [f,xi] = ksdensity(csivar11(m:n,index));
    plot(xi,f,'r');
    hold on;
    [f,xi] = ksdensity(csivar12(m:n,index));
    plot(xi,f,'g');
    hold on;
    title('oneperson');
    legend('5-5-22', '5-8-22', 'Location', 'SouthEast');
    
    figure(3)
    clf;
    [f,xi] = ksdensity(csivar21(m:n,index));
    plot(xi,f,'r');
    hold on;
    [f,xi] = ksdensity(csivar22(m:n,index));
    plot(xi,f,'g');
    hold on;   
    title('twoperson');
    legend('5-5-22', '5-8-22', 'Location', 'SouthEast');
    
    figure(4)
    clf;
    [f,xi] = ksdensity(csivar31(m:n,index));
    plot(xi,f,'r');
    hold on;
    [f,xi] = ksdensity(csivar32(m:n,index));
    plot(xi,f,'g');
    hold on;    
    title('threeperson');
    legend('5-5-22', '5-8-22', 'Location', 'SouthEast');
    
    figure(5)
    clf;
    [f,xi] = ksdensity(csivar41(m:n,index));
    plot(xi,f,'r');
    hold on;
    [f,xi] = ksdensity(csivar42(m:n,index));
    plot(xi,f,'g');
    hold on;    
    title('fourperson');
    legend('5-5-22', '5-8-22', 'Location', 'SouthEast');
    
    figure(6)
    clf;
    [f,xi] = ksdensity(csivar51(m:n,index));
    plot(xi,f,'r');
    hold on;
    [f,xi] = ksdensity(csivar52(m:n,index));
    plot(xi,f,'g');
    hold on;    
    title('fiveperson');
    legend('5-5-22', '5-8-22', 'Location', 'SouthEast');
    
    figure(7)
    clf;
    [f,xi] = ksdensity(csivar61(m:n,index));
    plot(xi,f,'r');
    hold on;
    [f,xi] = ksdensity(csivar62(m:n,index));
    plot(xi,f,'g');
    hold on;    
    title('sixperson');
    legend('5-5-22', '5-8-22', 'Location', 'SouthEast');

    figure(8)
    clf;
    [f,xi] = ksdensity(csivar01(m:n,index));
    plot(xi,f,'r');
    hold on;
    [f,xi] = ksdensity(csivar11(m:n,index));
    plot(xi,f,'g');
    hold on;
    [f,xi] = ksdensity(csivar21(m:n,index));
    plot(xi,f,'b');
    hold on;
    [f,xi] = ksdensity(csivar31(m:n,index));
    plot(xi,f,'k')
    hold on;
    [f,xi] = ksdensity(csivar41(m:n,index));
    plot(xi,f,'c')
    hold on;    
    [f,xi] = ksdensity(csivar51(m:n,index));
    plot(xi,f,'y')
    hold on;
    [f,xi] = ksdensity(csivar61(m:n,index));
    plot(xi,f,'m')
    hold on;    
    title('5-5-22');
%     axis([0 15 0 1]);
    ylim([0 0.6]);
    legend('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'Location', 'SouthEast' );
    
    figure(9)
    clf;
    [f,xi] = ksdensity(csivar02(m:n,index));
    plot(xi,f,'r');
    hold on;
    [f,xi] = ksdensity(csivar12(m:n,index));
    plot(xi,f,'g');
    hold on;
    [f,xi] = ksdensity(csivar22(m:n,index));
    plot(xi,f,'b');
    hold on;
    [f,xi] = ksdensity(csivar32(m:n,index));
    plot(xi,f,'k')
    hold on;
    [f,xi] = ksdensity(csivar42(m:n,index));
    plot(xi,f,'c')
    hold on;    
    [f,xi] = ksdensity(csivar52(m:n,index));
    plot(xi,f,'y')
    hold on;
    [f,xi] = ksdensity(csivar62(m:n,index));
    plot(xi,f,'m')
    hold on;    
    title('5-8-22');
%     axis([0 15 0 1]);
    ylim([0 0.6]);
    legend('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'Location', 'SouthEast' );
%{    
    figure(7)
    clf;
    [f,xi] = ksdensity(csivar03(m:n,index));
    plot(xi,f,'r');
    hold on;
    [f,xi] = ksdensity(csivar13(m:n,index));
    plot(xi,f,'g');
    hold on;
    [f,xi] = ksdensity(csivar23(m:n,index));
    plot(xi,f,'b');
    hold on;
    [f,xi] = ksdensity(csivar33(m:n,index));
    plot(xi,f,'k');
    hold on;
    title('4-20');
    axis([0 10 0 1]);
    legend('zero', 'one', 'two', 'three', 'Location', 'SouthEast' );

    figure(8)
    clf;
    [f,xi] = ksdensity(csivar04(m:n,index));
    plot(xi,f,'r');
    hold on;
    [f,xi] = ksdensity(csivar14(m:n,index));
    plot(xi,f,'g');
    hold on;
    [f,xi] = ksdensity(csivar24(m:n,index));
    plot(xi,f,'b');
    hold on;
    [f,xi] = ksdensity(csivar34(m:n,index));
    plot(xi,f,'k');
    hold on;
    title('4-20');
    axis([0 10 0 1]);
    legend('zero', 'one', 'two', 'three', 'Location', 'SouthEast' );
    
    figure(9)
    clf
    plot(csivar11(m:n,index),'r');
    hold on;
    plot(csivar21(m:n,index),'g');
    hold on;
    plot(csivar31(m:n,index),'b');
    hold on;    
%     title('zero');
    legend('oneperson', 'twoperson', 'threeperson', 'Location', 'SouthEast' );
%     legend('4-19-8', '4-19-10', '4-20', 'Location', 'SouthEast' );
    
    figure(10)
    clf
    plot(csivar12(m:n,index),'r');
    hold on;
    plot(csivar22(m:n,index),'g');
    hold on;
    plot(csivar32(m:n,index),'b');
    hold on;    
%     title('one');
    legend('oneperson', 'twoperson', 'threeperson', 'Location', 'SouthEast' );
%     legend('4-19-8', '4-19-10', '4-20', 'Location', 'SouthEast' );
    
    figure(11)
    clf
    plot(csivar13(m:n,index),'r');
    hold on;
    plot(csivar23(m:n,index),'g');
    hold on;
    plot(csivar33(m:n,index),'b');
    hold on;    
%     title('two');
    legend('oneperson', 'twoperson', 'threeperson', 'Location', 'SouthEast' );
%     legend('4-19-8', '4-19-10', '4-20', 'Location', 'SouthEast' );

    
    figure(12)
    clf
    plot(csivar14(m:n,index),'r');
    hold on;
    plot(csivar24(m:n,index),'g');
    hold on;
    plot(csivar34(m:n,index),'b');
    hold on;  
%     title('three');
    legend('oneperson', 'twoperson', 'threeperson', 'Location', 'SouthEast' );
%     legend('4-19-8', '4-19-10', '4-20', 'Location', 'SouthEast' );
%}    
    index = input('please input the index of the subcarrier, 0 to quit:');
end

csieig01 = load('../../Data/count/2016-5-8-22/noperson/noperson1_csieig.txt');
csieig11 = load('../../Data/count/2016-5-8-22/oneperson/oneperson1_csieig.txt');
csieig21 = load('../../Data/count/2016-5-8-22/twoperson/twoperson1_csieig.txt');
csieig31 = load('../../Data/count/2016-5-8-22/threeperson/threeperson1_csieig.txt');
csieig41 = load('../../Data/count/2016-5-8-22/fourperson/fourperson1_csieig.txt');
csieig51 = load('../../Data/count/2016-5-8-22/fiveperson/fiveperson1_csieig.txt');
csieig61 = load('../../Data/count/2016-5-8-22/sixperson/sixperson1_csieig.txt');
figure(13)
clf;
plot(csieig01(:),'r');
hold on;
plot(csieig11(:),'g');
hold on;
plot(csieig21(:),'b');
hold on;
plot(csieig31(:),'k');
hold on;

figure(14)
clf;
[f,xi] = ksdensity(csieig01(:));
plot(xi,f,'r')
hold on;
[f,xi] = ksdensity(csieig11(:));
plot(xi,f,'g')
hold on;
[f,xi] = ksdensity(csieig21(:));
plot(xi,f,'b')
hold on;
[f,xi] = ksdensity(csieig31(:));
plot(xi,f,'k')
hold on;
[f,xi] = ksdensity(csieig41(:));
plot(xi,f,'c')
hold on;
[f,xi] = ksdensity(csieig51(:));
plot(xi,f,'y')
hold on;
[f,xi] = ksdensity(csieig61(:));
plot(xi,f,'m')
hold on;
axis([1.5 2.1 0 30]);

%{
figure(1);
index = input('please input the index of the subcarrier, 0 to quit:');
while index ~= 0
    clf;
    plot(csivar11(1:200,index),'r');
    hold on;
    plot(csivar12(1:200,index),'g');
    hold on;
    plot(csivar21(1:200,index),'b');
    hold on;
    plot(csivar22(1:200,index),'k');
    hold on;
    plot(csivar31(1:200,index),'y');
    hold on;
    plot(csivar32(1:200,index),'m');
    hold on;
    legend('oneperson', 'oneperson', 'twoperson', 'twoperson','threeperson','threeperson','Location', 'SouthEast' );
    index = input('please input the index of the subcarrier, 0 to quit:');
end

figure(2);
index = input('please input the index of the subcarrier, 0 to quit:');
while index ~= 0
    clf;
    [f,xi] = ksdensity(csivar11(1:200,index));
    plot(xi,f,'r');
    hold on;
    [f,xi] = ksdensity(csivar12(1:200,index));
    plot(xi,f,'g');
    hold on;
    [f,xi] = ksdensity(csivar21(1:200,index));
    plot(xi,f,'b');
    hold on;
    [f,xi] = ksdensity(csivar22(1:200,index));
    plot(xi,f,'k');
    hold on;
    [f,xi] = ksdensity(csivar31(1:200,index));
    plot(xi,f,'y');
    hold on;
    [f,xi] = ksdensity(csivar32(1:200,index));
    plot(xi,f,'m');
    hold on;
    legend('oneperson', 'oneperson', 'twoperson', 'twoperson','threeperson','threeperson','Location', 'SouthEast' );
    %ylim([0 2]);
    axis([0 18 0 1]);
    index = input('please input the index of the subcarrier, 0 to quit:');
end
%}
