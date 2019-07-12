module.exports = {
    chainWebpack: config => {
        config.module
            .rule('core')
            .test(/\.glsl$/i)
            .use()
            .loader('shader-loader')
            .end()
    },
    devServer: {
        proxy: {
            '/api': {
                target: 'http://127.0.0.1:5000',
                changeOrigin: true
            }
        }
    }
}
