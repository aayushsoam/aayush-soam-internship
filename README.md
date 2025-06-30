# aayush-soam-internship
Machine learning project (Week 1,week2) by Aayush Soam: Cleaning greenhouse gas emission data for 🌐Edunetfoundation x Microsoft
<details> <summary><b>⭐⭐Click to expand Terminal Output⭐⭐</b></summary>
## Sample Output

```bash
python weak1_analysis.py
Processing year: 2010
  Commodity Shape: (1576, 15) | Industry Shape: (1580, 15)
Processing year: 2011
  Commodity Shape: (1576, 15) | Industry Shape: (1580, 15)
Processing year: 2012
  Commodity Shape: (1576, 15) | Industry Shape: (1580, 15)
Processing year: 2013
  Commodity Shape: (1576, 15) | Industry Shape: (1580, 15)
Processing year: 2014
  Commodity Shape: (1576, 15) | Industry Shape: (1580, 15)
Processing year: 2015
  Commodity Shape: (1576, 15) | Industry Shape: (1580, 15)
Processing year: 2016
  Commodity Shape: (1576, 15) | Industry Shape: (1580, 15)

Final dataset shape: (22092, 15)

    Code                                               Name  ...     Source  Year
0  1111A0  Fresh soybeans, canola, flaxseeds, and other o...  ...  Commodity  2010
1  1111A0  Fresh soybeans, canola, flaxseeds, and other o...  ...  Commodity  2010
2  1111A0  Fresh soybeans, canola, flaxseeds, and other o...  ...  Commodity  2010
3  1111A0  Fresh soybeans, canola, flaxseeds, and other o...  ...  Commodity  2010
4  1111B0          Fresh wheat, corn, rice, and other grains  ...  Commodity  2010

[5 rows x 15 columns]

🧹 Missing Values Summary:
Code                                                      0
Name                                                      0
Substance                                                 0
Unit                                                      0
Supply Chain Emission Factors without Margins             0
Margins of Supply Chain Emission Factors                  0
Supply Chain Emission Factors with Margins                0
Unnamed: 7                                            22092
DQ ReliabilityScore of Factors without Margins            0
DQ TemporalCorrelation of Factors without Margins         0
DQ GeographicalCorrelation of Factors without Margins     0
DQ TechnologicalCorrelation of Factors without Margins    0
DQ DataCollection of Factors without Margins              0
Source                                                    0
Year                                                      0
dtype: int64

Cleaned data saved as 'cleaned_ghg_data.csv'

 ### 🔗 **[Download the Cleaned Data CSV here!](https://github.com/user-attachments/files/20802185/cleaned_ghg_data.csv) 📥**

#python weak2.py

Dataset Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 22092 entries, 0 to 22091
Data columns (total 14 columns):
 #   Column                                                  Non-Null Count  Dtype
---  ------                                                  --------------  -----
 0   Code                                                    22092 non-null  object
 1   Name                                                    22092 non-null  object
 2   Substance                                               22092 non-null  int64
 3   Unit                                                    22092 non-null  int64
 4   Supply Chain Emission Factors without Margins           22092 non-null  float64
 5   Margins of Supply Chain Emission Factors                22092 non-null  float64
 6   Supply Chain Emission Factors with Margins              22092 non-null  float64
 7   DQ ReliabilityScore of Factors without Margins          22092 non-null  int64
 8   DQ TemporalCorrelation of Factors without Margins       22092 non-null  int64
 9   DQ GeographicalCorrelation of Factors without Margins   22092 non-null  int64
 10  DQ TechnologicalCorrelation of Factors without Margins  22092 non-null  int64
 11  DQ DataCollection of Factors without Margins            22092 non-null  int64
 12  Source                                                  22092 non-null  int64
 13  Year                                                    22092 non-null  int64
dtypes: float64(3), int64(9), object(2)
memory usage: 2.4+ MB
None

Null Values:
Code                                                      0
Name                                                      0
Substance                                                 0
Unit                                                      0
Supply Chain Emission Factors without Margins             0
Margins of Supply Chain Emission Factors                  0
Supply Chain Emission Factors with Margins                0
DQ ReliabilityScore of Factors without Margins            0
DQ TemporalCorrelation of Factors without Margins         0
DQ GeographicalCorrelation of Factors without Margins     0
DQ TechnologicalCorrelation of Factors without Margins    0
DQ DataCollection of Factors without Margins              0
Source                                                    0
Year                                                      0
dtype: int64

Summary Stats:
                                                      count         mean       std     min      25%       50%       75%       max
Substance                                           22092.0     1.500000  1.118059     0.0     0.75     1.500     2.250     3.000      
Unit                                                22092.0     0.250000  0.433023     0.0     0.00     0.000     0.250     1.000      
Supply Chain Emission Factors without Margins       22092.0     0.084807  0.267039     0.0     0.00     0.002     0.044     7.228      
Margins of Supply Chain Emission Factors            22092.0     0.012857  0.078720     0.0     0.00     0.000     0.000     3.349      
Supply Chain Emission Factors with Margins          22092.0     0.097681  0.288992     0.0     0.00     0.003     0.052     7.290      
DQ ReliabilityScore of Factors without Margins      22092.0     3.308030  0.499643     2.0     3.00     3.000     4.000     4.000      
DQ TemporalCorrelation of Factors without Margins   22092.0     2.571429  0.494883     2.0     2.00     3.000     3.000     3.000      
DQ GeographicalCorrelation of Factors without M...  22092.0     1.000000  0.000000     1.0     1.00     1.000     1.000     1.000      
DQ TechnologicalCorrelation of Factors without ...  22092.0     2.632129  1.135661     1.0     1.00     3.000     3.000     5.000      
DQ DataCollection of Factors without Margins        22092.0     1.000000  0.000000     1.0     1.00     1.000     1.000     1.000      
Source                                              22092.0     0.500634  0.500011     0.0     0.00     1.000     1.000     1.000      
Year                                                22092.0  2013.000000  2.000045  2010.0  2011.00  2013.000  2015.000  2016.000      
C:\Users\thaku\OneDrive\Desktop\my project\aj\aayush-soam-internship\weak2.py:55: FutureWarning: 

Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `y` variable to `hue` and set `legend=False` for the same effect.

  sns.barplot(

Feature shape: (22092, 10)

Target Preview:
0    0.470
1    0.002
2    0.002
3    0.002
4    0.740
Name: Supply Chain Emission Factors with Margins, dtype: float64




FutureWarning: 

Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `y` variable to `hue` and set `legend=False` for the same effect.       

  sns.barplot(
 Features normalized.
 Train/Test Split Done: (17673, 10) (4419, 10)

 Model Comparison:
               Model           MSE      RMSE        R2
0      Random Forest  3.774615e-05  0.006144  0.999328
1  Linear Regression  7.881378e-08  0.000281  0.999999

 Linear Regression model & scaler saved successfully!

