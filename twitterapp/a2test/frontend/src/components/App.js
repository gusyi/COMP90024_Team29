import React, { Component } from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import ReactDOM from 'react-dom';

import DeckGL from '@deck.gl/react';
import {StaticMap} from 'react-map-gl';
import {GeoJsonLayer} from '@deck.gl/layers';
import {scaleLinear, scaleThreshold} from 'd3-scale';

import Header from './layout/Header';
import Dataview from './layout/Dataview';

const COLOR_SCALE = scaleThreshold()
  .domain([0, 4, 8, 12, 20, 32, 52, 84, 136, 220])
  .range([
    [26, 152, 80],
    [102, 189, 99],
    [166, 217, 106],
    [217, 239, 139],
    [255, 255, 191],
    [254, 224, 139],
    [253, 174, 97],
    [244, 109, 67],
    [215, 48, 39],
    [168, 0, 0]
  ]);

const WIDTH_SCALE = scaleLinear()
  .clamp(true)
  .domain([0, 200])
  .range([10, 2000]);

const INITIAL_VIEW_STATE = {
    latitude: -36.951132,
    longitude: 144.600406,
    zoom: 4,
    minZoom: 2,
    maxZoom: 8
  };

class App extends Component {
    state = {
        tweets: {
            1: {
                _id: '0000000001',
                created_at: new Date(),
                userid: '00000000',
                text: 'Scott Morrison',
                City: 'Melbourne'
            },
            2: {
                _id: '0000000002',
                created_at: new Date(),
                userid: '00000001',
                text: 'Prime Minister',
                City: 'Melbourne'
            }
        }
    }

    render() {
        return (
            <div className="app">
                <Header tweets={this.state.tweets} />
                {/* <Dataview /> */}
            </div>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));