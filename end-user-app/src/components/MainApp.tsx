import { useState } from "react";
import Tab from "react-bootstrap/Tab";
import Tabs from "react-bootstrap/Tabs";
import PredictionTab from "./PredictionTab";

const MainApp = () => {
  const [tab, setTab] = useState<string>("prediction");
  return (
    <>
      <Tabs
        id="controlled-tab-example"
        activeKey={tab}
        onSelect={(tab) => setTab(tab !== null ? tab : "prediction")}
        className="mb-3"
      >
        <Tab eventKey="prediction" title="Prediction">
          <PredictionTab />
        </Tab>
      </Tabs>
    </>
  );
};

export default MainApp;
