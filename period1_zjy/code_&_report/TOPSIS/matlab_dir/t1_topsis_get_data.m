clc

%% 读取所有csv文件
file_path = '../data/*.csv';
folder_path = '../data/';
all_csvs = dir(file_path);

csv_size = size(all_csvs, 1);

file_name_list = cell(1, csv_size);
column_num_list = cell(1, csv_size);
this_csv_matric = [0, 0, 0, 0, 0];

for k = 1 : csv_size
    file_name = strcat(all_csvs(k, 1).folder, '/', all_csvs(k, 1).name);
    part_csv_matric = csvread(file_name, 1, 1);
    [n,~] = size(part_csv_matric);
    column_num_list{k} = n;
    file_name_list{k} = all_csvs(k, 1).name;
    
    this_csv_matric = [this_csv_matric; part_csv_matric];
end

[m, ~] = size(this_csv_matric);
this_csv_matric = this_csv_matric(2:m, :);

% 获取列数
col_num = size(this_csv_matric, 2);

X = this_csv_matric;
[n,m] = size(X);

%  正向化
disp(['共有' num2str(n) '个评价对象, ' num2str(m) '个评价指标']) 
Position = [4, 5];
Type = [1, 1];

for i = 1 : size(Position,2)  %这里需要对这些列分别处理，因此我们需要知道一共要处理的次数，即循环的次数
    X(:,Position(i)) = Positivization(X(:,Position(i)),Type(i),Position(i));
end


%% 让用户判断是否需要增加权重
Judge = 0;
if Judge == 1
    weigh = [0.2, 0.2, 0.3, 0.15, 0.15]
else
    weigh = ones(1,m) ./ m ; %如果不需要加权重就默认权重都相同，即都为1/m
end


%% 第三步：对正向化后的矩阵进行标准化
Z = X ./ repmat(sum(X.*X) .^ 0.5, n, 1);
Z(isnan(Z)) = 0;
%     disp('标准化矩阵 Z = ')
%     disp(Z)

%% 第四步：计算与最大值的距离和最小值的距离，并算出得分
D_P = sum([(Z - repmat(max(Z),n,1)) .^ 2 ] .* repmat(weigh,n,1) ,2) .^ 0.5;   % D+ 与最大值的距离向量
D_N = sum([(Z - repmat(min(Z),n,1)) .^ 2 ] .* repmat(weigh,n,1) ,2) .^ 0.5;   % D- 与最小值的距离向量
S = D_N ./ (D_P+D_N);    % 未归一化的得分
stand_S = S / sum(S);
[sorted_S,index] = sort(stand_S ,'descend');

%% 拼接 输出
currLine = 1;
[n, m] = size(stand_S);
for k = 1 : csv_size
    output_stand_S = stand_S(currLine:currLine+column_num_list{k}-1, :) * 10000;
    
    file_name = strcat(all_csvs(k, 1).folder, '/', file_name_list{k});
    output_S = csvread(file_name, 1, 0);
    various={'user_id','mean_score_of_committed','mean_score_of_submitted','commit_ratio','example_fronted_ratio','submit_times_commit_ratio','AHP_score'};
    result_table=table(output_S(:,1),output_S(:,2),output_S(:,3),output_S(:,4),output_S(:,5),output_S(:,6),output_stand_S,'VariableNames',various);
    writetable(result_table, strcat('ahp_data/ahp_',file_name_list{k}))
    
    currLine = currLine + column_num_list{k};
end

