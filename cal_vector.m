clear;
clc;
[h,m]=csvreadh('subset.csv',',');
function [v]=cal_vector(x1,y1,z1,x2,y2,z2)
    x=x1-x2;
    y=y1-y2;
    z=z1-z2;
    length=sqrt((x*x)+(y*y)+(z*z))
    x=x/length;
    y=y/length;
    z=z/length;
    v=[x y z];
end
