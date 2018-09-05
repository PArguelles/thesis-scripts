library(ppclust)
library(factoextra)
library(dbscan)

#################################
# PATH VARIABLES
#################################

path_wo <- "C:/ShareSSD/casp/clustering_results"
path_to_results <- "C:/ShareSSD/casp/clustering_results/pdb"
path_to_tables <- "C:/ShareSSD/casp/data_tables/"

structures <- c('T0859','T0860','T0861','T0862','T0863','T0864','T0865','T0866','T0867')

main <- function(){
	for(str in structures){
		#_pdbid_#
		patt <- paste("_",str,sep="")
		patt <- paste(patt,"_",sep="")
		files <- list.files(path=path_to_tables, full.names=FALSE, pattern = patt)

		dir.create(file.path(path_wo, str), showWarnings = FALSE)

		for(name in files){
				
			#################################
			# SET VARIABLES
			#################################
			
			table_path <- paste(path_to_tables,name, sep="")

			div <- strsplit(name,"_")

			structure <- div[[1]][2]
			measure1 <- div[[1]][3]
			measure2 <- div[[1]][4]
				
			aux <- paste(structure,"/",sep="")
			current_path <- gsub("pdb",aux,path_to_results)

			path_to_summaries <- paste(current_path,structure,sep="")
			path_to_summaries <- paste(path_to_summaries,measure1,sep="_")
			path_to_summaries <- paste(path_to_summaries,measure2,sep="_")
			path_to_summaries <- paste(path_to_summaries,"algorithm",sep="_")

			path_to_plots <- paste(current_path,"plot",sep="")
			path_to_plots <- paste(path_to_plots,structure,sep="_")
			path_to_plots <- paste(path_to_plots,measure1,sep="_")
			path_to_plots <- paste(path_to_plots,measure2,sep="_")
			path_to_plots <- paste(path_to_plots,"algorithm",sep="_")
			path_to_plots <- paste(path_to_plots,".png",sep="")

			#################################
			# LOAD DATA
			#################################
			
			df <- read.table(table_path, header = FALSE)
			x <- df[,c(2,3)]
			names(x) <- c(measure1, measure2)
				
			#perform_fcm(path_to_plots, path_to_summaries, x)
			#perform_snn(path_to_plots, path_to_summaries, x)
			new_fcm(path_to_plots, path_to_summaries, x)
		}	
	}
}

perform_fcm <- function(path_to_plots, path_to_summaries, x){
	#################################
	# FUZZY C-MEANS
	#################################
	
	n_centers <- 2
	res.fcm <- fcm(x, centers=n_centers)
	res.fcm2 <- ppclust2(res.fcm, "kmeans")

	fcm_path <- paste("fcm",n_centers,sep="_")
	fcm_summary_path <- gsub("algorithm",fcm_path,path_to_summaries)
	fcm_plot_path <- gsub("algorithm",fcm_path,path_to_plots)

	plotcmeans <- factoextra::fviz_cluster(res.fcm2, data = x, ellipse.type = "convex",
					palette = "jco", labelsize = 0, stand = FALSE, repel = FALSE, main = NULL)

	png(filename=fcm_plot_path)
	plot(plotcmeans)
	dev.off()
	sink(fcm_summary_path)
	print(res.fcm)
	sink()
}

new_fcm <- function(path_to_plots, path_to_summaries, x){
	#################################
	# FUZZY C-MEANS
	#################################
	
	n_centers <- 2
	res.fcm <- fcm(x, centers=n_centers)

	res.fcm3 <- ppclust2(res.fcm, "fanny")

	fcm_path <- paste("fcm",n_centers,sep="_")
	fcm_summary_path <- gsub("algorithm",fcm_path,path_to_summaries)
	fcm_plot_path <- gsub("algorithm",fcm_path,path_to_plots)

	plotcmeans <- cluster::clusplot(scale(x), res.fcm3$cluster,  
				main = "Cluster plot of Iris data set",
				color=TRUE, labels = 2, lines = 2, cex=1)

	png(filename=fcm_plot_path)
	plot(plotcmeans)
	dev.off()
	sink(fcm_summary_path)
	print(res.fcm)
	sink()
}

perform_snn <- function(path_to_plots, path_to_summaries, x){
	#################################
	# SHARED NEAREST NEIGHBORS
	#################################

	k = 450
	eps = 30
	minPts = 20
	cl <- sNNclust(x, k = k, eps = eps, minPts = minPts)
	
	snn_path <- paste("snn",k,sep="_")
	snn_path <- paste(snn_path,eps,sep="_")
	snn_path <- paste(snn_path,minPts,sep="_")
	snn_summary_path <- gsub("algorithm",snn_path,path_to_summaries)
	snn_plot_path <- gsub("algorithm",snn_path,path_to_plots)

	sink(snn_summary_path)
	print(cl)
	sink()
	png(filename=snn_plot_path)
	plot(x, col = cl$cluster + 1L, cex = .9, main = '')
	dev.off()
}

main()