setwd("E:/study/2020Spring/Êý¾Ý¿ÆÑ§»ù´¡/´ó×÷Òµ/github/datasci-coursework/period1_xzh/rasch/group_1")
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
#ï¿½ï¿½È¡ï¿½ï¿½ï¿½ï¿½
resp_all = read.csv("group1_results0_1.csv")
resp_array = read.csv("group1_results_array_0_1.csv")
resp_graph = read.csv("group1_results_graph_0_1.csv")
resp_linear = read.csv("group1_results_linear_0_1.csv")
resp_number = read.csv("group1_results_number_0_1.csv")
resp_searching = read.csv("group1_results_searching_0_1.csv")
resp_sorting = read.csv("group1_results_sorting_0_1.csv")
resp_string = read.csv("group1_results_string_0_1.csv")
resp_tree = read.csv("group1_results_tree_0_1.csv")




#ï¿½ï¿½tam
result_all = tam(resp_all)
result_array = tam(resp_array)
result_graph = tam(resp_graph)
result_linear = tam(resp_linear)
result_number = tam(resp_number)
result_searching = tam(resp_searching)
result_sorting = tam(resp_sorting)
result_string = tam(resp_string)
result_tree = tam(resp_tree)

#ï¿½ï¿½È¡ï¿½Ñ¶È²ï¿½ï¿½ï¿½

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


#Ñ§ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½
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



#ICC Í¼Æ¬ ï¿½ï¿½ï¿½ï¿½Í¼Æ¬ï¿½ï¿½ï¿½Ðµï¿½ï¿½Ò²ï¿½ï¿½ï¿½Ø¸ï¿?
ICC_all=plot(result_all,type="items",export=FALSE)
ICC_array=plot(result_array)
ICC_graph=plot(result_graph)
ICC_linear=plot(result_linear)
ICC_number=plot(result_number)
ICC_searching=plot(result_searching)
ICC_sorting=plot(result_sorting)
ICC_string=plot(result_string)
ICC_tree=plot(result_tree)


#wrightmapÍ¼Æ¬
install.packages("WrightMap")
library("WrightMap")
#windows()
jpeg(file="group2_all.jpg",width=1800,height=1000)
p=ggWrightMap(ability_param_all,difficulty_param_all,color = 'grey')
print(p)
dev.off()


jpeg(file="group1_array.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_array,difficulty_param_array,color = 'grey')
print(p)
dev.off()


jpeg(file="group1_graph.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_graph,difficulty_param_graph,color = 'grey')
print(p)
dev.off()


jpeg(file="group1_linear.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_linear,difficulty_param_linear,color = 'grey')
print(p)
dev.off()


jpeg(file="group1_number.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_number,difficulty_param_number,color = 'grey')
print(p)
dev.off()


jpeg(file="group1_searching.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_searching,difficulty_param_searching,color = 'grey')
print(p)
dev.off()


jpeg(file="group1_sorting.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_sorting,difficulty_param_sorting,color = 'grey')
print(p)
dev.off()


jpeg(file="group1_string.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_string,difficulty_param_string,color = 'grey')
print(p)
dev.off()


jpeg(file="group1_tree.jpg",width=1000,height=500)
p=ggWrightMap(ability_param_tree,difficulty_param_tree,color = 'grey')
print(p)
dev.off()


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
jpeg(file="personItemMap_group1_all.jpg",width=1800,height=1000)
p=plotPImap(res_rm_all, cex.gen = .8)
print(p)
dev.off()

jpeg(file="personItemMap_group1_array.jpg",width=800,height=800)
p=plotPImap(res_rm_array, cex.gen = .8)
print(p)
dev.off()

jpeg(file="personItemMap_group1_graph.jpg",width=800,height=800)
plotPImap(res_rm_graph, cex.gen = .8)
print(p)
dev.off()

jpeg(file="personItemMap_group1_linear.jpg",width=800,height=800)
plotPImap(res_rm_linear, cex.gen = .8)
print(p)
dev.off()

jpeg(file="personItemMap_group1_number.jpg",width=800,height=800)
plotPImap(res_rm_number, cex.gen = .8)
print(p)
dev.off()

jpeg(file="personItemMap_group1_searching.jpg",width=800,height=800)
plotPImap(res_rm_searching, cex.gen = .8)
print(p)
dev.off()

jpeg(file="personItemMap_group1_sorting.jpg",width=800,height=800)
plotPImap(res_rm_sorting, cex.gen = .8)
print(p)
dev.off()

jpeg(file="personItemMap_group1_string.jpg",width=800,height=800)
plotPImap(res_rm_string, cex.gen = .8)
print(p)
dev.off()

jpeg(file="personItemMap_group1_tree.jpg",width=800,height=800)
plotPImap(res_rm_tree, cex.gen = .8)
print(p)
dev.off()

jpeg(file="personItemMap_group1_linear.jpg",width=800,height=800)
plotPImap(res_rm_linear, cex.gen = .8)
print(p)
dev.off()


 