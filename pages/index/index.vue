<template>
	<view>
		<view class="top">
			<view class="os font-w">
				<text>22:34</text>
			</view>
			<view class="you font-w">
				<!-- <u-icon name="http://e.rubyonly.cn/img/sign1.png" size="60" ></u-icon> -->
				<u-image src="http://e.rubyonly.cn/img/sign1.png" width="80px" height="50px"></u-image>
			</view>
			<!-- <view class="font-w s5g">
				  5G
			</view> -->
		</view>
		<view class="headers">
			<u-icon name="home" size="22" color="#c0b6aa"></u-icon>
			<text>世界杯2022</text>
			<text class="ttasdf">滚球</text>
			<text class="ttasdf">今日</text>
			<text class="ttasdf">早盘</text>
		</view>
		<view class="user"></view>
		<view class="main_body">
			<view class="box-b">
				<view class="shisan">1 - 0</view>
				<view class="red">7.1</view>
			</view>
			<view class="box-b">
				<view class="shisan">1 - 0</view>
				<view class="red">7.1</view>
			</view>
			<view class="box-b">
				<view class="shisan">1 - 0</view>
				<view class="red">7.1</view>
			</view>

			<view class="box-b">
				<view class="shisan">1 - 0</view>
				<view class="red">7.1</view>
			</view>
		</view>
		<view class="foot-up">
			<view class="font-s">足球 波胆</view>
			<view class="col">世界杯2022(在卡塔尔)</view>
			<view class="font-600">
				* 墨西哥 v 波兰
			</view>
			<view class="bzdss font-800">
				2-3 @ <text>51</text>
			</view>
			<view class="conf">
				已确认
				<text>TDXXXXXXXXa</text>
			</view>
			<view class="xiaz">
				下注金额
				<text>可赢金额</text>
			</view>
			<view class="xiaz font-800">
				20.00
				<text class="lv">1000.00</text>
			</view>
			<view class="succ">
				您已成功投注
			</view>
			<view class="buttons">
				<u-button class="z" text="保留选项"></u-button>
				<u-button class="y" text="完成"></u-button>
			</view>
		</view>
		<view class="os-xxx">
			<u-image src="http://e.rubyonly.cn/img/foot.png" width="375px" mode="aspectFit"></u-image>
		</view>

	</view>
</template>

<script>
	export default {
		data() {
			return {
				title: 'Hello'
			}
		},
		onLoad() {

		},
		methods: {

		}
	}
</script>

<style lang="scss" scoped>
	.os-xxx {
		position: absolute;
		bottom : -70rpx;
		width: 750rpx;
		background-color: #f6f6f6;
		border-top: 1px solid #cdcdcd;

	}

	.foot-up {
		.buttons {
			border-top: 0;
			margin-top: 0rpx;
			width: 750rpx;
			margin-left: -30rpx;
			display: flex;

			.u-button {
				border-top: 0;
				height: 100rpx;
				font-weight: 600;
				border-bottom: 1px solid #cdcdcd;
			}

			.z {
				background-color: #ededed;
				color: #787878;
			}

			.y {
				background-color: #515151;
				color: #f2f2f2;
			}
		}

		.succ {
			background-color: #1a7f5c;
			text-align: center;
			color: #bce6da;
			font-size: 24rpx;
			padding: 10rpx;
			width: 750rpx;
			margin-left: -40rpx;
		}

		.lv {
			color: #267e60;
		}

		.xiaz {
			color: #6d6d6d;

			text {
				position: absolute;
				right: 90rpx;
			}
		}

		.conf {
			margin-top: 40rpx;
			color: #5d9582;

			text {
				color: #6f6f6f;
				position: absolute;
				right: 90rpx;
			}
		}

		.bzdss {
			text {
				color: #c03e41;
			}
		}

		.font-800 {
			font-weight: 800;
		}

		.font-600 {
			font-weight: 600;
		}

		view {
			margin-top: 20rpx;
		}

		font-size: 28rpx;

		.font-s {
			font-size: 28rpx;
		}

		.col {
			color: #858585;
		}

		box-shadow: 0 -5px 10px #e3e3e3;
		height: 600rpx;
		position: absolute;
		bottom: 240rpx;
		width: 750rpx;
		padding: 30rpx;
		z-index: 999;
	}

	.main_body {

		// display: flex;
		// padding-right:20rpx;
		.box-b {
			display: inline-block;
			width: 214rpx;
			min-width: 214rpx;
			height: 96rpx;
			border: 1px solid #cdcdcd;
			line-height: 48rpx;
			text-align: center;
			font-size: 26rpx;
			margin-left: 24rpx;
			margin-top: 40rpx;
			border-radius: 6rpx;

			.red {
				font-size: 30rpx;
				color: #cf4129;
				font-weight: 600;
			}
		}
	}

	.top {
		display: flex;
		margin: 20rpx 0 20rpx 40rpx;

		.os {}

		.you {
			margin-top: -30rpx;
			margin-left: 440rpx;
		}

		.font-w {
			font-weight: 600;
		}

		.s5g {
			margin-left: 10rpx;
		}
	}

	.headers {
		background-color: #4d3f34;
		height: 100rpx;
		line-height: 100rpx;
		padding: 10rpx 40rpx;
		display: flex;
		font-size: 28rpx;

		text {
			color: #d5bd96;
			margin-left: 44rpx;
		}

		.ttasdf {
			color: #b9aca5;
		}
	}

	.user {
		background-color: #503f32;
		// background-color: #aa0000;
		background-image: url("../../static/icon_account.svg");
		width: 118rpx;
		height: 118rpx;
		background-repeat: no-repeat;
		background-position: center;
		margin-left: 60rpx;
		position: absolute;
		right: 0rpx;
		z-index: 99;
		top: 87rpx;
		// border-left: 1px solid #fff;
		box-shadow: -5px 0px 5px #4a3b2e;
	}
</style>
