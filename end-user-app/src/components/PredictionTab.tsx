import Form from "react-bootstrap/Form";

import { Button, Col, Row } from "react-bootstrap";
import { useState } from "react";
import { emptyValueOnNull } from "../utils/fields";
import {
  LOCATION_CHOICES,
  EDUCATION_LEVEL_CHOICES,
  GENDER_CHOICES,
  PREFERRED_ACTIVITIES_CHOICES,
  FAVORITE_SEASON_CHOICES,
  AGE_RANGE_CHOICES,
} from "../models/prediction";

const PredictionTab = () => {
  const [income, setIncome] = useState<number | null>(null);
  const [travelFrecuency, setTravelFrequency] = useState<number | null>(null);
  const [vacationBudget, setVacationBudget] = useState<number | null>(null);
  const [proximityToMountains, setProximityToMountains] = useState<
    number | null
  >(null);
  const [proximityToBeaches, setProximityToBeaches] = useState<number | null>(
    null
  );
  const [gender, setGender] = useState<string | null>(null);
  const [educationLevel, setEducationLevel] = useState<string | null>(null);
  const [preferredActivities, setPreferredActivities] = useState<string | null>(
    null
  );
  const [location, setLocation] = useState<string | null>(null);
  const [favoriteSeason, setFavoriteSeason] = useState<string | null>(null);
  const [ageRange, setAgeRange] = useState<string | null>(null);

  const onIncomeChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newIncome = parseInt(e.target.value);
    setIncome(!isNaN(newIncome) ? newIncome : null);
  };

  const onTravelFrequencyChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newTravelFrequency = parseInt(e.target.value);
    setTravelFrequency(!isNaN(newTravelFrequency) ? newTravelFrequency : null);
  };

  const onVacationBudgetChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newVacationBudget = parseInt(e.target.value);
    setVacationBudget(!isNaN(newVacationBudget) ? newVacationBudget : null);
  };

  const onProximityToMountainsChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    const newProximityToMountains = parseInt(e.target.value);
    setProximityToMountains(
      !isNaN(newProximityToMountains) ? newProximityToMountains : null
    );
  };

  const onProximityToBeachesChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    const newProximityToBeaches = parseInt(e.target.value);
    setProximityToBeaches(
      !isNaN(newProximityToBeaches) ? newProximityToBeaches : null
    );
  };

  const onGenderChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setGender(e.target.value);
  };

  const onEducationLevelChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setEducationLevel(e.target.value);
  };

  const onPreferredActivitiesChange = (
    e: React.ChangeEvent<HTMLSelectElement>
  ) => {
    setPreferredActivities(e.target.value);
  };

  const onLocationChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setLocation(e.target.value);
  };

  const onFavoriteSeasonChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setFavoriteSeason(e.target.value);
  };

  const onAgeRangeChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setAgeRange(e.target.value);
  };

  return (
    <Form.Group>
      <Row>
        <Col md={6}>
          <Row className="mb-5">
            <Col>
              <h3>Prediction Fields</h3>
            </Col>
          </Row>
          <Row className="mb-1">
            <Col md={3}>
              <Form.Label>
                <span className="text-danger">*</span> Income:
              </Form.Label>
            </Col>
            <Col md={9}>
              <Form.Control
                onChange={onIncomeChange}
                aria-placeholder="Income"
                type="number"
                value={emptyValueOnNull(income)}
              ></Form.Control>
            </Col>
          </Row>
          <Row className="mb-1">
            <Col md={3}>
              <Form.Label>
                <span className="text-danger">*</span> Travel Frequency:
              </Form.Label>
            </Col>
            <Col md={9}>
              <Form.Control
                onChange={onTravelFrequencyChange}
                aria-placeholder="Travel Frequency"
                type="number"
                value={emptyValueOnNull(travelFrecuency)}
              ></Form.Control>
            </Col>
          </Row>
          <Row className="mb-1">
            <Col md={3}>
              <Form.Label>
                <span className="text-danger">*</span> Vacation Budget:
              </Form.Label>
            </Col>
            <Col md={9}>
              <Form.Control
                onChange={onVacationBudgetChange}
                aria-placeholder="Vacation Budget"
                type="number"
                min="0"
                value={emptyValueOnNull(vacationBudget)}
              ></Form.Control>
            </Col>
          </Row>
          <Row className="mb-1">
            <Col md={3}>
              <Form.Label>
                <span className="text-danger">*</span> Proximity to Mountains:
              </Form.Label>
            </Col>
            <Col md={9}>
              <Form.Control
                onChange={onProximityToMountainsChange}
                aria-placeholder="Proximity to Mountains"
                type="number"
                min="0"
                value={emptyValueOnNull(proximityToMountains)}
              ></Form.Control>
            </Col>
          </Row>
          <Row className="mb-1">
            <Col md={3}>
              <Form.Label>
                <span className="text-danger">*</span> Proximity to Beaches:
              </Form.Label>
            </Col>
            <Col md={9}>
              <Form.Control
                onChange={onProximityToBeachesChange}
                aria-placeholder="Proximity to Beaches"
                type="number"
                min="0"
                value={emptyValueOnNull(proximityToBeaches)}
              ></Form.Control>
            </Col>
          </Row>
          <Row className="mb-1">
            <Col md={3}>
              <Form.Label>
                <span className="text-danger">*</span> Gender:
              </Form.Label>
            </Col>
            <Col md={9}>
              <Form.Select onChange={onGenderChange}>
                <option>Open this select menu</option>
                {GENDER_CHOICES.map((value, idx) => (
                  <option key={idx} value={value}>
                    {value}
                  </option>
                ))}
              </Form.Select>
            </Col>
          </Row>
          <Row className="mb-1">
            <Col md={3}>
              <Form.Label>
                <span className="text-danger">*</span> Education Level:
              </Form.Label>
            </Col>
            <Col md={9}>
              <Form.Select onChange={onEducationLevelChange}>
                <option>Open this select menu</option>
                {EDUCATION_LEVEL_CHOICES.map((value, idx) => (
                  <option key={idx} value={value}>
                    {value}
                  </option>
                ))}
              </Form.Select>
            </Col>
          </Row>
          <Row className="mb-1">
            <Col md={3}>
              <Form.Label>
                <span className="text-danger">*</span> Preferred Activities:
              </Form.Label>
            </Col>
            <Col md={9}>
              <Form.Select onChange={onPreferredActivitiesChange}>
                <option>Open this select menu</option>
                {PREFERRED_ACTIVITIES_CHOICES.map((value, idx) => (
                  <option key={idx} value={value}>
                    {value}
                  </option>
                ))}
              </Form.Select>
            </Col>
          </Row>
          <Row className="mb-1">
            <Col md={3}>
              <Form.Label>
                <span className="text-danger">*</span> Location:
              </Form.Label>
            </Col>
            <Col md={9}>
              <Form.Select onChange={onLocationChange}>
                <option>Open this select menu</option>
                {LOCATION_CHOICES.map((value, idx) => (
                  <option key={idx} value={value}>
                    {value}
                  </option>
                ))}
              </Form.Select>
            </Col>
          </Row>
          <Row className="mb-1">
            <Col md={3}>
              <Form.Label>
                <span className="text-danger">*</span> Favorite Season:
              </Form.Label>
            </Col>
            <Col md={9}>
              <Form.Select onChange={onFavoriteSeasonChange}>
                <option>Open this select menu</option>
                {FAVORITE_SEASON_CHOICES.map((value, idx) => (
                  <option key={idx} value={value}>
                    {value}
                  </option>
                ))}
              </Form.Select>
            </Col>
          </Row>
          <Row className="mb-1">
            <Col md={3}>
              <Form.Label>
                <span className="text-danger">*</span> Age Range:
              </Form.Label>
            </Col>
            <Col md={9}>
              <Form.Select onChange={onAgeRangeChange}>
                <option>Open this select menu</option>
                {AGE_RANGE_CHOICES.map((value, idx) => (
                  <option key={idx} value={value}>
                    {value}
                  </option>
                ))}
              </Form.Select>
            </Col>
          </Row>
        </Col>
        <Col md={6}>
          <Row className="mb-5">
            <Col>
              <h3>Prediction</h3>
            </Col>
          </Row>
        </Col>
      </Row>
    </Form.Group>
  );
};

export default PredictionTab;
