var React = require('react');
var XkcdStore = require('../stores/XkcdStore');
var BlockMixin = require('../../dshbrd/utils/mixins/BlockMixin');
var $ = require('jquery');

var SubBlock = React.createClass({
    mixins: [BlockMixin],

    getInitialState: function() {
        return {
            'xkcd': XkcdStore.getData(),
            'loading': true
        }
    },

    componentWillMount: function() {console.log('mounted');},

    componentDidMount: function() {
        $.get(
            'http://127.0.0.1:5000/api/v1/block/xkcd/' + this.props.block_specifics.id, 
            function(result) {
                if (this.isMounted()) {
                    this.setState({
                        'xkcd': result,
                        'loading': false
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
            <div className={"valign-wrapper"}>
                <div className={"valign centerized"}>
                    <img src={this.state.xkcd.img.url} alt={this.state.xkcd.img.alt} title={this.state.xkcd.img.title}/>
                </div>
            </div>
        )
    },

    _onChange: function() {}
});

module.exports = SubBlock;
