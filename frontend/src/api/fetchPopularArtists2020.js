import axios  from 'axios';

const URL = 'http://localhost:5000/popular-artists-2020';

export const fetchPopularArtists2020 = async() => {
    const { data } = await axios.get(URL);
    return data;
}