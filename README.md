# IMDb Movie Genre Revenue Analysis


## Project Overview
This project analyzes key factors influencing the financial success of movies. By examining the relationship between movie genres, countries of origin, content ratings, and their corresponding incomes, the study identifies patterns and trends to inform decision-making in film production and distribution. The insights aim to help filmmakers, producers, and marketers optimize their strategies for maximizing box office returns and targeting the most profitable segments of the movie industry.


## Dataset
The analysis uses the IMDb dataset, which includes information about movies:
- **Source:** Kaggle IMDb Dataset
- **Key Features:**
  - `IMBD title ID`: Unique identifier for each movie
  - `Original title`: Name of the movie
  - `Release year`: Year the movie was released
  - `Genre`: Genre(s) of the movie
  - `Duration (mins)`: Duration of the movie in minutes
  - `Country`: Country of origin
  - `Content Rating`: Age rating of the movie
  - `Director`: Director of the movie
  - `Income ($)`: Box office earnings
  - `Votes`: Number of votes
  - `Score`: Movie rating


## Installation and Requirements
To run this project, you'll need Python 3.0 and the following libraries:
- pandas
- matplotlib
- seaborn


Install the required packages using:
```bash
pip install -r requirements.txt
```


## File Descriptions
- **README.md**: This file provides an overview of the project, including objectives, dataset details, methodology, and instructions for running the analysis.


- **Analysis_of_IMDb_Dataset.ipynb**: Jupyter Notebook containing the exploratory data analysis (EDA) and visualizations of the IMDb dataset. This notebook includes code, visualizations, and markdown explanations to help understand the insights derived from the analysis.


- **Data_Cleaning_on_IMDB_Dataset.py**: Python script used for data cleaning. This script handles tasks such as removing duplicates, dealing with missing values, and ensuring data consistency.


- **Analysis_of_IMDb_Dataset.py**: Python script for performing the analysis and generating results. This script includes code for exploratory data analysis, creating visualizations, and summarizing key findings from the IMDb dataset.


## Methodology
1. **Data Cleaning:** Removing duplicates, handling missing values, and ensuring data consistency.
2. **Exploratory Data Analysis (EDA):** Identifying key patterns and trends in the data.
3. **Visualization:** Using charts and plots to illustrate findings.


## Results
The analysis reveals that:
- Genres like Action, Adventure, and Drama, along with movies from countries like New Zealand, USA, and France, generally generate higher revenues.
- PG-13 rated movies tend to have a broader appeal, leading to increased financial success.
- The genre that generates the highest revenue varies by country, providing insights into regional preferences.


These insights can guide decisions in film production, marketing strategies, and distribution to enhance financial outcomes.


## Usage Instructions
1. **Data Cleaning:** Run `Data_Cleaning_on_IMDB_Dataset.py` to preprocess the dataset.
2. **Analysis:** Open `Analysis_of_IMDb_Dataset.ipynb` or run `Analysis_of_IMDb_Dataset.py` to perform the analysis and visualize the results.


## Example Output
The analysis will produce visualizations of genre performance across countries and insights into how different factors influence movie revenue. Refer to the Jupyter Notebook for detailed visual outputs.


## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.


## Acknowledgments
- The IMDb dataset is sourced from Kaggle.


## Contact Information
For any questions or feedback, feel free to reach out to me via [LinkedIn](https://www.linkedin.com/in/atim-edubio/) or [atimedubio500@gmail.com](mailto:atimedubio500@gmail.com).

