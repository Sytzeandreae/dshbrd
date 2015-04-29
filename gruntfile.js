module.exports = function(grunt) {
  grunt.initConfig({
      // Watch task config
    watch: {
      sass: {
        files: './sass/{,*/}*.scss',
        tasks: ['sass']    
      }
    },
    sass: {
      options: {
        includePaths: [
          './bower_components/foundation/scss',
          './bower_components/compass-mixins/lib',
          './bower_components/materialize/sass',
          './bower_components/sass-flex-mixin'
        ]
      },
      dev: {
        files: {
          './dshbrd/static/css/style.css' : './sass/style.scss'
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');
};
