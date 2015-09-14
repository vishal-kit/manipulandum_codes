function [theta]= vec_angle(x1,y1,z1,x2,y2,z2)
    length_1=sqrt((x1*x1)+(y1*y1)+(z1*z1));
    length_2=sqrt((x2*x2)+(y2*y2)+(z2*z2));
    x1=-x1/length_1;
    y1=-y1/length_1;
    z1=-z1/length_1;
    x2=x2/length_2;
    y2=y2/length_2;
    z2=z2/length_2;
    theta=acosd(((x1*x2)+(y1*y2)+(z1*z2))/(length_1*length_2));
end
