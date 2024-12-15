import { useEffect, useState } from "react";

import { Button, Col, Form, Row } from "react-bootstrap";
import Table from "react-bootstrap/Table";

import { ModelMetrics } from "../models/metrics";
import { getAbsoluteUrl } from "../api/urls";
import { errorAlert } from "./utils/messages";

const MetricsTab = () => {
  const [metrics, setMetrics] = useState<ModelMetrics | null>(null);
  const [loading, setLoading] = useState(false);
  const updateMetrics = async () => {
    setLoading(true);

    const url = getAbsoluteUrl("/metrics/");
    const res = await fetch(url, {
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      method: "GET",
      credentials: "include",
    });

    if (res.status !== 200) {
      errorAlert(
        "An error ocurred. Please, click on the refresh button to try again"
      );
      setLoading(false);
      return;
    }

    const responseData = (await res.json()) as {
      status: string;
      data: ModelMetrics;
    };

    setMetrics(responseData.data);

    setLoading(false);
  };
  useEffect(() => {
    updateMetrics();
  }, []);

  return (
    <>
      <Row className="mb-1">
        <Row className="mb-1">
          <Col>
            <h3>
              Metrics{" "}
              <Button onClick={updateMetrics}>
                <i className="fa fa-refresh" />
              </Button>
            </h3>
          </Col>
        </Row>
      </Row>
      <Row>
        <Col md={6}>
          <Row>
            <Col>
              <Form.Label>
                <h4>Scores</h4>
              </Form.Label>
            </Col>
          </Row>
          <Row>
            <Col>
              <Table striped bordered hover>
                <thead>
                  <tr>
                    <th>Metric</th>
                    <th>Value</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Accuracy</td>
                    <td style={{ textAlign: "right" }}>
                      {metrics !== null ? metrics.accuracy.toFixed(2) : "-"}
                    </td>
                  </tr>
                  <tr>
                    <td>Precision</td>
                    <td style={{ textAlign: "right" }}>
                      {metrics !== null ? metrics.precision.toFixed(2) : "-"}
                    </td>
                  </tr>
                  <tr>
                    <td>Recall</td>
                    <td style={{ textAlign: "right" }}>
                      {metrics !== null ? metrics.recall.toFixed(2) : "-"}
                    </td>
                  </tr>
                  <tr>
                    <td>F1 Score</td>
                    <td style={{ textAlign: "right" }}>
                      {metrics !== null ? metrics.f1_score.toFixed(2) : "-"}
                    </td>
                  </tr>
                  <tr>
                    <td>ROC AUC</td>
                    <td style={{ textAlign: "right" }}>
                      {metrics !== null ? metrics.roc_auc.toFixed(2) : "-"}
                    </td>
                  </tr>
                </tbody>
              </Table>
            </Col>
          </Row>
        </Col>
        <Col md={6}>
          <Row>
            <Col>
              <Form.Label>
                <h4>Classification Report</h4>
              </Form.Label>
            </Col>
          </Row>
          <Row>
            <Col>
              <Table striped bordered hover>
                <thead>
                  <tr>
                    <th></th>
                    <th>precision</th>
                    <th>recall</th>
                    <th>f1-score</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Beaches</td>
                    <td style={{ textAlign: "right" }}>
                      {metrics !== null
                        ? metrics.precision_false.toFixed(2)
                        : "-"}
                    </td>
                    <td style={{ textAlign: "right" }}>
                      {metrics !== null ? metrics.recall_false.toFixed(2) : "-"}
                    </td>
                    <td style={{ textAlign: "right" }}>
                      {metrics !== null
                        ? metrics.f1_score_false.toFixed(2)
                        : "-"}
                    </td>
                  </tr>
                  <tr>
                    <td>Mountains</td>
                    <td style={{ textAlign: "right" }}>
                      {metrics !== null
                        ? metrics.precision_true.toFixed(2)
                        : "-"}
                    </td>
                    <td style={{ textAlign: "right" }}>
                      {metrics !== null ? metrics.recall_true.toFixed(2) : "-"}
                    </td>
                    <td style={{ textAlign: "right" }}>
                      {metrics !== null
                        ? metrics.f1_score_true.toFixed(2)
                        : "-"}
                    </td>
                  </tr>
                </tbody>
              </Table>
            </Col>
          </Row>
          <Row>
            <Col>
              <Form.Label>
                <h4>Confusion Matrix</h4>
              </Form.Label>
            </Col>
          </Row>
          <Row>
            <Col>
              <Table striped bordered hover>
                <thead>
                  <tr>
                    <th></th>
                    <th>Beaches</th>
                    <th>Mountains</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Beaches</td>
                    <td>{metrics !== null ? metrics.conf_matrix_0_0 : "-"}</td>
                    <td>{metrics !== null ? metrics.conf_matrix_0_1 : "-"}</td>
                  </tr>
                  <tr>
                    <td>Mountains</td>
                    <td>{metrics !== null ? metrics.conf_matrix_1_0 : "-"}</td>
                    <td>{metrics !== null ? metrics.conf_matrix_1_1 : "-"}</td>
                  </tr>
                </tbody>
              </Table>
            </Col>
          </Row>
        </Col>
      </Row>
    </>
  );
};

export default MetricsTab;
