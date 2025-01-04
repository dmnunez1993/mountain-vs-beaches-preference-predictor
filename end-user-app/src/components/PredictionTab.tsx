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
  PredictionRequest,
  PredictionResposeItem,
} from "../models/prediction";
import { getAbsoluteUrl } from "../api/urls";
import { errorAlert } from "./utils/messages";

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
  const [environmentalConcerns, setEnvironmentalConcerns] = useState<
    boolean | null
  >(null);
  const [pets, setPets] = useState<boolean | null>(null);
  const [preference, setPreference] = useState<boolean | null>(null);

  const [submitting, setSubmitting] = useState(false);

  const [prediction, setPrediction] = useState<boolean | null>(null);
  const [probabilities, setProbabilities] = useState<number[] | null>(null);

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

  const onPetsChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    if (e.target.value === "yes") {
      setPets(true);
    } else if (e.target.value === "no") {
      setPets(false);
    } else {
      setPets(null);
    }
  };

  const onEnvironmentalConcernChanges = (
    e: React.ChangeEvent<HTMLSelectElement>
  ) => {
    if (e.target.value === "yes") {
      setEnvironmentalConcerns(true);
    } else if (e.target.value === "no") {
      setEnvironmentalConcerns(false);
    } else {
      setEnvironmentalConcerns(null);
    }
  };

  const onPreferenceChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    if (e.target.value === "mountains") {
      setPreference(true);
    } else if (e.target.value === "beaches") {
      setPreference(false);
    } else {
      setPreference(null);
    }
  };

  const onPredict = async () => {
    setSubmitting(true);
    const data: PredictionRequest = {
      income: income,
      travel_frequency: travelFrecuency,
      vacation_budget: vacationBudget,
      proximity_to_mountains: proximityToMountains,
      proximity_to_beaches: proximityToBeaches,
      gender: gender,
      education_level: educationLevel,
      preferred_activities: preferredActivities,
      location: location,
      favorite_season: favoriteSeason,
      age_range: ageRange,
      pets: pets,
      environmental_concerns: environmentalConcerns,
      preference: preference,
    };
    const url = getAbsoluteUrl("/predict/");
    const res = await fetch(url, {
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      method: "POST",
      credentials: "include",
      body: JSON.stringify([data]),
    });

    if (res.status !== 200) {
      errorAlert(
        "An error ocurred. Please, make sure all the mandatory fields are completed correctly"
      );
      setSubmitting(false);
      return;
    }

    const responseData = (await res.json()) as {
      status: string;
      data: PredictionResposeItem[];
    };

    if (responseData.data.length < 1) {
      errorAlert("An error ocurred. The predictor is not working properly");
      setSubmitting(false);
      return;
    }

    setPrediction(responseData.data[0].prediction);

    if (responseData.data[0].probabilities.length === 2) {
      setProbabilities(responseData.data[0].probabilities);
    }

    setSubmitting(false);
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
                max="1073741823"
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
                max="1073741823"
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
                max="1073741823"
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
                max="1073741823"
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
                max="1073741823"
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
              <Form.Select
                onChange={onGenderChange}
                value={emptyValueOnNull(gender)}
              >
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
              <Form.Select
                onChange={onEducationLevelChange}
                value={emptyValueOnNull(educationLevel)}
              >
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
              <Form.Select
                onChange={onPreferredActivitiesChange}
                value={emptyValueOnNull(preferredActivities)}
              >
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
              <Form.Select
                onChange={onLocationChange}
                value={emptyValueOnNull(location)}
              >
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
              <Form.Select
                onChange={onFavoriteSeasonChange}
                value={emptyValueOnNull(favoriteSeason)}
              >
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
              <Form.Select
                onChange={onAgeRangeChange}
                value={emptyValueOnNull(ageRange)}
              >
                <option>Open this select menu</option>
                {AGE_RANGE_CHOICES.map((value, idx) => (
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
                <span className="text-danger">*</span> Pets:
              </Form.Label>
            </Col>
            <Col md={9}>
              <Form.Select
                onChange={onPetsChange}
                value={pets !== null ? (pets ? "yes" : "no") : ""}
              >
                <option>Open this select menu</option>
                <option value="yes">Yes</option>
                <option value="no">No</option>
              </Form.Select>
            </Col>
          </Row>
          <Row className="mb-1">
            <Col md={3}>
              <Form.Label>
                <span className="text-danger">*</span> Environmental Concerns:
              </Form.Label>
            </Col>
            <Col md={9}>
              <Form.Select
                onChange={onEnvironmentalConcernChanges}
                value={
                  environmentalConcerns !== null
                    ? environmentalConcerns
                      ? "yes"
                      : "no"
                    : ""
                }
              >
                <option>Open this select menu</option>
                <option value="yes">Yes</option>
                <option value="no">No</option>
              </Form.Select>
            </Col>
          </Row>
          <Row className="mb-1">
            <Col md={3}>
              <Form.Label>Preference (optional):</Form.Label>
            </Col>
            <Col md={9}>
              <Form.Select
                onChange={onPreferenceChange}
                value={
                  preference !== null
                    ? preference
                      ? "mountains"
                      : "beaches"
                    : ""
                }
              >
                <option>Open this select menu</option>
                <option value="mountains">Mountains</option>
                <option value="beaches">Beaches</option>
              </Form.Select>
            </Col>
          </Row>
          <Row>
            <Col>
              <Button onClick={onPredict} disabled={submitting}>
                Predict
              </Button>
            </Col>
          </Row>
        </Col>
        <Col md={6}>
          <Row className="mb-5">
            <Col>
              <h3>Prediction</h3>
            </Col>
          </Row>
          <Row>
            <Col md={3}>
              <Form.Label>Predicted Preference:</Form.Label>
            </Col>
            <Col md={3}>
              <Form.Label>
                {prediction !== null
                  ? prediction
                    ? "Mountains"
                    : "Beaches"
                  : "-"}
              </Form.Label>
            </Col>
          </Row>
          <Row>
            <Col md={3}>
              <Form.Label>Real Preference:</Form.Label>
            </Col>
            <Col md={3}>
              <Form.Label>
                {preference !== null
                  ? preference
                    ? "Mountains"
                    : "Beaches"
                  : "-"}
              </Form.Label>
            </Col>
          </Row>
          <Row>
            <Col md={3}>
              <Form.Label>Probabilities:</Form.Label>
            </Col>
            <Col md={3}>
              <Form.Label>
                Mountains:{" "}
                {probabilities !== null ? probabilities[1].toFixed(2) : "-"}
              </Form.Label>
            </Col>
            <Col md={3}>
              <Form.Label>
                Beaches:{" "}
                {probabilities !== null ? probabilities[0].toFixed(2) : "-"}
              </Form.Label>
            </Col>
          </Row>
        </Col>
      </Row>
    </Form.Group>
  );
};

export default PredictionTab;
