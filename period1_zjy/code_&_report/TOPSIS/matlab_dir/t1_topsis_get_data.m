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
Position = [3];
Type = [1];

for i = 1 : size(Position,2)  %这里需要对这些列分别处理，因此我们需要知道一共要处理的次数，即循环的次数
    X(:,Position(i)) = Positivization(X(:,Position(i)),Type(i),Position(i));
end


%% 让用户判断是否需要增加权重
Judge = 0;
if Judge == 1
    weigh = [0.6491, 0.0539, 0.0178, 0.0474, 0.2316]
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
%                 #       2. 每个班级要有: user_id, mean_score_of_committed, mean_score_of_submitted,
%                 #                      submit_times_per_commit, commit_ratio, commit_diff_ratio
%% 拼接 输出
currLine = 1;
[n, m] = size(stand_S);
for k = 1 : csv_size
    output_stand_S = stand_S(currLine:currLine+column_num_list{k}-1, :) * 10000;
    
    file_name = strcat(all_csvs(k, 1).folder, '/', file_name_list{k});
    output_S = csvread(file_name, 1, 0);
    various={'user_id','mean_score_of_committed','mean_score_of_submitted', 'submit_times_per_commit','commit_ratio','commit_diff_ratio','AHP_score'};
    result_table=table(output_S(:,1),output_S(:,2),output_S(:,3),output_S(:,4),output_S(:,5),output_S(:,6),output_stand_S,'VariableNames',various);
    writetable(result_table, strcat('ahp_data/ahp_',file_name_list{k}))
    
    currLine = currLine + column_num_list{k};
end

