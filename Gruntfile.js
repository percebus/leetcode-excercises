module.exports = (grunt) => {
  'use strict'

  require('load-grunt-tasks')(grunt, {
    pattern: ['grunt-*', '!grunt-template-*']
  })

  grunt.initConfig({
    pylint: {
      options: { rcfile: '.pylintrc' },
      apps: ['apps/**/*.py']
    },
    shell: {
      standard_Gruntfile: 'standard --fix Gruntfile.js'
    }
  })

  grunt.registerTask('lint:js:Gruntfile', ['shell:standard_Gruntfile'])
  // grunt.registerTask('lint:python', ['pylint']) // FIXME doesn't work on mac
  grunt.registerTask('lint', [])

  grunt.registerTask('default', ['lint'])
  grunt.task.run('lint:js:Gruntfile')
}
