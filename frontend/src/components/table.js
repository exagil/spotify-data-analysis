import React from 'react';
import styles from './table.css'

const TrendingGenresTable  = ({ data }) => {

    return (
        <>
        <div className="container">
            <div className="row">
            <div className="col s12 board">
                <table>
                    <caption>Trending Genres Year Wise</caption>
                    <thead>
                        <tr>
                            <th>Year</th>
                            <th>Trending Genres</th>
                        </tr>
                    </thead>
                    <tbody>
                {  data && 
                    Object.keys(data).map((key, i) => (
                        <tr key={i}>
                            <td>{key}</td>
                            <td>{(data[key]).toString()}</td>
                        </tr>
                    ))
                }
                    </tbody>
                </table>
            </div>
            </div>
        </div>
        </>
  )
}

export default TrendingGenresTable;
