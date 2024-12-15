export interface PredictionRequest {
  income: number | null;
  travel_frequency: number | null;
  vacation_budget: number | null;
  proximity_to_mountains: number | null;
  proximity_to_beaches: number | null;
  gender: string | null;
  education_level: string | null;
  preferred_activities: string | null;
  location: string | null;
  favorite_season: string | null;
  age_range: string | null;
  pets: boolean | null;
  environmental_concerns: boolean | null;
  preference: boolean | null;
}

export interface PredictionResposeItem {
  prediction: boolean;
  real_value: boolean | null;
  probabilities: number[];
}

export const GENDER_CHOICES = ["male", "female", "non-binary"];
export const EDUCATION_LEVEL_CHOICES = [
  "high school",
  "bachelor",
  "master",
  "doctorate",
];
export const PREFERRED_ACTIVITIES_CHOICES = [
  "skiing",
  "swimming",
  "hiking",
  "sunbathing",
];
export const LOCATION_CHOICES = ["urban", "suburban", "rural"];
export const FAVORITE_SEASON_CHOICES = ["summer", "fall", "winter", "spring"];
export const AGE_RANGE_CHOICES = ["25-40", "18-25", "40-65", "65+"];
