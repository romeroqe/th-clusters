# TH clusters  
<a href="https://github.com/romeroqe/th-clusters"><img src="https://shields.io/github/v/release/romeroqe/th-clusters" alt="Release"></a>
<a href="http://creativecommons.org/licenses/by/4.0/"><img src="https://shields.io/github/license/romeroqe/th-clusters" alt="License"></a>
<a href="https://doi.org/10.5281/zenodo.10038644"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.10038644.svg" alt="DOI"></a>

This repository has the data sets containing temperature and salinity centroids, in addition to the location of the thermohaline, temperature and salinity clusters described in a scientific publication. The data set has the position of centroids of 2 to 50 clusters of Conservative Temperature, Absolute Salinity and Thermohaline, which allows delimiting coherent thermohaline structures in the global ocean at different spatial scales. The repository also contains demo notebooks of the use of these clusters and the procedures described in the manuscript.

## Datasets
In the `cluster-location.zip` there are the CSV files that contain the location of the salinity, temperature and thermohaline clusters, with the headers:
- `longitude`: Contains the longitude where the profile was measured.
- `latitude`: Contains the latitude where the profile was measured.
- `month`: Contains the month of the year when the profile was measured.
- `2_{param}`: Contains clusters from 0 to _k_-1 for 2 centroids (_k_=2).
- `3_{param}`: Contains clusters from 0 to _k_-1 for 2 centroids (_k_=3).
- ...
- `50_{param}`: Contains clusters from 0 to _k_-1 for 2 centroids (_k_=50).

In the `salinity-centroids.zip` and `temperature-centroids.zip` there are the CSV files that contain the data of the _k_ centroids (one centroid per column) from 10 m to 1500 m depth (rows). The centroid files are named `{k}_centroids.csv`, where _k_ is a string with the number of centroids (clusters) of interest to which a zero (0) is added at the beginning, until it reaches 2 digits.

Finally, `argo-profiles.zip` contains 5 profiles from the Argo snapshot of June 2023 (https://www.seanoe.org/data/00311/42182/#103075), used in the demo notebooks.

## Demo
To view the demos, go to each notebook and run it:

- `demo1.ipynb`: How to read the CSV files that contain the location of the salinity, temperature and thermohaline clusters, how to plot them and how to obtain thermohaline clusters from temperature and salinity clusters.
- `demo2.ipynb`: How to read the CSV files containing _k_ centroid data, how to implement Euclidean distance to classify new profiles, and how to plot your classified profiles on a T-S diagram.
- `demo3.ipynb`: How to use the K-means algorithm to group profiles of any parameter, how to obtain the centroids, how to assign the resulting clusters to each profile and how to plot the profiles by group in a p-T diagram.

## How to cite

> [!IMPORTANT]
> _If you use this repository, please include a reference to the following:_
> 
> Romero, E., Portela, E., Tenorio-Fernandez, L., and Sánchez-Velasco, L.: Detection of coherent thermohaline structures over the global ocean using clustering, Deep-Sea Res. I: Oceanogr. Res. Pap., 104344, https://doi.org/10.1016/j.dsr.2024.104344, 2024.

## Argo data acknowledgment
Argo data were collected and made freely available by the International Argo Program and the national programs that contribute to it. ([http://www.argo.ucsd.edu](http://www.argo.ucsd.edu), [http://argo.jcommops.org](http://argo.jcommops.org)). The Argo Program is part of the Global Ocean Observing System.

## License
  
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
