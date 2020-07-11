setwd("E:/study/2020Spring/数据科学基础/大作业/github/datasci-coursework/period1_xzh/rasch/group_5")
getwd()
install.packages('TAM')
library('TAM')
install.packages('ggplot2')
library('ggplot2')
install.packages('mirt')
install.packages('ShinyItemAnalysis')
library('ShinyItemAnalysis')
install.packages("eRm")
install.packages("ltm")
install.packages("difR")
library("eRm")
library("ltm")
library("difR")
library('mirt')

library('mirt')
#读取数据
resp_all = read.csv("group5_results0_1.csv")
resp_array = read.csv("group5_results_array_0_1.csv")
resp_graph = read.csv("group5_results_graph_0_1.csv")
resp_linear = read.csv("group5_results_linear_0_1.csv")
resp_number = read.csv("group5_results_number_0_1.csv")
resp_searching = read.csv("group5_results_searching_0_1.csv")
resp_sorting = read.csv("group5_results_sorting_0_1.csv")
resp_string = read.csv("group5_results_string_0_1.csv")
resp_tree = read.csv("group5_results_tree_0_1.csv")




#跑tam
result_all = tam(resp_all)
result_array = tam(resp_array)
result_graph = tam(resp_graph)
result_linear = tam(resp_linear)
result_number = tam(resp_number)
result_searching = tam(resp_searching)
result_sorting = tam(resp_sorting)
result_string = tam(resp_string)
result_tree = tam(resp_tree)

#获取难度参数

difficulty_param_all=result_all$xsi$xsi 
difficulty_param_array=result_array$xsi$xsi 
difficulty_param_graph=result_graph$xsi$xsi 
difficulty_param_linear=result_linear$xsi$xsi 
difficulty_param_number=result_number$xsi$xsi 
difficulty_param_searching=result_searching$xsi$xsi 
difficulty_param_sorting=result_sorting$xsi$xsi 
difficulty_param_string=result_string$xsi$xsi 
difficulty_param_tree=result_tree$xsi$xsi 
print(mean(difficulty_param_all),digits=4)
print(mean(difficulty_param_array),digits=4)
print(mean(difficulty_param_graph),digits=4)
print(mean(difficulty_param_linear),digits=4)
print(mean(difficulty_param_number),digits=4)
print(mean(difficulty_param_searching),digits=4)
print(mean(difficulty_param_sorting),digits=4)
print(mean(difficulty_param_string),digits=4)
print(mean(difficulty_param_tree),digits=4)


#学生能力
ability = tam.wle(result_all)
ability_param_all=(tam.wle(result_all))$theta 
ability_param_array=(tam.wle(result_array))$theta 
ability_param_graph=(tam.wle(result_graph))$theta 
ability_param_linear=(tam.wle(result_linear))$theta 
ability_param_number=(tam.wle(result_number))$theta 
ability_param_searching=(tam.wle(result_searching))$theta 
ability_param_sorting=(tam.wle(result_sorting))$theta 
ability_param_string=(tam.wle(result_string))$theta 
ability_param_tree=(tam.wle(result_tree))$theta 



#ICC 图片 这里图片量有点大，也有重复
ICC_all=plot(result_all)
ICC_array=plot(result_array)
ICC_graph=plot(result_graph)
ICC_linear=plot(result_linear)
ICC_number=plot(result_number)
ICC_searching=plot(result_searching)
ICC_sorting=plot(result_sorting)
ICC_string=plot(result_string)
ICC_tree=plot(result_tree)


#wrightmap图片
install.packages("WrightMap")
library("WrightMap")
#windows()
jpeg(file="group5_all.jpg",width=1800,height=1000)
p=ggWrightMap(ability_param_all,difficulty_param_all,color = 'grey')
print(p)
dev.off()


jpeg(file="group5_array.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_array,difficulty_param_array,color = 'grey')
print(p)
dev.off()


jpeg(file="group5_graph.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_graph,difficulty_param_graph,color = 'grey')
print(p)
dev.off()


jpeg(file="group5_linear.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_linear,difficulty_param_linear,color = 'grey')
print(p)
dev.off()


jpeg(file="group5_number.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_number,difficulty_param_number,color = 'grey')
print(p)
dev.off()


jpeg(file="group5_searching.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_searching,difficulty_param_searching,color = 'grey')
print(p)
dev.off()


jpeg(file="group5_sorting.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_sorting,difficulty_param_sorting,color = 'grey')
print(p)
dev.off()


jpeg(file="group5_string.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_string,difficulty_param_string,color = 'grey')
print(p)
dev.off()


jpeg(file="group5_tree.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_tree,difficulty_param_tree,color = 'grey')
print(p)
dev.off()
windows()
ggWrightMap(ability_param_all,difficulty_param_all,color = 'grey')



windows()
wrightMap(ability_param_all,difficulty_param_all,
          person.side = personDens,show.axis.logits = TRUE)




#ERM
res_rm_all = RM(resp_all)
res_rm_array =RM(resp_array)
res_rm_graph =RM(resp_graph1)
res_rm_linear =RM(resp_linear)
res_rm_number =RM(resp_number)
res_rm_searching =RM(resp_searching)
res_rm_sorting =RM(resp_sorting1)
res_rm_string =RM(resp_string1)
res_rm_tree =RM(resp_tree)
print(res_rm_all)

#personitemmap
jpeg(file="personItemMap_group5_all.jpg",width=1800,height=1000)
p=plotPImap(res_rm_all, cex.gen = .8)
print(p)
dev.off()
