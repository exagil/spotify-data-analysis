import React from 'react';
import { fetchTrendingGenres } from './api/fetchTrendingGenresByYear';
import { fetchPlotImg } from './api/fetchPlotImg';
import TrendingGenresTable from './components/table';

export default class App extends React.Component  {
    
    state = {
      data: null,
      fig: null,
      elbow_fig: null
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
    }

    componentWillUnmount(){
      if (this._asyncRequest){
        this._asyncRequest.cancel();
      }
    }

    render(){
        return(
            <div>
                <img src={`data:image/jpeg;base64,${this.state.elbow_fig}`} />
                <img src={`data:image/jpeg;base64,${this.state.fig}`} />
                <TrendingGenresTable data={this.state.data} />
            </div>
        );
    }
}