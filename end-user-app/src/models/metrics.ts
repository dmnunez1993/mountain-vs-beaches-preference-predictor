export interface ModelMetrics {
  model_name: string;
  accuracy: number;
  precision: number;
  recall: number;
  f1_score: number;
  roc_auc: number;
  precision_false: number;
  recall_false: number;
  f1_score_false: number;
  precision_true: number;
  recall_true: number;
  f1_score_true: number;
  conf_matrix_0_0: number;
  conf_matrix_0_1: number;
  conf_matrix_1_0: number;
  conf_matrix_1_1: number;
}
