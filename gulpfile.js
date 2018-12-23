var gulp = require('gulp');

// dependencies
var del = require('del');
var express = require('express');
var app = express();

// // gulp dependencies
var gulp = require('gulp');
var autoprefixer = require('gulp-autoprefixer');
var concat = require('gulp-concat');
var connect = require('gulp-connect');
var gutil = require('gulp-util');
var sass = require('gulp-sass');
var plumber = require('gulp-plumber');
var watch = require('gulp-watch');
//
// asset copy location maps
var copyLocations = [
  {
    src: './ui/assets/**/*.*',
    dest: './public/assets'
  },
  {
    src: './ui/index.html',
    dest: './public'
  },
  {
    src: './ui/vendor/**/*.css',
    dest: './public/css'
  },
  {
    src: './ui/vendor/**/*.js',
    dest: './public/js'
  }
];

var watchLocations = {
  sass: './ui/sass/**/*.scss',
  js: './ui/js/**/*.js',
  html: './ui/index.html'
};

var destLocations = {
  js: './public/js',
  css: './public/css'
};

/* ERROR HANDLER */
var onError = function(err) {
  gutil.log(gutil.colors.red('ERROR', err.plugin), err.message);
  gutil.beep();
  new gutil.PluginError(err.plugin, err, {showStack: true});
};

/* CLEAN */
gulp.task('clean', function(cb) {
  return del(['public/**/*'], cb);
});

/* COPY */
gulp.task('copy', function(cb) {
  var task;
  for (var i = 0; i < copyLocations.length; i++) {
    task = gulp.src(copyLocations[i].src)
    .pipe(plumber())
    .pipe(watch(copyLocations[i].src))
    .pipe(gulp.dest(copyLocations[i].dest))
    .pipe(connect.reload());
  }
  cb();
});

/* SASS */
gulp.task('sass', function(cb) {
  gulp.src(watchLocations.sass)
      .pipe(plumber())
      .pipe(sass())
      .pipe(autoprefixer())
      .pipe(gulp.dest(destLocations.css))
      .pipe(connect.reload());
  cb();
});

gulp.task('sass:watch', function(cb) {
  watch(watchLocations.sass, function() {
    gulp.src(watchLocations.sass)
        .pipe(plumber())
        .pipe(sass())
        .pipe(autoprefixer())
        .pipe(gulp.dest(destLocations.css))
        .pipe(connect.reload());
  });
  cb();
});

/* JS */
gulp.task('scripts', function(cb) {
  gulp.src(watchLocations.js)
      .pipe(concat('stack.js'))
      .pipe(gulp.dest(destLocations.js))
      .pipe(connect.reload());
  cb();
});

gulp.task('scripts:watch', function(cb) {
  watch(watchLocations.js, function() {
    gulp.src(watchLocations.js)
        .pipe(concat('stack.js'))
        .pipe(gulp.dest(destLocations.js))
        .pipe(connect.reload());
  });
  cb();
});

/* SERVER */
gulp.task('server', function(cb) {
  // Ideally it would work with gulp-connect module - to be figured out.
  // connect.server({
  //   root: './public',
  //   port: 3000,
  //   livereload: true
  // });

  // TODO - add live reload
  app.use(express.static('./public'));
  app.listen(3000);
});

/* MAIN TASKS */
gulp.task('dev', gulp.series(
  'clean',
  'copy',
  'sass',
  'sass:watch',
  'scripts',
  'scripts:watch',
  'server'
));

gulp.task('build', function() {
  // TODO: build task
});
