
a=importdata('x.txt')
a=reshape(a,[1,1024])
h1=[1/3,1/3,1/3]
h2=[-1/3,2/3,-1/3]
an=length(a)

A=[0,0,0,a,0,0,0]
Resultone=zeros(1,1026)
Resulttwo=zeros(1,1026)

for n=1:1026
    for m=1:3
        Resultone(n)=Resultone(n)+A(n-m+4)*h1(4-m);
    end
end

for n=1:1026
    for m=1:3
        Resulttwo(n)=Resulttwo(n)+A(n-m+4)*h2(4-m);
    end
end



% a plot
ax1 = nexttile;
plot(a)
title(ax1,'Signal')

% Resultone plot
ax2 = nexttile;
plot(Resultone)
title(ax2,'Resultone Plot')

% Resulttwo plot
ax2 = nexttile;
plot(Resulttwo)
title(ax2,'Resulttwo Plot')
