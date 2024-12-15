export interface PredictionRequest {
  income: number;
  travel_frequency: number;
  vacation_budget: number;
  proximity_to_mountains: number;
  proximity_to_eaches: number;
  gender: string;
  education_level: string;
  preferred_activities: string;
  location: string;
  favorite_season: string;
  age_range: string;
  pets: boolean;
  environmental_concerns: boolean;
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
