from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

data_file = Path(__file__).with_name("data.csv")
output_dir = Path(__file__).with_name("analysis_output")
output_dir.mkdir(exist_ok=True)

df = pd.read_csv(data_file)

required_columns = {"name", "age", "score"}
missing_columns = required_columns.difference(df.columns)
if missing_columns:
	raise ValueError(f"Colunas ausentes no CSV: {', '.join(sorted(missing_columns))}")
if df.empty:
	raise ValueError("O arquivo CSV não contém registros para analisar.")

age_summary = df.groupby("age")["score"].agg(["mean", "median", "count"]).sort_index()
mean_by_age = age_summary["mean"]
highest_mean_age = mean_by_age.idxmax()
lowest_mean_age = mean_by_age.idxmin()
mean_difference = mean_by_age[highest_mean_age] - mean_by_age[lowest_mean_age]
high_score_count = int((df["score"] >= 90).sum())
score_min = int(df["score"].min())
score_max = int(df["score"].max())

print("=== Primeiras 5 linhas ===")
print(df.head())

print("\n=== Estatísticas descritivas ===")
print(df.describe())
print(f"\nMediana das notas: {df['score'].median():.2f}")

print("\n=== Média das notas por idade ===")
print(age_summary["mean"].round(2).rename("mean_score"))

print("\n=== Insights ===")
print(
	f"Na amostra, estudantes de {highest_mean_age} anos tiveram a maior média "
	f"({mean_by_age[highest_mean_age]:.2f}), uma diferença de "
	f"{mean_difference:.2f} pontos em relação aos estudantes de "
	f"{lowest_mean_age} anos. Isso descreve este conjunto e não indica causalidade."
)
print(
	f"As notas variaram de {score_min} a {score_max}; "
	f"{high_score_count} de {len(df)} estudantes tiveram nota igual ou superior a 90."
)

histogram_path = output_dir / "score-distribution.png"
histogram, axis = plt.subplots(figsize=(8, 5))
axis.hist(df["score"], bins=6, color="#2D7F73", edgecolor="white")
axis.set_title("Distribuição das notas")
axis.set_xlabel("Nota")
axis.set_ylabel("Número de estudantes")
axis.grid(axis="y", alpha=0.25)
histogram.tight_layout()
histogram.savefig(histogram_path, dpi=160)
plt.close(histogram)

age_chart_path = output_dir / "average-score-by-age.png"
age_chart, axis = plt.subplots(figsize=(8, 5))
bars = axis.bar(
	age_summary.index.astype(str),
	age_summary["mean"],
	color="#D99335",
	width=0.55,
)
axis.bar_label(bars, fmt="%.2f", padding=4)
axis.set_title("Média das notas por idade")
axis.set_xlabel("Idade")
axis.set_ylabel("Nota média")
axis.set_ylim(0, max(age_summary["mean"]) * 1.15)
axis.grid(axis="y", alpha=0.25)
age_chart.tight_layout()
age_chart.savefig(age_chart_path, dpi=160)
plt.close(age_chart)

print(f"\nGráficos salvos em:\n- {histogram_path}\n- {age_chart_path}")
