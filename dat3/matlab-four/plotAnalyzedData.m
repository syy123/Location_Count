clear
clc
%csialt = load('../../Data/count/2016-4-6/noperson/noperson1_csialt.txt');
%{
for i = 1 : 400
    plot(csialt(i,1:30))
    drawnow;
    hold on;
    plot(csialt(i,31:60))
    drawnow;
    hold on;
    plot(csialt(i,61:90))
    drawnow;
    hold on;
    
    legend('RX Antenna A', 'RX Antenna B', 'RX Antenna C', 'Location', 'SouthEast' )
    xlabel('Subcarrier index')
    ylabel('SNR [dB]')
end
%}

%{
%%%% draw the surface of csi data along with time   %%%%
csialt1 = csialt(1:20:1000,1:30);
[m,n] = size(csialt1);
y = 1 : m;
x = 1 : n;
surf(x,y,csialt1);
%}

%{
csivar1 = load('../../Data/count/2016-4-15/noperson/noperson1_csivarseg.txt');
csivar2 = load('../../Data/count/2016-4-15/oneperson/oneperson1_csivarseg.txt');
csivar3 = load('../../Data/count/2016-4-15/twoperson/twoperson1_csivarseg.txt');
csivar4 = load('../../Data/count/2016-4-15/threeperson/threeperson1_csivarseg.txt');
csivar5 = load('../../Data/count/2016-4-15/fourperson/fourperson1_csivarseg.txt');
csivar6 = load('../../Data/count/2016-4-15/fiveperson/fiveperson1_csivarseg.txt');

figure(1);
index = input('please input the index of the subcarrier, 0 to quit:');
while index ~= 0
    clf;
    plot(csivar1(1:200,index),'r');
    hold on;
    plot(csivar2(:,index),'g');
    hold on;
    plot(csivar3(:,index),'b');
    hold on;
    plot(csivar4(:,index),'k');
    hold on;
    plot(csivar5(:,index),'y');
    hold on;
    plot(csivar6(:,index),'m');
    hold on;
    legend('noperson', 'oneperson', 'twoperson', 'threeperson','fourperson','fiveperson','Location', 'SouthEast' );
    index = input('please input the index of the subcarrier, 0 to quit:');
end

figure(2);
index = input('please input the index of the subcarrier, 0 to quit:');
while index ~= 0
    clf;
    [f,xi] = ksdensity(csivar1(1:200,index));
    plot(xi,f,'r');
    hold on;
    [f,xi] = ksdensity(csivar2(:,index));
    plot(xi,f,'g');
    hold on;
    [f,xi] = ksdensity(csivar3(:,index));
    plot(xi,f,'b');
    hold on;
    [f,xi] = ksdensity(csivar4(:,index));
    plot(xi,f,'k');
    hold on;
    [f,xi] = ksdensity(csivar5(:,index));
    plot(xi,f,'y');
    hold on;
    [f,xi] = ksdensity(csivar6(:,index));
    plot(xi,f,'m');
    hold on;
    legend('noperson', 'oneperson', 'twoperson', 'threeperson','fourperson','fiveperson','Location', 'SouthEast' );
    %ylim([0 2]);
    axis([0 18 0 1]);
    index = input('please input the index of the subcarrier, 0 to quit:');
end

figure(3);
index = input('please input the index of the subcarrier, 0 to quit:');
while index ~= 0
    clf;
    subplot(2,2,1);
    hist(csivar1(1:200,index));
    title('noperson');
    subplot(2,2,2);
    hist(csivar2(:,index));
    title('oneperson');
    subplot(2,2,3);
    hist(csivar3(:,index));
    title('twoperson');
    subplot(2,2,4);
    hist(csivar4(:,index));
    title('threeperson');
    hold on;
    index = input('please input the index of the subcarrier, 0 to quit:');
end

csivar1 = load('../../Data/count/2016-4-6/oneperson/oneperson1_csivarseg.txt');
csivar2 = load('../../Data/count/2016-4-6/oneperson/oneperson2_csivarseg.txt');
csivar3 = load('../../Data/count/2016-4-6/oneperson/oneperson3_csivarseg.txt');
csivar4 = load('../../Data/count/2016-4-6/oneperson/oneperson4_csivarseg.txt');
figure(4);
plot(csivar1(1:20,1),'r');
hold on;
plot(csivar2(1:20,1),'g');
hold on;
plot(csivar3(1:20,1),'b');
hold on;
plot(csivar4(1:20,1),'k');
hold on;

legend('Monitor1', 'Monitor2', 'Monitor3', 'Monitor4','Location', 'SouthEast' );
xlabel('Time');
ylabel('Variance');
%}











