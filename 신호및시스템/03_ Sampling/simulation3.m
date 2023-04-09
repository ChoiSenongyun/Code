
n=importdata("u.mat");
filter=importdata("h.mat");
[x, Fs] = audioread('input.wav');
N=length(x);
y=n+x;
X=fft(x,N);
nN=fft(n,N);
Y=fft(y,N);
w=(-N/2:N/2-1)/N*2*pi;

X_shift=fftshift(X);
nN_shift=fftshift(nN);
Y_shift=fftshift(Y);
%%%%%  1 - 1 %%%%%%%%%
%{
figure
subplot(3,1,1), plot(w, log(abs(X_shift)+1))
title('X(w) Magnitude')
subplot(3,1,2), plot(w,  log(1+abs(nN_shift)))
title('U(w) Magnitude')
subplot(3,1,3), plot(w, log(1+abs(Y_shift)))
title('Y(w) Magnitude')
%}

y_filter=conv(y,filter);

Y_Filter=fft(y_filter,N);
Filter=fft(filter,N);

Y_Filter_shift=fftshift(Y_Filter);
Filter_shift=fftshift(Filter);

%%%%%  1 - 2 %%%%%%%%%
%{
figure
subplot(2,1,1), plot(w, log(abs(Y_Filter_shift)+1))
title('Y1(w) Magnitude')
subplot(2,1,2), plot(w,  abs(Filter_shift))
title('H(w) Magnitude')
%}

Y=Y.';
Y_Filter_two=Y.*Filter;
Y_Filter_two_shift=fftshift(Y_Filter_two);

%%%%%  1 - 3 %%%%%%%%%
%{
figure
plot(w, log(abs(Y_Filter_two_shift)+1))
title('Y2(w) Magnitude')
%}
%%%%% 1 - 4 %%%%%
y_filter_two=ifft(Y_Filter,N);

%{
plot(y_filter_two)
title('y2[n]')
%}

y_filter=y_filter.';
y_filter_two=y_filter_two.';

%%%%%  2-2 %%%%%
%{
figure
subplot(2,1,1), plot(y_filter)
title('y1[n]')
subplot(2,1,2), plot(y_filter_two)
title('y2[n]')
figure
plot(y_filter(1:N)-y_filter_two(1:N))
%}


