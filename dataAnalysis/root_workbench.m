%For Nate's Xray root data
%computer vertical density for fixed depth
file=dir('*.png');
clear BW
for k=1:length(file)
I=imread(file(k).name);
BW(:,:,k)=I;
end
[x y z]=findND(BW==255);

[COEFF SCORE latent]=pca([x y z]);
elong=sqrt(latent(2)/latent(1));
flat=sqrt(latent(3)/latent(2));

%football
[COEFF SCORE latent]=pca([x y]);
football = sqrt(latent(2)/latent(1));

%biomass distribution
Depth=885;
pts=Depth/20:Depth/20:Depth; %885 for 113um
[f,xi] = ksdensity(z,pts,'bandwidth',20);
ConvH=zeros(size(BW));
if length(file)>Depth
    Solidity=zeros(1,length(file));
else
    Solidity=zeros(1,Depth);
end
for k=1:length(file)
    CH=bwconvhull(BW(:,:,k));
    ConvH(:,:,k)=CH;
    if length(find(ConvH(:,:,k))==1)>0
        Solidity(k)=length(find(BW(:,:,k))==255)/length(find(ConvH(:,:,k))==1);
    end
end
[cx cy cz]=findND(ConvH==1);

[cf,cxi] = ksdensity(cz,pts,'bandwidth',20);
sf = interp1([1:length(Solidity)],Solidity,pts,'spline');
volume=length(x)*0.113^3;

dlmwrite('biomd.txt', [volume elong flat football f cf sf], 'delimiter', '\t');