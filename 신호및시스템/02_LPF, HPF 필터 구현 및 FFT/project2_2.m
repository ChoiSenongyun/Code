
k = [-pi:0.001:pi];
f=1*(k>=-pi/4 & k<=pi/4); 
% 위의 f 가 0~2pi 범위에서의  frequency domain의 hpf 임으로 그대로 hh 해줘도 무방하다
hs=ifft(f);
hh=real(ifftshift(hs));
l=length(hh);
HH=fft(hs);
HH=fftshift(HH);

%혹은 1에서 구한 time domain low pass filter 에서 hh=real(hl).*((-1).^(c+1))의 식을
%사용하여 해줘도 똑같이 결과가 나옴을 확인 할수 있다.

%{
c=[1:1:l];
hh=real(hl).*((-1).^(c+1));
%}

%위의 주석안의 방법으로 만든 hh와 맨 앞에서 ifft로 구한 hh의 결과는 같다


% 2-1 PLOT
% 1. -pi~pi 파형을 가지는 주파수축 LPF
%  plot(k,log(abs(HH+1)))  

% 2. -pi~pi 파형의 시간축 LPF
%  plot(hh)
%  xlim([3100,3186])


a=[1:1:l];
b=[1:1:l];


Winone=1*(a>=l/2 & a<=l/2+2);
Wintwo=1*(b>=l/2-2 & b<=l/2+4);



hh3=hh.*Winone;
hh3=real(hh3);
% 2-2 PLOT 3 point 시간축
%  plot(real(hh3))  
%  xlim([3140,3146])

hh7=hh.*Wintwo;
hh7=real(hh7);

% 2-2 PLOT 7 point 시간축
%  plot(real(hh7)) 
%  xlim([3138,3148])

HH3=fft(hh3,l);
HH7=fft(hh7,l);
HH3=fftshift(HH3)
HH7=fftshift(HH7)
% 2-2 PLOT  3, 7 point 주파수축
%  plot(log(abs(HH3)+1))  % HL3(w) Magnitude
%  plot(log(abs(HH7)+1))  % HL7(w) Magnitude

