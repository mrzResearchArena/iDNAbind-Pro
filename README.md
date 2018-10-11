
# <center>iDNAbind-Pro: Identification of DNA-binding protein </center>

<!-- ### Authors: Rafsanjani Muhammod, Sajid Ahmed, Dewan Md Farid, Swakkhar Shatabda, Alok Sharma, Abdollah Dehzangi -->
<!-- ### <center> United International University, Dhaka, Bangladesh  </center> -->

&nbsp;

## 1. Download Package
### 1.1. Direct Download
We can directly [download](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/mrzResearchArena/iDNAbind-Pro) by clicking the link.

**Note:** The package will download in zip format `(.zip)` named `iDNAbind-Pro-master.zip`.

***`or,`***

### 1.2. Clone a GitHub Repository (Optional)

Cloning a repository syncs it to our local machine. After clone, we can add and edit files and then push and pull updates.
- Clone over HTTPS: `user@machine:~$ git clone https://github.com/mrzResearchArena/iDNAbind-Pro.git `
- Clone over SSH: `user@machine:~$ git clone git@github.com:mrzResearchArena/iDNAbind-Pro.git `

**Note:** If the clone was successful, a new sub-directory appears on our local drive. This directory has the same name (iDNAbind-Pro) as the `GitHub` repository that we cloned.


## 2. Installation Process
### 2.1. Required Python Packages
`Major (Generate Features):`
- Install: python (version >= 3.5)
- Install: numpy (version >= 1.13.0)

`Minor (Performance Measures):`
- Install: sklearn (version >= 0.19.0)
- Install: pandas (version >= 0.21.0)
- Install: matplotlib (version >= 2.1.0)

### 2.2. How to download
`Using PIP:`  pip install `<package name>`
```console
user@machine:~$ pip install scikit-learn
```
**`or,`**

`Using anaconda environment:` conda install `<package name>`

```console
user@machine:~$ conda install scikit-learn
```

## 3. Working Procedure

Run command on your console or terminal.

### 3.1. Generate Features
#### 3.1.1. Training Purpose
```console
user@machine:~$ python main.py --fullDataset=1 --optimumDataset=1 --fasta=/home/user/iDNAbind-Pro/ProteinDatasets/PDB1075_FASTA.txt --label=/home/user/iDNAbind-Pro/ProteinDatasets/PDB1075_Label.txt --kTuple=3 --kGap=5 --pseudoKNC=1 --monoMono=1 --monoDi=1 --monoTri=1 --diMono=1 --diDi=1 --diTri=1 --triMono=1 --triDi=1
```
***`or,`***

```console
user@machine:~$ python main.py -full=1 -optimum=1 -fa=/home/user/iDNAbind-Pro/ProteinDatasets/PDB1075_FASTA.txt -la=/home/user/iDNAbind-Pro/ProteinDatasets/PDB1075_Label.txt -ktuple=3 -kgap=5 -pseudo=1 -f11=1 -f12=1 -f13=1 -f21=1 -f22=1 -f23=1 -f31=1 -f32=1
```

#### 3.1.2. Evaluation Purpose

```console
user@machine:~$ python main.py --testDataset=1 --fasta=/home/user/iDNAbind-Pro/ProteinDatasets/PDB186_independentFASTA.txt --label=/home/user/iDNAbind-Pro/ProteinDatasets/PDB186_independentLabel.txt --kTuple=3 --kGap=5 --pseudoKNC=1 --monoMono=1 --monoDi=1 --monoTri=1 --diMono=1 --diDi=1 --diTri=1 --triMono=1 --triDi=1
```
***`or,`***

```console
user@machine:~$ python main.py -test=1 -fa=/home/user/iDNAbind-Pro/ProteinDatasets/PDB186_independentFASTA.txt -la=/home/user//Datasets/Protein/PDB186_PDB186_independentLabel.txt -ktuple=3 -kgap=5 -pseudo=1 -atgc=1 -f11=1 -f12=1 -f13=1 -f21=1 -f22=1 -f23=1 -f31=1 -f32=1
```

[ Comment: The `= sign` is optional. ]

**Note #1:** It will generate a full dataset named **fullDataset.csv** (if -full=1 `or,` --fullDataset==1) <br>
**Note #2:** It will generate a selected features dataset named **optimumDataset.csv** (if -optimum=1 `or,` --optimumDataset==1), and It will also track the selected features index. <br>
**Note #3:** It will generate a full dataset named **testDataset.csv** (if -test=1 `or,` --testDataset==1) [ Especially for the independent (testing) dataset purpose. ] **[ 3.1.2. ]** <br>
**Note #4:** The process will run smoothly for valid FASTA sequences and row-wise class label.

