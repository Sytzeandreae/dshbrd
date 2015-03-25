var BlockMixin = {
    render: function() {
        if (this.props.edit) {
            return this._renderEdit();
        } else if ((!this.state || this.state.loading) && !this.props.button) {
            return this._renderLoader();
        } else {
            return this._renderNormal();
        }
    },
    
    _renderLoader: function() {
        return (
            <div className={"valign-wrapper"}>
                <div className={"preloader-wrapper centerized small active valign"}>
                    <div className={"spinner-layer spinner-blue-only"}>
                        <div className={"circle-clipper left"}>
                            <div className={"circle"}></div>
                        </div>
                        <div className={"gap-patch"}>
                            <div className={"circle"}></div>
                        </div>
                        <div className={"circle-clipper right"}>
                            <div className={"circle"}></div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
};

module.exports = BlockMixin;
