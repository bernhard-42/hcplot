/**
  * Copyright 2017 Bernhard Walter
  *
  * Licensed under the Apache License, Version 2.0 (the "License");
  * you may not use this file except in compliance with the License.
  * You may obtain a copy of the License at
  *
  *    http://www.apache.org/licenses/LICENSE-2.0
  *
  * Unless required by applicable law or agreed to in writing, software
  * distributed under the License is distributed on an "AS IS" BASIS,
  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  * See the License for the specific language governing permissions and
  * limitations under the License.
  */

require.config({
    baseUrl: '/js',
    shim: {
        "highcharts-more":            ['highcharts'],
        "highcharts-export":          ['highcharts'],
        "highcharts-offline-export":  ['highcharts-export'],
        "highcharts-boost":           ['highcharts']
    },
    paths: {
        'highcharts':                 'http://code.highcharts.com/highcharts',
        'highcharts-more':            'http://code.highcharts.com/highcharts-more',
        'highcharts-export':          'http://code.highcharts.com/modules/exporting',
        'highcharts-offline-export':  'http://code.highcharts.com/modules/offline-exporting',
        'highcharts-boost':           'http://code.highcharts.com/modules/boost'
    }
});

requirejs.onError = function (err) {
    element.text(err.requireType, err.requireModules)
}

window.hc_charts = {}

window.hc_charts.promise = new Promise(function(resolve, reject) {
    var modules = ['highcharts', 'highcharts-more', 'highcharts-export', 'highcharts-offline-export', 'highcharts-boost'];
    requirejs(modules, function(hc) {
        element.text("Loaded HighCharts " + Highcharts.version)
        resolve(Highcharts)
    });
})