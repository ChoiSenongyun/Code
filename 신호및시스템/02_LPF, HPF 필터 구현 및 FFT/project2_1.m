k = [-pi:0.001:pi];
f=1*(k>=-pi/4 & k<=pi/4);
% iff시 0 2pi의 범위로 f를 보고 iff가 될것이다. 따라서 iff시 time domain 상에서는
% hpf가 나올것이다. 
hh=ifft(f);  


HL=fft(real(hh));% fft결과 -pi~pi의 LPF가 구현
HLS=fftshift(HL) %다시 fft를 한후 shift 해주었기때문에 0 ~ 2pi의 LPF가 구현

% 0~2pi 범위에서의 HL를 다시 ifft 하여 0 2pi 범위의 time domain 의 lpf 구현
hl=ifft(real(HLS));  
% shift를 통하여 -pi ~ pi 의 범위로 time domain 의 lpf로 바꾸고 window 진행
hl=ifftshift(hl)


% 1-1 PLOT

% 1. -pi~pi 파형을 가지는 주파수축 LPF
% plot(k,log(abs(HL+1)))  

% 2. -pi~pi 파형의 시간축 LPF
%  plot(hl)
%  xlim([3100,3186])

l=length(hl);
a=[1:1:l];
b=[1:1:l];

Winone=1*(a>=l/2 & a<=l/2+2);
Wintwo=1*(b>=l/2-2 & b<=l/2+4);

hl3=hl.*Winone;
hl3=real(hl3);
% 1-2 PLOT 3 point 시간축
% plot(real(hl3)) %hl3[n] 파형 plot
% xlim([3140,3146])
nhl3=hl3/abs(sum(hl3)); % normalise 시켜준다

hl7=hl.*Wintwo;
% 1-2 PLOT 7 point 시간축
% plot(real(hl7)) %hl7[n] 파형 plot
% xlim([3138,3148])
hl7=real(hl7);
nhl7=hl7/abs(sum(hl7));


HL3=fft(hl3,l);
HL7=fft(hl7,l);
HL3=fftshift(HL3);
HL7=fftshift(HL7);
% 1-2 PLOT  3, 7 point 주파수축
% plot(log(abs(HL3)+1))  % HL3(w) Magnitude
% plot(log(abs(HL7)+1))  % HL7(w) Magnitude


