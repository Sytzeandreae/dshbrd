var React = require('react');

var Item = React.createClass({
    render: function() {
        return (
            <div>
                <a href={this.props.item.link}>
                    <h4>{this.props.item.title}</h4>
                </a>
                <p><a href={this.props.item.comments}>Comments</a></p>
            </div>
        )
    } 
});

module.exports = Item;
