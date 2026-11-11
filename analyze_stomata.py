import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    if file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        df = pd.read_csv(file_path)
    return df

def calculate_indices(df):
    df['stomata_density_per_mm2'] = df['stomata_count'] / df['fov_area_mm2']
    df['epidermal_density_per_mm2'] = df['epidermal_cell_count'] / df['fov_area_mm2']
    df['stomatal_index'] = (df['stomata_count'] / (df['stomata_count'] + df['epidermal_cell_count'])) * 100
    return df

def summarize_species(df):
    summary = df.groupby(['species', 'leaf_surface']).agg({
        'stomata_density_per_mm2': ['mean', 'std'],
        'stomatal_index': ['mean', 'std']
    }).reset_index()
    summary.columns = ['Species', 'Leaf Surface', 'Mean Density', 'SD Density', 'Mean Index', 'SD Index']
    return summary

def plot_density_comparison(df, output_path='figures/stomatal_density_comparison.png'):
    summary = df.groupby(['species', 'leaf_surface'])['stomata_density_per_mm2'].mean().unstack()

    fig, ax = plt.subplots(figsize=(8, 5))
    summary.plot(kind='bar', ax=ax, color=['mediumseagreen', 'goldenrod'], width=0.6, edgecolor='black', linewidth=0.8)

    ax.set_title('Stomatal Density Across Plant Species (Abaxial vs Adaxial)', fontsize=12, pad=12)
    ax.set_xlabel('Plant Species', fontsize=10)
    ax.set_ylabel('Stomatal Density (stomata / mm²)', fontsize=10)
    ax.set_xticklabels(summary.index, rotation=15, ha='right')
    ax.legend(title='Leaf Surface', frameon=True)
    ax.grid(axis='y', linestyle='--', alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

def plot_stomatal_index(df, output_path='figures/stomatal_index_distribution.png'):
    abaxial_df = df[df['leaf_surface'] == 'Abaxial']
    species_list = abaxial_df['species'].unique()
    data = [abaxial_df[abaxial_df['species'] == sp]['stomatal_index'].values for sp in species_list]

    fig, ax = plt.subplots(figsize=(7, 4.5))
    box = ax.boxplot(data, tick_labels=species_list, patch_artist=True)

    colors = ['lightblue', 'lightgreen', 'peachpuff', 'plum']
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_edgecolor('black')

    ax.set_title('Stomatal Index Distribution (Lower / Abaxial Surface)', fontsize=12, pad=12)
    ax.set_xlabel('Plant Species', fontsize=10)
    ax.set_ylabel('Stomatal Index (%)', fontsize=10)
    ax.set_xticklabels(species_list, rotation=15, ha='right')
    ax.grid(axis='y', linestyle='--', alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

def main():
    input_file = 'data/stomatal_observations.csv'
    df = load_data(input_file)
    df = calculate_indices(df)

    summary = summarize_species(df)
    print("Stomatal Analysis Summary:")
    print("=" * 75)
    print(summary.to_string(index=False))

    df.to_csv('results/calculated_stomatal_indices.csv', index=False)
    summary.to_csv('results/species_summary_statistics.csv', index=False)

    plot_density_comparison(df, 'figures/stomatal_density_comparison.png')
    plot_stomatal_index(df, 'figures/stomatal_index_distribution.png')
    print("\nResults and figures successfully saved to results/ and figures/ directories.")

if __name__ == '__main__':
    main()
