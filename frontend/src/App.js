import React from 'react';
import { fetchTrendingGenres } from './api/fetchTrendingGenresByYear';
import { fetchPlotImg } from './api/fetchPlotImg';
import { fetchPopularArtists2020 } from './api/fetchPopularArtists2020';
import { fetchAvgDuration } from './api/fetchAvgDuration';
import TrendingGenresTable from './components/table';

export default class App extends React.Component  {
    
    state = {
      data: null,
      fig: null,
      elbow_fig: null,
      popular_artists_2020: null,
      avg_duration: null
    };

    componentDidMount() {
      this._asyncRequest = fetchTrendingGenres().then(
        data => {
          this._asyncRequest = null;
          this.setState({data})
        }
      );
      this._asyncRequest = fetchPlotImg().then(
        data => {
          this._asyncRequest = null;
          this.setState({fig: data['fig'], elbow_fig:data['elbow_fig']})
        }
      );
      this._asyncRequest = fetchPopularArtists2020().then(
        popular_artists_2020 => {
          this._asyncRequest = null;
          this.setState({popular_artists_2020})
        }
      );
      this._asyncRequest = fetchAvgDuration().then(
        data => {
          this._asyncRequest = null;
          this.setState({avg_duration : data['avg_duration'] })
        }
      );
    }

    componentWillUnmount(){
      if (this._asyncRequest){
        this._asyncRequest.cancel();
      }
    }

    render(){
        return(
            <div>
                <div>
                  {this.state.popular_artists_2020 ? (
                    <div>
                      <h4>Popular artists of 2020</h4>
                      <ul>
                        {this.state.popular_artists_2020 && this.state.popular_artists_2020.map(item => (
                          <li key={item}>{item}</li>
                        ))}
                      </ul>
                    </div>
                  ): (
                    <h4>Loading popular artists</h4>
                  )
                  }
                  {this.state.popular_artists_2020 ? (
                    <div>
                      <h4>Average duration of popular songs: {JSON.stringify(this.state.avg_duration)} seconds</h4>
                    </div>
                  ): (
                    <h4>Loading average duration of songs</h4>
                  )
                  }
                  
                </div>
                <img src={`data:image/jpeg;base64,${this.state.elbow_fig}`} />
                <img src={`data:image/jpeg;base64,${this.state.fig}`} />
                <TrendingGenresTable data={this.state.data} />
            </div>
        );
    }
}