import axios  from 'axios';

const URL = 'http://localhost:5000/popular-songs-duration-2020';

export const fetchAvgDuration = async() => {
    const { data } = await axios.get(URL);
    return data;
}