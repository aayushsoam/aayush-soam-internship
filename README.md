# aayush-soam-internship
Machine learning project (Week 1) by Aayush Soam: Cleaning greenhouse gas emission data for Edunet foundation x Microsoft 
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

[cleaned_ghg_data.csv](https://github.com/user-attachments/files/20802185/cleaned_ghg_data.csv)
