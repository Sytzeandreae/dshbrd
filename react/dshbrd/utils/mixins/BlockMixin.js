var BlockMixin = {
    render: function() {
        if (this.props.edit) {
            return this._renderEdit();
        } else {
            return this._renderNormal();
        }
    }
};

module.exports = BlockMixin;
