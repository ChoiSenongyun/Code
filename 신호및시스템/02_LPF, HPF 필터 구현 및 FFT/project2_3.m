
[y, Fs] = audioread('input.wav');

y1=y.';
YF=fft(y1);
YF=fftshift(YF);
hlf3=conv(nhl3,y1);
hlf7=conv(nhl7,y1);


HLF3=fft(hlf3);
HLF3=fftshift(HLF3);
HLF7=fft(hlf7);
HLF7=fftshift(HLF7);

%{
% 3 Point의 LPF CONVOLUTION 결과
plot(log(abs(YF)+1))
hold on
plot(log(abs(HLF3)+1))
%}


%{
% 7 Point의 LPF CONVOLUTION 결과
plot(log(abs(YF)+1))
hold on
plot(log(abs(HLF7)+1))
%}

hhf3=conv(y1,hh3);
hhf7=conv(y1,hh7);

HHF3=fft(hhf3);
HHF3=fftshift(HHF3);
HHF7=fft(hhf7);
HHF7=fftshift(HHF7);

%{
% 3 Point의 HPF CONVOLUTION 결과
plot(log(abs(YF)+1))
hold on
plot(log(abs(HHF3)+1))
%}

%{
% 7 Point의 HPF CONVOLUTION 결과
plot(log(abs(YF)+1))
hold on
plot(log(abs(HHF7)+1))
%}

%  sound(hlf7,Fs)
