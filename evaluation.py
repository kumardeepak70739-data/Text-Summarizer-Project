from rouge_score import rouge_scorer
def evaluate_summary(reference_summary, generated_summary):
    scorer=rouge_scorer.RougeScorer(['rouge1','rouge2','rougeL'],use_stemmer=True)
    scorer=scorer.score(reference_summary,generated_summary)
    return scorer