&nbsp;

#### Table 1: Arguments Details for the Features Generation
|   Argument     |   Corresponding Optional Argument |     Type     |   Default | Help   |
|     :---       |    :---:     |  :---:       |  :---:    | ---:|
| --fasta | -fa  | string |  | Enter a UNIX-like path; Example: /home/user/FASTA.txt |
| --label | -la  | string |  | Enter a UNIX-like path; Example: /home/user/Label.txt |
| --kGap | -kgap  | integer | --kGap=5  | Maximum number of gapped; Example: -kGap=5  |
| --kTuple | -ktuple  | integer | --kTuple=3  | Maximum number of nucleotides; Example: -kTuple=3 |
| --fullDataset | -full  | integer |  --fullDataset=0  | Set --fullDataset=1, if we don't want to save full dataset. |
| --testDataset | -test  | integer |  --testDataset=0  | Set --testDataset=1, if we don't want to save test dataset. |
| --optimumDataset | -optimum  | integer |  --optimumDataset=0  | Set --optimumDataset=1, if we don't want to save optimum dataset. |
| --pseudoKNC | -pseudo  | integer |  --pseudoKNC=0  | Set --pseudoKNC=1, if we want to generate features. |
| --monoMono | -f11  | integer |  --monoMono=0  | Set --monoMono=1, if we want to generate features. |
| --monoDi | -f12  | integer |  --monoDi=0  | Set --monoDi=1, if we want to generate features. |
| --monoTri | -f13  | integer |  --monoTri=0  | Set --monoTri=1, if we want to generate features. |
| --diMono | -f21  | integer |  --diMono=0  | Set --diMono=1, if we want to generate features. |
| --diDi | -f22  | integer |  --diDi=0  | Set --diDi=1, if we want to generate features. |
| --diTri | -f23  | integer |  --diTri=0  | Set --diTri=1, if we want to generate features. |
| --triMono | -f31  | integer |  --triMono=0  | Set --triMono=1, if we want to generate features. |
| --triDi | -f32  | integer |  --triDi=0  | Set --triDi=1, if we want to generate features. |


&nbsp;
&nbsp;
&nbsp;

#### Table 2: Features Description
| Feature Name | Feature Structure / Formula | Number of Features |
| :---         |        :---:      |         ---:    |
|pseudoKNC| X, XX, XXX | when --kTuple=3, then 8,420 features are extracted for the protein sequence|
|monoMonoKGap| X_X |when --kGap=1, then 400 features are extracted for the protein sequence|
|monoDiKGap| X_XX |when --kGap=1, then 8,000 features are extracted for the protein sequence|
|monoTriKGap| X_XXX |when --kGap=1, then 160,000 features are extracted for the protein sequence|
|diMonoKGap| XX_X |when --kGap=1, then 8,000 features are extracted for the protein sequence|
|diDiKGap| XX_XX |when --kGap=1, then 160,000 features are extracted for the protein sequence|
|diTriKGap| XX_XXX |when --kGap=1, then 3,200,000 features are extracted for the protein sequence|
|triMonoKGap| XXX_X |when --kGap=1, then 160,000 features are extracted for the protein sequence|
|triDiKGap| XXX_XX |when --kGap=1, then 3,200,000 features are extracted for the protein sequence|

**Note:** When sequence becomes protein then
X = {A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y}.

&nbsp;
&nbsp;
&nbsp;


### 3.2. Run Machine Learning Classifiers (Optional)
```console
user@machine:~$ python runClassifiers.py --nFCV=10 --dataset=optimumDataset.csv --auROC=1 --boxPlot=1
```

**Note #1:** It will provide classification results (**evaluationResults.txt**) from the user provides binary class dataset (**.csv** format). <br>
**Note #2:** Generate a ROC Curve (**auROC.png**). <br>
**Note #3:** Generate an accuracy comparison via boxPlot (**AccuracyBoxPlot.png**).


&nbsp;

#### Table 3: Arguments Details for the Machine Learning Classifiers
|   Argument     |   Corresponding Optional Argument  |     Type     |   Default | Help   |
|     :---       |    :---:     |  :---:       |  :---:    | ---:|
| --nFCV | -cv | integer | --nFCV=10 | How many numbers of cross-validation? |
| --dataset | -data  | string | --dataset=optimumDataset.csv | Enter a UNIX-like path for a .csv file; Example: /home/User/dataset.csv |
|--auROC|-roc|integer|--auROC=1|Set --auROC=0, if we didn't want to generate the ROC Curve.|
|--boxPlot|-box|integer|--boxPlot=1|Set --boxPlot=0, if we didn't want to generate the accuracy box-plot.|

