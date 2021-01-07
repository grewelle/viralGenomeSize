import pandas
import seaborn as sns
from matplotlib import pyplot as plt
#sns.set(style="white")
sns.set(font_scale=3)

def main():

    viruses = pandas.read_csv("C:/Users/Richard/Desktop/desktop/masterVirusList_human.csv")
    ax2 = sns.catplot(x="Group", y="Genome", hue="Zoonotic", kind="violin", data=viruses, size=16)

    ax2.set(yscale='log')
    ax2.set_axis_labels('Baltimore group', 'Genome size')

    ax2.savefig('violin_humans.png')
    plt.show()
main()