% 
% % 对csv进行拼接后输出
% output_S = csvread(file_name, 1, 0);
% 
% %表头
% various={'user_id','mean_score_of_committed','mean_score_of_submitted','commit_ratio','example_fronted_ratio','submit_times_commit_ratio','AHP_score'};
% %表的内容
% result_table=table(output_S(:,1),output_S(:,2),output_S(:,3),output_S(:,4),output_S(:,5),output_S(:,6),stand_S,'VariableNames',various);
% %创建csv表格
% writetable(result_table, strcat('ahp_data/ahp_',all_csvs(k, 1).name))
% 
% 
% 
% 
% 
% 
% 
% for k = 1 : csv_size
%     file_name = strcat(all_csvs(k, 1).folder, '/', all_csvs(k, 1).name);
%     this_csv_matric = csvread(file_name, 1, 1);
%    
%     % 获取列数
%     col_num = size(this_csv_matric, 2);
%     
%     X = this_csv_matric;
%     [n,m] = size(X);
%     
%     %  正向化
%     disp(['共有' num2str(n) '个评价对象, ' num2str(m) '个评价指标']) 
%     Position = [4, 5];
%     Type = [1, 1];
%     
%     for i = 1 : size(Position,2)  %这里需要对这些列分别处理，因此我们需要知道一共要处理的次数，即循环的次数
%         X(:,Position(i)) = Positivization(X(:,Position(i)),Type(i),Position(i));
%     % Positivization是我们自己定义的函数，其作用是进行正向化，其一共接收三个参数
%     % 第一个参数是要正向化处理的那一列向量 X(:,Position(i))   回顾上一讲的知识，X(:,n)表示取第n列的全部元素
%     % 第二个参数是对应的这一列的指标类型（1：极小型， 2：中间型， 3：区间型）
%     % 第三个参数是告诉函数我们正在处理的是原始矩阵中的哪一列
%     % 该函数有一个返回值，它返回正向化之后的指标，我们可以将其直接赋值给我们原始要处理的那一列向量
%     end
%     
%     
%     %% 作业：在这里增加是否需要算加权
%     % 补充一个基础知识：m*n维的矩阵A 点乘 n维行向量B，等于这个A的每一行都点乘B
%     % （注意：2017以及之后版本的Matlab才支持，老版本Matlab会报错）
%     % % 假如原始数据为：
%     %   A=[1, 2, 3;
%     %        2, 4, 6] 
%     % % 权重矩阵为：
%     %   B=[ 0.2, 0.5 ,0.3 ] 
%     % % 加权后为：
%     %   C=A .* B
%     %     0.2000    1.0000    0.9000
%     %     0.4000    2.0000    1.8000
%     % 类似的，还有矩阵和向量的点除， 大家可以自己试试计算A ./ B
%     % 注意，矩阵和向量没有 .- 和 .+ 哦 ，大家可以试试，如果计算A.+B 和 A.-B会报什么错误。
% 
% 
%     %% 让用户判断是否需要增加权重
%     Judge = 0;
%     if Judge == 1
%         weigh = [0.2, 0.2, 0.3, 0.15, 0.15]
%     else
%         weigh = ones(1,m) ./ m ; %如果不需要加权重就默认权重都相同，即都为1/m
%     end
% 
% 
%     %% 第三步：对正向化后的矩阵进行标准化
%     Z = X ./ repmat(sum(X.*X) .^ 0.5, n, 1);
%     Z(isnan(Z)) = 0;
% %     disp('标准化矩阵 Z = ')
% %     disp(Z)
% 
%     %% 第四步：计算与最大值的距离和最小值的距离，并算出得分
%     D_P = sum([(Z - repmat(max(Z),n,1)) .^ 2 ] .* repmat(weigh,n,1) ,2) .^ 0.5;   % D+ 与最大值的距离向量
%     D_N = sum([(Z - repmat(min(Z),n,1)) .^ 2 ] .* repmat(weigh,n,1) ,2) .^ 0.5;   % D- 与最小值的距离向量
%     S = D_N ./ (D_P+D_N);    % 未归一化的得分
%     stand_S = S / sum(S);
%     [sorted_S,index] = sort(stand_S ,'descend');
%     
%     % 对csv进行拼接后输出
%     output_S = csvread(file_name, 1, 0);
%     
%     %表头
%     various={'user_id','mean_score_of_committed','mean_score_of_submitted','commit_ratio','example_fronted_ratio','submit_times_commit_ratio','AHP_score'};
%     %表的内容
%     result_table=table(output_S(:,1),output_S(:,2),output_S(:,3),output_S(:,4),output_S(:,5),output_S(:,6),stand_S,'VariableNames',various);
%     %创建csv表格
%     writetable(result_table, strcat('ahp_data/ahp_',all_csvs(k, 1).name))
% end