&nbsp;
### 3.3. Training Model (Optional)

```console
user@machine:~$ python trainModel.py --dataset=optimumDataset.csv --model=LR
```

**Note #1:** It will provide a **dumpModel.pkl** from the user provides binary class dataset (**.csv** format). <br>

&nbsp;

#### Table 4: Arguments Details for Training Model
|   Argument     |   Corresponding Optional Argument   |     Type     |   Default | Help   |
|     :---       |    :---:     |  :---:       |  :---:    | ---:|
| --dataset | -data  | string | --dataset=optimumDataset.csv | Enter a UNIX-like path for a .csv file; Example: /home/User/dataset.csv |
|--model|-m|string|--model=LR|We can use LR, SVM, KNN, DT, SVM, NB, Bagging, RF, AB, GB, and LDA as an option; All options are case sensitive.|
| --K | -k  | integer | --K=5 | Only for the KNN classifier; Number of neighbor |

**Note:** LR, SVM, KNN, DT, NB, Bagging, RF, AB, GB, and LDA represents Logistics Regression, Support Vector Machine, k-Nearest Neighbor, Decision Tree, Naive Bayes, Bagging, Random Forest, AdaBoost, Gradient Boosting, Linear Discriminant Analysis classifier respectively.

&nbsp;
&nbsp;
&nbsp;

### 3.4. Evaluation Model (Optional)

```console
user@machine:~$ python evaluateModel.py --optimumDatasetPath=optimumDataset.csv --testDatasetPath=testDataset.csv
```

**Note #1:** Here, **optimumDataset.csv**, and **testDataset.csv** using as a traing dataset and test dataset respectively.

&nbsp;

#### Table 5: Arguments Details for Evaluation Model
|   Argument     | Corresponding Optional Argument   |     Type     |   Default | Help   |
|     :---       |    :---:     |  :---:       |  :---:    | ---:|
| --optimumDatasetPath | -optimumPath  | string | --optimumDatasetPath=optimumDataset.csv | Enter a UNIX-like path for a .csv file; Example: /home/User/dataset.csv |
| --testDatasetPath | -testPath  | string | --testDatasetPath=testDataset.csv | Enter a UNIX-like path for a .csv file; Example: /home/User/dataset.csv |


&nbsp;
&nbsp;
&nbsp;

## References

**[1]** Bin Liu, Fule Liu, Longyun Fang, Xiaolong Wang, and Kuo-Chen Chou. repdna: a python pack-
age to generate various modes of feature vectors for dna sequences by incorporating user-defined
physicochemical properties and sequence-order effects. Bioinformatics, 31(8):1307–1309, 2014.

**[2]** Dong-Sheng Cao, Qing-Song Xu, and Yi-Zeng Liang. propy: a tool to generate various modes of
chous pseaac. Bioinformatics, 29(7):960–962, 2013.

**[3]** Bin Liu. Bioseq-analysis: a platform for dna, rna and protein sequence analysis based on machine
learning approaches. Briefings in bioinformatics, 2017.

**[4]** Zhen Chen, Pei Zhao, Fuyi Li, André Leier, Tatiana T Marquez-Lago, Yanan Wang, Geoffrey I Webb,
A Ian Smith, Roger J Daly, Kuo-Chen Chou, et al. ifeature: a python package and web server for
features extraction and selection from protein and peptide sequences. Bioinformatics, 1:4, 2018.

**[5]** Bin Liu, Hao Wu, Deyuan Zhang, Xiaolong Wang, and Kuo-Chen Chou. Pse-analysis: a python
package for dna/rna and protein/peptide sequence analysis based on pseudo components and kernel
methods. Oncotarget, 8(8):13338, 2017.

**[6]** Bin Liu, Fule Liu, Xiaolong Wang, Junjie Chen, Longyun Fang, and Kuo-Chen Chou. Pse-in-one: a
web server for generating various modes of pseudo components of dna, rna, and protein sequences.
Nucleic acids research, 43(W1):W65–W71, 2015.

**[7]** Fabian Pedregosa, Gaël Varoquaux, Alexandre Gramfort, Vincent Michel, Bertrand Thirion, Olivier
Grisel, Mathieu Blondel, Peter Prettenhofer, Ron Weiss, Vincent Dubourg, et al. Scikit-learn: Ma-
chine learning in python. Journal of machine learning research, 12(Oct):2825–2830, 2011.
