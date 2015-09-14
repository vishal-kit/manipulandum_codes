function myfun()
%[h,m]=chvreadh('subset.scv')
for i= 1:191
    [hip_sh(i,1),hip_sh(i,2),hip_sh(i,3)]=cal_vector(right_hip_2x(i),right_hip_2y(i),right_hip_2z(i),...
                                          right_shoulder_2x(i),right_shoulder_2y(i),right_shoulder_2z(i));
    [sh_el(i,1),sh_el(i,2),sh_el(i,3)]=cal_vector(right_shoulder_2x(i),right_shoulder_2y(i),...
                                       right_shoulder_2z(i),right_elbow_2x(i),right_elbow2y(i),...
                                       right_elbow_2z(i));
    theta(i)=vec_angle(hip_sh(i,1),hip_sh(i,2),hip_sh(i,3),sh_el(i,1),sh_el(i,2),sh_el(i,3));
end
end


