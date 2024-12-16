module.exports = {
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
        './node_modules/tailwindcss/**/*.js',
    ],
    theme: {
        extend: {},
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
