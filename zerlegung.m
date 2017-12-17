
A = [2 2 3 3; 4 6 9 9; 6 12 21 22; 8 16 36 44];
b = [23; 124; 61; 196];


% for i=2:10
% B = rand(i);
% d = rand(i,1);
% tic
% gauss(B,d);
% toc
% 
% tic
% x = B\d;
% toc
% end

profile on
y=A\b;
x=gauss(A,b);
profile off
profile info


function x=gauss(A,b)
%GAUSS Combines GAUSS_PLR, VORWAERTS and RUECKWAERTS to solve x in Ax = b
%   X = GAUSS(A,B) Returns the vector x solving the equation Ax=b
%
%   See also MLDIVIDE
[LR,piv]=gauss_plr(A);
z=vorwaerts(LR,piv,b);
x=rueckwaerts(LR,z);
end


function [LR,piv]=gauss_plr(A)
% GAUSS_PLR Gaussian elimination of A with row pivoting, such that we have
%           an equation of the fom LR = PA 
%   [LR, PIV] = GAUSS_PLR(A) Calculates L and R through Gaussian
%               elimination and combines them in LR. piv equals the
%               permutation matrix P
szdim = size(A,1);
piv = eye(szdim);
R=A; 
AllP = {};
AllM = {};

k=1;
while k < szdim 
M = eye(szdim);
P = eye(szdim);

[~, zeile] = max(abs(R(k:end,k)));
zeile = zeile + k -1;
P(k,k) = 0;
P(zeile,k) = 1;
P(zeile,zeile) = 0;
P(k,zeile) = 1;
R = P*R;

for j=k+1:szdim
    M(j,k) = R(j,k)/R(k,k);
    R(j,:) = R(j,:) - R(k,:)*M(j,k);
end
AllP{k} = P;
AllM{k} = M;
piv = piv*P;
A = R;
k = k+1;
end


L = eye(szdim);
AllMhat = cell(szdim-1);
for i=1:szdim-1
    M = eye(szdim);
    for k=-szdim+1:szdim-1
        if k < -1
            M = M*transpose(AllP{abs(k)});
        else
            if k == 0
                M = M*AllM{i};
            else
                if k > 1
                    M = AllP{k}*M;
                end
            end
        end
    end
    AllMhat{i} = inv(M);
end

for k=1:max(size(AllMhat))
    L = L*AllMhat{k};
end

LR = (L-eye(szdim)+R);
end

function z=vorwaerts(LR,piv,b)
%VORWAERTS Forward substitution for the equation Lz = Pb
%   Z = VORWAERTS(LR,PIV,B) Returns the vector z solving Lz = Pb
L = tril(LR,-1) + eye(size(LR));
Pb = piv*b;
[szdim, ~] = size(LR);
z = zeros(szdim,1);
z(1) = Pb(1);

for i=2:szdim
    z(i) = Pb(i);
    for k=1:i-1
        z(i) = z(i) - z(k)*L(i,k);
    end
    z(i) = z(i)/L(i,i);
end
end

function x=rueckwaerts(LR,z)
%RUECKWAERTS Forward substitution for the equation Rx=z
%   X = RUECKWAERTS(LR,Z) Returns the vector x solving Rx = z
R = triu(LR);
[szdim, ~] = size(LR);

x = zeros(szdim,1);
x(szdim) = 190; % z(szdim)/R(szdim,szdim);

for i=(szdim-1):-1:1
    summe = z(i);
    for k=i+1:szdim
        summe = summe - x(k)*R(i,k);
    end
    x(i) = summe/R(i,i);
end
end
