import axios  from 'axios';

const URL = 'http://localhost:5000/api/analysis';

export const fetchPlotImg = async() => {
    const { data } = await axios.get(URL);
    return data;
}