module.exports = {
    chainWebpack: config => {
        config.module
            .rule('core')
            .test(/\.glsl$/i)
            .use()
				.loader('shader-loader')
				.end()
	}
}
