# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:09:18 2022

@author: dharm
"""
function [ K, L ] = TRUSS_ELEMENT_2D ( x1, y1, x2, y2, EA )
% [ K, L ] = TRUSS_ELEMENT_2D ( X1, Y1, X2, Y2, EA, T )
% Compute the element stiffness matrix for a 2D truss bar in global coordinates
%
% INPUT DATA:
% X1,Y1 is the location of joint 1 of the truss bar
% X2,Y2 is the location of joint 2 of the truss bar
% EA is the product of the elastic modulus and the section area
%
% OUTPUT DATA:
% K is the 4x4 truss bar element stiffness matrix in global element coord’s
% L is the length of the truss bar
L = sqrt( (x2-x1)ˆ2 + (y2-y1)ˆ2 ); % length of the bar
c = ( x2 - x1 ) / L; % cosine of bar angle
s = ( y2 - y1 ) / L; % sine of bar angle
K = (EA/L) * [ cˆ2 c*s -cˆ2 -c*s ;
c*s sˆ2 -c*s -sˆ2 ;
-cˆ2 -c*s cˆ2 c*s ;
-c*s -sˆ2 c*s sˆ2 ];
% --------------------------------------------------------- TRUSS_ELEMENT_2D
>> format bank % two decimal places after the .
>> E = 3e4; % modulus of elasticity
>> A = 10; % area of cross section
>> EA = E*A;
>> [ K1, L(1) ] = truss_2d_element( 0, 0, 12*16, 12*12, EA ) % truss element 1
K1 =
800.00 600.00 -800.00 -600.00
600.00 450.00 -600.00 -450.00
-800.00 -600.00 800.00 600.00
-600.00 -450.00 600.00 450.00
>> [ K2, L(2) ] = truss_2d_element( 0, 0, 12*16, 0, EA ) % truss element 2
K2 =
1562.50 0.00 -1562.50 0.00
0.00 0.00 0.00 0.00
CC BY-NC-ND H.P. Gavin
6 CEE 421L. Matrix Structural Analysis – Duke University – Fall 2014 – H.P. Gavin
-1562.50 0.00 1562.50 0.00
0.00 0.00 0.00 0.00
>> [ K3, L(3) ] = truss_2d_element( 12*16, 0, 12*16, 12*12, EA ) % truss element 3
K3 =
0.00 0.00 0.00 0.00
0.00 2083.33 0.00 -2083.33
0.00 0.00 0.00 0.00
0.00 -2083.33 0.00 2083.33
>> [ K4, L(4) ] = truss_2d_element( 12*16, 12*12, 12*32, 12*12, EA ) % truss element 4
K4 =
1562.50 0.00 -1562.50 0.00
0.00 0.00 0.00 0.00
-1562.50 0.00 1562.50 0.00
0.00 0.00 0.00 0.00
>> [ K5, L(5) ] = truss_2d_element( 12*16, 12*12, 12*32, 0, EA ) % truss element 5
K5 =
800.00 -600.00 -800.00 600.00
-600.00 450.00 600.00 -450.00
-800.00 600.00 800.00 -600.00
600.00 -450.00 -600.00 450.00
>> [ K6, L(6) ] = truss_2d_element( 12*16, 0, 12*32, 12*12, EA ) % truss element 6
K6 =
800.00 600.00 -800.00 -600.00
600.00 450.00 -600.00 -450.00
-800.00 -600.00 800.00 600.00
-600.00 -450.00 600.00 450.00
>> [ K7, L(7) ] = truss_2d_element( 12*16, 0, 12*32, 0, EA ) % truss element 7
K7 =
1562.50 0.00 -1562.50 0.00
0.00 0.00 0.00 0.00
-1562.50 0.00 1562.50 0.00
0.00 0.00 0.00 0.00
CC BY-NC-ND H.P. Gavin
The Matrix Stiffness Method for 2D Trusses 7
>> [ K8, L(8) ] = truss_2d_element( 12*32, 0, 12*32, 12*12, EA ) % truss element 8
K8 =
0.00 0.00 0.00 0.00
0.00 2083.33 0.00 -2083.33
0.00 0.00 0.00 0.00
0.00 -2083.33 0.00 2083.33
% ---------------------------- assemble the global structural stiffness matrix ...
>> Ks = [ 3925 600 0 0 -800 -600 ;
> 600 2533.33 0 -2083.33 -600 -450 ;
> 0 0 3162.5 0 -1562.5 0 ;
> 0 -2083.33 0 2983.33 0 0 ;
> -800 -600 -1562.5 0 2362.5 600 ;
> -600 -450 0 0 600 2533.33 ]
Ks =
3925.00 600.00 0.00 0.00 -800.00 -600.00
600.00 2533.33 0.00 -2083.33 -600.00 -450.00
0.00 0.00 3162.50 0.00 -1562.50 0.00
0.00 -2083.33 0.00 2983.33 0.00 0.00
-800.00 -600.00 -1562.50 0.00 2362.50 600.00
-600.00 -450.00 0.00 0.00 600.00 2533.33
>> find(Ks-Ks’) % check to see if Ks is symmetric ...
ans = [](0x0) % It is!
>> p = [ 0 -100 0 0 50 0 ]’ % input the load vector
p =
0.00
-100.00
0.00
CC BY-NC-ND H.P. Gavin
8 CEE 421L. Matrix Structural Analysis – Duke University – Fall 2014 – H.P. Gavin
0.00
50.00
0.00
>> format % change formats for more sig. fig’s
>> d = Ks \ p % compute the joint displacements
d =
0.0146067
-0.1046405
0.0027214
-0.0730729
0.0055080
-0.0164325