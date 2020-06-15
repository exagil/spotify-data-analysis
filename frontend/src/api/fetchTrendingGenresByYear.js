import axios  from 'axios';

const URL = 'http://localhost:5000/';

export const fetchTrendingGenres = async() => {
    const { data } = await axios.get(URL);
    return data;
}