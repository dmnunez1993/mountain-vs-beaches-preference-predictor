import {
  API_ENDPOINT,
  API_URL_SAME_ADDR,
  API_URL_SAME_ADDR_PORT,
} from "../config/api";

export const getAbsoluteUrl = (relative_url: string): string => {
  if (API_URL_SAME_ADDR) {
    const hostname = window.location.hostname;
    return `http://${hostname}:${API_URL_SAME_ADDR_PORT}${relative_url}`;
  }

  return `${API_ENDPOINT}${relative_url}`;
};
