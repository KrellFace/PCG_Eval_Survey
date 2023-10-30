
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



inputFile = 'Data/PCG Survey - Annotated V1.csv'


def generate_histogram(columns, counts, title, filename, horizontal = True, colour = "lightblue"):
    
    fig, ax = plt.subplots()

    if(horizontal):
        ax.bar(columns, counts, color = colour)
        ax.set_ylabel('Frequency', fontsize=20)
        plt.grid(axis='y')
        for rect in ax.patches:
            height = rect.get_height()
            ax.annotate(f'{int(height)}', xy=(rect.get_x()+rect.get_width()/2, height), 
                        xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
        bottom, top = plt.ylim()
        plt.ylim(bottom, top+5) 
        plt.yticks(fontsize=14)
    else:
        """
        barpos = []
        increm = 1
        curr = 1
        for i in range(len(columns)):
            barpos.append(increm)
            curr+=increm
        """

        ax.barh( columns, counts, color = colour)
        ax.invert_yaxis()
        ax.set_xlabel('Frequency', fontsize=20)
        plt.grid(axis='x')


        for rect in ax.patches:
            width = rect.get_width()
            ax.annotate(f'{int(width)}', xy=(width+.5, rect.get_y()+rect.get_height()-.2), 
                        xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
        min, max = plt.xlim()
        plt.xlim(min, max+5) 
        plt.yticks(fontsize=10)

        
    plt.xticks(fontsize=14, rotation='vertical')
    ax.set_title(title, fontsize=30)

    plt.tight_layout()
    plt.show()
    #plt.savefig('output/'+filename)

def main():
    #full_data = pd.read_csv(inputFile, skiprows=[1,2],header=[3])
    full_data = pd.read_csv(inputFile,header=[3])

    print(full_data.head)

    df_filtered1 = full_data[full_data['Paper Accessible?'] == 'Yes']
    df_filtered2 = df_filtered1[df_filtered1['Introduces novel PCG system for game levels or Virtual Environments'] == 'Yes']

    filtered_df = full_data.loc[(full_data['G1'] == 'Yes') & (full_data['G2'] == 'Yes')]

    print(filtered_df.head)

    
    methods_only = filtered_df[['M1', 'M2', 'M3', 'M4']]
    methods = ['Representation\nDirect', 'Human\nPlay', 'Agent\nPlay', 'MI\nCreation']
    method_counts = [methods_only['M1'].value_counts()['Yes'], methods_only['M2'].value_counts()['Yes'], methods_only['M3'].value_counts()['Yes'], methods_only['M4'].value_counts()['Yes']]
    #generate_histogram(methods, method_counts, "Methods Used for Evaluation", "EvalMethods", True, "powderblue")

    
    point_of_comparison = filtered_df[['C1', 'C2', 'C3', 'C4', 'C5', 'C6']]
    poc = ['With Algorithm\nvs Without', 'Alt\nParameters', 'Alt\nAlgorithms',  'System from\nPrior Research', 'Multiple\nGenerators Contrasted', 'Exemplar\nContent' ]
    poc_counts = [point_of_comparison['C1'].value_counts()['Yes'], point_of_comparison['C2'].value_counts()['Yes'], 
                  point_of_comparison['C3'].value_counts()['Yes'], point_of_comparison['C4'].value_counts()['Yes'], point_of_comparison['C5'].value_counts()['Yes'], point_of_comparison['C6'].value_counts()['Yes']]
    #generate_histogram(poc, poc_counts, "Points of Comparison", 'CompPoints', True, "orange")
    

    features_only = filtered_df[['CM1','CM2','CM3','CM4','CM5','CM6','CM7','CM8','CM9','CM10','CM11','CM12']]
    features = ['Fitness', 'Playability/\nWin Rate', 'Validated\nQuestionnaire', 'Custom\nQuestions', 'Biological\nReadings' , 'Computational Performance\nof Generator', 'Qualatative\nVisual Traits\nof a Sample', 	
                'Metric\nDiversity', 'Similarity to\ntraining levels',  'ERA'	,'Controllability', 'Performance\nas RL Curiculum']
    features_counts = [features_only['CM1'].value_counts()['Yes'],features_only['CM2'].value_counts()['Yes'],features_only['CM3'].value_counts()['Yes'],features_only['CM4'].value_counts()['Yes'],features_only['CM5'].value_counts()['Yes'],features_only['CM6'].value_counts()['Yes'],features_only['CM7'].value_counts()['Yes'],features_only['CM8'].value_counts()['Yes'],features_only['CM9'].value_counts()['Yes'],features_only['CM10'].value_counts()['Yes'],features_only['CM11'].value_counts()['Yes'],features_only['CM12'].value_counts()['Yes']]
    generate_histogram(features, features_counts, "Features Used for Comparison", 'Features', False, "lightcoral")

    domain_type_only = filtered_df[['DO1', 'DO2', 'DO3']]
    domain_types = ['Commercial Game\nor Mod', 'Pre-Existing\nResearch Platform', 'Original\nSystem']
    domain_counts = [domain_type_only['DO1'].value_counts()['Yes'],domain_type_only['DO3'].value_counts()['Yes'],domain_type_only['DO2'].value_counts()['Yes']]
    generate_histogram(domain_types, domain_counts, "Domain Types Observed", 'DomainTypes', True, "pink")
    






if __name__ == "__main__":
    main()
