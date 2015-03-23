var React = require('react');
var XkcdStore = require('../stores/XkcdStore');
var BlockMixin = require('../../dshbrd/utils/mixins/BlockMixin');
var $ = require('jquery');

var SubBlock = React.createClass({
    mixins: [BlockMixin],

    getInitialState: function() {
        return {
            'xkcd': XkcdStore.getData()
        }
    },

    componentWillMount: function() {console.log('mounted');},

    componentDidMount: function() {
        $.get(
            'http://127.0.0.1:5000/api/v1/block/xkcd/' + this.props.block_specifics.id, 
            function(result) {
                if (this.isMounted()) {
                    this.setState({
                        'xkcd': result
                    });
                }
            }.bind(this));
        XkcdStore.addChangeListener(this._onChange);
    },

    componentWillUnmount: function() {
        XkcdStore.removeChangeListener(this._onChange);
    },

    _renderEdit: function() { return <div/> },
    _renderNormal: function() {
        return (
            <div dangerouslySetInnerHTML={{__html: this.state.xkcd.description}} />
        )
    },

    _onChange: function() {}
});

module.exports = SubBlock;
