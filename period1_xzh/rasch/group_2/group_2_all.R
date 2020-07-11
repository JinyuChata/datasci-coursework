setwd("E:/study/2020Spring/数据科学基础/大作业/github/datasci-coursework/period1_xzh/rasch/group_2")
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
resp_all = read.csv("group2_results0_1.csv")
resp_array = read.csv("group2_results_array_0_1.csv")
resp_graph = read.csv("group2_results_graph_0_1.csv")
resp_linear = read.csv("group2_results_linear_0_1.csv")
resp_number = read.csv("group2_results_number_0_1.csv")
resp_searching = read.csv("group2_results_searching_0_1.csv")
resp_sorting = read.csv("group2_results_sorting_0_1.csv")
resp_string = read.csv("group2_results_string_0_1.csv")
resp_tree = read.csv("group2_results_tree_0_1.csv")




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
jpeg(file="group2_all.jpg",width=2400,height=1000)
p=ggWrightMap(ability_param_all,difficulty_param_all,color = 'grey')
print(p)
dev.off()


jpeg(file="group2_array.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_array,difficulty_param_array,color = 'grey')
print(p)
dev.off()


jpeg(file="group2_graph.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_graph,difficulty_param_graph,color = 'grey')
print(p)
dev.off()


jpeg(file="group2_linear.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_linear,difficulty_param_linear,color = 'grey')
print(p)
dev.off()


jpeg(file="group2_number.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_number,difficulty_param_number,color = 'grey')
print(p)
dev.off()


jpeg(file="group2_searching.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_searching,difficulty_param_searching,color = 'grey')
print(p)
dev.off()


jpeg(file="group2_sorting.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_sorting,difficulty_param_sorting,color = 'grey')
print(p)
dev.off()


jpeg(file="group2_string.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_string,difficulty_param_string,color = 'grey')
print(p)
dev.off()


jpeg(file="group2_tree.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_tree,difficulty_param_tree,color = 'grey')
print(p)
dev.off()




windows()
wrightMap(ability_param_all,difficulty_param_all,
          person.side = personDens,show.axis.logits = TRUE)







#ERM




jpeg(file="group2_all_jointICC.jpg",width=1000,height=500)
res_rm_all = RM(resp_all)
p=plotjointICC(res_rm_all,  cex = .6,xlab="ability",main="group 2, all categories jointICC")
print(p)
dev.off()

jpeg(file="group2_array_jointICC.jpg",width=1000,height=500)
res_rm_array =RM(resp_array)
p=plotjointICC(res_rm_array,xlab="ability",main ="group 2, array category jointICC")
print(p)
dev.off()

jpeg(file="group2_graph_jointICC.jpg",width=1000,height=500)
resp_graph1=resp_graph[,-12]
res_rm_graph =RM(resp_graph1)
p=plotjointICC(res_rm_graph,xlab="ability",main ="group 2, graph category jointICC")
print(p)
dev.off()

jpeg(file="group2_linear_jointICC.jpg",width=1000,height=500)
res_rm_linear =RM(resp_linear)
p=plotjointICC(res_rm_linear,xlab="ability",main ="group 2, linear category jointICC")
print(p)
dev.off()

jpeg(file="group2_number_jointICC.jpg",width=1000,height=500)
#resp_number1=resp_number[,-13]
res_rm_number =RM(resp_number)
p=plotjointICC(res_rm_number,xlab="ability",main ="group 2, number category jointICC")
print(p)
dev.off()



jpeg(file="group2_searching_jointICC.jpg",width=1000,height=500)
res_rm_searching =RM(resp_searching)
p=plotjointICC(res_rm_searching,xlab="ability",main ="group 2, searching category jointICC")
print(p)
dev.off()






jpeg(file="group2_sorting_jointICC.jpg",width=1000,height=500)
resp_sorting1=resp_sorting[,-3]
resp_sorting1=resp_sorting1[,-4]
resp_sorting1=resp_sorting1[,-4]
resp_sorting1=resp_sorting1[,-4]
resp_sorting1=resp_sorting1[,-4]
resp_sorting1=resp_sorting1[,-5]
res_rm_sorting =RM(resp_sorting1)
p=plotjointICC(res_rm_sorting,xlab="ability",main ="group 2, sorting category jointICC")
print(p)
dev.off()





jpeg(file="group1_string_jointICC.jpg",width=1000,height=500)
resp_string1=resp_string[,-13]
resp_string1=resp_string1[,-13]
resp_string1=resp_string1[,-13]
resp_string1=resp_string1[,-13]
resp_string1=resp_string1[,-13]
res_rm_string =RM(resp_string1)

p=plotjointICC(res_rm_string,xlab="ability",main ="group 1, string category jointICC")
print(p)
dev.off()


jpeg(file="group1_tree_jointICC.jpg",width=1000,height=500)
res_rm_tree =RM(resp_tree)
p=plotjointICC(res_rm_tree,xlab="ability",main ="group 1, tree category jointICC")
print(p)
dev.off()


#personitemmap
jpeg(file="personItemMap_group2_all.jpg",width=1800,height=1000)
p=plotPImap(res_rm_all, cex.gen = .8)
print(p)
dev.off()

jpeg(file="personItemMap_group2_array.jpg",width=200,height=800)
p=plotPImap(res_rm_array, cex.gen = .8)
print(p)
dev.off()

jpeg(file="personItemMap_group2_graph.jpg",width=800,height=800)
plotPImap(res_rm_graph, cex.gen = .8)
print(p)
dev.off()

jpeg(file="personItemMap_group2_linear.jpg",width=800,height=800)
plotPImap(res_rm_linear, cex.gen = .8)
print(p)
dev.off()

jpeg(file="personItemMap_group2_number.jpg",width=800,height=800)
plotPImap(res_rm_number, cex.gen = .8)
print(p)
dev.off()

jpeg(file="personItemMap_group2_searching.jpg",width=800,height=800)
plotPImap(res_rm_searching, cex.gen = .8)
print(p)
dev.off()

jpeg(file="personItemMap_group2_sorting.jpg",width=800,height=800)
plotPImap(res_rm_sorting, cex.gen = .8)
print(p)
dev.off()

jpeg(file="personItemMap_group2_string.jpg",width=800,height=800)
plotPImap(res_rm_string, cex.gen = .8)
print(p)
dev.off()

jpeg(file="personItemMap_group2_tree.jpg",width=800,height=800)
plotPImap(res_rm_tree, cex.gen = .8)
print(p)
dev.off()

jpeg(file="personItemMap_group2_linear.jpg",width=800,height=800)
plotPImap(res_rm_linear, cex.gen = .8)
print(p)
dev.off()

