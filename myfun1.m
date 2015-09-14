function [theta]= myfun1()
[h,subset]=csvreadh('subset.csv',',');
for i= 1:191
    [hip_sh(i,1),hip_sh(i,2),hip_sh(i,3)]=cal_vector(subset(i,13),subset(i,14),subset(i,15),...
                                          subset(i,4),subset(i,5),subset(i,6));
    [sh_el(i,1),sh_el(i,2),sh_el(i,3)]=cal_vector(subset(i,4),subset(i,5),...
                                       subset(i,6),subset(i,7),subset(i,8),...
                                       subset(i,9));
    theta(i)=vec_angle(hip_sh(i,1),hip_sh(i,2),hip_sh(i,3),sh_el(i,1),sh_el(i,2),sh_el(i,3));
end
end
