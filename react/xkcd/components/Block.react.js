var React = require('react');
var XkcdStore = require('../stores/XkcdStore');
var BlockMixin = require('../../dshbrd/utils/mixins/BlockMixin');
var $ = require('jquery');

var SubBlock = React.createClass({
    getInitialState: function() {
        return {
            'xkcd': XkcdStore.getData()
        }
    },

    componentWillMount: function() {console.log('mounted');},

    componentDidMount: function() {
        $.get('http://127.0.0.1:5000/api/v1/xkcd/2', function(result) {
            if (this.isMounted()) {
                this.setState({
                    'xkcd': result
                });
            }
        }.bind(this));
        //XkcdStore.addChangeListener(this._onChange);
    },

    componentWillUnmount: function() {
        //XkcdStore.removeChangeListener(this._onChange);
    },
    render: function() {return (<div/>)},

    _renderEdit: function() { return <div/> },
    _renderNormal: function() {
        return (
            <div></div>
        )
    },

    _onChange: function() {}
})
